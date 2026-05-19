# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
"""
This file contains the exact signatures for all functions in module
PySide6.Qt3DInput, except for defaults which are replaced by "...".
"""

# mypy: disable-error-code="override, overload-overlap"
# Module `PySide6.Qt3DInput`

import PySide6.Qt3DInput
import PySide6.QtCore
import PySide6.QtGui
import PySide6.Qt3DCore

import enum
import typing
import collections.abc
from PySide6.QtCore import Signal
import shiboken6


class QIntList:
    ...


class Qt3DInput(shiboken6.Shiboken.Object):
    class QAbstractActionInput(PySide6.Qt3DCore.Qt3DCore.QNode):
        ...

    class QAbstractAxisInput(PySide6.Qt3DCore.Qt3DCore.QNode):
        # sourceDeviceChanged(QAbstractPhysicalDevice*)
        sourceDeviceChanged: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice], [PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice], [PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice], [PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice], [PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice], [PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice], [PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice], [PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice]
        ]]

        def setSourceDevice(self, sourceDevice: PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice, /) -> None: ...
        def sourceDevice(self, /) -> PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice: ...

    class QAbstractPhysicalDevice(PySide6.Qt3DCore.Qt3DCore.QNode):
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...) -> None: ...

        def addAxisSetting(self, axisSetting: PySide6.Qt3DInput.Qt3DInput.QAxisSetting, /) -> None: ...
        def axisCount(self, /) -> int: ...
        def axisIdentifier(self, name: str, /) -> int: ...
        def axisNames(self, /) -> typing.List[str]: ...
        def axisSettings(self, /) -> typing.List[PySide6.Qt3DInput.Qt3DInput.QAxisSetting]: ...
        def buttonCount(self, /) -> int: ...
        def buttonIdentifier(self, name: str, /) -> int: ...
        def buttonNames(self, /) -> typing.List[str]: ...
        def removeAxisSetting(self, axisSetting: PySide6.Qt3DInput.Qt3DInput.QAxisSetting, /) -> None: ...

    class QAction(PySide6.Qt3DCore.Qt3DCore.QNode):
        # activeChanged(bool)
        activeChanged: typing.ClassVar[Signal[
            [bool], [], [], [], [], [], [], [],
            [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, active: bool | None = ...) -> None: ...

        def addInput(self, input: PySide6.Qt3DInput.Qt3DInput.QAbstractActionInput, /) -> None: ...
        def inputs(self, /) -> typing.List[PySide6.Qt3DInput.Qt3DInput.QAbstractActionInput]: ...
        def isActive(self, /) -> bool: ...
        def removeInput(self, input: PySide6.Qt3DInput.Qt3DInput.QAbstractActionInput, /) -> None: ...

    class QActionInput(PySide6.Qt3DInput.Qt3DInput.QAbstractActionInput):
        # buttonsChanged(QList<int>)
        buttonsChanged: typing.ClassVar[Signal[
            [collections.abc.Sequence[int]], [], [], [], [], [], [], [],
            [collections.abc.Sequence[int]], [collections.abc.Sequence[int]], [collections.abc.Sequence[int]], [collections.abc.Sequence[int]], [collections.abc.Sequence[int]], [collections.abc.Sequence[int]], [collections.abc.Sequence[int]], [collections.abc.Sequence[int]]
        ]]
        # sourceDeviceChanged(QAbstractPhysicalDevice*)
        sourceDeviceChanged: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice], [PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice], [PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice], [PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice], [PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice], [PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice], [PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice], [PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, sourceDevice: PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice | None = ..., buttons: collections.abc.Sequence[int] | None = ...) -> None: ...

        def buttons(self, /) -> typing.List[int]: ...
        def setButtons(self, buttons: collections.abc.Sequence[int], /) -> None: ...
        def setSourceDevice(self, sourceDevice: PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice, /) -> None: ...
        def sourceDevice(self, /) -> PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice: ...

    class QAnalogAxisInput(PySide6.Qt3DInput.Qt3DInput.QAbstractAxisInput):
        # axisChanged(int)
        axisChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, axis: int | None = ...) -> None: ...

        def axis(self, /) -> int: ...
        def setAxis(self, axis: int, /) -> None: ...

    class QAxis(PySide6.Qt3DCore.Qt3DCore.QNode):
        # valueChanged(float)
        valueChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, value: float | None = ...) -> None: ...

        def addInput(self, input: PySide6.Qt3DInput.Qt3DInput.QAbstractAxisInput, /) -> None: ...
        def inputs(self, /) -> typing.List[PySide6.Qt3DInput.Qt3DInput.QAbstractAxisInput]: ...
        def removeInput(self, input: PySide6.Qt3DInput.Qt3DInput.QAbstractAxisInput, /) -> None: ...
        def value(self, /) -> float: ...

    class QAxisAccumulator(PySide6.Qt3DCore.Qt3DCore.QComponent):
        # scaleChanged(float)
        scaleChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # sourceAxisChanged(Qt3DInput::QAxis*)
        sourceAxisChanged: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QAxis], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QAxis], [PySide6.Qt3DInput.Qt3DInput.QAxis], [PySide6.Qt3DInput.Qt3DInput.QAxis], [PySide6.Qt3DInput.Qt3DInput.QAxis], [PySide6.Qt3DInput.Qt3DInput.QAxis], [PySide6.Qt3DInput.Qt3DInput.QAxis], [PySide6.Qt3DInput.Qt3DInput.QAxis], [PySide6.Qt3DInput.Qt3DInput.QAxis]
        ]]
        # sourceAxisTypeChanged(QAxisAccumulator::SourceAxisType)
        sourceAxisTypeChanged: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QAxisAccumulator.SourceAxisType], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QAxisAccumulator.SourceAxisType], [PySide6.Qt3DInput.Qt3DInput.QAxisAccumulator.SourceAxisType], [PySide6.Qt3DInput.Qt3DInput.QAxisAccumulator.SourceAxisType], [PySide6.Qt3DInput.Qt3DInput.QAxisAccumulator.SourceAxisType], [PySide6.Qt3DInput.Qt3DInput.QAxisAccumulator.SourceAxisType], [PySide6.Qt3DInput.Qt3DInput.QAxisAccumulator.SourceAxisType], [PySide6.Qt3DInput.Qt3DInput.QAxisAccumulator.SourceAxisType], [PySide6.Qt3DInput.Qt3DInput.QAxisAccumulator.SourceAxisType]
        ]]
        # valueChanged(float)
        valueChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # velocityChanged(float)
        velocityChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]

        class SourceAxisType(enum.Enum):
            Velocity                  = 0x0
            Acceleration              = 0x1

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, sourceAxis: PySide6.Qt3DInput.Qt3DInput.QAxis | None = ..., sourceAxisType: PySide6.Qt3DInput.Qt3DInput.QAxisAccumulator.SourceAxisType | None = ..., scale: float | None = ..., value: float | None = ..., velocity: float | None = ...) -> None: ...

        def scale(self, /) -> float: ...
        def setScale(self, scale: float, /) -> None: ...
        def setSourceAxis(self, sourceAxis: PySide6.Qt3DInput.Qt3DInput.QAxis, /) -> None: ...
        def setSourceAxisType(self, sourceAxisType: PySide6.Qt3DInput.Qt3DInput.QAxisAccumulator.SourceAxisType, /) -> None: ...
        def sourceAxis(self, /) -> PySide6.Qt3DInput.Qt3DInput.QAxis: ...
        def sourceAxisType(self, /) -> PySide6.Qt3DInput.Qt3DInput.QAxisAccumulator.SourceAxisType: ...
        def value(self, /) -> float: ...
        def velocity(self, /) -> float: ...

    class QAxisSetting(PySide6.Qt3DCore.Qt3DCore.QNode):
        # axesChanged(QList<int>)
        axesChanged: typing.ClassVar[Signal[
            [collections.abc.Sequence[int]], [], [], [], [], [], [], [],
            [collections.abc.Sequence[int]], [collections.abc.Sequence[int]], [collections.abc.Sequence[int]], [collections.abc.Sequence[int]], [collections.abc.Sequence[int]], [collections.abc.Sequence[int]], [collections.abc.Sequence[int]], [collections.abc.Sequence[int]]
        ]]
        # deadZoneRadiusChanged(float)
        deadZoneRadiusChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # smoothChanged(bool)
        smoothChanged: typing.ClassVar[Signal[
            [bool], [], [], [], [], [], [], [],
            [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, deadZoneRadius: float | None = ..., axes: collections.abc.Sequence[int] | None = ..., smooth: bool | None = ...) -> None: ...

        def axes(self, /) -> typing.List[int]: ...
        def deadZoneRadius(self, /) -> float: ...
        def isSmoothEnabled(self, /) -> bool: ...
        def setAxes(self, axes: collections.abc.Sequence[int], /) -> None: ...
        def setDeadZoneRadius(self, deadZoneRadius: float, /) -> None: ...
        def setSmoothEnabled(self, enabled: bool, /) -> None: ...

    class QButtonAxisInput(PySide6.Qt3DInput.Qt3DInput.QAbstractAxisInput):
        # accelerationChanged(float)
        accelerationChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # buttonsChanged(QList<int>)
        buttonsChanged: typing.ClassVar[Signal[
            [collections.abc.Sequence[int]], [], [], [], [], [], [], [],
            [collections.abc.Sequence[int]], [collections.abc.Sequence[int]], [collections.abc.Sequence[int]], [collections.abc.Sequence[int]], [collections.abc.Sequence[int]], [collections.abc.Sequence[int]], [collections.abc.Sequence[int]], [collections.abc.Sequence[int]]
        ]]
        # decelerationChanged(float)
        decelerationChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # scaleChanged(float)
        scaleChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, scale: float | None = ..., buttons: collections.abc.Sequence[int] | None = ..., acceleration: float | None = ..., deceleration: float | None = ...) -> None: ...

        def acceleration(self, /) -> float: ...
        def buttons(self, /) -> typing.List[int]: ...
        def deceleration(self, /) -> float: ...
        def scale(self, /) -> float: ...
        def setAcceleration(self, acceleration: float, /) -> None: ...
        def setButtons(self, buttons: collections.abc.Sequence[int], /) -> None: ...
        def setDeceleration(self, deceleration: float, /) -> None: ...
        def setScale(self, scale: float, /) -> None: ...

    class QInputAspect(PySide6.Qt3DCore.Qt3DCore.QAbstractAspect):
        def __init__(self, /, parent: PySide6.QtCore.QObject | None = ...) -> None: ...

        def availablePhysicalDevices(self, /) -> typing.List[str]: ...
        def createPhysicalDevice(self, name: str, /) -> PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice: ...

    class QInputChord(PySide6.Qt3DInput.Qt3DInput.QAbstractActionInput):
        # timeoutChanged(int)
        timeoutChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, timeout: int | None = ...) -> None: ...

        def addChord(self, input: PySide6.Qt3DInput.Qt3DInput.QAbstractActionInput, /) -> None: ...
        def chords(self, /) -> typing.List[PySide6.Qt3DInput.Qt3DInput.QAbstractActionInput]: ...
        def removeChord(self, input: PySide6.Qt3DInput.Qt3DInput.QAbstractActionInput, /) -> None: ...
        def setTimeout(self, timeout: int, /) -> None: ...
        def timeout(self, /) -> int: ...

    class QInputSequence(PySide6.Qt3DInput.Qt3DInput.QAbstractActionInput):
        # buttonIntervalChanged(int)
        buttonIntervalChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]
        # timeoutChanged(int)
        timeoutChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, timeout: int | None = ..., buttonInterval: int | None = ...) -> None: ...

        def addSequence(self, input: PySide6.Qt3DInput.Qt3DInput.QAbstractActionInput, /) -> None: ...
        def buttonInterval(self, /) -> int: ...
        def removeSequence(self, input: PySide6.Qt3DInput.Qt3DInput.QAbstractActionInput, /) -> None: ...
        def sequences(self, /) -> typing.List[PySide6.Qt3DInput.Qt3DInput.QAbstractActionInput]: ...
        def setButtonInterval(self, buttonInterval: int, /) -> None: ...
        def setTimeout(self, timeout: int, /) -> None: ...
        def timeout(self, /) -> int: ...

    class QInputSettings(PySide6.Qt3DCore.Qt3DCore.QComponent):
        # eventSourceChanged(QObject*)
        eventSourceChanged: typing.ClassVar[Signal[
            [PySide6.QtCore.QObject], [], [], [], [], [], [], [],
            [PySide6.QtCore.QObject], [PySide6.QtCore.QObject], [PySide6.QtCore.QObject], [PySide6.QtCore.QObject], [PySide6.QtCore.QObject], [PySide6.QtCore.QObject], [PySide6.QtCore.QObject], [PySide6.QtCore.QObject]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, eventSource: PySide6.QtCore.QObject | None = ...) -> None: ...

        def eventSource(self, /) -> PySide6.QtCore.QObject: ...
        def setEventSource(self, eventSource: PySide6.QtCore.QObject, /) -> None: ...

    class QKeyEvent(PySide6.QtCore.QObject):
        @typing.overload
        def __init__(self, type: PySide6.QtCore.QEvent.Type, key: int, modifiers: PySide6.QtCore.Qt.KeyboardModifier, /, text: str = ..., autorep: bool = ..., count: int = ..., *, isAutoRepeat: bool | None = ..., nativeScanCode: int | None = ..., accepted: bool | None = ...) -> None: ...
        @typing.overload
        def __init__(self, ke: PySide6.QtGui.QKeyEvent, /, *, key: int | None = ..., text: str | None = ..., modifiers: int | None = ..., isAutoRepeat: bool | None = ..., count: int | None = ..., nativeScanCode: int | None = ..., accepted: bool | None = ...) -> None: ...

        def count(self, /) -> int: ...
        def isAccepted(self, /) -> bool: ...
        def isAutoRepeat(self, /) -> bool: ...
        def key(self, /) -> int: ...
        def matches(self, key_: PySide6.QtGui.QKeySequence.StandardKey, /) -> bool: ...
        def modifiers(self, /) -> int: ...
        def nativeScanCode(self, /) -> int: ...
        def setAccepted(self, accepted: bool, /) -> None: ...
        def text(self, /) -> str: ...
        def type(self, /) -> PySide6.QtCore.QEvent.Type: ...

    class QKeyboardDevice(PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice):
        # activeInputChanged(QKeyboardHandler*)
        activeInputChanged: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyboardHandler], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyboardHandler], [PySide6.Qt3DInput.Qt3DInput.QKeyboardHandler], [PySide6.Qt3DInput.Qt3DInput.QKeyboardHandler], [PySide6.Qt3DInput.Qt3DInput.QKeyboardHandler], [PySide6.Qt3DInput.Qt3DInput.QKeyboardHandler], [PySide6.Qt3DInput.Qt3DInput.QKeyboardHandler], [PySide6.Qt3DInput.Qt3DInput.QKeyboardHandler], [PySide6.Qt3DInput.Qt3DInput.QKeyboardHandler]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, activeInput: PySide6.Qt3DInput.Qt3DInput.QKeyboardHandler | None = ...) -> None: ...

        def activeInput(self, /) -> PySide6.Qt3DInput.Qt3DInput.QKeyboardHandler: ...
        def axisCount(self, /) -> int: ...
        def axisIdentifier(self, name: str, /) -> int: ...
        def axisNames(self, /) -> typing.List[str]: ...
        def buttonCount(self, /) -> int: ...
        def buttonIdentifier(self, name: str, /) -> int: ...
        def buttonNames(self, /) -> typing.List[str]: ...

    class QKeyboardHandler(PySide6.Qt3DCore.Qt3DCore.QComponent):
        # asteriskPressed(Qt3DInput::QKeyEvent*)
        asteriskPressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # backPressed(Qt3DInput::QKeyEvent*)
        backPressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # backtabPressed(Qt3DInput::QKeyEvent*)
        backtabPressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # callPressed(Qt3DInput::QKeyEvent*)
        callPressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # cancelPressed(Qt3DInput::QKeyEvent*)
        cancelPressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # context1Pressed(Qt3DInput::QKeyEvent*)
        context1Pressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # context2Pressed(Qt3DInput::QKeyEvent*)
        context2Pressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # context3Pressed(Qt3DInput::QKeyEvent*)
        context3Pressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # context4Pressed(Qt3DInput::QKeyEvent*)
        context4Pressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # deletePressed(Qt3DInput::QKeyEvent*)
        deletePressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # digit0Pressed(Qt3DInput::QKeyEvent*)
        digit0Pressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # digit1Pressed(Qt3DInput::QKeyEvent*)
        digit1Pressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # digit2Pressed(Qt3DInput::QKeyEvent*)
        digit2Pressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # digit3Pressed(Qt3DInput::QKeyEvent*)
        digit3Pressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # digit4Pressed(Qt3DInput::QKeyEvent*)
        digit4Pressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # digit5Pressed(Qt3DInput::QKeyEvent*)
        digit5Pressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # digit6Pressed(Qt3DInput::QKeyEvent*)
        digit6Pressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # digit7Pressed(Qt3DInput::QKeyEvent*)
        digit7Pressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # digit8Pressed(Qt3DInput::QKeyEvent*)
        digit8Pressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # digit9Pressed(Qt3DInput::QKeyEvent*)
        digit9Pressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # downPressed(Qt3DInput::QKeyEvent*)
        downPressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # enterPressed(Qt3DInput::QKeyEvent*)
        enterPressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # escapePressed(Qt3DInput::QKeyEvent*)
        escapePressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # flipPressed(Qt3DInput::QKeyEvent*)
        flipPressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # focusChanged(bool)
        focusChanged: typing.ClassVar[Signal[
            [bool], [], [], [], [], [], [], [],
            [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
        ]]
        # hangupPressed(Qt3DInput::QKeyEvent*)
        hangupPressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # leftPressed(Qt3DInput::QKeyEvent*)
        leftPressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # menuPressed(Qt3DInput::QKeyEvent*)
        menuPressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # noPressed(Qt3DInput::QKeyEvent*)
        noPressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # numberSignPressed(Qt3DInput::QKeyEvent*)
        numberSignPressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # pressed(Qt3DInput::QKeyEvent*)
        pressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # released(Qt3DInput::QKeyEvent*)
        released: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # returnPressed(Qt3DInput::QKeyEvent*)
        returnPressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # rightPressed(Qt3DInput::QKeyEvent*)
        rightPressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # selectPressed(Qt3DInput::QKeyEvent*)
        selectPressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # sourceDeviceChanged(QKeyboardDevice*)
        sourceDeviceChanged: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyboardDevice], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyboardDevice], [PySide6.Qt3DInput.Qt3DInput.QKeyboardDevice], [PySide6.Qt3DInput.Qt3DInput.QKeyboardDevice], [PySide6.Qt3DInput.Qt3DInput.QKeyboardDevice], [PySide6.Qt3DInput.Qt3DInput.QKeyboardDevice], [PySide6.Qt3DInput.Qt3DInput.QKeyboardDevice], [PySide6.Qt3DInput.Qt3DInput.QKeyboardDevice], [PySide6.Qt3DInput.Qt3DInput.QKeyboardDevice]
        ]]
        # spacePressed(Qt3DInput::QKeyEvent*)
        spacePressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # tabPressed(Qt3DInput::QKeyEvent*)
        tabPressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # upPressed(Qt3DInput::QKeyEvent*)
        upPressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # volumeDownPressed(Qt3DInput::QKeyEvent*)
        volumeDownPressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # volumeUpPressed(Qt3DInput::QKeyEvent*)
        volumeUpPressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]
        # yesPressed(Qt3DInput::QKeyEvent*)
        yesPressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent], [PySide6.Qt3DInput.Qt3DInput.QKeyEvent]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, sourceDevice: PySide6.Qt3DInput.Qt3DInput.QKeyboardDevice | None = ..., focus: bool | None = ...) -> None: ...

        def focus(self, /) -> bool: ...
        def setFocus(self, focus: bool, /) -> None: ...
        def setSourceDevice(self, keyboardDevice: PySide6.Qt3DInput.Qt3DInput.QKeyboardDevice, /) -> None: ...
        def sourceDevice(self, /) -> PySide6.Qt3DInput.Qt3DInput.QKeyboardDevice: ...

    class QLogicalDevice(PySide6.Qt3DCore.Qt3DCore.QComponent):
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...) -> None: ...

        def actions(self, /) -> typing.List[PySide6.Qt3DInput.Qt3DInput.QAction]: ...
        def addAction(self, action: PySide6.Qt3DInput.Qt3DInput.QAction, /) -> None: ...
        def addAxis(self, axis: PySide6.Qt3DInput.Qt3DInput.QAxis, /) -> None: ...
        def axes(self, /) -> typing.List[PySide6.Qt3DInput.Qt3DInput.QAxis]: ...
        def removeAction(self, action: PySide6.Qt3DInput.Qt3DInput.QAction, /) -> None: ...
        def removeAxis(self, axis: PySide6.Qt3DInput.Qt3DInput.QAxis, /) -> None: ...

    class QMouseDevice(PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice):
        # sensitivityChanged(float)
        sensitivityChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # updateAxesContinuouslyChanged(bool)
        updateAxesContinuouslyChanged: typing.ClassVar[Signal[
            [bool], [], [], [], [], [], [], [],
            [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
        ]]

        class Axis(enum.Enum):
            X                         = 0x0
            Y                         = 0x1
            WheelX                    = 0x2
            WheelY                    = 0x3

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, sensitivity: float | None = ..., updateAxesContinuously: bool | None = ...) -> None: ...

        def axisCount(self, /) -> int: ...
        def axisIdentifier(self, name: str, /) -> int: ...
        def axisNames(self, /) -> typing.List[str]: ...
        def buttonCount(self, /) -> int: ...
        def buttonIdentifier(self, name: str, /) -> int: ...
        def buttonNames(self, /) -> typing.List[str]: ...
        def sensitivity(self, /) -> float: ...
        def setSensitivity(self, value: float, /) -> None: ...
        def setUpdateAxesContinuously(self, updateAxesContinuously: bool, /) -> None: ...
        def updateAxesContinuously(self, /) -> bool: ...

    class QMouseEvent(PySide6.QtCore.QObject):
        class Buttons(enum.Enum):
            NoButton                  = 0x0
            LeftButton                = 0x1
            RightButton               = 0x2
            MiddleButton              = 0x4
            BackButton                = 0x8

        class Modifiers(enum.Enum):
            NoModifier                = 0x0
            ShiftModifier             = 0x2000000
            ControlModifier           = 0x4000000
            AltModifier               = 0x8000000
            MetaModifier              = 0x10000000
            KeypadModifier            = 0x20000000

        def __init__(self, e: PySide6.QtGui.QMouseEvent, /, *, x: int | None = ..., y: int | None = ..., wasHeld: bool | None = ..., button: PySide6.Qt3DInput.Qt3DInput.QMouseEvent.Buttons | None = ..., buttons: int | None = ..., modifiers: PySide6.Qt3DInput.Qt3DInput.QMouseEvent.Modifiers | None = ..., accepted: bool | None = ...) -> None: ...

        def button(self, /) -> PySide6.Qt3DInput.Qt3DInput.QMouseEvent.Buttons: ...
        def buttons(self, /) -> int: ...
        def isAccepted(self, /) -> bool: ...
        def modifiers(self, /) -> PySide6.Qt3DInput.Qt3DInput.QMouseEvent.Modifiers: ...
        def setAccepted(self, accepted: bool, /) -> None: ...
        def type(self, /) -> PySide6.QtCore.QEvent.Type: ...
        def wasHeld(self, /) -> bool: ...
        def x(self, /) -> int: ...
        def y(self, /) -> int: ...

    class QMouseHandler(PySide6.Qt3DCore.Qt3DCore.QComponent):
        # clicked(Qt3DInput::QMouseEvent*)
        clicked: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent]
        ]]
        # containsMouseChanged(bool)
        containsMouseChanged: typing.ClassVar[Signal[
            [bool], [], [], [], [], [], [], [],
            [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
        ]]
        # doubleClicked(Qt3DInput::QMouseEvent*)
        doubleClicked: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent]
        ]]
        # entered()
        entered: typing.ClassVar[Signal[
            [], [], [], [], [], [], [], [],
            [], [], [], [], [], [], [], []
        ]]
        # exited()
        exited: typing.ClassVar[Signal[
            [], [], [], [], [], [], [], [],
            [], [], [], [], [], [], [], []
        ]]
        # positionChanged(Qt3DInput::QMouseEvent*)
        positionChanged: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent]
        ]]
        # pressAndHold(Qt3DInput::QMouseEvent*)
        pressAndHold: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent]
        ]]
        # pressed(Qt3DInput::QMouseEvent*)
        pressed: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent]
        ]]
        # released(Qt3DInput::QMouseEvent*)
        released: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent], [PySide6.Qt3DInput.Qt3DInput.QMouseEvent]
        ]]
        # sourceDeviceChanged(QMouseDevice*)
        sourceDeviceChanged: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QMouseDevice], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QMouseDevice], [PySide6.Qt3DInput.Qt3DInput.QMouseDevice], [PySide6.Qt3DInput.Qt3DInput.QMouseDevice], [PySide6.Qt3DInput.Qt3DInput.QMouseDevice], [PySide6.Qt3DInput.Qt3DInput.QMouseDevice], [PySide6.Qt3DInput.Qt3DInput.QMouseDevice], [PySide6.Qt3DInput.Qt3DInput.QMouseDevice], [PySide6.Qt3DInput.Qt3DInput.QMouseDevice]
        ]]
        # wheel(Qt3DInput::QWheelEvent*)
        wheel: typing.ClassVar[Signal[
            [PySide6.Qt3DInput.Qt3DInput.QWheelEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DInput.Qt3DInput.QWheelEvent], [PySide6.Qt3DInput.Qt3DInput.QWheelEvent], [PySide6.Qt3DInput.Qt3DInput.QWheelEvent], [PySide6.Qt3DInput.Qt3DInput.QWheelEvent], [PySide6.Qt3DInput.Qt3DInput.QWheelEvent], [PySide6.Qt3DInput.Qt3DInput.QWheelEvent], [PySide6.Qt3DInput.Qt3DInput.QWheelEvent], [PySide6.Qt3DInput.Qt3DInput.QWheelEvent]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, sourceDevice: PySide6.Qt3DInput.Qt3DInput.QMouseDevice | None = ..., containsMouse: bool | None = ...) -> None: ...

        def containsMouse(self, /) -> bool: ...
        def setContainsMouse(self, contains: bool, /) -> None: ...
        def setSourceDevice(self, mouseDevice: PySide6.Qt3DInput.Qt3DInput.QMouseDevice, /) -> None: ...
        def sourceDevice(self, /) -> PySide6.Qt3DInput.Qt3DInput.QMouseDevice: ...

    class QWheelEvent(PySide6.QtCore.QObject):
        class Buttons(enum.Enum):
            NoButton                  = 0x0
            LeftButton                = 0x1
            RightButton               = 0x2
            MiddleButton              = 0x4
            BackButton                = 0x8

        class Modifiers(enum.Enum):
            NoModifier                = 0x0
            ShiftModifier             = 0x2000000
            ControlModifier           = 0x4000000
            AltModifier               = 0x8000000
            MetaModifier              = 0x10000000
            KeypadModifier            = 0x20000000

        def __init__(self, e: PySide6.QtGui.QWheelEvent, /, *, x: int | None = ..., y: int | None = ..., angleDelta: PySide6.QtCore.QPoint | None = ..., buttons: int | None = ..., modifiers: PySide6.Qt3DInput.Qt3DInput.QWheelEvent.Modifiers | None = ..., accepted: bool | None = ...) -> None: ...

        def angleDelta(self, /) -> PySide6.QtCore.QPoint: ...
        def buttons(self, /) -> int: ...
        def isAccepted(self, /) -> bool: ...
        def modifiers(self, /) -> PySide6.Qt3DInput.Qt3DInput.QWheelEvent.Modifiers: ...
        def setAccepted(self, accepted: bool, /) -> None: ...
        def type(self, /) -> PySide6.QtCore.QEvent.Type: ...
        def x(self, /) -> int: ...
        def y(self, /) -> int: ...


# eof
