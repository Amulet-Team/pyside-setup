LICENSE_TEXT = """
# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
"""
MYPY_TEXT = """
# mypy: disable-error-code="override, overload-overlap"
"""

# flake8: noqa E:402

"""
pyi_generator.py

This script generates .pyi files for arbitrary modules.
"""

import argparse
import inspect
import io
import logging
import os
import re
import sys

from pathlib import Path
from contextlib import contextmanager
from textwrap import dedent

from shibokensupport.signature.lib.enum_sig import (
    HintingEnumerator,
    BaseFormatter,
    EnumFormatter,
    SignalFormatter,
    AttributeFormatter,
    SectionFormatter
)
from shibokensupport.signature.lib.tool import build_brace_pattern

indent = " " * 4
MaxSignalSignatures = 8

TYPE_MAP = {
    # Qt integer types
    "qint64": "int",
    "qint32": "int",
    "qint16": "int",
    "qsizetype": "int",
    "quint32": "int",
    "quint64": "int",
    "qlonglong": "int",
    "qulonglong": "int",
    "size_t": "int",
    "uint": "int",
    "ushort": "int",
    "ulong": "int",
    "unsigned char": "int",
    "unsigned int": "int",
    "short": "int",
    "uchar": "int",

    # Qt floating types
    "qreal": "float",
    "double": "float",

    # Qt string-like
    "QString": "str",
    "QStringList": "typing.List[str]",
    "QChar": "str",

    # Qt containers (minimal)
    "QList": "typing.List",
    "QVariant": "typing.Any",

    # C strings
    "char*": "str",
    "const char*": "str",

    # Types used in signals
    "PySide6.QtCore.Qt.WindowFlags": "PySide6.QtCore.Qt.WindowType",
    "PySide6.QtCore.Qt.DockWidgetAreas": "PySide6.QtCore.Qt.DockWidgetArea",
    "PySide6.QtCore.Qt.WindowStates": "PySide6.QtCore.Qt.WindowState",
    "PySide6.QtCore.Qt.ToolBarAreas": "PySide6.QtCore.Qt.ToolBarArea",
    "PySide6.QtCore.Qt.Alignment": "PySide6.QtCore.Qt.AlignmentFlag",
    "PySide6.Qt3DRender.Qt3DRender.QAbstractRayCaster.Hits": "collections.abc.Sequence[PySide6.Qt3DRender.Qt3DRender.QRayCasterHit]",
    "PySide6.Qt3DRender.Qt3DRender.QMemoryBarrier.Operations": "PySide6.Qt3DRender.Qt3DRender.QMemoryBarrier.Operation",
    "PySide6.QtBluetooth.QBluetoothDeviceInfo.Fields": "PySide6.QtBluetooth.QBluetoothDeviceInfo.Field",
    "BlurHints": "PySide6.QtWidgets.QGraphicsBlurEffect.BlurHint",
    "Capabilities": "PySide6.QtGui.QInputDevice.Capability",
    "Feature": "PySide6.QtDesigner.QDesignerFormWindowInterface.FeatureFlag",
    "PySide6.QtDataVisualization.QAbstract3DGraph.OptimizationHints": "PySide6.QtDataVisualization.QAbstract3DGraph.OptimizationHint",
    "PySide6.QtDataVisualization.QAbstract3DGraph.SelectionFlags": "PySide6.QtDataVisualization.QAbstract3DGraph.SelectionFlag",
    "PySide6.QtGraphs.QSurface3DSeries.DrawFlags": "PySide6.QtGraphs.QSurface3DSeries.DrawFlag",
    "PySide6.QtGraphs.QValueAxis.TickType": "PySide6.QtCharts.QValueAxis.TickType",
    "PySide6.QtGraphs.QXYSeries.PointsConfigurationHash": "typing.Any",
    "PySide6.QtGraphs.QtGraphs3D.SelectionFlags": "PySide6.QtGraphs.QtGraphs3D.SelectionFlag",
    "PySide6.QtSerialPort.QSerialPort.Directions": "PySide6.QtSerialPort.QSerialPort.Direction",
    "PySide6.QtWidgets.QDockWidget.DockWidgetFeatures": "PySide6.QtWidgets.QDockWidget.DockWidgetFeature",
    "QBarDataArray": "collections.abc.Sequence[collections.abc.Sequence[QBarDataItem]]",
    "QModelIndexList": "collections.abc.Sequence[PySide6.QtCore.QModelIndex]",
    "QRemoteObjectSourceLocation": "tuple[str, PySide6.QtRemoteObjects.QRemoteObjectSourceLocationInfo]",
    "QScatterDataArray": "collections.abc.Sequence[PySide6.QtGraphs.QScatterDataItem]",
    "QSurfaceDataArray": "collections.abc.Sequence[collections.abc.Sequence[PySide6.QtGraphs.QSurfaceDataItem]]",
    "QJsonObject": "typing.Dict[str, PySide6.QtCore.QJsonValue]",
    "QVariantMap": "collections.abc.Mapping[str, typing.Any]",
    "std.chrono.seconds": "int",
    "HANDLE": "int",

    # These are private but exposed in Python for some reason
    "QQuickCloseEvent": "typing.Any",
    "QQuickShapeGradient": "typing.Any",
}

QtObjMap: dict[str, str] = {}


def get_qt_obj_map() -> dict[str, str]:
    if not QtObjMap:
        import importlib
        import PySide6
        module_names = list(PySide6.__all__)
        graphs_i = module_names.index("QtGraphs")
        charts_i = module_names.index("QtCharts")
        if charts_i < graphs_i:
            module_names[charts_i], module_names[graphs_i] = module_names[graphs_i], module_names[charts_i]
        for mod_name in module_names:
            mod = importlib.import_module(f"PySide6.{mod_name}")
            for obj_name in dir(mod):
                QtObjMap.setdefault(obj_name, f"PySide6.{mod_name}.{obj_name}")
                if obj_name == mod_name:
                    obj = getattr(mod, obj_name)
                    for obj_name_2 in dir(obj):
                        QtObjMap.setdefault(obj_name_2, f"PySide6.{mod_name}.{obj_name}.{obj_name_2}")
    return QtObjMap


def cpp_to_py(cpp_type: str) -> str:
    cpp_type = cpp_type.rstrip("*&")
    if cpp_type.endswith(">"):
        if cpp_type.startswith("QList<"):
            return f"collections.abc.Sequence[{cpp_to_py(cpp_type[6:-1])}]"
        elif cpp_type.startswith("QMultiMap<"):
            args = cpp_type[10:-1]
            comma_index = args.find(",")
            return f"collections.abc.Mapping[{cpp_to_py(args[:comma_index])}, {cpp_to_py(args[comma_index+1:])}]"
        elif cpp_type.startswith("QSet<"):
            return f"collections.abc.Set[{cpp_to_py(cpp_type[5:-1])}]"
    if "::" in cpp_type:
        cls, extra = cpp_type.split("::", 1)
        extra = extra.replace("::", ".")
        cpp_type = f"{get_qt_obj_map().get(cls, cls)}.{extra}"
    else:
        cpp_type = get_qt_obj_map().get(cpp_type, cpp_type)
    cpp_type = TYPE_MAP.get(cpp_type, cpp_type)
    return cpp_type


EmitTypeVars = ", ".join(f"EmitT{num}" for num in range(1, MaxSignalSignatures + 1))
ArgsTypeVars = ", ".join(f"ArgsT{num}" for num in range(1, MaxSignalSignatures + 1))


def get_signal_hint() -> str:
    lines = [
        "signatures: tuple[str, ...]",
        ""
    ]
    for arg_count in [*range(MaxSignalSignatures), -1]:
        if arg_count >= 0:
            arg_hints =  ", ".join("[" + ", ".join(f"T{num}" for num in range(1, arg_count_2 + 1)) + "]" if arg_count_2 <= arg_count else "[]" for arg_count_2 in range(MaxSignalSignatures))
            emit_hints = ", ".join("[" + ", ".join(f"T{num}" for num in range(1, arg_count + 1)) + "]" for _ in range(MaxSignalSignatures))
            self_hint = f": Signal[{arg_hints}, {emit_hints}]"
            args = "".join(f"type_{num}: type[T{num}], " for num in range(1, arg_count + 1)) + "*, "
        else:
            self_hint = ""
            args = "*types: type, "
        lines.append(f"""\
@typing.overload
def __init__(self{self_hint}, /, {args}name: str = "", arguments: typing.Sequence[str] = ()) -> None: ...""")

    lines.append(f"""\

@typing.overload
def __get__(self, instance: PySide6.QtCore.QObject, owner: typing.Any | None, /) -> PySide6.QtCore.SignalInstance[{ArgsTypeVars}, {EmitTypeVars}]: ...
@typing.overload
def __get__(self, instance: None, owner: typing.Any | None, /) -> PySide6.QtCore.Signal[{ArgsTypeVars}, {EmitTypeVars}]: ...
""")

    return "\n".join(lines)


def get_signal_instance_hint() -> str:
    lines = []

    slot_hint = " | ".join([
        *[f"PySide6.QtCore._SignalInstance[ArgsT{num}]" for num in range(1, MaxSignalSignatures + 1)],
        *[f"typing.Callable[ArgsT{num}, typing.Any]" for num in range(1, MaxSignalSignatures + 1)]
    ])

    lines.append(f"def connect(self, slot: {slot_hint}, /, type: PySide6.QtCore.Qt.ConnectionType = PySide6.QtCore.Qt.ConnectionType.AutoConnection) -> PySide6.QtCore.QMetaObject.Connection: ...")
    lines.append(f"def disconnect(self, /, slot: {slot_hint} | None = None) -> bool: ...")

    for arg_i in range(1, MaxSignalSignatures + 1):
        lines.append("@typing.overload")
        lines.append(f"def emit(self, /, *args: EmitT{arg_i}.args, **kwargs: EmitT{arg_i}.kwargs) -> bool: ...")
    lines.append("")
    return "\n".join(lines)


def get_slot_constructors() -> str:
    def get_stub(arg_count: int) -> str:
        if arg_count >= 0:
            arg_params = ", ".join(f"T{num}" for num in range(1, arg_count + 1))
            self_hint = f": Slot[[{arg_params}], R]"
            args = "".join(f"type_{num}: type[T{num}], " for num in range(1, arg_count + 1)) + "*, "
        else:
            self_hint = ""
            args = "*types: type | str, "
        return f"""\
@typing.overload
def __init__(self{self_hint}, /, {args}name: str = "", result: type[R] | str | None = None, tag: str = "") -> None: ...
"""

    return "".join(map(get_stub, range(MaxSignalSignatures))) + get_stub(-1)

StubOverrides: dict[tuple[str, str], tuple[str, str]] = {
    ("PySide6.QtCore", "Signal"): (f"class Signal(typing.Generic[{ArgsTypeVars}, {EmitTypeVars}]):", get_signal_hint()),
    ("PySide6.QtCore", "SignalInstance"): (f"""\
class _SignalInstance(typing.Protocol[P]):
    def emit(self, /, *args: P.args, **kwargs: P.kwargs) -> bool: ...


class SignalInstance(typing.Generic[{ArgsTypeVars}, {EmitTypeVars}]):""", get_signal_instance_hint()),
    ("PySide6.QtCore", "Slot"): ("class Slot(typing.Generic[P, R]):", f"""\
{get_slot_constructors()}\

def __call__(self, function: typing.Callable[typing.Concatenate[T, P], R], /) -> typing.Callable[typing.Concatenate[T, P], R]: ...
"""),
}


class Writer:
    def __init__(self, outfile, *args):
        self.outfile = outfile
        self.history = [True, True]

    def print(self, *args, **kw):
        # controlling too much blank lines
        if self.outfile:
            if args == () or args == ("",):
                # We use that to skip too many blank lines:
                if self.history[-2:] == [True, True]:
                    return
                print("", file=self.outfile, **kw)
                self.history.append(True)
            else:
                print(*args, file=self.outfile, **kw)
                self.history.append(False)


class Formatter(Writer, BaseFormatter, EnumFormatter, SignalFormatter, AttributeFormatter, SectionFormatter):
    """
    Formatter is formatting the signature listing of an enumerator.

    It is written as context managers in order to avoid many callbacks.
    The separation in formatter and enumerator is done to keep the
    unrelated tasks of enumeration and formatting apart.
    """

    def __init__(self, outfile, options, *args):
        self.options = options
        BaseFormatter.__init__(self)
        Writer.__init__(self, outfile, *args)

    # Re-add the `typing` prefix that inspect would throw away.
    # We do that by overwriting the relevant part of the function.

    backup = inspect.formatannotation

    @classmethod
    def formatannotation(cls, annotation, base_module=None, *args, **kwargs):
        if getattr(annotation, '__module__', None) == 'typing':
            # do not remove the prefix!
            return repr(annotation)
        # do the normal action.
        return cls.backup(annotation, base_module, *args, **kwargs)

    @classmethod
    def fix_typing_prefix(cls, signature):
        # modify the module, format the signature, restore the module.
        inspect.formatannotation = cls.formatannotation
        stringized = str(signature)
        inspect.formatannotation = cls.backup
        return stringized

    @classmethod
    def normalize_type(cls, type_repr: str) -> str:
        if not type_repr:
            return "typing.Any"
        if type_repr in {"void", "void*"}:
            return "typing.Any"
        if any(x in type_repr for x in ("QRhi", ".ComponentType", ".Semantic")):
            return "int"
        if ( " " in type_repr and
            not any(x in type_repr for x in ("*", "::", "<", ">", "[", "]"))):
            return "typing.Any"
        if type_repr.startswith("QList["):
            inner = type_repr[len("QList["):-1]
            inner = cls.normalize_type(inner)
            return f"typing.List[{inner}]"
        if type_repr.startswith("QMap[") or type_repr.startswith("QHash["):
            inner = type_repr[type_repr.find("[") + 1:-1]
            key, value = map(str.strip, inner.split(",", 1))
            key = cls.normalize_type(key)
            value = cls.normalize_type(value)
            return f"typing.Dict[{key}, {value}]"
        return TYPE_MAP.get(type_repr, type_repr)

    # Adding a pattern to substitute "Union[T, NoneType]" by "Optional[T]"
    # I tried hard to replace typing.Optional by a simple override, but
    # this became _way_ too much.
    # See also the comment in layout.py .

    # PYSIDE-2786: Since Python 3.9, we can use the "|" notation.
    #              Transform "Union" and "Optional" this way.
    brace_pat = build_brace_pattern(3, ",=")
    opt_uni_searcher = re.compile(fr"""
            \b                      # edge of a word
            (typing\.Optional |
             typing\.Union)         # word to find
            \s*                     # optional whitespace
            (?= \[ )                # Lookahead enforces a square bracket
            {brace_pat}             # braces tower, one capturing brace level
        """, flags=re.VERBOSE)
    brace_searcher = re.compile(brace_pat, flags=re.VERBOSE)
    split = brace_searcher.split

    @classmethod
    def last_fixups(cls, source):
        # PYSIDE-2517: findChild/findChildren type hints:
        # PlaceholderType fix to avoid the '~' from TypeVar.__repr__
        if "~PlaceholderType" in source:
            source = source.replace("~PlaceholderType", "PlaceholderType")
        if "~_QmlType" in source:
            source = source.replace("~_QmlType", "_QmlType")
        # Replace all "NoneType" strings by "None" which is a typing convention.
        return source.replace("NoneType", "None")

    # self.is_method() is true for non-plain functions.

    def section(self):
        self.print()

    @contextmanager
    def module(self, mod_name):
        self.mod_name = mod_name
        txt = f"""\
            # Module `{mod_name}`

            <<IMPORTS>>
            """
        self.print(dedent(txt))
        yield

    @contextmanager
    def klass(self, class_name, class_str, has_misc_error=None):
        override = StubOverrides.get((self.mod_name, class_name), None)
        spaces = indent * self.level
        if override is not None:
            self.print(f"{spaces}{override[0]}")
        else:
            err_ignore = "  # type: ignore[misc]"
            opt_comment = err_ignore if has_misc_error else ""
            while "." in class_name:
                class_name = class_name.split(".", 1)[-1]
                class_str = class_str.split(".", 1)[-1]
            self.print(f"{spaces}class {class_str}:{opt_comment}")
        self.level += 1
        yield
        spaces_2 = indent * self.level
        if override is not None:
            self.print(spaces_2 + f"\n{spaces_2}".join(override[1].split("\n")))
        elif not self.have_body:
            self.print(f"{spaces_2}...")
            self.print()
        self.level -= 1

    @contextmanager
    def function(self, func_name, signature, decorator=None, aug_ass=None, incon_err=None):
        key = func_name
        spaces = indent * self.level
        err_ignore = "  # type: ignore[misc]"
        if incon_err:
            err_ignore = "  # type: ignore[misc, overload-cannot-match]"
        if isinstance(signature, list):
            # PYSIDE-2846: Disable errors in augmented assignments.
            opt_comment = (err_ignore if aug_ass or incon_err else "")
            for sig in signature:
                self.print(f'{spaces}@typing.overload{opt_comment}')
                if incon_err:
                    # need to mark all overloads
                    pass
                else:
                    opt_comment = ""
                self._function(func_name, sig, spaces, None, opt_comment)
        else:
            opt_comment = err_ignore if aug_ass else ""
            self._function(func_name, signature, spaces, decorator, opt_comment)
        yield key

    def _function(self, func_name, signature, spaces, decorator=None, opt_comment=""):
        if decorator:
            # In case of a PyClassProperty the classmethod decorator is not used.
            self.print(f'{spaces}@{decorator}')
        elif self.is_method() and "self" not in signature.parameters:
            kind = "class" if "cls" in signature.parameters else "static"
            self.print(f'{spaces}@{kind}method')
        # the formatting with the inspect module explicitly removes the `typing` prefix.
        signature = self.fix_typing_prefix(signature)
        # from now on, the signature will be stringized.
        signature = self.last_fixups(signature)
        self.print(f'{spaces}def {func_name}{signature}: ...{opt_comment}')

    @contextmanager
    def enum(self, class_name, enum_name, value):
        spaces = indent * self.level
        hexval = hex(value)
        self.print(f"{spaces}{enum_name:25} = {hexval if value >= 0 else value}")
        yield

    @contextmanager
    def attribute(self, attr_name, attr_value):
        spaces = indent * self.level
        # PYSIDE-2903: Use a fully qualified name in the type comment.
        full_name = f"{type(attr_value).__module__}.{type(attr_value).__qualname__}"
        if full_name == "builtins.getset_descriptor":
            # PYSIDE-3034: Public variable types added to __doc__
            type_repr = self.normalize_type(attr_value.__doc__)
            self.print(f"{spaces}@property")
            self.print(f"{spaces}def {attr_name}(self) -> {type_repr}: ...")
            self.print(f"{spaces}@{attr_name}.setter")
            self.print(f"{spaces}def {attr_name}(self, {attr_name}: {type_repr}) -> None: ...")
        else:
            self.print(f"{spaces}{attr_name:25} = ...  # type: {full_name}")
        yield

    @contextmanager
    def signal(self, class_name, sig_name, sig_strs: list[str]):
        spaces = indent * self.level
        spaces_2 = indent * (self.level + 1)

        emit_signatures: list[list[str]] = []
        for sig_str in sig_strs:
            sig = []
            signatures = sig_str.split("(", 1)[1].rsplit(")", 1)[0].split(",")
            while signatures:
                type_hint = signatures.pop(0)
                if type_hint.count("<") != type_hint.count(">"):
                    type_hint += f",{signatures.pop(0)}"
                type_hint = type_hint.strip()
                if not type_hint:
                    continue
                type_hint = cpp_to_py(type_hint)
                sig.append(self.normalize_type(type_hint))
            if sig not in emit_signatures:
                emit_signatures.append(sig)

        arg_signatures: list[list[str]] = [[]]
        for sigs in emit_signatures:
            while sigs:
                if sigs not in arg_signatures:
                    arg_signatures.insert(-1, sigs)
                sigs = sigs[:-1]

        if len(arg_signatures) > MaxSignalSignatures:
            raise RuntimeError(f"{sig_name} has more signatures than has been configured. ({len(arg_signatures)} > {MaxSignalSignatures})")

        # Pad unused signatures with the first signature.
        emit_signatures += [emit_signatures[0]] * (MaxSignalSignatures - len(emit_signatures))
        arg_signatures += [arg_signatures[-1]] * (MaxSignalSignatures - len(arg_signatures))

        emit_hints = ", ".join([f"[{', '.join(sig)}]" for sig in emit_signatures])
        arg_hints = ", ".join([f"[{', '.join(sig)}]" for sig in arg_signatures])
        signature_comment = "; ".join(sig_strs)
        self.print(f"{spaces}# {signature_comment}")
        self.print(f"{spaces}{sig_name}: typing.ClassVar[{class_name}[")
        self.print(f"{spaces_2}{arg_hints},")
        self.print(f"{spaces_2}{emit_hints}")
        self.print(f"{spaces}]]")

        yield


def find_imports(text):
    return [imp for imp in PySide6.__all__ if f"PySide6.{imp}." in text]


FROM_IMPORTS = [
    (None, ["builtins"]),
    (None, ["os"]),
    (None, ["enum"]),
    (None, ["typing"]),
    (None, ["collections.abc"]),
    ("PySide6.QtCore", ["PyClassProperty", "Signal", "SignalInstance"]),
    ("shiboken6", ["Shiboken"]),
    ]


def filter_from_imports(from_struct, text):
    """
    Build a reduced new `from` structure (nfs) with found entries, only
    """
    nfs = []
    for mod, imports in from_struct:
        lis = []
        nfs.append((mod, lis))
        for each in imports:
            # PYSIDE-1603: We search text that is a usage of the class `each`,
            #              but only if the class is not also defined here.
            if f"class {each}(" not in text and f"class {each}:" not in text:
                if re.search(rf"(\b|@){each}\b([^\s\(:]|\n)", text):
                    lis.append(each)
                # Search if a type is present in the return statement
                # of function declarations: '... -> here:'
                if re.search(rf"->.*{each}.*:", text):
                    lis.append(each)
        if not lis:
            nfs.pop()
    return nfs


def find_module(import_name, outpath, from_pyside):
    """
    Find a module either directly by import, or use the full path,
    add the path to sys.path and import then.
    """
    if from_pyside:
        # internal mode for generate_pyi.py
        plainname = import_name.split(".")[-1]
        outfilepath = Path(outpath) / f"{plainname}.pyi"
        return import_name, plainname, outfilepath
    # we are alone in external module mode
    p = Path(import_name).resolve()
    if not p.exists():
        raise ValueError(f"File {p} does not exist.")
    if not outpath:
        outpath = p.parent
    # temporarily add the path and do the import
    sys.path.insert(0, os.fspath(p.parent))
    plainname = p.name.split(".")[0]
    __import__(plainname)
    sys.path.pop(0)
    return plainname, plainname, Path(outpath) / (plainname + ".pyi")


def generate_pyi(import_name, outpath, options):
    """
    Generates a .pyi file.
    """
    import_name, plainname, outfilepath = find_module(import_name, outpath, options._pyside_call)
    top = __import__(import_name)
    obj = getattr(top, plainname) if import_name != plainname else top
    if not getattr(obj, "__file__", None) or Path(obj.__file__).is_dir():
        raise ModuleNotFoundError(f"We do not accept a namespace as module `{plainname}`")

    outfile = io.StringIO()
    fmt = Formatter(outfile, options)
    fmt.print(LICENSE_TEXT.strip())
    fmt.print(dedent(f'''\
        """
        This file contains the exact signatures for all functions in module
        {import_name}, except for defaults which are replaced by "...".
        """
        '''))
    fmt.print(MYPY_TEXT.strip())
    HintingEnumerator(fmt).module(import_name)
    fmt.print("# eof")
    # Postprocess: resolve the imports
    if options._pyside_call:
        global PySide6
        import PySide6
    with outfilepath.open("w") as realfile:
        wr = Writer(realfile)
        outfile.seek(0)
        while True:
            line = outfile.readline()
            if not line:
                break
            line = line.rstrip()
            # we remove the "<<IMPORTS>>" marker and insert imports if needed
            if line == "<<IMPORTS>>":
                text = outfile.getvalue()
                wr.print("import " + import_name)
                for mod_name in find_imports(text):
                    imp = "PySide6." + mod_name
                    if imp != import_name:
                        wr.print("import " + imp)
                wr.print()
                for mod, imports in filter_from_imports(FROM_IMPORTS, text):
                    # Sorting, and getting uniques to avoid duplications
                    # on "Iterable" having a couple of entries.
                    import_args = ', '.join(sorted(set(imports)))
                    if mod is None:
                        # special case, a normal import
                        wr.print(f"import {import_args}")
                    else:
                        wr.print(f"from {mod} import {import_args}")
                wr.print()
                # We use it only in QtCore at the moment, but this
                # could be extended to other modules. (must import QObject then)
                if import_name == "PySide6.QtCore":
                    wr.print("PlaceholderType = typing.TypeVar(\"PlaceholderType\", "
                             "bound=PySide6.QtCore.QObject)")
                    wr.print('T = typing.TypeVar("T")')
                    for num in range(1, MaxSignalSignatures + 1):
                        wr.print(f'T{num} = typing.TypeVar("T{num}")')
                    wr.print('P = typing.ParamSpec("P")')
                    wr.print('R = typing.TypeVar("R")')
                    for num in range(1, MaxSignalSignatures + 1):
                        wr.print(f'EmitT{num} = typing.ParamSpec("EmitT{num}")')
                    for num in range(1, MaxSignalSignatures + 1):
                        wr.print(f'ArgsT{num} = typing.ParamSpec("ArgsT{num}")')
                    wr.print()
                    # PYSIDE-2516: Qt.KeyboardModifier and Qt.Modifier support cross-type | with
                    # Qt.Key producing QKeyCombination, which enum.Flag.__or__ cannot express.
                    # Therefore these overloads must be injected manually.
                    wr.print(dedent("""\
                        class _SupportsOrKey(enum.Flag): # type: ignore[misc]
                            @typing.overload
                            def __or__(self, other: typing.Self) -> Qt.KeyboardModifier: ...
                            @typing.overload
                            def __or__(self, other: Qt.Key) -> QKeyCombination: ...
                            @typing.overload
                            def __ror__(self, other: typing.Self) -> Qt.KeyboardModifier: ...
                            @typing.overload
                            def __ror__(self, other: Qt.Key) -> QKeyCombination: ...
                    """))
                elif import_name == "PySide6.QtQml":
                    wr.print("_QmlType  = typing.TypeVar(\"_QmlType\")")
                    wr.print()
                wr.print()
            else:
                wr.print(line)
    if not options.quiet:
        options.logger.info(f"Generated: {outfilepath}")


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=dedent("""\
            pyi_generator.py
            ----------------

            This script generates the .pyi file for an arbitrary module.
            You pass in the full path of a compiled, importable module.
            pyi_generator will try to generate an interface "<module>.pyi".
            """))
    parser.add_argument("module",
        help="The full path name of an importable module binary (.pyd, .so)")  # noqa E:128
    parser.add_argument("--quiet", action="store_true", help="Run quietly")
    parser.add_argument("--outpath",
        help="the output directory (default = location of module binary)")  # noqa E:128
    options = parser.parse_args()
    module = options.module
    outpath = options.outpath

    qtest_env = os.environ.get("QTEST_ENVIRONMENT", "")
    logging.basicConfig(level=logging.DEBUG if qtest_env else logging.INFO)
    logger = logging.getLogger("pyi_generator")

    if outpath and not Path(outpath).exists():
        os.makedirs(outpath)
        logger.info(f"+++ Created path {outpath}")
    options._pyside_call = False
    options.is_ci = qtest_env == "ci"

    options.logger = logger
    generate_pyi(module, outpath, options=options)


if __name__ == "__main__":
    main()
# eof
