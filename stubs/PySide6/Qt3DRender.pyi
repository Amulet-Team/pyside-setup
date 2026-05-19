# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
"""
This file contains the exact signatures for all functions in module
PySide6.Qt3DRender, except for defaults which are replaced by "...".
"""

# mypy: disable-error-code="override, overload-overlap"
# Module `PySide6.Qt3DRender`

import PySide6.Qt3DRender
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtMultimedia
import PySide6.QtOpenGL
import PySide6.Qt3DCore

import enum
import typing
import collections.abc
from PySide6.QtCore import Signal
import shiboken6


class QIntList:
    ...


class Qt3DRender(shiboken6.Shiboken.Object):
    class API(enum.Enum):
        OpenGL                    = 0x0
        Vulkan                    = 0x1
        DirectX                   = 0x2
        Metal                     = 0x3
        RHI                       = 0x4
        Null                      = 0x5

    class PropertyReaderInterface(shiboken6.Shiboken.Object):
        def __init__(self, /) -> None: ...

        def readProperty(self, v: typing.Any, /) -> typing.Any: ...

    class PropertyReaderInterfacePtr(shiboken6.Shiboken.Object):
        @typing.overload
        def __init__(self, /) -> None: ...
        @typing.overload
        def __init__(self, pointee: PySide6.Qt3DRender.Qt3DRender.PropertyReaderInterface, /) -> None: ...

        def __copy__(self, /) -> PySide6.Qt3DRender.Qt3DRender.PropertyReaderInterfacePtr: ...
        def __dir__(self, /) -> collections.abc.Iterable[str]: ...
        def __repr__(self, /) -> str: ...
        def data(self, /) -> PySide6.Qt3DRender.Qt3DRender.PropertyReaderInterface: ...
        @typing.overload
        def reset(self, /) -> None: ...
        @typing.overload
        def reset(self, t: PySide6.Qt3DRender.Qt3DRender.PropertyReaderInterface, /) -> None: ...

    class QAbstractLight(PySide6.Qt3DCore.Qt3DCore.QComponent):
        # colorChanged(QColor)
        colorChanged: typing.ClassVar[Signal[
            [PySide6.QtGui.QColor], [], [], [], [], [], [], [],
            [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor]
        ]]
        # intensityChanged(float)
        intensityChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]

        class Type(enum.Enum):
            PointLight                = 0x0
            DirectionalLight          = 0x1
            SpotLight                 = 0x2

        def color(self, /) -> PySide6.QtGui.QColor: ...
        def intensity(self, /) -> float: ...
        def setColor(self, color: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
        def setIntensity(self, intensity: float, /) -> None: ...
        def type(self, /) -> PySide6.Qt3DRender.Qt3DRender.QAbstractLight.Type: ...

    class QAbstractRayCaster(PySide6.Qt3DCore.Qt3DCore.QComponent):
        # filterModeChanged(Qt3DRender::QAbstractRayCaster::FilterMode)
        filterModeChanged: typing.ClassVar[Signal[
            [PySide6.Qt3DRender.Qt3DRender.QAbstractRayCaster.FilterMode], [], [], [], [], [], [], [],
            [PySide6.Qt3DRender.Qt3DRender.QAbstractRayCaster.FilterMode], [PySide6.Qt3DRender.Qt3DRender.QAbstractRayCaster.FilterMode], [PySide6.Qt3DRender.Qt3DRender.QAbstractRayCaster.FilterMode], [PySide6.Qt3DRender.Qt3DRender.QAbstractRayCaster.FilterMode], [PySide6.Qt3DRender.Qt3DRender.QAbstractRayCaster.FilterMode], [PySide6.Qt3DRender.Qt3DRender.QAbstractRayCaster.FilterMode], [PySide6.Qt3DRender.Qt3DRender.QAbstractRayCaster.FilterMode], [PySide6.Qt3DRender.Qt3DRender.QAbstractRayCaster.FilterMode]
        ]]
        # hitsChanged(Qt3DRender::QAbstractRayCaster::Hits)
        hitsChanged: typing.ClassVar[Signal[
            [collections.abc.Sequence[PySide6.Qt3DRender.Qt3DRender.QRayCasterHit]], [], [], [], [], [], [], [],
            [collections.abc.Sequence[PySide6.Qt3DRender.Qt3DRender.QRayCasterHit]], [collections.abc.Sequence[PySide6.Qt3DRender.Qt3DRender.QRayCasterHit]], [collections.abc.Sequence[PySide6.Qt3DRender.Qt3DRender.QRayCasterHit]], [collections.abc.Sequence[PySide6.Qt3DRender.Qt3DRender.QRayCasterHit]], [collections.abc.Sequence[PySide6.Qt3DRender.Qt3DRender.QRayCasterHit]], [collections.abc.Sequence[PySide6.Qt3DRender.Qt3DRender.QRayCasterHit]], [collections.abc.Sequence[PySide6.Qt3DRender.Qt3DRender.QRayCasterHit]], [collections.abc.Sequence[PySide6.Qt3DRender.Qt3DRender.QRayCasterHit]]
        ]]
        # runModeChanged(Qt3DRender::QAbstractRayCaster::RunMode)
        runModeChanged: typing.ClassVar[Signal[
            [PySide6.Qt3DRender.Qt3DRender.QAbstractRayCaster.RunMode], [], [], [], [], [], [], [],
            [PySide6.Qt3DRender.Qt3DRender.QAbstractRayCaster.RunMode], [PySide6.Qt3DRender.Qt3DRender.QAbstractRayCaster.RunMode], [PySide6.Qt3DRender.Qt3DRender.QAbstractRayCaster.RunMode], [PySide6.Qt3DRender.Qt3DRender.QAbstractRayCaster.RunMode], [PySide6.Qt3DRender.Qt3DRender.QAbstractRayCaster.RunMode], [PySide6.Qt3DRender.Qt3DRender.QAbstractRayCaster.RunMode], [PySide6.Qt3DRender.Qt3DRender.QAbstractRayCaster.RunMode], [PySide6.Qt3DRender.Qt3DRender.QAbstractRayCaster.RunMode]
        ]]

        class FilterMode(enum.Enum):
            AcceptAnyMatchingLayers   = 0x0
            AcceptAllMatchingLayers   = 0x1
            DiscardAnyMatchingLayers  = 0x2
            DiscardAllMatchingLayers  = 0x3

        class RunMode(enum.Enum):
            Continuous                = 0x0
            SingleShot                = 0x1

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, runMode: PySide6.Qt3DRender.Qt3DRender.QAbstractRayCaster.RunMode | None = ..., filterMode: PySide6.Qt3DRender.Qt3DRender.QAbstractRayCaster.FilterMode | None = ..., hits: collections.abc.Sequence[PySide6.Qt3DRender.Qt3DRender.QRayCasterHit] | None = ...) -> None: ...

        def addLayer(self, layer: PySide6.Qt3DRender.Qt3DRender.QLayer, /) -> None: ...
        def filterMode(self, /) -> PySide6.Qt3DRender.Qt3DRender.QAbstractRayCaster.FilterMode: ...
        def hits(self, /) -> typing.List[PySide6.Qt3DRender.Qt3DRender.QRayCasterHit]: ...
        def layers(self, /) -> typing.List[PySide6.Qt3DRender.Qt3DRender.QLayer]: ...
        def removeLayer(self, layer: PySide6.Qt3DRender.Qt3DRender.QLayer, /) -> None: ...
        def runMode(self, /) -> PySide6.Qt3DRender.Qt3DRender.QAbstractRayCaster.RunMode: ...
        def setFilterMode(self, filterMode: PySide6.Qt3DRender.Qt3DRender.QAbstractRayCaster.FilterMode, /) -> None: ...
        def setRunMode(self, runMode: PySide6.Qt3DRender.Qt3DRender.QAbstractRayCaster.RunMode, /) -> None: ...

    class QAbstractTexture(PySide6.Qt3DCore.Qt3DCore.QNode):
        # comparisonFunctionChanged(ComparisonFunction)
        comparisonFunctionChanged: typing.ClassVar[Signal[
            [ComparisonFunction], [], [], [], [], [], [], [],
            [ComparisonFunction], [ComparisonFunction], [ComparisonFunction], [ComparisonFunction], [ComparisonFunction], [ComparisonFunction], [ComparisonFunction], [ComparisonFunction]
        ]]
        # comparisonModeChanged(ComparisonMode)
        comparisonModeChanged: typing.ClassVar[Signal[
            [ComparisonMode], [], [], [], [], [], [], [],
            [ComparisonMode], [ComparisonMode], [ComparisonMode], [ComparisonMode], [ComparisonMode], [ComparisonMode], [ComparisonMode], [ComparisonMode]
        ]]
        # depthChanged(int)
        depthChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]
        # formatChanged(TextureFormat)
        formatChanged: typing.ClassVar[Signal[
            [TextureFormat], [], [], [], [], [], [], [],
            [TextureFormat], [TextureFormat], [TextureFormat], [TextureFormat], [TextureFormat], [TextureFormat], [TextureFormat], [TextureFormat]
        ]]
        # generateMipMapsChanged(bool)
        generateMipMapsChanged: typing.ClassVar[Signal[
            [bool], [], [], [], [], [], [], [],
            [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
        ]]
        # handleChanged(QVariant)
        handleChanged: typing.ClassVar[Signal[
            [typing.Any], [], [], [], [], [], [], [],
            [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any]
        ]]
        # handleTypeChanged(HandleType)
        handleTypeChanged: typing.ClassVar[Signal[
            [HandleType], [], [], [], [], [], [], [],
            [HandleType], [HandleType], [HandleType], [HandleType], [HandleType], [HandleType], [HandleType], [HandleType]
        ]]
        # heightChanged(int)
        heightChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]
        # layersChanged(int)
        layersChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]
        # magnificationFilterChanged(Filter)
        magnificationFilterChanged: typing.ClassVar[Signal[
            [Filter], [], [], [], [], [], [], [],
            [Filter], [Filter], [Filter], [Filter], [Filter], [Filter], [Filter], [Filter]
        ]]
        # maximumAnisotropyChanged(float)
        maximumAnisotropyChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # minificationFilterChanged(Filter)
        minificationFilterChanged: typing.ClassVar[Signal[
            [Filter], [], [], [], [], [], [], [],
            [Filter], [Filter], [Filter], [Filter], [Filter], [Filter], [Filter], [Filter]
        ]]
        # mipLevelsChanged(int)
        mipLevelsChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]
        # samplesChanged(int)
        samplesChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]
        # statusChanged(Status)
        statusChanged: typing.ClassVar[Signal[
            [Status], [], [], [], [], [], [], [],
            [Status], [Status], [Status], [Status], [Status], [Status], [Status], [Status]
        ]]
        # widthChanged(int)
        widthChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]

        class ComparisonFunction(enum.Enum):
            CompareNever              = 0x200
            CompareLess               = 0x201
            CompareEqual              = 0x202
            CompareLessEqual          = 0x203
            CompareGreater            = 0x204
            CommpareNotEqual          = 0x205
            CompareGreaterEqual       = 0x206
            CompareAlways             = 0x207

        class ComparisonMode(enum.Enum):
            CompareNone               = 0x0
            CompareRefToTexture       = 0x884e

        class CubeMapFace(enum.Enum):
            CubeMapPositiveX          = 0x8515
            CubeMapNegativeX          = 0x8516
            CubeMapPositiveY          = 0x8517
            CubeMapNegativeY          = 0x8518
            CubeMapPositiveZ          = 0x8519
            CubeMapNegativeZ          = 0x851a
            AllFaces                  = 0x851b

        class Filter(enum.Enum):
            Nearest                   = 0x2600
            Linear                    = 0x2601
            NearestMipMapNearest      = 0x2700
            LinearMipMapNearest       = 0x2701
            NearestMipMapLinear       = 0x2702
            LinearMipMapLinear        = 0x2703

        class HandleType(enum.Enum):
            NoHandle                  = 0x0
            OpenGLTextureId           = 0x1
            RHITextureId              = 0x2

        class Status(enum.Enum):
            None_                     = 0x0
            Loading                   = 0x1
            Ready                     = 0x2
            Error                     = 0x3

        class Target(enum.Enum):
            TargetAutomatic           = 0x0
            Target1D                  = 0xde0
            Target2D                  = 0xde1
            Target3D                  = 0x806f
            TargetRectangle           = 0x84f5
            TargetCubeMap             = 0x8513
            Target1DArray             = 0x8c18
            Target2DArray             = 0x8c1a
            TargetBuffer              = 0x8c2a
            TargetCubeMapArray        = 0x9009
            Target2DMultisample       = 0x9100
            Target2DMultisampleArray  = 0x9102

        class TextureFormat(enum.Enum):
            NoFormat                  = 0x0
            Automatic                 = 0x1
            DepthFormat               = 0x1902
            AlphaFormat               = 0x1906
            RGBFormat                 = 0x1907
            RGBAFormat                = 0x1908
            LuminanceFormat           = 0x1909
            LuminanceAlphaFormat      = 0x190a
            RG3B2                     = 0x2a10
            RGB8_UNorm                = 0x8051
            RGB16_UNorm               = 0x8054
            RGBA4                     = 0x8056
            RGB5A1                    = 0x8057
            RGBA8_UNorm               = 0x8058
            RGB10A2                   = 0x8059
            RGBA16_UNorm              = 0x805b
            D16                       = 0x81a5
            D24                       = 0x81a6
            D32                       = 0x81a7
            R8_UNorm                  = 0x8229
            R16_UNorm                 = 0x822a
            RG8_UNorm                 = 0x822b
            RG16_UNorm                = 0x822c
            R16F                      = 0x822d
            R32F                      = 0x822e
            RG16F                     = 0x822f
            RG32F                     = 0x8230
            R8I                       = 0x8231
            R8U                       = 0x8232
            R16I                      = 0x8233
            R16U                      = 0x8234
            R32I                      = 0x8235
            R32U                      = 0x8236
            RG8I                      = 0x8237
            RG8U                      = 0x8238
            RG16I                     = 0x8239
            RG16U                     = 0x823a
            RG32I                     = 0x823b
            RG32U                     = 0x823c
            RGB_DXT1                  = 0x83f0
            RGBA_DXT1                 = 0x83f1
            RGBA_DXT3                 = 0x83f2
            RGBA_DXT5                 = 0x83f3
            RGBA32F                   = 0x8814
            RGB32F                    = 0x8815
            RGBA16F                   = 0x881a
            RGB16F                    = 0x881b
            D24S8                     = 0x88f0
            RG11B10F                  = 0x8c3a
            RGB9E5                    = 0x8c3d
            SRGB8                     = 0x8c41
            SRGB8_Alpha8              = 0x8c43
            SRGB_DXT1                 = 0x8c4c
            SRGB_Alpha_DXT1           = 0x8c4d
            SRGB_Alpha_DXT3           = 0x8c4e
            SRGB_Alpha_DXT5           = 0x8c4f
            D32F                      = 0x8cac
            D32FS8X24                 = 0x8cad
            R5G6B5                    = 0x8d62
            RGB8_ETC1                 = 0x8d64
            RGBA32U                   = 0x8d70
            RGB32U                    = 0x8d71
            RGBA16U                   = 0x8d76
            RGB16U                    = 0x8d77
            RGBA8U                    = 0x8d7c
            RGB8U                     = 0x8d7d
            RGBA32I                   = 0x8d82
            RGB32I                    = 0x8d83
            RGBA16I                   = 0x8d88
            RGB16I                    = 0x8d89
            RGBA8I                    = 0x8d8e
            RGB8I                     = 0x8d8f
            R_ATI1N_UNorm             = 0x8dbb
            R_ATI1N_SNorm             = 0x8dbc
            RG_ATI2N_UNorm            = 0x8dbd
            RG_ATI2N_SNorm            = 0x8dbe
            RGB_BP_UNorm              = 0x8e8c
            SRGB_BP_UNorm             = 0x8e8d
            RGB_BP_SIGNED_FLOAT       = 0x8e8e
            RGB_BP_UNSIGNED_FLOAT     = 0x8e8f
            R8_SNorm                  = 0x8f94
            RG8_SNorm                 = 0x8f95
            RGB8_SNorm                = 0x8f96
            RGBA8_SNorm               = 0x8f97
            R16_SNorm                 = 0x8f98
            RG16_SNorm                = 0x8f99
            RGB16_SNorm               = 0x8f9a
            RGBA16_SNorm              = 0x8f9b
            RGB10A2U                  = 0x906f
            R11_EAC_UNorm             = 0x9270
            R11_EAC_SNorm             = 0x9271
            RG11_EAC_UNorm            = 0x9272
            RG11_EAC_SNorm            = 0x9273
            RGB8_ETC2                 = 0x9274
            SRGB8_ETC2                = 0x9275
            RGB8_PunchThrough_Alpha1_ETC2 = 0x9276
            SRGB8_PunchThrough_Alpha1_ETC2 = 0x9277
            RGBA8_ETC2_EAC            = 0x9278
            SRGB8_Alpha8_ETC2_EAC     = 0x9279

        @typing.overload
        def __init__(self, target: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.Target, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, format: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.TextureFormat | None = ..., generateMipMaps: bool | None = ..., wrapMode: PySide6.Qt3DRender.Qt3DRender.QTextureWrapMode | None = ..., status: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.Status | None = ..., width: int | None = ..., height: int | None = ..., depth: int | None = ..., mipLevels: int | None = ..., magnificationFilter: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.Filter | None = ..., minificationFilter: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.Filter | None = ..., maximumAnisotropy: float | None = ..., comparisonFunction: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.ComparisonFunction | None = ..., comparisonMode: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.ComparisonMode | None = ..., layers: int | None = ..., samples: int | None = ..., handleType: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.HandleType | None = ..., handle: typing.Any | None = ...) -> None: ...
        @typing.overload
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, target: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.Target | None = ..., format: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.TextureFormat | None = ..., generateMipMaps: bool | None = ..., wrapMode: PySide6.Qt3DRender.Qt3DRender.QTextureWrapMode | None = ..., status: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.Status | None = ..., width: int | None = ..., height: int | None = ..., depth: int | None = ..., mipLevels: int | None = ..., magnificationFilter: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.Filter | None = ..., minificationFilter: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.Filter | None = ..., maximumAnisotropy: float | None = ..., comparisonFunction: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.ComparisonFunction | None = ..., comparisonMode: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.ComparisonMode | None = ..., layers: int | None = ..., samples: int | None = ..., handleType: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.HandleType | None = ..., handle: typing.Any | None = ...) -> None: ...

        def addTextureImage(self, textureImage: PySide6.Qt3DRender.Qt3DRender.QAbstractTextureImage, /) -> None: ...
        def comparisonFunction(self, /) -> PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.ComparisonFunction: ...
        def comparisonMode(self, /) -> PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.ComparisonMode: ...
        def depth(self, /) -> int: ...
        def format(self, /) -> PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.TextureFormat: ...
        def generateMipMaps(self, /) -> bool: ...
        def handle(self, /) -> typing.Any: ...
        def handleType(self, /) -> PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.HandleType: ...
        def height(self, /) -> int: ...
        def layers(self, /) -> int: ...
        def magnificationFilter(self, /) -> PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.Filter: ...
        def maximumAnisotropy(self, /) -> float: ...
        def minificationFilter(self, /) -> PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.Filter: ...
        def mipLevels(self, /) -> int: ...
        def removeTextureImage(self, textureImage: PySide6.Qt3DRender.Qt3DRender.QAbstractTextureImage, /) -> None: ...
        def samples(self, /) -> int: ...
        def setComparisonFunction(self, function: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.ComparisonFunction, /) -> None: ...
        def setComparisonMode(self, mode: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.ComparisonMode, /) -> None: ...
        def setDepth(self, depth: int, /) -> None: ...
        def setFormat(self, format: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.TextureFormat, /) -> None: ...
        def setGenerateMipMaps(self, gen: bool, /) -> None: ...
        def setHandle(self, handle: typing.Any, /) -> None: ...
        def setHandleType(self, type: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.HandleType, /) -> None: ...
        def setHeight(self, height: int, /) -> None: ...
        def setLayers(self, layers: int, /) -> None: ...
        def setMagnificationFilter(self, f: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.Filter, /) -> None: ...
        def setMaximumAnisotropy(self, anisotropy: float, /) -> None: ...
        def setMinificationFilter(self, f: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.Filter, /) -> None: ...
        def setMipLevels(self, mipLevels: int, /) -> None: ...
        def setSamples(self, samples: int, /) -> None: ...
        def setSize(self, width: int, /, height: int = ..., depth: int = ...) -> None: ...
        def setStatus(self, status: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.Status, /) -> None: ...
        def setWidth(self, width: int, /) -> None: ...
        def setWrapMode(self, wrapMode: PySide6.Qt3DRender.Qt3DRender.QTextureWrapMode, /) -> None: ...
        def status(self, /) -> PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.Status: ...
        def target(self, /) -> PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.Target: ...
        def textureImages(self, /) -> typing.List[PySide6.Qt3DRender.Qt3DRender.QAbstractTextureImage]: ...
        def updateData(self, update: PySide6.Qt3DRender.Qt3DRender.QTextureDataUpdate, /) -> None: ...
        def width(self, /) -> int: ...
        def wrapMode(self, /) -> PySide6.Qt3DRender.Qt3DRender.QTextureWrapMode: ...

    class QAbstractTextureImage(PySide6.Qt3DCore.Qt3DCore.QNode):
        # faceChanged(QAbstractTexture::CubeMapFace)
        faceChanged: typing.ClassVar[Signal[
            [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.CubeMapFace], [], [], [], [], [], [], [],
            [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.CubeMapFace], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.CubeMapFace], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.CubeMapFace], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.CubeMapFace], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.CubeMapFace], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.CubeMapFace], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.CubeMapFace], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.CubeMapFace]
        ]]
        # layerChanged(int)
        layerChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]
        # mipLevelChanged(int)
        mipLevelChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, mipLevel: int | None = ..., layer: int | None = ..., face: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.CubeMapFace | None = ...) -> None: ...

        def dataGenerator(self, /) -> PySide6.Qt3DRender.Qt3DRender.QTextureImageDataGeneratorPtr: ...
        def face(self, /) -> PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.CubeMapFace: ...
        def layer(self, /) -> int: ...
        def mipLevel(self, /) -> int: ...
        def notifyDataGeneratorChanged(self, /) -> None: ...
        def setFace(self, face: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.CubeMapFace, /) -> None: ...
        def setLayer(self, layer: int, /) -> None: ...
        def setMipLevel(self, level: int, /) -> None: ...

    class QAlphaCoverage(PySide6.Qt3DRender.Qt3DRender.QRenderState):
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...) -> None: ...

    class QAlphaTest(PySide6.Qt3DRender.Qt3DRender.QRenderState):
        # alphaFunctionChanged(AlphaFunction)
        alphaFunctionChanged: typing.ClassVar[Signal[
            [AlphaFunction], [], [], [], [], [], [], [],
            [AlphaFunction], [AlphaFunction], [AlphaFunction], [AlphaFunction], [AlphaFunction], [AlphaFunction], [AlphaFunction], [AlphaFunction]
        ]]
        # referenceValueChanged(float)
        referenceValueChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]

        class AlphaFunction(enum.Enum):
            Never                     = 0x200
            Less                      = 0x201
            Equal                     = 0x202
            LessOrEqual               = 0x203
            Greater                   = 0x204
            NotEqual                  = 0x205
            GreaterOrEqual            = 0x206
            Always                    = 0x207

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, alphaFunction: PySide6.Qt3DRender.Qt3DRender.QAlphaTest.AlphaFunction | None = ..., referenceValue: float | None = ...) -> None: ...

        def alphaFunction(self, /) -> PySide6.Qt3DRender.Qt3DRender.QAlphaTest.AlphaFunction: ...
        def referenceValue(self, /) -> float: ...
        def setAlphaFunction(self, alphaFunction: PySide6.Qt3DRender.Qt3DRender.QAlphaTest.AlphaFunction, /) -> None: ...
        def setReferenceValue(self, referenceValue: float, /) -> None: ...

    class QBlendEquation(PySide6.Qt3DRender.Qt3DRender.QRenderState):
        # blendFunctionChanged(BlendFunction)
        blendFunctionChanged: typing.ClassVar[Signal[
            [BlendFunction], [], [], [], [], [], [], [],
            [BlendFunction], [BlendFunction], [BlendFunction], [BlendFunction], [BlendFunction], [BlendFunction], [BlendFunction], [BlendFunction]
        ]]

        class BlendFunction(enum.Enum):
            Add                       = 0x8006
            Min                       = 0x8007
            Max                       = 0x8008
            Subtract                  = 0x800a
            ReverseSubtract           = 0x800b

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, blendFunction: PySide6.Qt3DRender.Qt3DRender.QBlendEquation.BlendFunction | None = ...) -> None: ...

        def blendFunction(self, /) -> PySide6.Qt3DRender.Qt3DRender.QBlendEquation.BlendFunction: ...
        def setBlendFunction(self, blendFunction: PySide6.Qt3DRender.Qt3DRender.QBlendEquation.BlendFunction, /) -> None: ...

    class QBlendEquationArguments(PySide6.Qt3DRender.Qt3DRender.QRenderState):
        # bufferIndexChanged(int)
        bufferIndexChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]
        # destinationAlphaChanged(Blending)
        destinationAlphaChanged: typing.ClassVar[Signal[
            [Blending], [], [], [], [], [], [], [],
            [Blending], [Blending], [Blending], [Blending], [Blending], [Blending], [Blending], [Blending]
        ]]
        # destinationRgbChanged(Blending)
        destinationRgbChanged: typing.ClassVar[Signal[
            [Blending], [], [], [], [], [], [], [],
            [Blending], [Blending], [Blending], [Blending], [Blending], [Blending], [Blending], [Blending]
        ]]
        # destinationRgbaChanged(Blending)
        destinationRgbaChanged: typing.ClassVar[Signal[
            [Blending], [], [], [], [], [], [], [],
            [Blending], [Blending], [Blending], [Blending], [Blending], [Blending], [Blending], [Blending]
        ]]
        # sourceAlphaChanged(Blending)
        sourceAlphaChanged: typing.ClassVar[Signal[
            [Blending], [], [], [], [], [], [], [],
            [Blending], [Blending], [Blending], [Blending], [Blending], [Blending], [Blending], [Blending]
        ]]
        # sourceRgbChanged(Blending)
        sourceRgbChanged: typing.ClassVar[Signal[
            [Blending], [], [], [], [], [], [], [],
            [Blending], [Blending], [Blending], [Blending], [Blending], [Blending], [Blending], [Blending]
        ]]
        # sourceRgbaChanged(Blending)
        sourceRgbaChanged: typing.ClassVar[Signal[
            [Blending], [], [], [], [], [], [], [],
            [Blending], [Blending], [Blending], [Blending], [Blending], [Blending], [Blending], [Blending]
        ]]

        class Blending(enum.Enum):
            Zero                      = 0x0
            One                       = 0x1
            SourceColor               = 0x300
            OneMinusSourceColor       = 0x301
            SourceAlpha               = 0x302
            OneMinusSourceAlpha       = 0x303
            Source1Alpha              = 0x303
            DestinationAlpha          = 0x304
            Source1Color              = 0x304
            OneMinusDestinationAlpha  = 0x305
            DestinationColor          = 0x306
            OneMinusDestinationColor  = 0x307
            SourceAlphaSaturate       = 0x308
            ConstantColor             = 0x8001
            OneMinusConstantColor     = 0x8002
            ConstantAlpha             = 0x8003
            OneMinusConstantAlpha     = 0x8004
            OneMinusSource1Alpha      = 0x8005
            OneMinusSource1Color      = 0x8006
            OneMinusSource1Color0     = 0x8006

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, sourceRgb: PySide6.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending | None = ..., sourceAlpha: PySide6.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending | None = ..., destinationRgb: PySide6.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending | None = ..., destinationAlpha: PySide6.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending | None = ..., bufferIndex: int | None = ...) -> None: ...

        def bufferIndex(self, /) -> int: ...
        def destinationAlpha(self, /) -> PySide6.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending: ...
        def destinationRgb(self, /) -> PySide6.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending: ...
        def setBufferIndex(self, index: int, /) -> None: ...
        def setDestinationAlpha(self, destinationAlpha: PySide6.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending, /) -> None: ...
        def setDestinationRgb(self, destinationRgb: PySide6.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending, /) -> None: ...
        def setDestinationRgba(self, destinationRgba: PySide6.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending, /) -> None: ...
        def setSourceAlpha(self, sourceAlpha: PySide6.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending, /) -> None: ...
        def setSourceRgb(self, sourceRgb: PySide6.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending, /) -> None: ...
        def setSourceRgba(self, sourceRgba: PySide6.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending, /) -> None: ...
        def sourceAlpha(self, /) -> PySide6.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending: ...
        def sourceRgb(self, /) -> PySide6.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending: ...

    class QBlitFramebuffer(PySide6.Qt3DRender.Qt3DRender.QFrameGraphNode):
        # destinationAttachmentPointChanged()
        destinationAttachmentPointChanged: typing.ClassVar[Signal[
            [], [], [], [], [], [], [], [],
            [], [], [], [], [], [], [], []
        ]]
        # destinationChanged()
        destinationChanged: typing.ClassVar[Signal[
            [], [], [], [], [], [], [], [],
            [], [], [], [], [], [], [], []
        ]]
        # destinationRectChanged()
        destinationRectChanged: typing.ClassVar[Signal[
            [], [], [], [], [], [], [], [],
            [], [], [], [], [], [], [], []
        ]]
        # interpolationMethodChanged()
        interpolationMethodChanged: typing.ClassVar[Signal[
            [], [], [], [], [], [], [], [],
            [], [], [], [], [], [], [], []
        ]]
        # sourceAttachmentPointChanged()
        sourceAttachmentPointChanged: typing.ClassVar[Signal[
            [], [], [], [], [], [], [], [],
            [], [], [], [], [], [], [], []
        ]]
        # sourceChanged()
        sourceChanged: typing.ClassVar[Signal[
            [], [], [], [], [], [], [], [],
            [], [], [], [], [], [], [], []
        ]]
        # sourceRectChanged()
        sourceRectChanged: typing.ClassVar[Signal[
            [], [], [], [], [], [], [], [],
            [], [], [], [], [], [], [], []
        ]]

        class InterpolationMethod(enum.Enum):
            Nearest                   = 0x0
            Linear                    = 0x1

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, source: PySide6.Qt3DRender.Qt3DRender.QRenderTarget | None = ..., destination: PySide6.Qt3DRender.Qt3DRender.QRenderTarget | None = ..., sourceRect: PySide6.QtCore.QRectF | None = ..., destinationRect: PySide6.QtCore.QRectF | None = ..., sourceAttachmentPoint: PySide6.Qt3DRender.Qt3DRender.QRenderTargetOutput.AttachmentPoint | None = ..., destinationAttachmentPoint: PySide6.Qt3DRender.Qt3DRender.QRenderTargetOutput.AttachmentPoint | None = ..., interpolationMethod: PySide6.Qt3DRender.Qt3DRender.QBlitFramebuffer.InterpolationMethod | None = ...) -> None: ...

        def destination(self, /) -> PySide6.Qt3DRender.Qt3DRender.QRenderTarget: ...
        def destinationAttachmentPoint(self, /) -> PySide6.Qt3DRender.Qt3DRender.QRenderTargetOutput.AttachmentPoint: ...
        def destinationRect(self, /) -> PySide6.QtCore.QRectF: ...
        def interpolationMethod(self, /) -> PySide6.Qt3DRender.Qt3DRender.QBlitFramebuffer.InterpolationMethod: ...
        def setDestination(self, destination: PySide6.Qt3DRender.Qt3DRender.QRenderTarget, /) -> None: ...
        def setDestinationAttachmentPoint(self, destinationAttachmentPoint: PySide6.Qt3DRender.Qt3DRender.QRenderTargetOutput.AttachmentPoint, /) -> None: ...
        def setDestinationRect(self, destinationRect: PySide6.QtCore.QRectF | PySide6.QtCore.QRect, /) -> None: ...
        def setInterpolationMethod(self, interpolationMethod: PySide6.Qt3DRender.Qt3DRender.QBlitFramebuffer.InterpolationMethod, /) -> None: ...
        def setSource(self, source: PySide6.Qt3DRender.Qt3DRender.QRenderTarget, /) -> None: ...
        def setSourceAttachmentPoint(self, sourceAttachmentPoint: PySide6.Qt3DRender.Qt3DRender.QRenderTargetOutput.AttachmentPoint, /) -> None: ...
        def setSourceRect(self, sourceRect: PySide6.QtCore.QRectF | PySide6.QtCore.QRect, /) -> None: ...
        def source(self, /) -> PySide6.Qt3DRender.Qt3DRender.QRenderTarget: ...
        def sourceAttachmentPoint(self, /) -> PySide6.Qt3DRender.Qt3DRender.QRenderTargetOutput.AttachmentPoint: ...
        def sourceRect(self, /) -> PySide6.QtCore.QRectF: ...

    class QBufferCapture(PySide6.Qt3DRender.Qt3DRender.QFrameGraphNode):
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...) -> None: ...

    class QCamera(PySide6.Qt3DCore.Qt3DCore.QEntity):
        # aspectRatioChanged(float)
        aspectRatioChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # bottomChanged(float)
        bottomChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # exposureChanged(float)
        exposureChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # farPlaneChanged(float)
        farPlaneChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # fieldOfViewChanged(float)
        fieldOfViewChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # leftChanged(float)
        leftChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # nearPlaneChanged(float)
        nearPlaneChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # positionChanged(QVector3D)
        positionChanged: typing.ClassVar[Signal[
            [PySide6.QtGui.QVector3D], [], [], [], [], [], [], [],
            [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D]
        ]]
        # projectionMatrixChanged(QMatrix4x4)
        projectionMatrixChanged: typing.ClassVar[Signal[
            [PySide6.QtGui.QMatrix4x4], [], [], [], [], [], [], [],
            [PySide6.QtGui.QMatrix4x4], [PySide6.QtGui.QMatrix4x4], [PySide6.QtGui.QMatrix4x4], [PySide6.QtGui.QMatrix4x4], [PySide6.QtGui.QMatrix4x4], [PySide6.QtGui.QMatrix4x4], [PySide6.QtGui.QMatrix4x4], [PySide6.QtGui.QMatrix4x4]
        ]]
        # projectionTypeChanged(QCameraLens::ProjectionType)
        projectionTypeChanged: typing.ClassVar[Signal[
            [PySide6.Qt3DRender.Qt3DRender.QCameraLens.ProjectionType], [], [], [], [], [], [], [],
            [PySide6.Qt3DRender.Qt3DRender.QCameraLens.ProjectionType], [PySide6.Qt3DRender.Qt3DRender.QCameraLens.ProjectionType], [PySide6.Qt3DRender.Qt3DRender.QCameraLens.ProjectionType], [PySide6.Qt3DRender.Qt3DRender.QCameraLens.ProjectionType], [PySide6.Qt3DRender.Qt3DRender.QCameraLens.ProjectionType], [PySide6.Qt3DRender.Qt3DRender.QCameraLens.ProjectionType], [PySide6.Qt3DRender.Qt3DRender.QCameraLens.ProjectionType], [PySide6.Qt3DRender.Qt3DRender.QCameraLens.ProjectionType]
        ]]
        # rightChanged(float)
        rightChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # topChanged(float)
        topChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # upVectorChanged(QVector3D)
        upVectorChanged: typing.ClassVar[Signal[
            [PySide6.QtGui.QVector3D], [], [], [], [], [], [], [],
            [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D]
        ]]
        # viewCenterChanged(QVector3D)
        viewCenterChanged: typing.ClassVar[Signal[
            [PySide6.QtGui.QVector3D], [], [], [], [], [], [], [],
            [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D]
        ]]
        # viewMatrixChanged()
        viewMatrixChanged: typing.ClassVar[Signal[
            [], [], [], [], [], [], [], [],
            [], [], [], [], [], [], [], []
        ]]
        # viewVectorChanged(QVector3D)
        viewVectorChanged: typing.ClassVar[Signal[
            [PySide6.QtGui.QVector3D], [], [], [], [], [], [], [],
            [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D]
        ]]

        class CameraTranslationOption(enum.Enum):
            TranslateViewCenter       = 0x0
            DontTranslateViewCenter   = 0x1

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, projectionType: PySide6.Qt3DRender.Qt3DRender.QCameraLens.ProjectionType | None = ..., nearPlane: float | None = ..., farPlane: float | None = ..., fieldOfView: float | None = ..., aspectRatio: float | None = ..., left: float | None = ..., right: float | None = ..., bottom: float | None = ..., top: float | None = ..., projectionMatrix: PySide6.QtGui.QMatrix4x4 | None = ..., exposure: float | None = ..., position: PySide6.QtGui.QVector3D | None = ..., upVector: PySide6.QtGui.QVector3D | None = ..., viewCenter: PySide6.QtGui.QVector3D | None = ..., viewVector: PySide6.QtGui.QVector3D | None = ..., viewMatrix: PySide6.QtGui.QMatrix4x4 | None = ..., lens: PySide6.Qt3DRender.Qt3DRender.QCameraLens | None = ..., transform: PySide6.Qt3DCore.Qt3DCore.QTransform | None = ...) -> None: ...

        def aspectRatio(self, /) -> float: ...
        def bottom(self, /) -> float: ...
        def exposure(self, /) -> float: ...
        def farPlane(self, /) -> float: ...
        def fieldOfView(self, /) -> float: ...
        def left(self, /) -> float: ...
        def lens(self, /) -> PySide6.Qt3DRender.Qt3DRender.QCameraLens: ...
        def nearPlane(self, /) -> float: ...
        @typing.overload
        def pan(self, angle: float, /) -> None: ...
        @typing.overload
        def pan(self, angle: float, axis: PySide6.QtGui.QVector3D, /) -> None: ...
        @typing.overload
        def panAboutViewCenter(self, angle: float, /) -> None: ...
        @typing.overload
        def panAboutViewCenter(self, angle: float, axis: PySide6.QtGui.QVector3D, /) -> None: ...
        def panRotation(self, angle: float, /) -> PySide6.QtGui.QQuaternion: ...
        def position(self, /) -> PySide6.QtGui.QVector3D: ...
        def projectionMatrix(self, /) -> PySide6.QtGui.QMatrix4x4: ...
        def projectionType(self, /) -> PySide6.Qt3DRender.Qt3DRender.QCameraLens.ProjectionType: ...
        def right(self, /) -> float: ...
        def roll(self, angle: float, /) -> None: ...
        def rollAboutViewCenter(self, angle: float, /) -> None: ...
        def rollRotation(self, angle: float, /) -> PySide6.QtGui.QQuaternion: ...
        def rotate(self, q: PySide6.QtGui.QQuaternion, /) -> None: ...
        def rotateAboutViewCenter(self, q: PySide6.QtGui.QQuaternion, /) -> None: ...
        def rotation(self, angle: float, axis: PySide6.QtGui.QVector3D, /) -> PySide6.QtGui.QQuaternion: ...
        def setAspectRatio(self, aspectRatio: float, /) -> None: ...
        def setBottom(self, bottom: float, /) -> None: ...
        def setExposure(self, exposure: float, /) -> None: ...
        def setFarPlane(self, farPlane: float, /) -> None: ...
        def setFieldOfView(self, fieldOfView: float, /) -> None: ...
        def setLeft(self, left: float, /) -> None: ...
        def setNearPlane(self, nearPlane: float, /) -> None: ...
        def setPosition(self, position: PySide6.QtGui.QVector3D, /) -> None: ...
        def setProjectionMatrix(self, projectionMatrix: PySide6.QtGui.QMatrix4x4 | PySide6.QtGui.QTransform, /) -> None: ...
        def setProjectionType(self, type: PySide6.Qt3DRender.Qt3DRender.QCameraLens.ProjectionType, /) -> None: ...
        def setRight(self, right: float, /) -> None: ...
        def setTop(self, top: float, /) -> None: ...
        def setUpVector(self, upVector: PySide6.QtGui.QVector3D, /) -> None: ...
        def setViewCenter(self, viewCenter: PySide6.QtGui.QVector3D, /) -> None: ...
        def tilt(self, angle: float, /) -> None: ...
        def tiltAboutViewCenter(self, angle: float, /) -> None: ...
        def tiltRotation(self, angle: float, /) -> PySide6.QtGui.QQuaternion: ...
        def top(self, /) -> float: ...
        def transform(self, /) -> PySide6.Qt3DCore.Qt3DCore.QTransform: ...
        def translate(self, vLocal: PySide6.QtGui.QVector3D, /, option: PySide6.Qt3DRender.Qt3DRender.QCamera.CameraTranslationOption = ...) -> None: ...
        def translateWorld(self, vWorld: PySide6.QtGui.QVector3D, /, option: PySide6.Qt3DRender.Qt3DRender.QCamera.CameraTranslationOption = ...) -> None: ...
        def upVector(self, /) -> PySide6.QtGui.QVector3D: ...
        def viewAll(self, /) -> None: ...
        def viewCenter(self, /) -> PySide6.QtGui.QVector3D: ...
        def viewEntity(self, entity: PySide6.Qt3DCore.Qt3DCore.QEntity, /) -> None: ...
        def viewMatrix(self, /) -> PySide6.QtGui.QMatrix4x4: ...
        def viewSphere(self, center: PySide6.QtGui.QVector3D, radius: float, /) -> None: ...
        def viewVector(self, /) -> PySide6.QtGui.QVector3D: ...

    class QCameraLens(PySide6.Qt3DCore.Qt3DCore.QComponent):
        # aspectRatioChanged(float)
        aspectRatioChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # bottomChanged(float)
        bottomChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # exposureChanged(float)
        exposureChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # farPlaneChanged(float)
        farPlaneChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # fieldOfViewChanged(float)
        fieldOfViewChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # leftChanged(float)
        leftChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # nearPlaneChanged(float)
        nearPlaneChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # projectionMatrixChanged(QMatrix4x4)
        projectionMatrixChanged: typing.ClassVar[Signal[
            [PySide6.QtGui.QMatrix4x4], [], [], [], [], [], [], [],
            [PySide6.QtGui.QMatrix4x4], [PySide6.QtGui.QMatrix4x4], [PySide6.QtGui.QMatrix4x4], [PySide6.QtGui.QMatrix4x4], [PySide6.QtGui.QMatrix4x4], [PySide6.QtGui.QMatrix4x4], [PySide6.QtGui.QMatrix4x4], [PySide6.QtGui.QMatrix4x4]
        ]]
        # projectionTypeChanged(QCameraLens::ProjectionType)
        projectionTypeChanged: typing.ClassVar[Signal[
            [PySide6.Qt3DRender.Qt3DRender.QCameraLens.ProjectionType], [], [], [], [], [], [], [],
            [PySide6.Qt3DRender.Qt3DRender.QCameraLens.ProjectionType], [PySide6.Qt3DRender.Qt3DRender.QCameraLens.ProjectionType], [PySide6.Qt3DRender.Qt3DRender.QCameraLens.ProjectionType], [PySide6.Qt3DRender.Qt3DRender.QCameraLens.ProjectionType], [PySide6.Qt3DRender.Qt3DRender.QCameraLens.ProjectionType], [PySide6.Qt3DRender.Qt3DRender.QCameraLens.ProjectionType], [PySide6.Qt3DRender.Qt3DRender.QCameraLens.ProjectionType], [PySide6.Qt3DRender.Qt3DRender.QCameraLens.ProjectionType]
        ]]
        # rightChanged(float)
        rightChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # topChanged(float)
        topChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # viewSphere(QVector3D,float)
        viewSphere: typing.ClassVar[Signal[
            [PySide6.QtGui.QVector3D, float], [PySide6.QtGui.QVector3D], [], [], [], [], [], [],
            [PySide6.QtGui.QVector3D, float], [PySide6.QtGui.QVector3D, float], [PySide6.QtGui.QVector3D, float], [PySide6.QtGui.QVector3D, float], [PySide6.QtGui.QVector3D, float], [PySide6.QtGui.QVector3D, float], [PySide6.QtGui.QVector3D, float], [PySide6.QtGui.QVector3D, float]
        ]]

        class ProjectionType(enum.Enum):
            OrthographicProjection    = 0x0
            PerspectiveProjection     = 0x1
            FrustumProjection         = 0x2
            CustomProjection          = 0x3

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, projectionType: PySide6.Qt3DRender.Qt3DRender.QCameraLens.ProjectionType | None = ..., nearPlane: float | None = ..., farPlane: float | None = ..., fieldOfView: float | None = ..., aspectRatio: float | None = ..., left: float | None = ..., right: float | None = ..., bottom: float | None = ..., top: float | None = ..., projectionMatrix: PySide6.QtGui.QMatrix4x4 | None = ..., exposure: float | None = ...) -> None: ...

        def aspectRatio(self, /) -> float: ...
        def bottom(self, /) -> float: ...
        def exposure(self, /) -> float: ...
        def farPlane(self, /) -> float: ...
        def fieldOfView(self, /) -> float: ...
        def left(self, /) -> float: ...
        def nearPlane(self, /) -> float: ...
        def projectionMatrix(self, /) -> PySide6.QtGui.QMatrix4x4: ...
        def projectionType(self, /) -> PySide6.Qt3DRender.Qt3DRender.QCameraLens.ProjectionType: ...
        def right(self, /) -> float: ...
        def setAspectRatio(self, aspectRatio: float, /) -> None: ...
        def setBottom(self, bottom: float, /) -> None: ...
        def setExposure(self, exposure: float, /) -> None: ...
        def setFarPlane(self, farPlane: float, /) -> None: ...
        def setFieldOfView(self, fieldOfView: float, /) -> None: ...
        def setFrustumProjection(self, left: float, right: float, bottom: float, top: float, nearPlane: float, farPlane: float, /) -> None: ...
        def setLeft(self, left: float, /) -> None: ...
        def setNearPlane(self, nearPlane: float, /) -> None: ...
        def setOrthographicProjection(self, left: float, right: float, bottom: float, top: float, nearPlane: float, farPlane: float, /) -> None: ...
        def setPerspectiveProjection(self, fieldOfView: float, aspect: float, nearPlane: float, farPlane: float, /) -> None: ...
        def setProjectionMatrix(self, projectionMatrix: PySide6.QtGui.QMatrix4x4 | PySide6.QtGui.QTransform, /) -> None: ...
        def setProjectionType(self, projectionType: PySide6.Qt3DRender.Qt3DRender.QCameraLens.ProjectionType, /) -> None: ...
        def setRight(self, right: float, /) -> None: ...
        def setTop(self, top: float, /) -> None: ...
        def top(self, /) -> float: ...
        def viewAll(self, cameraId: PySide6.Qt3DCore.Qt3DCore.QNodeId, /) -> None: ...
        def viewEntity(self, entityId: PySide6.Qt3DCore.Qt3DCore.QNodeId, cameraId: PySide6.Qt3DCore.Qt3DCore.QNodeId, /) -> None: ...

    class QCameraSelector(PySide6.Qt3DRender.Qt3DRender.QFrameGraphNode):
        # cameraChanged(Qt3DCore::QEntity*)
        cameraChanged: typing.ClassVar[Signal[
            [PySide6.Qt3DCore.Qt3DCore.QEntity], [], [], [], [], [], [], [],
            [PySide6.Qt3DCore.Qt3DCore.QEntity], [PySide6.Qt3DCore.Qt3DCore.QEntity], [PySide6.Qt3DCore.Qt3DCore.QEntity], [PySide6.Qt3DCore.Qt3DCore.QEntity], [PySide6.Qt3DCore.Qt3DCore.QEntity], [PySide6.Qt3DCore.Qt3DCore.QEntity], [PySide6.Qt3DCore.Qt3DCore.QEntity], [PySide6.Qt3DCore.Qt3DCore.QEntity]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, camera: PySide6.Qt3DCore.Qt3DCore.QEntity | None = ...) -> None: ...

        def camera(self, /) -> PySide6.Qt3DCore.Qt3DCore.QEntity: ...
        def setCamera(self, camera: PySide6.Qt3DCore.Qt3DCore.QEntity, /) -> None: ...

    class QClearBuffers(PySide6.Qt3DRender.Qt3DRender.QFrameGraphNode):
        # buffersChanged(BufferType)
        buffersChanged: typing.ClassVar[Signal[
            [BufferType], [], [], [], [], [], [], [],
            [BufferType], [BufferType], [BufferType], [BufferType], [BufferType], [BufferType], [BufferType], [BufferType]
        ]]
        # clearColorChanged(QColor)
        clearColorChanged: typing.ClassVar[Signal[
            [PySide6.QtGui.QColor], [], [], [], [], [], [], [],
            [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor]
        ]]
        # clearDepthValueChanged(float)
        clearDepthValueChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # clearStencilValueChanged(int)
        clearStencilValueChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]
        # colorBufferChanged(QRenderTargetOutput*)
        colorBufferChanged: typing.ClassVar[Signal[
            [PySide6.Qt3DRender.Qt3DRender.QRenderTargetOutput], [], [], [], [], [], [], [],
            [PySide6.Qt3DRender.Qt3DRender.QRenderTargetOutput], [PySide6.Qt3DRender.Qt3DRender.QRenderTargetOutput], [PySide6.Qt3DRender.Qt3DRender.QRenderTargetOutput], [PySide6.Qt3DRender.Qt3DRender.QRenderTargetOutput], [PySide6.Qt3DRender.Qt3DRender.QRenderTargetOutput], [PySide6.Qt3DRender.Qt3DRender.QRenderTargetOutput], [PySide6.Qt3DRender.Qt3DRender.QRenderTargetOutput], [PySide6.Qt3DRender.Qt3DRender.QRenderTargetOutput]
        ]]

        class BufferType(enum.Flag):
            AllBuffers                = -1
            None_                     = 0x0
            ColorBuffer               = 0x1
            DepthBuffer               = 0x2
            ColorDepthBuffer          = 0x3
            StencilBuffer             = 0x4
            DepthStencilBuffer        = 0x6
            ColorDepthStencilBuffer   = 0x7

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, buffers: PySide6.Qt3DRender.Qt3DRender.QClearBuffers.BufferType | None = ..., clearColor: PySide6.QtGui.QColor | None = ..., clearDepthValue: float | None = ..., clearStencilValue: int | None = ..., colorBuffer: PySide6.Qt3DRender.Qt3DRender.QRenderTargetOutput | None = ...) -> None: ...

        def buffers(self, /) -> PySide6.Qt3DRender.Qt3DRender.QClearBuffers.BufferType: ...
        def clearColor(self, /) -> PySide6.QtGui.QColor: ...
        def clearDepthValue(self, /) -> float: ...
        def clearStencilValue(self, /) -> int: ...
        def colorBuffer(self, /) -> PySide6.Qt3DRender.Qt3DRender.QRenderTargetOutput: ...
        def setBuffers(self, buffers: PySide6.Qt3DRender.Qt3DRender.QClearBuffers.BufferType, /) -> None: ...
        def setClearColor(self, color: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
        def setClearDepthValue(self, clearDepthValue: float, /) -> None: ...
        def setClearStencilValue(self, clearStencilValue: int, /) -> None: ...
        def setColorBuffer(self, buffer: PySide6.Qt3DRender.Qt3DRender.QRenderTargetOutput, /) -> None: ...

    class QClipPlane(PySide6.Qt3DRender.Qt3DRender.QRenderState):
        # distanceChanged(float)
        distanceChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # normalChanged(QVector3D)
        normalChanged: typing.ClassVar[Signal[
            [PySide6.QtGui.QVector3D], [], [], [], [], [], [], [],
            [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D]
        ]]
        # planeIndexChanged(int)
        planeIndexChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, planeIndex: int | None = ..., normal: PySide6.QtGui.QVector3D | None = ..., distance: float | None = ...) -> None: ...

        def distance(self, /) -> float: ...
        def normal(self, /) -> PySide6.QtGui.QVector3D: ...
        def planeIndex(self, /) -> int: ...
        def setDistance(self, arg__1: float, /) -> None: ...
        def setNormal(self, arg__1: PySide6.QtGui.QVector3D, /) -> None: ...
        def setPlaneIndex(self, arg__1: int, /) -> None: ...

    class QColorMask(PySide6.Qt3DRender.Qt3DRender.QRenderState):
        # alphaMaskedChanged(bool)
        alphaMaskedChanged: typing.ClassVar[Signal[
            [bool], [], [], [], [], [], [], [],
            [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
        ]]
        # blueMaskedChanged(bool)
        blueMaskedChanged: typing.ClassVar[Signal[
            [bool], [], [], [], [], [], [], [],
            [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
        ]]
        # greenMaskedChanged(bool)
        greenMaskedChanged: typing.ClassVar[Signal[
            [bool], [], [], [], [], [], [], [],
            [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
        ]]
        # redMaskedChanged(bool)
        redMaskedChanged: typing.ClassVar[Signal[
            [bool], [], [], [], [], [], [], [],
            [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, redMasked: bool | None = ..., greenMasked: bool | None = ..., blueMasked: bool | None = ..., alphaMasked: bool | None = ...) -> None: ...

        def isAlphaMasked(self, /) -> bool: ...
        def isBlueMasked(self, /) -> bool: ...
        def isGreenMasked(self, /) -> bool: ...
        def isRedMasked(self, /) -> bool: ...
        def setAlphaMasked(self, alphaMasked: bool, /) -> None: ...
        def setBlueMasked(self, blueMasked: bool, /) -> None: ...
        def setGreenMasked(self, greenMasked: bool, /) -> None: ...
        def setRedMasked(self, redMasked: bool, /) -> None: ...

    class QComputeCommand(PySide6.Qt3DCore.Qt3DCore.QComponent):
        # runTypeChanged()
        runTypeChanged: typing.ClassVar[Signal[
            [], [], [], [], [], [], [], [],
            [], [], [], [], [], [], [], []
        ]]
        # workGroupXChanged()
        workGroupXChanged: typing.ClassVar[Signal[
            [], [], [], [], [], [], [], [],
            [], [], [], [], [], [], [], []
        ]]
        # workGroupYChanged()
        workGroupYChanged: typing.ClassVar[Signal[
            [], [], [], [], [], [], [], [],
            [], [], [], [], [], [], [], []
        ]]
        # workGroupZChanged()
        workGroupZChanged: typing.ClassVar[Signal[
            [], [], [], [], [], [], [], [],
            [], [], [], [], [], [], [], []
        ]]

        class RunType(enum.Enum):
            Continuous                = 0x0
            Manual                    = 0x1

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, workGroupX: int | None = ..., workGroupY: int | None = ..., workGroupZ: int | None = ..., runType: PySide6.Qt3DRender.Qt3DRender.QComputeCommand.RunType | None = ...) -> None: ...

        def runType(self, /) -> PySide6.Qt3DRender.Qt3DRender.QComputeCommand.RunType: ...
        def setRunType(self, runType: PySide6.Qt3DRender.Qt3DRender.QComputeCommand.RunType, /) -> None: ...
        def setWorkGroupX(self, workGroupX: int, /) -> None: ...
        def setWorkGroupY(self, workGroupY: int, /) -> None: ...
        def setWorkGroupZ(self, workGroupZ: int, /) -> None: ...
        @typing.overload
        def trigger(self, /, frameCount: int = ...) -> None: ...
        @typing.overload
        def trigger(self, workGroupX: int, workGroupY: int, workGroupZ: int, /, frameCount: int = ...) -> None: ...
        def workGroupX(self, /) -> int: ...
        def workGroupY(self, /) -> int: ...
        def workGroupZ(self, /) -> int: ...

    class QCullFace(PySide6.Qt3DRender.Qt3DRender.QRenderState):
        # modeChanged(CullingMode)
        modeChanged: typing.ClassVar[Signal[
            [CullingMode], [], [], [], [], [], [], [],
            [CullingMode], [CullingMode], [CullingMode], [CullingMode], [CullingMode], [CullingMode], [CullingMode], [CullingMode]
        ]]

        class CullingMode(enum.Enum):
            NoCulling                 = 0x0
            Front                     = 0x404
            Back                      = 0x405
            FrontAndBack              = 0x408

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, mode: PySide6.Qt3DRender.Qt3DRender.QCullFace.CullingMode | None = ...) -> None: ...

        def mode(self, /) -> PySide6.Qt3DRender.Qt3DRender.QCullFace.CullingMode: ...
        def setMode(self, mode: PySide6.Qt3DRender.Qt3DRender.QCullFace.CullingMode, /) -> None: ...

    class QDebugOverlay(PySide6.Qt3DRender.Qt3DRender.QFrameGraphNode):
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...) -> None: ...

    class QDepthRange(PySide6.Qt3DRender.Qt3DRender.QRenderState):
        # farValueChanged(double)
        farValueChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # nearValueChanged(double)
        nearValueChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, nearValue: float | None = ..., farValue: float | None = ...) -> None: ...

        def farValue(self, /) -> float: ...
        def nearValue(self, /) -> float: ...
        def setFarValue(self, value: float, /) -> None: ...
        def setNearValue(self, value: float, /) -> None: ...

    class QDepthTest(PySide6.Qt3DRender.Qt3DRender.QRenderState):
        # depthFunctionChanged(DepthFunction)
        depthFunctionChanged: typing.ClassVar[Signal[
            [DepthFunction], [], [], [], [], [], [], [],
            [DepthFunction], [DepthFunction], [DepthFunction], [DepthFunction], [DepthFunction], [DepthFunction], [DepthFunction], [DepthFunction]
        ]]

        class DepthFunction(enum.Enum):
            Never                     = 0x200
            Less                      = 0x201
            Equal                     = 0x202
            LessOrEqual               = 0x203
            Greater                   = 0x204
            NotEqual                  = 0x205
            GreaterOrEqual            = 0x206
            Always                    = 0x207

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, depthFunction: PySide6.Qt3DRender.Qt3DRender.QDepthTest.DepthFunction | None = ...) -> None: ...

        def depthFunction(self, /) -> PySide6.Qt3DRender.Qt3DRender.QDepthTest.DepthFunction: ...
        def setDepthFunction(self, depthFunction: PySide6.Qt3DRender.Qt3DRender.QDepthTest.DepthFunction, /) -> None: ...

    class QDirectionalLight(PySide6.Qt3DRender.Qt3DRender.QAbstractLight):
        # worldDirectionChanged(QVector3D)
        worldDirectionChanged: typing.ClassVar[Signal[
            [PySide6.QtGui.QVector3D], [], [], [], [], [], [], [],
            [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, worldDirection: PySide6.QtGui.QVector3D | None = ...) -> None: ...

        def setWorldDirection(self, worldDirection: PySide6.QtGui.QVector3D, /) -> None: ...
        def worldDirection(self, /) -> PySide6.QtGui.QVector3D: ...

    class QDispatchCompute(PySide6.Qt3DRender.Qt3DRender.QFrameGraphNode):
        # workGroupXChanged()
        workGroupXChanged: typing.ClassVar[Signal[
            [], [], [], [], [], [], [], [],
            [], [], [], [], [], [], [], []
        ]]
        # workGroupYChanged()
        workGroupYChanged: typing.ClassVar[Signal[
            [], [], [], [], [], [], [], [],
            [], [], [], [], [], [], [], []
        ]]
        # workGroupZChanged()
        workGroupZChanged: typing.ClassVar[Signal[
            [], [], [], [], [], [], [], [],
            [], [], [], [], [], [], [], []
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, workGroupX: int | None = ..., workGroupY: int | None = ..., workGroupZ: int | None = ...) -> None: ...

        def setWorkGroupX(self, workGroupX: int, /) -> None: ...
        def setWorkGroupY(self, workGroupY: int, /) -> None: ...
        def setWorkGroupZ(self, workGroupZ: int, /) -> None: ...
        def workGroupX(self, /) -> int: ...
        def workGroupY(self, /) -> int: ...
        def workGroupZ(self, /) -> int: ...

    class QDithering(PySide6.Qt3DRender.Qt3DRender.QRenderState):
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...) -> None: ...

    class QEffect(PySide6.Qt3DCore.Qt3DCore.QNode):
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...) -> None: ...

        def addParameter(self, parameter: PySide6.Qt3DRender.Qt3DRender.QParameter, /) -> None: ...
        def addTechnique(self, t: PySide6.Qt3DRender.Qt3DRender.QTechnique, /) -> None: ...
        def parameters(self, /) -> typing.List[PySide6.Qt3DRender.Qt3DRender.QParameter]: ...
        def removeParameter(self, parameter: PySide6.Qt3DRender.Qt3DRender.QParameter, /) -> None: ...
        def removeTechnique(self, t: PySide6.Qt3DRender.Qt3DRender.QTechnique, /) -> None: ...
        def techniques(self, /) -> typing.List[PySide6.Qt3DRender.Qt3DRender.QTechnique]: ...

    class QEnvironmentLight(PySide6.Qt3DCore.Qt3DCore.QComponent):
        # irradianceChanged(Qt3DRender::QAbstractTexture*)
        irradianceChanged: typing.ClassVar[Signal[
            [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture], [], [], [], [], [], [], [],
            [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture]
        ]]
        # specularChanged(Qt3DRender::QAbstractTexture*)
        specularChanged: typing.ClassVar[Signal[
            [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture], [], [], [], [], [], [], [],
            [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, irradiance: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture | None = ..., specular: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture | None = ...) -> None: ...

        def irradiance(self, /) -> PySide6.Qt3DRender.Qt3DRender.QAbstractTexture: ...
        def setIrradiance(self, irradiance: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture, /) -> None: ...
        def setSpecular(self, specular: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture, /) -> None: ...
        def specular(self, /) -> PySide6.Qt3DRender.Qt3DRender.QAbstractTexture: ...

    class QFilterKey(PySide6.Qt3DCore.Qt3DCore.QNode):
        # nameChanged(QString)
        nameChanged: typing.ClassVar[Signal[
            [str], [], [], [], [], [], [], [],
            [str], [str], [str], [str], [str], [str], [str], [str]
        ]]
        # valueChanged(QVariant)
        valueChanged: typing.ClassVar[Signal[
            [typing.Any], [], [], [], [], [], [], [],
            [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, value: typing.Any | None = ..., name: str | None = ...) -> None: ...

        def name(self, /) -> str: ...
        def setName(self, customType: str, /) -> None: ...
        def setValue(self, value: typing.Any, /) -> None: ...
        def value(self, /) -> typing.Any: ...

    class QFrameGraphNode(PySide6.Qt3DCore.Qt3DCore.QNode):
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...) -> None: ...

        def parentFrameGraphNode(self, /) -> PySide6.Qt3DRender.Qt3DRender.QFrameGraphNode: ...

    class QFrontFace(PySide6.Qt3DRender.Qt3DRender.QRenderState):
        # directionChanged(WindingDirection)
        directionChanged: typing.ClassVar[Signal[
            [WindingDirection], [], [], [], [], [], [], [],
            [WindingDirection], [WindingDirection], [WindingDirection], [WindingDirection], [WindingDirection], [WindingDirection], [WindingDirection], [WindingDirection]
        ]]

        class WindingDirection(enum.Enum):
            ClockWise                 = 0x900
            CounterClockWise          = 0x901

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, direction: PySide6.Qt3DRender.Qt3DRender.QFrontFace.WindingDirection | None = ...) -> None: ...

        def direction(self, /) -> PySide6.Qt3DRender.Qt3DRender.QFrontFace.WindingDirection: ...
        def setDirection(self, direction: PySide6.Qt3DRender.Qt3DRender.QFrontFace.WindingDirection, /) -> None: ...

    class QFrustumCulling(PySide6.Qt3DRender.Qt3DRender.QFrameGraphNode):
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...) -> None: ...

    class QGeometryRenderer(PySide6.Qt3DCore.Qt3DCore.QBoundingVolume):
        # firstInstanceChanged(int)
        firstInstanceChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]
        # firstVertexChanged(int)
        firstVertexChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]
        # geometryChanged(Qt3DCore::QGeometry*)
        geometryChanged: typing.ClassVar[Signal[
            [PySide6.Qt3DCore.Qt3DCore.QGeometry], [], [], [], [], [], [], [],
            [PySide6.Qt3DCore.Qt3DCore.QGeometry], [PySide6.Qt3DCore.Qt3DCore.QGeometry], [PySide6.Qt3DCore.Qt3DCore.QGeometry], [PySide6.Qt3DCore.Qt3DCore.QGeometry], [PySide6.Qt3DCore.Qt3DCore.QGeometry], [PySide6.Qt3DCore.Qt3DCore.QGeometry], [PySide6.Qt3DCore.Qt3DCore.QGeometry], [PySide6.Qt3DCore.Qt3DCore.QGeometry]
        ]]
        # indexBufferByteOffsetChanged(int)
        indexBufferByteOffsetChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]
        # indexOffsetChanged(int)
        indexOffsetChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]
        # instanceCountChanged(int)
        instanceCountChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]
        # primitiveRestartEnabledChanged(bool)
        primitiveRestartEnabledChanged: typing.ClassVar[Signal[
            [bool], [], [], [], [], [], [], [],
            [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
        ]]
        # primitiveTypeChanged(PrimitiveType)
        primitiveTypeChanged: typing.ClassVar[Signal[
            [PrimitiveType], [], [], [], [], [], [], [],
            [PrimitiveType], [PrimitiveType], [PrimitiveType], [PrimitiveType], [PrimitiveType], [PrimitiveType], [PrimitiveType], [PrimitiveType]
        ]]
        # restartIndexValueChanged(int)
        restartIndexValueChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]
        # sortIndexChanged(float)
        sortIndexChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # vertexCountChanged(int)
        vertexCountChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]
        # verticesPerPatchChanged(int)
        verticesPerPatchChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]

        class PrimitiveType(enum.Enum):
            Points                    = 0x0
            Lines                     = 0x1
            LineLoop                  = 0x2
            LineStrip                 = 0x3
            Triangles                 = 0x4
            TriangleStrip             = 0x5
            TriangleFan               = 0x6
            LinesAdjacency            = 0xa
            LineStripAdjacency        = 0xb
            TrianglesAdjacency        = 0xc
            TriangleStripAdjacency    = 0xd
            Patches                   = 0xe

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, instanceCount: int | None = ..., vertexCount: int | None = ..., indexOffset: int | None = ..., firstInstance: int | None = ..., firstVertex: int | None = ..., indexBufferByteOffset: int | None = ..., restartIndexValue: int | None = ..., verticesPerPatch: int | None = ..., primitiveRestartEnabled: bool | None = ..., geometry: PySide6.Qt3DCore.Qt3DCore.QGeometry | None = ..., primitiveType: PySide6.Qt3DRender.Qt3DRender.QGeometryRenderer.PrimitiveType | None = ..., sortIndex: float | None = ...) -> None: ...

        def firstInstance(self, /) -> int: ...
        def firstVertex(self, /) -> int: ...
        def geometry(self, /) -> PySide6.Qt3DCore.Qt3DCore.QGeometry: ...
        def indexBufferByteOffset(self, /) -> int: ...
        def indexOffset(self, /) -> int: ...
        def instanceCount(self, /) -> int: ...
        def primitiveRestartEnabled(self, /) -> bool: ...
        def primitiveType(self, /) -> PySide6.Qt3DRender.Qt3DRender.QGeometryRenderer.PrimitiveType: ...
        def restartIndexValue(self, /) -> int: ...
        def setFirstInstance(self, firstInstance: int, /) -> None: ...
        def setFirstVertex(self, firstVertex: int, /) -> None: ...
        def setGeometry(self, geometry: PySide6.Qt3DCore.Qt3DCore.QGeometry, /) -> None: ...
        def setIndexBufferByteOffset(self, offset: int, /) -> None: ...
        def setIndexOffset(self, indexOffset: int, /) -> None: ...
        def setInstanceCount(self, instanceCount: int, /) -> None: ...
        def setPrimitiveRestartEnabled(self, enabled: bool, /) -> None: ...
        def setPrimitiveType(self, primitiveType: PySide6.Qt3DRender.Qt3DRender.QGeometryRenderer.PrimitiveType, /) -> None: ...
        def setRestartIndexValue(self, index: int, /) -> None: ...
        def setSortIndex(self, sortIndex: float, /) -> None: ...
        def setVertexCount(self, vertexCount: int, /) -> None: ...
        def setVerticesPerPatch(self, verticesPerPatch: int, /) -> None: ...
        def sortIndex(self, /) -> float: ...
        def vertexCount(self, /) -> int: ...
        def verticesPerPatch(self, /) -> int: ...

    class QGraphicsApiFilter(PySide6.QtCore.QObject):
        # apiChanged(Qt3DRender::QGraphicsApiFilter::Api)
        apiChanged: typing.ClassVar[Signal[
            [PySide6.Qt3DRender.Qt3DRender.QGraphicsApiFilter.Api], [], [], [], [], [], [], [],
            [PySide6.Qt3DRender.Qt3DRender.QGraphicsApiFilter.Api], [PySide6.Qt3DRender.Qt3DRender.QGraphicsApiFilter.Api], [PySide6.Qt3DRender.Qt3DRender.QGraphicsApiFilter.Api], [PySide6.Qt3DRender.Qt3DRender.QGraphicsApiFilter.Api], [PySide6.Qt3DRender.Qt3DRender.QGraphicsApiFilter.Api], [PySide6.Qt3DRender.Qt3DRender.QGraphicsApiFilter.Api], [PySide6.Qt3DRender.Qt3DRender.QGraphicsApiFilter.Api], [PySide6.Qt3DRender.Qt3DRender.QGraphicsApiFilter.Api]
        ]]
        # extensionsChanged(QStringList)
        extensionsChanged: typing.ClassVar[Signal[
            [typing.List[str]], [], [], [], [], [], [], [],
            [typing.List[str]], [typing.List[str]], [typing.List[str]], [typing.List[str]], [typing.List[str]], [typing.List[str]], [typing.List[str]], [typing.List[str]]
        ]]
        # graphicsApiFilterChanged()
        graphicsApiFilterChanged: typing.ClassVar[Signal[
            [], [], [], [], [], [], [], [],
            [], [], [], [], [], [], [], []
        ]]
        # majorVersionChanged(int)
        majorVersionChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]
        # minorVersionChanged(int)
        minorVersionChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]
        # profileChanged(Qt3DRender::QGraphicsApiFilter::OpenGLProfile)
        profileChanged: typing.ClassVar[Signal[
            [PySide6.Qt3DRender.Qt3DRender.QGraphicsApiFilter.OpenGLProfile], [], [], [], [], [], [], [],
            [PySide6.Qt3DRender.Qt3DRender.QGraphicsApiFilter.OpenGLProfile], [PySide6.Qt3DRender.Qt3DRender.QGraphicsApiFilter.OpenGLProfile], [PySide6.Qt3DRender.Qt3DRender.QGraphicsApiFilter.OpenGLProfile], [PySide6.Qt3DRender.Qt3DRender.QGraphicsApiFilter.OpenGLProfile], [PySide6.Qt3DRender.Qt3DRender.QGraphicsApiFilter.OpenGLProfile], [PySide6.Qt3DRender.Qt3DRender.QGraphicsApiFilter.OpenGLProfile], [PySide6.Qt3DRender.Qt3DRender.QGraphicsApiFilter.OpenGLProfile], [PySide6.Qt3DRender.Qt3DRender.QGraphicsApiFilter.OpenGLProfile]
        ]]
        # vendorChanged(QString)
        vendorChanged: typing.ClassVar[Signal[
            [str], [], [], [], [], [], [], [],
            [str], [str], [str], [str], [str], [str], [str], [str]
        ]]

        class Api(enum.Enum):
            OpenGL                    = 0x1
            OpenGLES                  = 0x2
            Vulkan                    = 0x3
            DirectX                   = 0x4
            RHI                       = 0x5

        class OpenGLProfile(enum.Enum):
            NoProfile                 = 0x0
            CoreProfile               = 0x1
            CompatibilityProfile      = 0x2

        def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., *, api: PySide6.Qt3DRender.Qt3DRender.QGraphicsApiFilter.Api | None = ..., profile: PySide6.Qt3DRender.Qt3DRender.QGraphicsApiFilter.OpenGLProfile | None = ..., minorVersion: int | None = ..., majorVersion: int | None = ..., extensions: collections.abc.Sequence[str] | None = ..., vendor: str | None = ...) -> None: ...

        def api(self, /) -> PySide6.Qt3DRender.Qt3DRender.QGraphicsApiFilter.Api: ...
        def extensions(self, /) -> typing.List[str]: ...
        def majorVersion(self, /) -> int: ...
        def minorVersion(self, /) -> int: ...
        def profile(self, /) -> PySide6.Qt3DRender.Qt3DRender.QGraphicsApiFilter.OpenGLProfile: ...
        def setApi(self, api: PySide6.Qt3DRender.Qt3DRender.QGraphicsApiFilter.Api, /) -> None: ...
        def setExtensions(self, extensions: collections.abc.Sequence[str], /) -> None: ...
        def setMajorVersion(self, majorVersion: int, /) -> None: ...
        def setMinorVersion(self, minorVersion: int, /) -> None: ...
        def setProfile(self, profile: PySide6.Qt3DRender.Qt3DRender.QGraphicsApiFilter.OpenGLProfile, /) -> None: ...
        def setVendor(self, vendor: str, /) -> None: ...
        def vendor(self, /) -> str: ...

    class QLayer(PySide6.Qt3DCore.Qt3DCore.QComponent):
        # recursiveChanged()
        recursiveChanged: typing.ClassVar[Signal[
            [], [], [], [], [], [], [], [],
            [], [], [], [], [], [], [], []
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, recursive: bool | None = ...) -> None: ...

        def recursive(self, /) -> bool: ...
        def setRecursive(self, recursive: bool, /) -> None: ...

    class QLayerFilter(PySide6.Qt3DRender.Qt3DRender.QFrameGraphNode):
        # filterModeChanged(FilterMode)
        filterModeChanged: typing.ClassVar[Signal[
            [FilterMode], [], [], [], [], [], [], [],
            [FilterMode], [FilterMode], [FilterMode], [FilterMode], [FilterMode], [FilterMode], [FilterMode], [FilterMode]
        ]]

        class FilterMode(enum.Enum):
            AcceptAnyMatchingLayers   = 0x0
            AcceptAllMatchingLayers   = 0x1
            DiscardAnyMatchingLayers  = 0x2
            DiscardAllMatchingLayers  = 0x3

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, filterMode: PySide6.Qt3DRender.Qt3DRender.QLayerFilter.FilterMode | None = ...) -> None: ...

        def addLayer(self, layer: PySide6.Qt3DRender.Qt3DRender.QLayer, /) -> None: ...
        def filterMode(self, /) -> PySide6.Qt3DRender.Qt3DRender.QLayerFilter.FilterMode: ...
        def layers(self, /) -> typing.List[PySide6.Qt3DRender.Qt3DRender.QLayer]: ...
        def removeLayer(self, layer: PySide6.Qt3DRender.Qt3DRender.QLayer, /) -> None: ...
        def setFilterMode(self, filterMode: PySide6.Qt3DRender.Qt3DRender.QLayerFilter.FilterMode, /) -> None: ...

    class QLevelOfDetail(PySide6.Qt3DCore.Qt3DCore.QComponent):
        # cameraChanged(QCamera*)
        cameraChanged: typing.ClassVar[Signal[
            [PySide6.QtMultimedia.QCamera], [], [], [], [], [], [], [],
            [PySide6.QtMultimedia.QCamera], [PySide6.QtMultimedia.QCamera], [PySide6.QtMultimedia.QCamera], [PySide6.QtMultimedia.QCamera], [PySide6.QtMultimedia.QCamera], [PySide6.QtMultimedia.QCamera], [PySide6.QtMultimedia.QCamera], [PySide6.QtMultimedia.QCamera]
        ]]
        # currentIndexChanged(int)
        currentIndexChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]
        # thresholdTypeChanged(ThresholdType)
        thresholdTypeChanged: typing.ClassVar[Signal[
            [ThresholdType], [], [], [], [], [], [], [],
            [ThresholdType], [ThresholdType], [ThresholdType], [ThresholdType], [ThresholdType], [ThresholdType], [ThresholdType], [ThresholdType]
        ]]
        # thresholdsChanged(QList<qreal>)
        thresholdsChanged: typing.ClassVar[Signal[
            [collections.abc.Sequence[float]], [], [], [], [], [], [], [],
            [collections.abc.Sequence[float]], [collections.abc.Sequence[float]], [collections.abc.Sequence[float]], [collections.abc.Sequence[float]], [collections.abc.Sequence[float]], [collections.abc.Sequence[float]], [collections.abc.Sequence[float]], [collections.abc.Sequence[float]]
        ]]
        # volumeOverrideChanged(QLevelOfDetailBoundingSphere)
        volumeOverrideChanged: typing.ClassVar[Signal[
            [PySide6.Qt3DRender.Qt3DRender.QLevelOfDetailBoundingSphere], [], [], [], [], [], [], [],
            [PySide6.Qt3DRender.Qt3DRender.QLevelOfDetailBoundingSphere], [PySide6.Qt3DRender.Qt3DRender.QLevelOfDetailBoundingSphere], [PySide6.Qt3DRender.Qt3DRender.QLevelOfDetailBoundingSphere], [PySide6.Qt3DRender.Qt3DRender.QLevelOfDetailBoundingSphere], [PySide6.Qt3DRender.Qt3DRender.QLevelOfDetailBoundingSphere], [PySide6.Qt3DRender.Qt3DRender.QLevelOfDetailBoundingSphere], [PySide6.Qt3DRender.Qt3DRender.QLevelOfDetailBoundingSphere], [PySide6.Qt3DRender.Qt3DRender.QLevelOfDetailBoundingSphere]
        ]]

        class ThresholdType(enum.Enum):
            DistanceToCameraThreshold = 0x0
            ProjectedScreenPixelSizeThreshold = 0x1

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, camera: PySide6.Qt3DRender.Qt3DRender.QCamera | None = ..., currentIndex: int | None = ..., thresholdType: PySide6.Qt3DRender.Qt3DRender.QLevelOfDetail.ThresholdType | None = ..., thresholds: collections.abc.Sequence[float] | None = ..., volumeOverride: PySide6.Qt3DRender.Qt3DRender.QLevelOfDetailBoundingSphere | None = ...) -> None: ...

        def camera(self, /) -> PySide6.Qt3DRender.Qt3DRender.QCamera: ...
        def createBoundingSphere(self, center: PySide6.QtGui.QVector3D, radius: float, /) -> PySide6.Qt3DRender.Qt3DRender.QLevelOfDetailBoundingSphere: ...
        def currentIndex(self, /) -> int: ...
        def setCamera(self, camera: PySide6.Qt3DRender.Qt3DRender.QCamera, /) -> None: ...
        def setCurrentIndex(self, currentIndex: int, /) -> None: ...
        def setThresholdType(self, thresholdType: PySide6.Qt3DRender.Qt3DRender.QLevelOfDetail.ThresholdType, /) -> None: ...
        def setThresholds(self, thresholds: collections.abc.Sequence[float], /) -> None: ...
        def setVolumeOverride(self, volumeOverride: PySide6.Qt3DRender.Qt3DRender.QLevelOfDetailBoundingSphere, /) -> None: ...
        def thresholdType(self, /) -> PySide6.Qt3DRender.Qt3DRender.QLevelOfDetail.ThresholdType: ...
        def thresholds(self, /) -> typing.List[float]: ...
        def volumeOverride(self, /) -> PySide6.Qt3DRender.Qt3DRender.QLevelOfDetailBoundingSphere: ...

    class QLevelOfDetailBoundingSphere(shiboken6.Shiboken.Object):
        @typing.overload
        def __init__(self, other: PySide6.Qt3DRender.Qt3DRender.QLevelOfDetailBoundingSphere, /, *, center: PySide6.QtGui.QVector3D | None = ..., radius: float | None = ...) -> None: ...
        @typing.overload
        def __init__(self, /, center: PySide6.QtGui.QVector3D = ..., radius: float = ...) -> None: ...

        def __eq__(self, other: PySide6.Qt3DRender.Qt3DRender.QLevelOfDetailBoundingSphere, /) -> bool: ...
        def __ne__(self, other: PySide6.Qt3DRender.Qt3DRender.QLevelOfDetailBoundingSphere, /) -> bool: ...
        def center(self, /) -> PySide6.QtGui.QVector3D: ...
        def isEmpty(self, /) -> bool: ...
        def radius(self, /) -> float: ...

    class QLevelOfDetailSwitch(PySide6.Qt3DRender.Qt3DRender.QLevelOfDetail):
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...) -> None: ...

    class QLineWidth(PySide6.Qt3DRender.Qt3DRender.QRenderState):
        # smoothChanged(bool)
        smoothChanged: typing.ClassVar[Signal[
            [bool], [], [], [], [], [], [], [],
            [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
        ]]
        # valueChanged(float)
        valueChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, value: float | None = ..., smooth: bool | None = ...) -> None: ...

        def setSmooth(self, enabled: bool, /) -> None: ...
        def setValue(self, value: float, /) -> None: ...
        def smooth(self, /) -> bool: ...
        def value(self, /) -> float: ...

    class QMaterial(PySide6.Qt3DCore.Qt3DCore.QComponent):
        # effectChanged(QEffect*)
        effectChanged: typing.ClassVar[Signal[
            [PySide6.Qt3DRender.Qt3DRender.QEffect], [], [], [], [], [], [], [],
            [PySide6.Qt3DRender.Qt3DRender.QEffect], [PySide6.Qt3DRender.Qt3DRender.QEffect], [PySide6.Qt3DRender.Qt3DRender.QEffect], [PySide6.Qt3DRender.Qt3DRender.QEffect], [PySide6.Qt3DRender.Qt3DRender.QEffect], [PySide6.Qt3DRender.Qt3DRender.QEffect], [PySide6.Qt3DRender.Qt3DRender.QEffect], [PySide6.Qt3DRender.Qt3DRender.QEffect]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, effect: PySide6.Qt3DRender.Qt3DRender.QEffect | None = ...) -> None: ...

        def addParameter(self, parameter: PySide6.Qt3DRender.Qt3DRender.QParameter, /) -> None: ...
        def effect(self, /) -> PySide6.Qt3DRender.Qt3DRender.QEffect: ...
        def parameters(self, /) -> typing.List[PySide6.Qt3DRender.Qt3DRender.QParameter]: ...
        def removeParameter(self, parameter: PySide6.Qt3DRender.Qt3DRender.QParameter, /) -> None: ...
        def setEffect(self, effect: PySide6.Qt3DRender.Qt3DRender.QEffect, /) -> None: ...

    class QMemoryBarrier(PySide6.Qt3DRender.Qt3DRender.QFrameGraphNode):
        # waitOperationsChanged(QMemoryBarrier::Operations)
        waitOperationsChanged: typing.ClassVar[Signal[
            [PySide6.Qt3DRender.Qt3DRender.QMemoryBarrier.Operation], [], [], [], [], [], [], [],
            [PySide6.Qt3DRender.Qt3DRender.QMemoryBarrier.Operation], [PySide6.Qt3DRender.Qt3DRender.QMemoryBarrier.Operation], [PySide6.Qt3DRender.Qt3DRender.QMemoryBarrier.Operation], [PySide6.Qt3DRender.Qt3DRender.QMemoryBarrier.Operation], [PySide6.Qt3DRender.Qt3DRender.QMemoryBarrier.Operation], [PySide6.Qt3DRender.Qt3DRender.QMemoryBarrier.Operation], [PySide6.Qt3DRender.Qt3DRender.QMemoryBarrier.Operation], [PySide6.Qt3DRender.Qt3DRender.QMemoryBarrier.Operation]
        ]]

        class Operation(enum.Flag):
            All                       = -1
            None_                     = 0x0
            VertexAttributeArray      = 0x1
            ElementArray              = 0x2
            Uniform                   = 0x4
            TextureFetch              = 0x8
            ShaderImageAccess         = 0x10
            Command                   = 0x20
            PixelBuffer               = 0x40
            TextureUpdate             = 0x80
            BufferUpdate              = 0x100
            FrameBuffer               = 0x200
            TransformFeedback         = 0x400
            AtomicCounter             = 0x800
            ShaderStorage             = 0x1000
            QueryBuffer               = 0x2000

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...) -> None: ...

        def setWaitOperations(self, operations: PySide6.Qt3DRender.Qt3DRender.QMemoryBarrier.Operation, /) -> None: ...
        def waitOperations(self, /) -> PySide6.Qt3DRender.Qt3DRender.QMemoryBarrier.Operation: ...

    class QMesh(PySide6.Qt3DRender.Qt3DRender.QGeometryRenderer):
        # meshNameChanged(QString)
        meshNameChanged: typing.ClassVar[Signal[
            [str], [], [], [], [], [], [], [],
            [str], [str], [str], [str], [str], [str], [str], [str]
        ]]
        # sourceChanged(QUrl)
        sourceChanged: typing.ClassVar[Signal[
            [PySide6.QtCore.QUrl], [], [], [], [], [], [], [],
            [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl]
        ]]
        # statusChanged(Status)
        statusChanged: typing.ClassVar[Signal[
            [Status], [], [], [], [], [], [], [],
            [Status], [Status], [Status], [Status], [Status], [Status], [Status], [Status]
        ]]

        class Status(enum.Enum):
            None_                     = 0x0
            Loading                   = 0x1
            Ready                     = 0x2
            Error                     = 0x3

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, source: PySide6.QtCore.QUrl | None = ..., meshName: str | None = ..., status: PySide6.Qt3DRender.Qt3DRender.QMesh.Status | None = ...) -> None: ...

        def meshName(self, /) -> str: ...
        def setMeshName(self, meshName: str, /) -> None: ...
        def setSource(self, source: PySide6.QtCore.QUrl | str, /) -> None: ...
        def source(self, /) -> PySide6.QtCore.QUrl: ...
        def status(self, /) -> PySide6.Qt3DRender.Qt3DRender.QMesh.Status: ...

    class QMultiSampleAntiAliasing(PySide6.Qt3DRender.Qt3DRender.QRenderState):
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...) -> None: ...

    class QNoDepthMask(PySide6.Qt3DRender.Qt3DRender.QRenderState):
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...) -> None: ...

    class QNoDraw(PySide6.Qt3DRender.Qt3DRender.QFrameGraphNode):
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...) -> None: ...

    class QNoPicking(PySide6.Qt3DRender.Qt3DRender.QFrameGraphNode):
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...) -> None: ...

    class QObjectPicker(PySide6.Qt3DCore.Qt3DCore.QComponent):
        # clicked(Qt3DRender::QPickEvent*)
        clicked: typing.ClassVar[Signal[
            [PySide6.Qt3DRender.Qt3DRender.QPickEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DRender.Qt3DRender.QPickEvent], [PySide6.Qt3DRender.Qt3DRender.QPickEvent], [PySide6.Qt3DRender.Qt3DRender.QPickEvent], [PySide6.Qt3DRender.Qt3DRender.QPickEvent], [PySide6.Qt3DRender.Qt3DRender.QPickEvent], [PySide6.Qt3DRender.Qt3DRender.QPickEvent], [PySide6.Qt3DRender.Qt3DRender.QPickEvent], [PySide6.Qt3DRender.Qt3DRender.QPickEvent]
        ]]
        # containsMouseChanged(bool)
        containsMouseChanged: typing.ClassVar[Signal[
            [bool], [], [], [], [], [], [], [],
            [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
        ]]
        # dragEnabledChanged(bool)
        dragEnabledChanged: typing.ClassVar[Signal[
            [bool], [], [], [], [], [], [], [],
            [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
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
        # hoverEnabledChanged(bool)
        hoverEnabledChanged: typing.ClassVar[Signal[
            [bool], [], [], [], [], [], [], [],
            [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
        ]]
        # moved(Qt3DRender::QPickEvent*)
        moved: typing.ClassVar[Signal[
            [PySide6.Qt3DRender.Qt3DRender.QPickEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DRender.Qt3DRender.QPickEvent], [PySide6.Qt3DRender.Qt3DRender.QPickEvent], [PySide6.Qt3DRender.Qt3DRender.QPickEvent], [PySide6.Qt3DRender.Qt3DRender.QPickEvent], [PySide6.Qt3DRender.Qt3DRender.QPickEvent], [PySide6.Qt3DRender.Qt3DRender.QPickEvent], [PySide6.Qt3DRender.Qt3DRender.QPickEvent], [PySide6.Qt3DRender.Qt3DRender.QPickEvent]
        ]]
        # pressed(Qt3DRender::QPickEvent*)
        pressed: typing.ClassVar[Signal[
            [PySide6.Qt3DRender.Qt3DRender.QPickEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DRender.Qt3DRender.QPickEvent], [PySide6.Qt3DRender.Qt3DRender.QPickEvent], [PySide6.Qt3DRender.Qt3DRender.QPickEvent], [PySide6.Qt3DRender.Qt3DRender.QPickEvent], [PySide6.Qt3DRender.Qt3DRender.QPickEvent], [PySide6.Qt3DRender.Qt3DRender.QPickEvent], [PySide6.Qt3DRender.Qt3DRender.QPickEvent], [PySide6.Qt3DRender.Qt3DRender.QPickEvent]
        ]]
        # pressedChanged(bool)
        pressedChanged: typing.ClassVar[Signal[
            [bool], [], [], [], [], [], [], [],
            [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
        ]]
        # priorityChanged(int)
        priorityChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]
        # released(Qt3DRender::QPickEvent*)
        released: typing.ClassVar[Signal[
            [PySide6.Qt3DRender.Qt3DRender.QPickEvent], [], [], [], [], [], [], [],
            [PySide6.Qt3DRender.Qt3DRender.QPickEvent], [PySide6.Qt3DRender.Qt3DRender.QPickEvent], [PySide6.Qt3DRender.Qt3DRender.QPickEvent], [PySide6.Qt3DRender.Qt3DRender.QPickEvent], [PySide6.Qt3DRender.Qt3DRender.QPickEvent], [PySide6.Qt3DRender.Qt3DRender.QPickEvent], [PySide6.Qt3DRender.Qt3DRender.QPickEvent], [PySide6.Qt3DRender.Qt3DRender.QPickEvent]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, hoverEnabled: bool | None = ..., dragEnabled: bool | None = ..., pressed: bool | None = ..., containsMouse: bool | None = ..., priority: int | None = ...) -> None: ...

        def containsMouse(self, /) -> bool: ...
        def isDragEnabled(self, /) -> bool: ...
        def isHoverEnabled(self, /) -> bool: ...
        def isPressed(self, /) -> bool: ...
        def priority(self, /) -> int: ...
        def setDragEnabled(self, dragEnabled: bool, /) -> None: ...
        def setHoverEnabled(self, hoverEnabled: bool, /) -> None: ...
        def setPriority(self, priority: int, /) -> None: ...

    class QPaintedTextureImage(PySide6.Qt3DRender.Qt3DRender.QAbstractTextureImage):
        # heightChanged(int)
        heightChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]
        # sizeChanged(QSize)
        sizeChanged: typing.ClassVar[Signal[
            [PySide6.QtCore.QSize], [], [], [], [], [], [], [],
            [PySide6.QtCore.QSize], [PySide6.QtCore.QSize], [PySide6.QtCore.QSize], [PySide6.QtCore.QSize], [PySide6.QtCore.QSize], [PySide6.QtCore.QSize], [PySide6.QtCore.QSize], [PySide6.QtCore.QSize]
        ]]
        # widthChanged(int)
        widthChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, width: int | None = ..., height: int | None = ..., size: PySide6.QtCore.QSize | None = ...) -> None: ...

        def dataGenerator(self, /) -> PySide6.Qt3DRender.Qt3DRender.QTextureImageDataGeneratorPtr: ...
        def height(self, /) -> int: ...
        def paint(self, painter: PySide6.QtGui.QPainter, /) -> None: ...
        def setHeight(self, h: int, /) -> None: ...
        def setSize(self, size: PySide6.QtCore.QSize, /) -> None: ...
        def setWidth(self, w: int, /) -> None: ...
        def size(self, /) -> PySide6.QtCore.QSize: ...
        def update(self, /, rect: PySide6.QtCore.QRect = ...) -> None: ...
        def width(self, /) -> int: ...

    class QParameter(PySide6.Qt3DCore.Qt3DCore.QNode):
        # nameChanged(QString)
        nameChanged: typing.ClassVar[Signal[
            [str], [], [], [], [], [], [], [],
            [str], [str], [str], [str], [str], [str], [str], [str]
        ]]
        # valueChanged(QVariant)
        valueChanged: typing.ClassVar[Signal[
            [typing.Any], [], [], [], [], [], [], [],
            [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any]
        ]]

        @typing.overload
        def __init__(self, name: str, texture: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, value: typing.Any | None = ...) -> None: ...
        @typing.overload
        def __init__(self, name: str, value: typing.Any, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...) -> None: ...
        @typing.overload
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, name: str | None = ..., value: typing.Any | None = ...) -> None: ...

        def name(self, /) -> str: ...
        def setName(self, name: str, /) -> None: ...
        def setValue(self, dv: typing.Any, /) -> None: ...
        def value(self, /) -> typing.Any: ...

    class QPickEvent(PySide6.QtCore.QObject):
        # acceptedChanged(bool)
        acceptedChanged: typing.ClassVar[Signal[
            [bool], [], [], [], [], [], [], [],
            [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
        ]]

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

        @typing.overload
        def __init__(self, position: PySide6.QtCore.QPointF | PySide6.QtCore.QPoint | PySide6.QtGui.QPainterPath.Element, worldIntersection: PySide6.QtGui.QVector3D, localIntersection: PySide6.QtGui.QVector3D, distance: float, button: PySide6.Qt3DRender.Qt3DRender.QPickEvent.Buttons, buttons: int, modifiers: int, /, *, accepted: bool | None = ..., viewport: PySide6.Qt3DRender.Qt3DRender.QViewport | None = ..., entity: PySide6.Qt3DCore.Qt3DCore.QEntity | None = ...) -> None: ...
        @typing.overload
        def __init__(self, position: PySide6.QtCore.QPointF | PySide6.QtCore.QPoint | PySide6.QtGui.QPainterPath.Element, worldIntersection: PySide6.QtGui.QVector3D, localIntersection: PySide6.QtGui.QVector3D, distance: float, /, *, accepted: bool | None = ..., button: PySide6.Qt3DRender.Qt3DRender.QPickEvent.Buttons | None = ..., buttons: int | None = ..., modifiers: int | None = ..., viewport: PySide6.Qt3DRender.Qt3DRender.QViewport | None = ..., entity: PySide6.Qt3DCore.Qt3DCore.QEntity | None = ...) -> None: ...
        @typing.overload
        def __init__(self, /, *, accepted: bool | None = ..., position: PySide6.QtCore.QPointF | None = ..., distance: float | None = ..., localIntersection: PySide6.QtGui.QVector3D | None = ..., worldIntersection: PySide6.QtGui.QVector3D | None = ..., button: PySide6.Qt3DRender.Qt3DRender.QPickEvent.Buttons | None = ..., buttons: int | None = ..., modifiers: int | None = ..., viewport: PySide6.Qt3DRender.Qt3DRender.QViewport | None = ..., entity: PySide6.Qt3DCore.Qt3DCore.QEntity | None = ...) -> None: ...

        def button(self, /) -> PySide6.Qt3DRender.Qt3DRender.QPickEvent.Buttons: ...
        def buttons(self, /) -> int: ...
        def distance(self, /) -> float: ...
        def entity(self, /) -> PySide6.Qt3DCore.Qt3DCore.QEntity: ...
        def isAccepted(self, /) -> bool: ...
        def localIntersection(self, /) -> PySide6.QtGui.QVector3D: ...
        def modifiers(self, /) -> int: ...
        def position(self, /) -> PySide6.QtCore.QPointF: ...
        def setAccepted(self, accepted: bool, /) -> None: ...
        def viewport(self, /) -> PySide6.Qt3DRender.Qt3DRender.QViewport: ...
        def worldIntersection(self, /) -> PySide6.QtGui.QVector3D: ...

    class QPickLineEvent(PySide6.Qt3DRender.Qt3DRender.QPickEvent):
        @typing.overload
        def __init__(self, position: PySide6.QtCore.QPointF | PySide6.QtCore.QPoint | PySide6.QtGui.QPainterPath.Element, worldIntersection: PySide6.QtGui.QVector3D, localIntersection: PySide6.QtGui.QVector3D, distance: float, edgeIndex: int, vertex1Index: int, vertex2Index: int, button: PySide6.Qt3DRender.Qt3DRender.QPickEvent.Buttons, buttons: int, modifiers: int, /) -> None: ...
        @typing.overload
        def __init__(self, /, *, edgeIndex: int | None = ..., vertex1Index: int | None = ..., vertex2Index: int | None = ...) -> None: ...

        def edgeIndex(self, /) -> int: ...
        def vertex1Index(self, /) -> int: ...
        def vertex2Index(self, /) -> int: ...

    class QPickPointEvent(PySide6.Qt3DRender.Qt3DRender.QPickEvent):
        @typing.overload
        def __init__(self, position: PySide6.QtCore.QPointF | PySide6.QtCore.QPoint | PySide6.QtGui.QPainterPath.Element, worldIntersection: PySide6.QtGui.QVector3D, localIntersection: PySide6.QtGui.QVector3D, distance: float, pointIndex: int, button: PySide6.Qt3DRender.Qt3DRender.QPickEvent.Buttons, buttons: int, modifiers: int, /) -> None: ...
        @typing.overload
        def __init__(self, /, *, pointIndex: int | None = ...) -> None: ...

        def pointIndex(self, /) -> int: ...

    class QPickTriangleEvent(PySide6.Qt3DRender.Qt3DRender.QPickEvent):
        @typing.overload
        def __init__(self, position: PySide6.QtCore.QPointF | PySide6.QtCore.QPoint | PySide6.QtGui.QPainterPath.Element, worldIntersection: PySide6.QtGui.QVector3D, localIntersection: PySide6.QtGui.QVector3D, distance: float, triangleIndex: int, vertex1Index: int, vertex2Index: int, vertex3Index: int, button: PySide6.Qt3DRender.Qt3DRender.QPickEvent.Buttons, buttons: int, modifiers: int, uvw: PySide6.QtGui.QVector3D, /) -> None: ...
        @typing.overload
        def __init__(self, position: PySide6.QtCore.QPointF | PySide6.QtCore.QPoint | PySide6.QtGui.QPainterPath.Element, worldIntersection: PySide6.QtGui.QVector3D, localIntersection: PySide6.QtGui.QVector3D, distance: float, triangleIndex: int, vertex1Index: int, vertex2Index: int, vertex3Index: int, /, *, uvw: PySide6.QtGui.QVector3D | None = ...) -> None: ...
        @typing.overload
        def __init__(self, /, *, triangleIndex: int | None = ..., vertex1Index: int | None = ..., vertex2Index: int | None = ..., vertex3Index: int | None = ..., uvw: PySide6.QtGui.QVector3D | None = ...) -> None: ...

        def triangleIndex(self, /) -> int: ...
        def uvw(self, /) -> PySide6.QtGui.QVector3D: ...
        def vertex1Index(self, /) -> int: ...
        def vertex2Index(self, /) -> int: ...
        def vertex3Index(self, /) -> int: ...

    class QPickingProxy(PySide6.Qt3DCore.Qt3DCore.QBoundingVolume):
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...) -> None: ...

    class QPickingSettings(PySide6.Qt3DCore.Qt3DCore.QNode):
        # faceOrientationPickingModeChanged(QPickingSettings::FaceOrientationPickingMode)
        faceOrientationPickingModeChanged: typing.ClassVar[Signal[
            [PySide6.Qt3DRender.Qt3DRender.QPickingSettings.FaceOrientationPickingMode], [], [], [], [], [], [], [],
            [PySide6.Qt3DRender.Qt3DRender.QPickingSettings.FaceOrientationPickingMode], [PySide6.Qt3DRender.Qt3DRender.QPickingSettings.FaceOrientationPickingMode], [PySide6.Qt3DRender.Qt3DRender.QPickingSettings.FaceOrientationPickingMode], [PySide6.Qt3DRender.Qt3DRender.QPickingSettings.FaceOrientationPickingMode], [PySide6.Qt3DRender.Qt3DRender.QPickingSettings.FaceOrientationPickingMode], [PySide6.Qt3DRender.Qt3DRender.QPickingSettings.FaceOrientationPickingMode], [PySide6.Qt3DRender.Qt3DRender.QPickingSettings.FaceOrientationPickingMode], [PySide6.Qt3DRender.Qt3DRender.QPickingSettings.FaceOrientationPickingMode]
        ]]
        # pickMethodChanged(QPickingSettings::PickMethod)
        pickMethodChanged: typing.ClassVar[Signal[
            [PySide6.Qt3DRender.Qt3DRender.QPickingSettings.PickMethod], [], [], [], [], [], [], [],
            [PySide6.Qt3DRender.Qt3DRender.QPickingSettings.PickMethod], [PySide6.Qt3DRender.Qt3DRender.QPickingSettings.PickMethod], [PySide6.Qt3DRender.Qt3DRender.QPickingSettings.PickMethod], [PySide6.Qt3DRender.Qt3DRender.QPickingSettings.PickMethod], [PySide6.Qt3DRender.Qt3DRender.QPickingSettings.PickMethod], [PySide6.Qt3DRender.Qt3DRender.QPickingSettings.PickMethod], [PySide6.Qt3DRender.Qt3DRender.QPickingSettings.PickMethod], [PySide6.Qt3DRender.Qt3DRender.QPickingSettings.PickMethod]
        ]]
        # pickResultModeChanged(QPickingSettings::PickResultMode)
        pickResultModeChanged: typing.ClassVar[Signal[
            [PySide6.Qt3DRender.Qt3DRender.QPickingSettings.PickResultMode], [], [], [], [], [], [], [],
            [PySide6.Qt3DRender.Qt3DRender.QPickingSettings.PickResultMode], [PySide6.Qt3DRender.Qt3DRender.QPickingSettings.PickResultMode], [PySide6.Qt3DRender.Qt3DRender.QPickingSettings.PickResultMode], [PySide6.Qt3DRender.Qt3DRender.QPickingSettings.PickResultMode], [PySide6.Qt3DRender.Qt3DRender.QPickingSettings.PickResultMode], [PySide6.Qt3DRender.Qt3DRender.QPickingSettings.PickResultMode], [PySide6.Qt3DRender.Qt3DRender.QPickingSettings.PickResultMode], [PySide6.Qt3DRender.Qt3DRender.QPickingSettings.PickResultMode]
        ]]
        # worldSpaceToleranceChanged(float)
        worldSpaceToleranceChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]

        class FaceOrientationPickingMode(enum.Enum):
            FrontFace                 = 0x1
            BackFace                  = 0x2
            FrontAndBackFace          = 0x3

        class PickMethod(enum.Enum):
            BoundingVolumePicking     = 0x0
            TrianglePicking           = 0x1
            LinePicking               = 0x2
            PointPicking              = 0x4
            PrimitivePicking          = 0x7

        class PickResultMode(enum.Enum):
            NearestPick               = 0x0
            AllPicks                  = 0x1
            NearestPriorityPick       = 0x2

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, pickMethod: PySide6.Qt3DRender.Qt3DRender.QPickingSettings.PickMethod | None = ..., pickResultMode: PySide6.Qt3DRender.Qt3DRender.QPickingSettings.PickResultMode | None = ..., faceOrientationPickingMode: PySide6.Qt3DRender.Qt3DRender.QPickingSettings.FaceOrientationPickingMode | None = ..., worldSpaceTolerance: float | None = ...) -> None: ...

        def faceOrientationPickingMode(self, /) -> PySide6.Qt3DRender.Qt3DRender.QPickingSettings.FaceOrientationPickingMode: ...
        def pickMethod(self, /) -> PySide6.Qt3DRender.Qt3DRender.QPickingSettings.PickMethod: ...
        def pickResultMode(self, /) -> PySide6.Qt3DRender.Qt3DRender.QPickingSettings.PickResultMode: ...
        def setFaceOrientationPickingMode(self, faceOrientationPickingMode: PySide6.Qt3DRender.Qt3DRender.QPickingSettings.FaceOrientationPickingMode, /) -> None: ...
        def setPickMethod(self, pickMethod: PySide6.Qt3DRender.Qt3DRender.QPickingSettings.PickMethod, /) -> None: ...
        def setPickResultMode(self, pickResultMode: PySide6.Qt3DRender.Qt3DRender.QPickingSettings.PickResultMode, /) -> None: ...
        def setWorldSpaceTolerance(self, worldSpaceTolerance: float, /) -> None: ...
        def worldSpaceTolerance(self, /) -> float: ...

    class QPointLight(PySide6.Qt3DRender.Qt3DRender.QAbstractLight):
        # constantAttenuationChanged(float)
        constantAttenuationChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # linearAttenuationChanged(float)
        linearAttenuationChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # quadraticAttenuationChanged(float)
        quadraticAttenuationChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, constantAttenuation: float | None = ..., linearAttenuation: float | None = ..., quadraticAttenuation: float | None = ...) -> None: ...

        def constantAttenuation(self, /) -> float: ...
        def linearAttenuation(self, /) -> float: ...
        def quadraticAttenuation(self, /) -> float: ...
        def setConstantAttenuation(self, value: float, /) -> None: ...
        def setLinearAttenuation(self, value: float, /) -> None: ...
        def setQuadraticAttenuation(self, value: float, /) -> None: ...

    class QPointSize(PySide6.Qt3DRender.Qt3DRender.QRenderState):
        # sizeModeChanged(SizeMode)
        sizeModeChanged: typing.ClassVar[Signal[
            [SizeMode], [], [], [], [], [], [], [],
            [SizeMode], [SizeMode], [SizeMode], [SizeMode], [SizeMode], [SizeMode], [SizeMode], [SizeMode]
        ]]
        # valueChanged(float)
        valueChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]

        class SizeMode(enum.Enum):
            Fixed                     = 0x0
            Programmable              = 0x1

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, sizeMode: PySide6.Qt3DRender.Qt3DRender.QPointSize.SizeMode | None = ..., value: float | None = ...) -> None: ...

        def setSizeMode(self, sizeMode: PySide6.Qt3DRender.Qt3DRender.QPointSize.SizeMode, /) -> None: ...
        def setValue(self, value: float, /) -> None: ...
        def sizeMode(self, /) -> PySide6.Qt3DRender.Qt3DRender.QPointSize.SizeMode: ...
        def value(self, /) -> float: ...

    class QPolygonOffset(PySide6.Qt3DRender.Qt3DRender.QRenderState):
        # depthStepsChanged(float)
        depthStepsChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # scaleFactorChanged(float)
        scaleFactorChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, scaleFactor: float | None = ..., depthSteps: float | None = ...) -> None: ...

        def depthSteps(self, /) -> float: ...
        def scaleFactor(self, /) -> float: ...
        def setDepthSteps(self, depthSteps: float, /) -> None: ...
        def setScaleFactor(self, scaleFactor: float, /) -> None: ...

    class QProximityFilter(PySide6.Qt3DRender.Qt3DRender.QFrameGraphNode):
        # distanceThresholdChanged(float)
        distanceThresholdChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # entityChanged(Qt3DCore::QEntity*)
        entityChanged: typing.ClassVar[Signal[
            [PySide6.Qt3DCore.Qt3DCore.QEntity], [], [], [], [], [], [], [],
            [PySide6.Qt3DCore.Qt3DCore.QEntity], [PySide6.Qt3DCore.Qt3DCore.QEntity], [PySide6.Qt3DCore.Qt3DCore.QEntity], [PySide6.Qt3DCore.Qt3DCore.QEntity], [PySide6.Qt3DCore.Qt3DCore.QEntity], [PySide6.Qt3DCore.Qt3DCore.QEntity], [PySide6.Qt3DCore.Qt3DCore.QEntity], [PySide6.Qt3DCore.Qt3DCore.QEntity]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, entity: PySide6.Qt3DCore.Qt3DCore.QEntity | None = ..., distanceThreshold: float | None = ...) -> None: ...

        def distanceThreshold(self, /) -> float: ...
        def entity(self, /) -> PySide6.Qt3DCore.Qt3DCore.QEntity: ...
        def setDistanceThreshold(self, distanceThreshold: float, /) -> None: ...
        def setEntity(self, entity: PySide6.Qt3DCore.Qt3DCore.QEntity, /) -> None: ...

    class QRasterMode(PySide6.Qt3DRender.Qt3DRender.QRenderState):
        # faceModeChanged(FaceMode)
        faceModeChanged: typing.ClassVar[Signal[
            [FaceMode], [], [], [], [], [], [], [],
            [FaceMode], [FaceMode], [FaceMode], [FaceMode], [FaceMode], [FaceMode], [FaceMode], [FaceMode]
        ]]
        # rasterModeChanged(RasterMode)
        rasterModeChanged: typing.ClassVar[Signal[
            [RasterMode], [], [], [], [], [], [], [],
            [RasterMode], [RasterMode], [RasterMode], [RasterMode], [RasterMode], [RasterMode], [RasterMode], [RasterMode]
        ]]

        class FaceMode(enum.Enum):
            Front                     = 0x404
            Back                      = 0x405
            FrontAndBack              = 0x408

        class RasterMode(enum.Enum):
            Points                    = 0x1b00
            Lines                     = 0x1b01
            Fill                      = 0x1b02

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, rasterMode: PySide6.Qt3DRender.Qt3DRender.QRasterMode.RasterMode | None = ..., faceMode: PySide6.Qt3DRender.Qt3DRender.QRasterMode.FaceMode | None = ...) -> None: ...

        def faceMode(self, /) -> PySide6.Qt3DRender.Qt3DRender.QRasterMode.FaceMode: ...
        def rasterMode(self, /) -> PySide6.Qt3DRender.Qt3DRender.QRasterMode.RasterMode: ...
        def setFaceMode(self, faceMode: PySide6.Qt3DRender.Qt3DRender.QRasterMode.FaceMode, /) -> None: ...
        def setRasterMode(self, rasterMode: PySide6.Qt3DRender.Qt3DRender.QRasterMode.RasterMode, /) -> None: ...

    class QRayCaster(PySide6.Qt3DRender.Qt3DRender.QAbstractRayCaster):
        # directionChanged(QVector3D)
        directionChanged: typing.ClassVar[Signal[
            [PySide6.QtGui.QVector3D], [], [], [], [], [], [], [],
            [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D]
        ]]
        # lengthChanged(float)
        lengthChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # originChanged(QVector3D)
        originChanged: typing.ClassVar[Signal[
            [PySide6.QtGui.QVector3D], [], [], [], [], [], [], [],
            [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, origin: PySide6.QtGui.QVector3D | None = ..., direction: PySide6.QtGui.QVector3D | None = ..., length: float | None = ...) -> None: ...

        def direction(self, /) -> PySide6.QtGui.QVector3D: ...
        def length(self, /) -> float: ...
        def origin(self, /) -> PySide6.QtGui.QVector3D: ...
        def pick(self, origin: PySide6.QtGui.QVector3D, direction: PySide6.QtGui.QVector3D, length: float, /) -> typing.List[PySide6.Qt3DRender.Qt3DRender.QRayCasterHit]: ...
        def setDirection(self, direction: PySide6.QtGui.QVector3D, /) -> None: ...
        def setLength(self, length: float, /) -> None: ...
        def setOrigin(self, origin: PySide6.QtGui.QVector3D, /) -> None: ...
        @typing.overload
        def trigger(self, /) -> None: ...
        @typing.overload
        def trigger(self, origin: PySide6.QtGui.QVector3D, direction: PySide6.QtGui.QVector3D, length: float, /) -> None: ...

    class QRayCasterHit(shiboken6.Shiboken.Object):
        class HitType(enum.Enum):
            TriangleHit               = 0x0
            LineHit                   = 0x1
            PointHit                  = 0x2
            EntityHit                 = 0x3

        @typing.overload
        def __init__(self, type: PySide6.Qt3DRender.Qt3DRender.QRayCasterHit.HitType, id: PySide6.Qt3DCore.Qt3DCore.QNodeId, distance: float, localIntersect: PySide6.QtGui.QVector3D, worldIntersect: PySide6.QtGui.QVector3D, primitiveIndex: int, v1: int, v2: int, v3: int, /, *, entityId: PySide6.Qt3DCore.Qt3DCore.QNodeId | None = ..., entity: PySide6.Qt3DCore.Qt3DCore.QEntity | None = ..., localIntersection: PySide6.QtGui.QVector3D | None = ..., worldIntersection: PySide6.QtGui.QVector3D | None = ..., vertex1Index: int | None = ..., vertex2Index: int | None = ..., vertex3Index: int | None = ...) -> None: ...
        @typing.overload
        def __init__(self, other: PySide6.Qt3DRender.Qt3DRender.QRayCasterHit, /, *, type: PySide6.Qt3DRender.Qt3DRender.QRayCasterHit.HitType | None = ..., entityId: PySide6.Qt3DCore.Qt3DCore.QNodeId | None = ..., entity: PySide6.Qt3DCore.Qt3DCore.QEntity | None = ..., distance: float | None = ..., localIntersection: PySide6.QtGui.QVector3D | None = ..., worldIntersection: PySide6.QtGui.QVector3D | None = ..., primitiveIndex: int | None = ..., vertex1Index: int | None = ..., vertex2Index: int | None = ..., vertex3Index: int | None = ...) -> None: ...
        @typing.overload
        def __init__(self, /, *, type: PySide6.Qt3DRender.Qt3DRender.QRayCasterHit.HitType | None = ..., entityId: PySide6.Qt3DCore.Qt3DCore.QNodeId | None = ..., entity: PySide6.Qt3DCore.Qt3DCore.QEntity | None = ..., distance: float | None = ..., localIntersection: PySide6.QtGui.QVector3D | None = ..., worldIntersection: PySide6.QtGui.QVector3D | None = ..., primitiveIndex: int | None = ..., vertex1Index: int | None = ..., vertex2Index: int | None = ..., vertex3Index: int | None = ...) -> None: ...

        def __copy__(self, /) -> PySide6.Qt3DRender.Qt3DRender.QRayCasterHit: ...
        def distance(self, /) -> float: ...
        def entity(self, /) -> PySide6.Qt3DCore.Qt3DCore.QEntity: ...
        def entityId(self, /) -> PySide6.Qt3DCore.Qt3DCore.QNodeId: ...
        def localIntersection(self, /) -> PySide6.QtGui.QVector3D: ...
        def primitiveIndex(self, /) -> int: ...
        def toString(self, /) -> str: ...
        def type(self, /) -> PySide6.Qt3DRender.Qt3DRender.QRayCasterHit.HitType: ...
        def vertex1Index(self, /) -> int: ...
        def vertex2Index(self, /) -> int: ...
        def vertex3Index(self, /) -> int: ...
        def worldIntersection(self, /) -> PySide6.QtGui.QVector3D: ...

    class QRenderAspect(PySide6.Qt3DCore.Qt3DCore.QAbstractAspect):
        class SubmissionType(enum.Enum):
            Automatic                 = 0x0
            Manual                    = 0x1

        @typing.overload
        def __init__(self, submissionType: PySide6.Qt3DRender.Qt3DRender.QRenderAspect.SubmissionType, /, parent: PySide6.QtCore.QObject | None = ...) -> None: ...
        @typing.overload
        def __init__(self, /, parent: PySide6.QtCore.QObject | None = ...) -> None: ...

        def dependencies(self, /) -> typing.List[str]: ...

    class QRenderCapabilities(PySide6.QtCore.QObject):
        class API(enum.Enum):
            OpenGL                    = 0x1
            OpenGLES                  = 0x2
            Vulkan                    = 0x3
            DirectX                   = 0x4
            RHI                       = 0x5

        class Profile(enum.Enum):
            NoProfile                 = 0x0
            CoreProfile               = 0x1
            CompatibilityProfile      = 0x2

        def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., *, valid: bool | None = ..., api: PySide6.Qt3DRender.Qt3DRender.QRenderCapabilities.API | None = ..., profile: PySide6.Qt3DRender.Qt3DRender.QRenderCapabilities.Profile | None = ..., majorVersion: int | None = ..., minorVersion: int | None = ..., extensions: collections.abc.Sequence[str] | None = ..., vendor: str | None = ..., renderer: str | None = ..., driverVersion: str | None = ..., glslVersion: str | None = ..., maxSamples: int | None = ..., maxTextureSize: int | None = ..., maxTextureUnits: int | None = ..., maxTextureLayers: int | None = ..., supportsUBO: bool | None = ..., maxUBOSize: int | None = ..., maxUBOBindings: int | None = ..., supportsSSBO: bool | None = ..., maxSSBOSize: int | None = ..., maxSSBOBindings: int | None = ..., supportsImageStore: bool | None = ..., maxImageUnits: int | None = ..., supportsCompute: bool | None = ..., maxWorkGroupCountX: int | None = ..., maxWorkGroupCountY: int | None = ..., maxWorkGroupCountZ: int | None = ..., maxWorkGroupSizeX: int | None = ..., maxWorkGroupSizeY: int | None = ..., maxWorkGroupSizeZ: int | None = ..., maxComputeInvocations: int | None = ..., maxComputeSharedMemorySize: int | None = ...) -> None: ...

        def api(self, /) -> PySide6.Qt3DRender.Qt3DRender.QRenderCapabilities.API: ...
        def driverVersion(self, /) -> str: ...
        def extensions(self, /) -> typing.List[str]: ...
        def glslVersion(self, /) -> str: ...
        def isValid(self, /) -> bool: ...
        def majorVersion(self, /) -> int: ...
        def maxComputeInvocations(self, /) -> int: ...
        def maxComputeSharedMemorySize(self, /) -> int: ...
        def maxImageUnits(self, /) -> int: ...
        def maxSSBOBindings(self, /) -> int: ...
        def maxSSBOSize(self, /) -> int: ...
        def maxSamples(self, /) -> int: ...
        def maxTextureLayers(self, /) -> int: ...
        def maxTextureSize(self, /) -> int: ...
        def maxTextureUnits(self, /) -> int: ...
        def maxUBOBindings(self, /) -> int: ...
        def maxUBOSize(self, /) -> int: ...
        def maxWorkGroupCountX(self, /) -> int: ...
        def maxWorkGroupCountY(self, /) -> int: ...
        def maxWorkGroupCountZ(self, /) -> int: ...
        def maxWorkGroupSizeX(self, /) -> int: ...
        def maxWorkGroupSizeY(self, /) -> int: ...
        def maxWorkGroupSizeZ(self, /) -> int: ...
        def minorVersion(self, /) -> int: ...
        def profile(self, /) -> PySide6.Qt3DRender.Qt3DRender.QRenderCapabilities.Profile: ...
        def renderer(self, /) -> str: ...
        def supportsCompute(self, /) -> bool: ...
        def supportsImageStore(self, /) -> bool: ...
        def supportsSSBO(self, /) -> bool: ...
        def supportsUBO(self, /) -> bool: ...
        def vendor(self, /) -> str: ...

    class QRenderCapture(PySide6.Qt3DRender.Qt3DRender.QFrameGraphNode):
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...) -> None: ...

        @typing.overload
        def requestCapture(self, /) -> PySide6.Qt3DRender.Qt3DRender.QRenderCaptureReply: ...
        @typing.overload
        def requestCapture(self, rect: PySide6.QtCore.QRect, /) -> PySide6.Qt3DRender.Qt3DRender.QRenderCaptureReply: ...
        @typing.overload
        def requestCapture(self, captureId: int, /) -> PySide6.Qt3DRender.Qt3DRender.QRenderCaptureReply: ...

    class QRenderCaptureReply(PySide6.QtCore.QObject):
        # completed()
        completed: typing.ClassVar[Signal[
            [], [], [], [], [], [], [], [],
            [], [], [], [], [], [], [], []
        ]]

        def captureId(self, /) -> int: ...
        def image(self, /) -> PySide6.QtGui.QImage: ...
        def isComplete(self, /) -> bool: ...
        def saveImage(self, fileName: str, /) -> bool: ...

    class QRenderPass(PySide6.Qt3DCore.Qt3DCore.QNode):
        # shaderProgramChanged(QShaderProgram*)
        shaderProgramChanged: typing.ClassVar[Signal[
            [PySide6.Qt3DRender.Qt3DRender.QShaderProgram], [], [], [], [], [], [], [],
            [PySide6.Qt3DRender.Qt3DRender.QShaderProgram], [PySide6.Qt3DRender.Qt3DRender.QShaderProgram], [PySide6.Qt3DRender.Qt3DRender.QShaderProgram], [PySide6.Qt3DRender.Qt3DRender.QShaderProgram], [PySide6.Qt3DRender.Qt3DRender.QShaderProgram], [PySide6.Qt3DRender.Qt3DRender.QShaderProgram], [PySide6.Qt3DRender.Qt3DRender.QShaderProgram], [PySide6.Qt3DRender.Qt3DRender.QShaderProgram]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, shaderProgram: PySide6.Qt3DRender.Qt3DRender.QShaderProgram | None = ...) -> None: ...

        def addFilterKey(self, filterKey: PySide6.Qt3DRender.Qt3DRender.QFilterKey, /) -> None: ...
        def addParameter(self, p: PySide6.Qt3DRender.Qt3DRender.QParameter, /) -> None: ...
        def addRenderState(self, state: PySide6.Qt3DRender.Qt3DRender.QRenderState, /) -> None: ...
        def filterKeys(self, /) -> typing.List[PySide6.Qt3DRender.Qt3DRender.QFilterKey]: ...
        def parameters(self, /) -> typing.List[PySide6.Qt3DRender.Qt3DRender.QParameter]: ...
        def removeFilterKey(self, filterKey: PySide6.Qt3DRender.Qt3DRender.QFilterKey, /) -> None: ...
        def removeParameter(self, p: PySide6.Qt3DRender.Qt3DRender.QParameter, /) -> None: ...
        def removeRenderState(self, state: PySide6.Qt3DRender.Qt3DRender.QRenderState, /) -> None: ...
        def renderStates(self, /) -> typing.List[PySide6.Qt3DRender.Qt3DRender.QRenderState]: ...
        def setShaderProgram(self, shaderProgram: PySide6.Qt3DRender.Qt3DRender.QShaderProgram, /) -> None: ...
        def shaderProgram(self, /) -> PySide6.Qt3DRender.Qt3DRender.QShaderProgram: ...

    class QRenderPassFilter(PySide6.Qt3DRender.Qt3DRender.QFrameGraphNode):
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...) -> None: ...

        def addMatch(self, filterKey: PySide6.Qt3DRender.Qt3DRender.QFilterKey, /) -> None: ...
        def addParameter(self, parameter: PySide6.Qt3DRender.Qt3DRender.QParameter, /) -> None: ...
        def matchAny(self, /) -> typing.List[PySide6.Qt3DRender.Qt3DRender.QFilterKey]: ...
        def parameters(self, /) -> typing.List[PySide6.Qt3DRender.Qt3DRender.QParameter]: ...
        def removeMatch(self, filterKey: PySide6.Qt3DRender.Qt3DRender.QFilterKey, /) -> None: ...
        def removeParameter(self, parameter: PySide6.Qt3DRender.Qt3DRender.QParameter, /) -> None: ...

    class QRenderSettings(PySide6.Qt3DCore.Qt3DCore.QComponent):
        # activeFrameGraphChanged(QFrameGraphNode*)
        activeFrameGraphChanged: typing.ClassVar[Signal[
            [PySide6.Qt3DRender.Qt3DRender.QFrameGraphNode], [], [], [], [], [], [], [],
            [PySide6.Qt3DRender.Qt3DRender.QFrameGraphNode], [PySide6.Qt3DRender.Qt3DRender.QFrameGraphNode], [PySide6.Qt3DRender.Qt3DRender.QFrameGraphNode], [PySide6.Qt3DRender.Qt3DRender.QFrameGraphNode], [PySide6.Qt3DRender.Qt3DRender.QFrameGraphNode], [PySide6.Qt3DRender.Qt3DRender.QFrameGraphNode], [PySide6.Qt3DRender.Qt3DRender.QFrameGraphNode], [PySide6.Qt3DRender.Qt3DRender.QFrameGraphNode]
        ]]
        # renderPolicyChanged(RenderPolicy)
        renderPolicyChanged: typing.ClassVar[Signal[
            [RenderPolicy], [], [], [], [], [], [], [],
            [RenderPolicy], [RenderPolicy], [RenderPolicy], [RenderPolicy], [RenderPolicy], [RenderPolicy], [RenderPolicy], [RenderPolicy]
        ]]

        class RenderPolicy(enum.Enum):
            OnDemand                  = 0x0
            Always                    = 0x1

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, renderCapabilities: PySide6.Qt3DRender.Qt3DRender.QRenderCapabilities | None = ..., pickingSettings: PySide6.Qt3DRender.Qt3DRender.QPickingSettings | None = ..., renderPolicy: PySide6.Qt3DRender.Qt3DRender.QRenderSettings.RenderPolicy | None = ..., activeFrameGraph: PySide6.Qt3DRender.Qt3DRender.QFrameGraphNode | None = ...) -> None: ...

        def activeFrameGraph(self, /) -> PySide6.Qt3DRender.Qt3DRender.QFrameGraphNode: ...
        def pickingSettings(self, /) -> PySide6.Qt3DRender.Qt3DRender.QPickingSettings: ...
        def renderCapabilities(self, /) -> PySide6.Qt3DRender.Qt3DRender.QRenderCapabilities: ...
        def renderPolicy(self, /) -> PySide6.Qt3DRender.Qt3DRender.QRenderSettings.RenderPolicy: ...
        def setActiveFrameGraph(self, activeFrameGraph: PySide6.Qt3DRender.Qt3DRender.QFrameGraphNode, /) -> None: ...
        def setRenderPolicy(self, renderPolicy: PySide6.Qt3DRender.Qt3DRender.QRenderSettings.RenderPolicy, /) -> None: ...

    class QRenderState(PySide6.Qt3DCore.Qt3DCore.QNode):
        ...

    class QRenderStateSet(PySide6.Qt3DRender.Qt3DRender.QFrameGraphNode):
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...) -> None: ...

        def addRenderState(self, state: PySide6.Qt3DRender.Qt3DRender.QRenderState, /) -> None: ...
        def removeRenderState(self, state: PySide6.Qt3DRender.Qt3DRender.QRenderState, /) -> None: ...
        def renderStates(self, /) -> typing.List[PySide6.Qt3DRender.Qt3DRender.QRenderState]: ...

    class QRenderSurfaceSelector(PySide6.Qt3DRender.Qt3DRender.QFrameGraphNode):
        # externalRenderTargetSizeChanged(QSize)
        externalRenderTargetSizeChanged: typing.ClassVar[Signal[
            [PySide6.QtCore.QSize], [], [], [], [], [], [], [],
            [PySide6.QtCore.QSize], [PySide6.QtCore.QSize], [PySide6.QtCore.QSize], [PySide6.QtCore.QSize], [PySide6.QtCore.QSize], [PySide6.QtCore.QSize], [PySide6.QtCore.QSize], [PySide6.QtCore.QSize]
        ]]
        # surfaceChanged(QObject*)
        surfaceChanged: typing.ClassVar[Signal[
            [PySide6.QtCore.QObject], [], [], [], [], [], [], [],
            [PySide6.QtCore.QObject], [PySide6.QtCore.QObject], [PySide6.QtCore.QObject], [PySide6.QtCore.QObject], [PySide6.QtCore.QObject], [PySide6.QtCore.QObject], [PySide6.QtCore.QObject], [PySide6.QtCore.QObject]
        ]]
        # surfacePixelRatioChanged(float)
        surfacePixelRatioChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, surface: PySide6.QtCore.QObject | None = ..., externalRenderTargetSize: PySide6.QtCore.QSize | None = ..., surfacePixelRatio: float | None = ...) -> None: ...

        def externalRenderTargetSize(self, /) -> PySide6.QtCore.QSize: ...
        def setExternalRenderTargetSize(self, size: PySide6.QtCore.QSize, /) -> None: ...
        def setSurface(self, surfaceObject: PySide6.QtCore.QObject, /) -> None: ...
        def setSurfacePixelRatio(self, ratio: float, /) -> None: ...
        def surface(self, /) -> PySide6.QtCore.QObject: ...
        def surfacePixelRatio(self, /) -> float: ...

    class QRenderTarget(PySide6.Qt3DCore.Qt3DCore.QComponent):
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...) -> None: ...

        def addOutput(self, output: PySide6.Qt3DRender.Qt3DRender.QRenderTargetOutput, /) -> None: ...
        def outputs(self, /) -> typing.List[PySide6.Qt3DRender.Qt3DRender.QRenderTargetOutput]: ...
        def removeOutput(self, output: PySide6.Qt3DRender.Qt3DRender.QRenderTargetOutput, /) -> None: ...

    class QRenderTargetOutput(PySide6.Qt3DCore.Qt3DCore.QNode):
        # attachmentPointChanged(AttachmentPoint)
        attachmentPointChanged: typing.ClassVar[Signal[
            [AttachmentPoint], [], [], [], [], [], [], [],
            [AttachmentPoint], [AttachmentPoint], [AttachmentPoint], [AttachmentPoint], [AttachmentPoint], [AttachmentPoint], [AttachmentPoint], [AttachmentPoint]
        ]]
        # faceChanged(QAbstractTexture::CubeMapFace)
        faceChanged: typing.ClassVar[Signal[
            [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.CubeMapFace], [], [], [], [], [], [], [],
            [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.CubeMapFace], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.CubeMapFace], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.CubeMapFace], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.CubeMapFace], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.CubeMapFace], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.CubeMapFace], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.CubeMapFace], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.CubeMapFace]
        ]]
        # layerChanged(int)
        layerChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]
        # mipLevelChanged(int)
        mipLevelChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]
        # textureChanged(QAbstractTexture*)
        textureChanged: typing.ClassVar[Signal[
            [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture], [], [], [], [], [], [], [],
            [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture]
        ]]

        class AttachmentPoint(enum.Enum):
            Color0                    = 0x0
            Color1                    = 0x1
            Color2                    = 0x2
            Color3                    = 0x3
            Color4                    = 0x4
            Color5                    = 0x5
            Color6                    = 0x6
            Color7                    = 0x7
            Color8                    = 0x8
            Color9                    = 0x9
            Color10                   = 0xa
            Color11                   = 0xb
            Color12                   = 0xc
            Color13                   = 0xd
            Color14                   = 0xe
            Color15                   = 0xf
            Depth                     = 0x10
            Stencil                   = 0x11
            DepthStencil              = 0x12
            Left                      = 0x13
            Right                     = 0x14

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, attachmentPoint: PySide6.Qt3DRender.Qt3DRender.QRenderTargetOutput.AttachmentPoint | None = ..., texture: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture | None = ..., mipLevel: int | None = ..., layer: int | None = ..., face: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.CubeMapFace | None = ...) -> None: ...

        def attachmentPoint(self, /) -> PySide6.Qt3DRender.Qt3DRender.QRenderTargetOutput.AttachmentPoint: ...
        def face(self, /) -> PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.CubeMapFace: ...
        def layer(self, /) -> int: ...
        def mipLevel(self, /) -> int: ...
        def setAttachmentPoint(self, attachmentPoint: PySide6.Qt3DRender.Qt3DRender.QRenderTargetOutput.AttachmentPoint, /) -> None: ...
        def setFace(self, face: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.CubeMapFace, /) -> None: ...
        def setLayer(self, layer: int, /) -> None: ...
        def setMipLevel(self, level: int, /) -> None: ...
        def setTexture(self, texture: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture, /) -> None: ...
        def texture(self, /) -> PySide6.Qt3DRender.Qt3DRender.QAbstractTexture: ...

    class QRenderTargetSelector(PySide6.Qt3DRender.Qt3DRender.QFrameGraphNode):
        # targetChanged(QRenderTarget*)
        targetChanged: typing.ClassVar[Signal[
            [PySide6.Qt3DRender.Qt3DRender.QRenderTarget], [], [], [], [], [], [], [],
            [PySide6.Qt3DRender.Qt3DRender.QRenderTarget], [PySide6.Qt3DRender.Qt3DRender.QRenderTarget], [PySide6.Qt3DRender.Qt3DRender.QRenderTarget], [PySide6.Qt3DRender.Qt3DRender.QRenderTarget], [PySide6.Qt3DRender.Qt3DRender.QRenderTarget], [PySide6.Qt3DRender.Qt3DRender.QRenderTarget], [PySide6.Qt3DRender.Qt3DRender.QRenderTarget], [PySide6.Qt3DRender.Qt3DRender.QRenderTarget]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, target: PySide6.Qt3DRender.Qt3DRender.QRenderTarget | None = ...) -> None: ...

        def setTarget(self, target: PySide6.Qt3DRender.Qt3DRender.QRenderTarget, /) -> None: ...
        def target(self, /) -> PySide6.Qt3DRender.Qt3DRender.QRenderTarget: ...

    class QSceneLoader(PySide6.Qt3DCore.Qt3DCore.QComponent):
        # sourceChanged(QUrl)
        sourceChanged: typing.ClassVar[Signal[
            [PySide6.QtCore.QUrl], [], [], [], [], [], [], [],
            [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl]
        ]]
        # statusChanged(Status)
        statusChanged: typing.ClassVar[Signal[
            [Status], [], [], [], [], [], [], [],
            [Status], [Status], [Status], [Status], [Status], [Status], [Status], [Status]
        ]]

        class ComponentType(enum.Enum):
            UnknownComponent          = 0x0
            GeometryRendererComponent = 0x1
            TransformComponent        = 0x2
            MaterialComponent         = 0x3
            LightComponent            = 0x4
            CameraLensComponent       = 0x5

        class Status(enum.Enum):
            None_                     = 0x0
            Loading                   = 0x1
            Ready                     = 0x2
            Error                     = 0x3

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, source: PySide6.QtCore.QUrl | None = ..., status: PySide6.Qt3DRender.Qt3DRender.QSceneLoader.Status | None = ...) -> None: ...

        def component(self, entityName: str, componentType: PySide6.Qt3DRender.Qt3DRender.QSceneLoader.ComponentType, /) -> PySide6.Qt3DCore.Qt3DCore.QComponent: ...
        def entity(self, entityName: str, /) -> PySide6.Qt3DCore.Qt3DCore.QEntity: ...
        def entityNames(self, /) -> typing.List[str]: ...
        def setSource(self, arg: PySide6.QtCore.QUrl | str, /) -> None: ...
        def source(self, /) -> PySide6.QtCore.QUrl: ...
        def status(self, /) -> PySide6.Qt3DRender.Qt3DRender.QSceneLoader.Status: ...

    class QScissorTest(PySide6.Qt3DRender.Qt3DRender.QRenderState):
        # bottomChanged(int)
        bottomChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]
        # heightChanged(int)
        heightChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]
        # leftChanged(int)
        leftChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]
        # widthChanged(int)
        widthChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, left: int | None = ..., bottom: int | None = ..., width: int | None = ..., height: int | None = ...) -> None: ...

        def bottom(self, /) -> int: ...
        def height(self, /) -> int: ...
        def left(self, /) -> int: ...
        def setBottom(self, bottom: int, /) -> None: ...
        def setHeight(self, height: int, /) -> None: ...
        def setLeft(self, left: int, /) -> None: ...
        def setWidth(self, width: int, /) -> None: ...
        def width(self, /) -> int: ...

    class QScreenRayCaster(PySide6.Qt3DRender.Qt3DRender.QAbstractRayCaster):
        # positionChanged(QPoint)
        positionChanged: typing.ClassVar[Signal[
            [PySide6.QtCore.QPoint], [], [], [], [], [], [], [],
            [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, position: PySide6.QtCore.QPoint | None = ...) -> None: ...

        def pick(self, position: PySide6.QtCore.QPoint, /) -> typing.List[PySide6.Qt3DRender.Qt3DRender.QRayCasterHit]: ...
        def position(self, /) -> PySide6.QtCore.QPoint: ...
        def setPosition(self, position: PySide6.QtCore.QPoint, /) -> None: ...
        @typing.overload
        def trigger(self, /) -> None: ...
        @typing.overload
        def trigger(self, position: PySide6.QtCore.QPoint, /) -> None: ...

    class QSeamlessCubemap(PySide6.Qt3DRender.Qt3DRender.QRenderState):
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...) -> None: ...

    class QSetFence(PySide6.Qt3DRender.Qt3DRender.QFrameGraphNode):
        # handleChanged(QVariant)
        handleChanged: typing.ClassVar[Signal[
            [typing.Any], [], [], [], [], [], [], [],
            [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any]
        ]]
        # handleTypeChanged(HandleType)
        handleTypeChanged: typing.ClassVar[Signal[
            [HandleType], [], [], [], [], [], [], [],
            [HandleType], [HandleType], [HandleType], [HandleType], [HandleType], [HandleType], [HandleType], [HandleType]
        ]]

        class HandleType(enum.Enum):
            NoHandle                  = 0x0
            OpenGLFenceId             = 0x1

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, handleType: PySide6.Qt3DRender.Qt3DRender.QSetFence.HandleType | None = ..., handle: typing.Any | None = ...) -> None: ...

        def handle(self, /) -> typing.Any: ...
        def handleType(self, /) -> PySide6.Qt3DRender.Qt3DRender.QSetFence.HandleType: ...

    class QShaderData(PySide6.Qt3DCore.Qt3DCore.QComponent):
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...) -> None: ...

        def event(self, event: PySide6.QtCore.QEvent, /) -> bool: ...
        def propertyReader(self, /) -> PySide6.Qt3DRender.Qt3DRender.PropertyReaderInterfacePtr: ...

    class QShaderImage(PySide6.Qt3DCore.Qt3DCore.QNode):
        # accessChanged(Access)
        accessChanged: typing.ClassVar[Signal[
            [Access], [], [], [], [], [], [], [],
            [Access], [Access], [Access], [Access], [Access], [Access], [Access], [Access]
        ]]
        # formatChanged(ImageFormat)
        formatChanged: typing.ClassVar[Signal[
            [ImageFormat], [], [], [], [], [], [], [],
            [ImageFormat], [ImageFormat], [ImageFormat], [ImageFormat], [ImageFormat], [ImageFormat], [ImageFormat], [ImageFormat]
        ]]
        # layerChanged(int)
        layerChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]
        # layeredChanged(bool)
        layeredChanged: typing.ClassVar[Signal[
            [bool], [], [], [], [], [], [], [],
            [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
        ]]
        # mipLevelChanged(int)
        mipLevelChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]
        # textureChanged(Qt3DRender::QAbstractTexture*)
        textureChanged: typing.ClassVar[Signal[
            [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture], [], [], [], [], [], [], [],
            [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture], [PySide6.Qt3DRender.Qt3DRender.QAbstractTexture]
        ]]

        class Access(enum.Enum):
            ReadOnly                  = 0x0
            WriteOnly                 = 0x1
            ReadWrite                 = 0x2

        class ImageFormat(enum.Enum):
            NoFormat                  = 0x0
            Automatic                 = 0x1
            RGBA8_UNorm               = 0x8058
            RGB10A2                   = 0x8059
            RGBA16_UNorm              = 0x805b
            R8_UNorm                  = 0x8229
            R16_UNorm                 = 0x822a
            RG8_UNorm                 = 0x822b
            RG16_UNorm                = 0x822c
            R16F                      = 0x822d
            R32F                      = 0x822e
            RG16F                     = 0x822f
            RG32F                     = 0x8230
            R8I                       = 0x8231
            R8U                       = 0x8232
            R16I                      = 0x8233
            R16U                      = 0x8234
            R32I                      = 0x8235
            R32U                      = 0x8236
            RG8I                      = 0x8237
            RG8U                      = 0x8238
            RG16I                     = 0x8239
            RG16U                     = 0x823a
            RG32I                     = 0x823b
            RG32U                     = 0x823c
            RGBA32F                   = 0x8814
            RGBA16F                   = 0x881a
            RG11B10F                  = 0x8c3a
            RGBA32U                   = 0x8d70
            RGBA16U                   = 0x8d76
            RGBA8U                    = 0x8d7c
            RGBA32I                   = 0x8d82
            RGBA16I                   = 0x8d88
            RGBA8I                    = 0x8d8e
            R8_SNorm                  = 0x8f94
            RG8_SNorm                 = 0x8f95
            RGBA8_SNorm               = 0x8f97
            R16_SNorm                 = 0x8f98
            RG16_SNorm                = 0x8f99
            RGBA16_SNorm              = 0x8f9b
            RGB10A2U                  = 0x906f

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, texture: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture | None = ..., layered: bool | None = ..., mipLevel: int | None = ..., layer: int | None = ..., access: PySide6.Qt3DRender.Qt3DRender.QShaderImage.Access | None = ..., format: PySide6.Qt3DRender.Qt3DRender.QShaderImage.ImageFormat | None = ...) -> None: ...

        def access(self, /) -> PySide6.Qt3DRender.Qt3DRender.QShaderImage.Access: ...
        def format(self, /) -> PySide6.Qt3DRender.Qt3DRender.QShaderImage.ImageFormat: ...
        def layer(self, /) -> int: ...
        def layered(self, /) -> bool: ...
        def mipLevel(self, /) -> int: ...
        def setAccess(self, access: PySide6.Qt3DRender.Qt3DRender.QShaderImage.Access, /) -> None: ...
        def setFormat(self, format: PySide6.Qt3DRender.Qt3DRender.QShaderImage.ImageFormat, /) -> None: ...
        def setLayer(self, layer: int, /) -> None: ...
        def setLayered(self, layered: bool, /) -> None: ...
        def setMipLevel(self, mipLevel: int, /) -> None: ...
        def setTexture(self, texture: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture, /) -> None: ...
        def texture(self, /) -> PySide6.Qt3DRender.Qt3DRender.QAbstractTexture: ...

    class QShaderProgram(PySide6.Qt3DCore.Qt3DCore.QNode):
        # computeShaderCodeChanged(QByteArray)
        computeShaderCodeChanged: typing.ClassVar[Signal[
            [PySide6.QtCore.QByteArray], [], [], [], [], [], [], [],
            [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray]
        ]]
        # formatChanged(Format)
        formatChanged: typing.ClassVar[Signal[
            [Format], [], [], [], [], [], [], [],
            [Format], [Format], [Format], [Format], [Format], [Format], [Format], [Format]
        ]]
        # fragmentShaderCodeChanged(QByteArray)
        fragmentShaderCodeChanged: typing.ClassVar[Signal[
            [PySide6.QtCore.QByteArray], [], [], [], [], [], [], [],
            [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray]
        ]]
        # geometryShaderCodeChanged(QByteArray)
        geometryShaderCodeChanged: typing.ClassVar[Signal[
            [PySide6.QtCore.QByteArray], [], [], [], [], [], [], [],
            [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray]
        ]]
        # logChanged(QString)
        logChanged: typing.ClassVar[Signal[
            [str], [], [], [], [], [], [], [],
            [str], [str], [str], [str], [str], [str], [str], [str]
        ]]
        # statusChanged(Status)
        statusChanged: typing.ClassVar[Signal[
            [Status], [], [], [], [], [], [], [],
            [Status], [Status], [Status], [Status], [Status], [Status], [Status], [Status]
        ]]
        # tessellationControlShaderCodeChanged(QByteArray)
        tessellationControlShaderCodeChanged: typing.ClassVar[Signal[
            [PySide6.QtCore.QByteArray], [], [], [], [], [], [], [],
            [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray]
        ]]
        # tessellationEvaluationShaderCodeChanged(QByteArray)
        tessellationEvaluationShaderCodeChanged: typing.ClassVar[Signal[
            [PySide6.QtCore.QByteArray], [], [], [], [], [], [], [],
            [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray]
        ]]
        # vertexShaderCodeChanged(QByteArray)
        vertexShaderCodeChanged: typing.ClassVar[Signal[
            [PySide6.QtCore.QByteArray], [], [], [], [], [], [], [],
            [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray]
        ]]

        class Format(enum.Enum):
            GLSL                      = 0x0
            SPIRV                     = 0x1

        class ShaderType(enum.Enum):
            Vertex                    = 0x0
            Fragment                  = 0x1
            TessellationControl       = 0x2
            TessellationEvaluation    = 0x3
            Geometry                  = 0x4
            Compute                   = 0x5

        class Status(enum.Enum):
            NotReady                  = 0x0
            Ready                     = 0x1
            Error                     = 0x2

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, vertexShaderCode: PySide6.QtCore.QByteArray | bytes | bytearray | memoryview | None = ..., tessellationControlShaderCode: PySide6.QtCore.QByteArray | bytes | bytearray | memoryview | None = ..., tessellationEvaluationShaderCode: PySide6.QtCore.QByteArray | bytes | bytearray | memoryview | None = ..., geometryShaderCode: PySide6.QtCore.QByteArray | bytes | bytearray | memoryview | None = ..., fragmentShaderCode: PySide6.QtCore.QByteArray | bytes | bytearray | memoryview | None = ..., computeShaderCode: PySide6.QtCore.QByteArray | bytes | bytearray | memoryview | None = ..., log: str | None = ..., status: PySide6.Qt3DRender.Qt3DRender.QShaderProgram.Status | None = ..., format: PySide6.Qt3DRender.Qt3DRender.QShaderProgram.Format | None = ...) -> None: ...

        def computeShaderCode(self, /) -> PySide6.QtCore.QByteArray: ...
        def format(self, /) -> PySide6.Qt3DRender.Qt3DRender.QShaderProgram.Format: ...
        def fragmentShaderCode(self, /) -> PySide6.QtCore.QByteArray: ...
        def geometryShaderCode(self, /) -> PySide6.QtCore.QByteArray: ...
        @staticmethod
        def loadSource(sourceUrl: PySide6.QtCore.QUrl | str, /) -> PySide6.QtCore.QByteArray: ...
        def log(self, /) -> str: ...
        def setComputeShaderCode(self, computeShaderCode: PySide6.QtCore.QByteArray | bytes | bytearray | str, /) -> None: ...
        def setFormat(self, format: PySide6.Qt3DRender.Qt3DRender.QShaderProgram.Format, /) -> None: ...
        def setFragmentShaderCode(self, fragmentShaderCode: PySide6.QtCore.QByteArray | bytes | bytearray | str, /) -> None: ...
        def setGeometryShaderCode(self, geometryShaderCode: PySide6.QtCore.QByteArray | bytes | bytearray | str, /) -> None: ...
        def setShaderCode(self, type: PySide6.Qt3DRender.Qt3DRender.QShaderProgram.ShaderType, shaderCode: PySide6.QtCore.QByteArray | bytes | bytearray | str, /) -> None: ...
        def setTessellationControlShaderCode(self, tessellationControlShaderCode: PySide6.QtCore.QByteArray | bytes | bytearray | str, /) -> None: ...
        def setTessellationEvaluationShaderCode(self, tessellationEvaluationShaderCode: PySide6.QtCore.QByteArray | bytes | bytearray | str, /) -> None: ...
        def setVertexShaderCode(self, vertexShaderCode: PySide6.QtCore.QByteArray | bytes | bytearray | str, /) -> None: ...
        def shaderCode(self, type: PySide6.Qt3DRender.Qt3DRender.QShaderProgram.ShaderType, /) -> PySide6.QtCore.QByteArray: ...
        def status(self, /) -> PySide6.Qt3DRender.Qt3DRender.QShaderProgram.Status: ...
        def tessellationControlShaderCode(self, /) -> PySide6.QtCore.QByteArray: ...
        def tessellationEvaluationShaderCode(self, /) -> PySide6.QtCore.QByteArray: ...
        def vertexShaderCode(self, /) -> PySide6.QtCore.QByteArray: ...

    class QShaderProgramBuilder(PySide6.Qt3DCore.Qt3DCore.QNode):
        # computeShaderCodeChanged(QByteArray)
        computeShaderCodeChanged: typing.ClassVar[Signal[
            [PySide6.QtCore.QByteArray], [], [], [], [], [], [], [],
            [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray]
        ]]
        # computeShaderGraphChanged(QUrl)
        computeShaderGraphChanged: typing.ClassVar[Signal[
            [PySide6.QtCore.QUrl], [], [], [], [], [], [], [],
            [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl]
        ]]
        # enabledLayersChanged(QStringList)
        enabledLayersChanged: typing.ClassVar[Signal[
            [typing.List[str]], [], [], [], [], [], [], [],
            [typing.List[str]], [typing.List[str]], [typing.List[str]], [typing.List[str]], [typing.List[str]], [typing.List[str]], [typing.List[str]], [typing.List[str]]
        ]]
        # fragmentShaderCodeChanged(QByteArray)
        fragmentShaderCodeChanged: typing.ClassVar[Signal[
            [PySide6.QtCore.QByteArray], [], [], [], [], [], [], [],
            [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray]
        ]]
        # fragmentShaderGraphChanged(QUrl)
        fragmentShaderGraphChanged: typing.ClassVar[Signal[
            [PySide6.QtCore.QUrl], [], [], [], [], [], [], [],
            [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl]
        ]]
        # geometryShaderCodeChanged(QByteArray)
        geometryShaderCodeChanged: typing.ClassVar[Signal[
            [PySide6.QtCore.QByteArray], [], [], [], [], [], [], [],
            [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray]
        ]]
        # geometryShaderGraphChanged(QUrl)
        geometryShaderGraphChanged: typing.ClassVar[Signal[
            [PySide6.QtCore.QUrl], [], [], [], [], [], [], [],
            [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl]
        ]]
        # shaderProgramChanged(Qt3DRender::QShaderProgram*)
        shaderProgramChanged: typing.ClassVar[Signal[
            [PySide6.Qt3DRender.Qt3DRender.QShaderProgram], [], [], [], [], [], [], [],
            [PySide6.Qt3DRender.Qt3DRender.QShaderProgram], [PySide6.Qt3DRender.Qt3DRender.QShaderProgram], [PySide6.Qt3DRender.Qt3DRender.QShaderProgram], [PySide6.Qt3DRender.Qt3DRender.QShaderProgram], [PySide6.Qt3DRender.Qt3DRender.QShaderProgram], [PySide6.Qt3DRender.Qt3DRender.QShaderProgram], [PySide6.Qt3DRender.Qt3DRender.QShaderProgram], [PySide6.Qt3DRender.Qt3DRender.QShaderProgram]
        ]]
        # tessellationControlShaderCodeChanged(QByteArray)
        tessellationControlShaderCodeChanged: typing.ClassVar[Signal[
            [PySide6.QtCore.QByteArray], [], [], [], [], [], [], [],
            [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray]
        ]]
        # tessellationControlShaderGraphChanged(QUrl)
        tessellationControlShaderGraphChanged: typing.ClassVar[Signal[
            [PySide6.QtCore.QUrl], [], [], [], [], [], [], [],
            [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl]
        ]]
        # tessellationEvaluationShaderCodeChanged(QByteArray)
        tessellationEvaluationShaderCodeChanged: typing.ClassVar[Signal[
            [PySide6.QtCore.QByteArray], [], [], [], [], [], [], [],
            [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray]
        ]]
        # tessellationEvaluationShaderGraphChanged(QUrl)
        tessellationEvaluationShaderGraphChanged: typing.ClassVar[Signal[
            [PySide6.QtCore.QUrl], [], [], [], [], [], [], [],
            [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl]
        ]]
        # vertexShaderCodeChanged(QByteArray)
        vertexShaderCodeChanged: typing.ClassVar[Signal[
            [PySide6.QtCore.QByteArray], [], [], [], [], [], [], [],
            [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray]
        ]]
        # vertexShaderGraphChanged(QUrl)
        vertexShaderGraphChanged: typing.ClassVar[Signal[
            [PySide6.QtCore.QUrl], [], [], [], [], [], [], [],
            [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, shaderProgram: PySide6.Qt3DRender.Qt3DRender.QShaderProgram | None = ..., enabledLayers: collections.abc.Sequence[str] | None = ..., vertexShaderGraph: PySide6.QtCore.QUrl | None = ..., tessellationControlShaderGraph: PySide6.QtCore.QUrl | None = ..., tessellationEvaluationShaderGraph: PySide6.QtCore.QUrl | None = ..., geometryShaderGraph: PySide6.QtCore.QUrl | None = ..., fragmentShaderGraph: PySide6.QtCore.QUrl | None = ..., computeShaderGraph: PySide6.QtCore.QUrl | None = ..., vertexShaderCode: PySide6.QtCore.QByteArray | bytes | bytearray | memoryview | None = ..., tessellationControlShaderCode: PySide6.QtCore.QByteArray | bytes | bytearray | memoryview | None = ..., tessellationEvaluationShaderCode: PySide6.QtCore.QByteArray | bytes | bytearray | memoryview | None = ..., geometryShaderCode: PySide6.QtCore.QByteArray | bytes | bytearray | memoryview | None = ..., fragmentShaderCode: PySide6.QtCore.QByteArray | bytes | bytearray | memoryview | None = ..., computeShaderCode: PySide6.QtCore.QByteArray | bytes | bytearray | memoryview | None = ...) -> None: ...

        def computeShaderCode(self, /) -> PySide6.QtCore.QByteArray: ...
        def computeShaderGraph(self, /) -> PySide6.QtCore.QUrl: ...
        def enabledLayers(self, /) -> typing.List[str]: ...
        def fragmentShaderCode(self, /) -> PySide6.QtCore.QByteArray: ...
        def fragmentShaderGraph(self, /) -> PySide6.QtCore.QUrl: ...
        def geometryShaderCode(self, /) -> PySide6.QtCore.QByteArray: ...
        def geometryShaderGraph(self, /) -> PySide6.QtCore.QUrl: ...
        def setComputeShaderGraph(self, computeShaderGraph: PySide6.QtCore.QUrl | str, /) -> None: ...
        def setEnabledLayers(self, layers: collections.abc.Sequence[str], /) -> None: ...
        def setFragmentShaderGraph(self, fragmentShaderGraph: PySide6.QtCore.QUrl | str, /) -> None: ...
        def setGeometryShaderGraph(self, geometryShaderGraph: PySide6.QtCore.QUrl | str, /) -> None: ...
        def setShaderProgram(self, program: PySide6.Qt3DRender.Qt3DRender.QShaderProgram, /) -> None: ...
        def setTessellationControlShaderGraph(self, tessellationControlShaderGraph: PySide6.QtCore.QUrl | str, /) -> None: ...
        def setTessellationEvaluationShaderGraph(self, tessellationEvaluationShaderGraph: PySide6.QtCore.QUrl | str, /) -> None: ...
        def setVertexShaderGraph(self, vertexShaderGraph: PySide6.QtCore.QUrl | str, /) -> None: ...
        def shaderProgram(self, /) -> PySide6.Qt3DRender.Qt3DRender.QShaderProgram: ...
        def tessellationControlShaderCode(self, /) -> PySide6.QtCore.QByteArray: ...
        def tessellationControlShaderGraph(self, /) -> PySide6.QtCore.QUrl: ...
        def tessellationEvaluationShaderCode(self, /) -> PySide6.QtCore.QByteArray: ...
        def tessellationEvaluationShaderGraph(self, /) -> PySide6.QtCore.QUrl: ...
        def vertexShaderCode(self, /) -> PySide6.QtCore.QByteArray: ...
        def vertexShaderGraph(self, /) -> PySide6.QtCore.QUrl: ...

    class QSharedGLTexture(PySide6.Qt3DRender.Qt3DRender.QAbstractTexture):
        # textureIdChanged(int)
        textureIdChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, textureId: int | None = ...) -> None: ...

        def setTextureId(self, id: int, /) -> None: ...
        def textureId(self, /) -> int: ...

    class QSortPolicy(PySide6.Qt3DRender.Qt3DRender.QFrameGraphNode):
        # sortTypesChanged(QList<SortType>); sortTypesChanged(QList<int>)
        sortTypesChanged: typing.ClassVar[Signal[
            [collections.abc.Sequence[SortType]], [collections.abc.Sequence[int]], [], [], [], [], [], [],
            [collections.abc.Sequence[SortType]], [collections.abc.Sequence[int]], [collections.abc.Sequence[SortType]], [collections.abc.Sequence[SortType]], [collections.abc.Sequence[SortType]], [collections.abc.Sequence[SortType]], [collections.abc.Sequence[SortType]], [collections.abc.Sequence[SortType]]
        ]]

        class SortType(enum.Enum):
            StateChangeCost           = 0x1
            BackToFront               = 0x2
            Material                  = 0x4
            FrontToBack               = 0x8
            Texture                   = 0x10
            Uniform                   = 0x20

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, sortTypes: collections.abc.Sequence[int] | None = ...) -> None: ...

        @typing.overload
        def setSortTypes(self, sortTypes: collections.abc.Sequence[PySide6.Qt3DRender.Qt3DRender.QSortPolicy.SortType], /) -> None: ...
        @typing.overload
        def setSortTypes(self, sortTypesInt: collections.abc.Sequence[int], /) -> None: ...
        def sortTypes(self, /) -> typing.List[PySide6.Qt3DRender.Qt3DRender.QSortPolicy.SortType]: ...
        def sortTypesInt(self, /) -> typing.List[int]: ...

    class QSpotLight(PySide6.Qt3DRender.Qt3DRender.QAbstractLight):
        # constantAttenuationChanged(float)
        constantAttenuationChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # cutOffAngleChanged(float)
        cutOffAngleChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # linearAttenuationChanged(float)
        linearAttenuationChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # localDirectionChanged(QVector3D)
        localDirectionChanged: typing.ClassVar[Signal[
            [PySide6.QtGui.QVector3D], [], [], [], [], [], [], [],
            [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D]
        ]]
        # quadraticAttenuationChanged(float)
        quadraticAttenuationChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, constantAttenuation: float | None = ..., linearAttenuation: float | None = ..., quadraticAttenuation: float | None = ..., localDirection: PySide6.QtGui.QVector3D | None = ..., cutOffAngle: float | None = ...) -> None: ...

        def constantAttenuation(self, /) -> float: ...
        def cutOffAngle(self, /) -> float: ...
        def linearAttenuation(self, /) -> float: ...
        def localDirection(self, /) -> PySide6.QtGui.QVector3D: ...
        def quadraticAttenuation(self, /) -> float: ...
        def setConstantAttenuation(self, value: float, /) -> None: ...
        def setCutOffAngle(self, cutOffAngle: float, /) -> None: ...
        def setLinearAttenuation(self, value: float, /) -> None: ...
        def setLocalDirection(self, localDirection: PySide6.QtGui.QVector3D, /) -> None: ...
        def setQuadraticAttenuation(self, value: float, /) -> None: ...

    class QStencilMask(PySide6.Qt3DRender.Qt3DRender.QRenderState):
        # backOutputMaskChanged(uint)
        backOutputMaskChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]
        # frontOutputMaskChanged(uint)
        frontOutputMaskChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, frontOutputMask: int | None = ..., backOutputMask: int | None = ...) -> None: ...

        def backOutputMask(self, /) -> int: ...
        def frontOutputMask(self, /) -> int: ...
        def setBackOutputMask(self, backOutputMask: int, /) -> None: ...
        def setFrontOutputMask(self, frontOutputMask: int, /) -> None: ...

    class QStencilOperation(PySide6.Qt3DRender.Qt3DRender.QRenderState):
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, front: PySide6.Qt3DRender.Qt3DRender.QStencilOperationArguments | None = ..., back: PySide6.Qt3DRender.Qt3DRender.QStencilOperationArguments | None = ...) -> None: ...

        def back(self, /) -> PySide6.Qt3DRender.Qt3DRender.QStencilOperationArguments: ...
        def front(self, /) -> PySide6.Qt3DRender.Qt3DRender.QStencilOperationArguments: ...

    class QStencilOperationArguments(PySide6.QtCore.QObject):
        # allTestsPassOperationChanged(Operation)
        allTestsPassOperationChanged: typing.ClassVar[Signal[
            [Operation], [], [], [], [], [], [], [],
            [Operation], [Operation], [Operation], [Operation], [Operation], [Operation], [Operation], [Operation]
        ]]
        # depthTestFailureOperationChanged(Operation)
        depthTestFailureOperationChanged: typing.ClassVar[Signal[
            [Operation], [], [], [], [], [], [], [],
            [Operation], [Operation], [Operation], [Operation], [Operation], [Operation], [Operation], [Operation]
        ]]
        # faceModeChanged(FaceMode)
        faceModeChanged: typing.ClassVar[Signal[
            [FaceMode], [], [], [], [], [], [], [],
            [FaceMode], [FaceMode], [FaceMode], [FaceMode], [FaceMode], [FaceMode], [FaceMode], [FaceMode]
        ]]
        # stencilTestFailureOperationChanged(Operation)
        stencilTestFailureOperationChanged: typing.ClassVar[Signal[
            [Operation], [], [], [], [], [], [], [],
            [Operation], [Operation], [Operation], [Operation], [Operation], [Operation], [Operation], [Operation]
        ]]

        class FaceMode(enum.Enum):
            Front                     = 0x404
            Back                      = 0x405
            FrontAndBack              = 0x408

        class Operation(enum.Enum):
            Zero                      = 0x0
            Invert                    = 0x150a
            Keep                      = 0x1e00
            Replace                   = 0x1e01
            Increment                 = 0x1e02
            Decrement                 = 0x1e03
            IncrementWrap             = 0x8507
            DecrementWrap             = 0x8508

        def allTestsPassOperation(self, /) -> PySide6.Qt3DRender.Qt3DRender.QStencilOperationArguments.Operation: ...
        def depthTestFailureOperation(self, /) -> PySide6.Qt3DRender.Qt3DRender.QStencilOperationArguments.Operation: ...
        def faceMode(self, /) -> PySide6.Qt3DRender.Qt3DRender.QStencilOperationArguments.FaceMode: ...
        def setAllTestsPassOperation(self, operation: PySide6.Qt3DRender.Qt3DRender.QStencilOperationArguments.Operation, /) -> None: ...
        def setDepthTestFailureOperation(self, operation: PySide6.Qt3DRender.Qt3DRender.QStencilOperationArguments.Operation, /) -> None: ...
        def setStencilTestFailureOperation(self, operation: PySide6.Qt3DRender.Qt3DRender.QStencilOperationArguments.Operation, /) -> None: ...
        def stencilTestFailureOperation(self, /) -> PySide6.Qt3DRender.Qt3DRender.QStencilOperationArguments.Operation: ...

    class QStencilTest(PySide6.Qt3DRender.Qt3DRender.QRenderState):
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, front: PySide6.Qt3DRender.Qt3DRender.QStencilTestArguments | None = ..., back: PySide6.Qt3DRender.Qt3DRender.QStencilTestArguments | None = ...) -> None: ...

        def back(self, /) -> PySide6.Qt3DRender.Qt3DRender.QStencilTestArguments: ...
        def front(self, /) -> PySide6.Qt3DRender.Qt3DRender.QStencilTestArguments: ...

    class QStencilTestArguments(PySide6.QtCore.QObject):
        # comparisonMaskChanged(uint)
        comparisonMaskChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]
        # faceModeChanged(StencilFaceMode)
        faceModeChanged: typing.ClassVar[Signal[
            [StencilFaceMode], [], [], [], [], [], [], [],
            [StencilFaceMode], [StencilFaceMode], [StencilFaceMode], [StencilFaceMode], [StencilFaceMode], [StencilFaceMode], [StencilFaceMode], [StencilFaceMode]
        ]]
        # referenceValueChanged(int)
        referenceValueChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]
        # stencilFunctionChanged(StencilFunction)
        stencilFunctionChanged: typing.ClassVar[Signal[
            [StencilFunction], [], [], [], [], [], [], [],
            [StencilFunction], [StencilFunction], [StencilFunction], [StencilFunction], [StencilFunction], [StencilFunction], [StencilFunction], [StencilFunction]
        ]]

        class StencilFaceMode(enum.Enum):
            Front                     = 0x404
            Back                      = 0x405
            FrontAndBack              = 0x408

        class StencilFunction(enum.Enum):
            Never                     = 0x200
            Less                      = 0x201
            Equal                     = 0x202
            LessOrEqual               = 0x203
            Greater                   = 0x204
            NotEqual                  = 0x205
            GreaterOrEqual            = 0x206
            Always                    = 0x207

        def comparisonMask(self, /) -> int: ...
        def faceMode(self, /) -> PySide6.Qt3DRender.Qt3DRender.QStencilTestArguments.StencilFaceMode: ...
        def referenceValue(self, /) -> int: ...
        def setComparisonMask(self, comparisonMask: int, /) -> None: ...
        def setReferenceValue(self, referenceValue: int, /) -> None: ...
        def setStencilFunction(self, stencilFunction: PySide6.Qt3DRender.Qt3DRender.QStencilTestArguments.StencilFunction, /) -> None: ...
        def stencilFunction(self, /) -> PySide6.Qt3DRender.Qt3DRender.QStencilTestArguments.StencilFunction: ...

    class QSubtreeEnabler(PySide6.Qt3DRender.Qt3DRender.QFrameGraphNode):
        # enablementChanged(Qt3DRender::QSubtreeEnabler::Enablement)
        enablementChanged: typing.ClassVar[Signal[
            [PySide6.Qt3DRender.Qt3DRender.QSubtreeEnabler.Enablement], [], [], [], [], [], [], [],
            [PySide6.Qt3DRender.Qt3DRender.QSubtreeEnabler.Enablement], [PySide6.Qt3DRender.Qt3DRender.QSubtreeEnabler.Enablement], [PySide6.Qt3DRender.Qt3DRender.QSubtreeEnabler.Enablement], [PySide6.Qt3DRender.Qt3DRender.QSubtreeEnabler.Enablement], [PySide6.Qt3DRender.Qt3DRender.QSubtreeEnabler.Enablement], [PySide6.Qt3DRender.Qt3DRender.QSubtreeEnabler.Enablement], [PySide6.Qt3DRender.Qt3DRender.QSubtreeEnabler.Enablement], [PySide6.Qt3DRender.Qt3DRender.QSubtreeEnabler.Enablement]
        ]]

        class Enablement(enum.Enum):
            Persistent                = 0x0
            SingleShot                = 0x1

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, enablement: PySide6.Qt3DRender.Qt3DRender.QSubtreeEnabler.Enablement | None = ...) -> None: ...

        def enablement(self, /) -> PySide6.Qt3DRender.Qt3DRender.QSubtreeEnabler.Enablement: ...
        def requestUpdate(self, /) -> None: ...
        def setEnablement(self, enablement: PySide6.Qt3DRender.Qt3DRender.QSubtreeEnabler.Enablement, /) -> None: ...

    class QTechnique(PySide6.Qt3DCore.Qt3DCore.QNode):
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, graphicsApiFilter: PySide6.Qt3DRender.Qt3DRender.QGraphicsApiFilter | None = ...) -> None: ...

        def addFilterKey(self, filterKey: PySide6.Qt3DRender.Qt3DRender.QFilterKey, /) -> None: ...
        def addParameter(self, p: PySide6.Qt3DRender.Qt3DRender.QParameter, /) -> None: ...
        def addRenderPass(self, pass_: PySide6.Qt3DRender.Qt3DRender.QRenderPass, /) -> None: ...
        def filterKeys(self, /) -> typing.List[PySide6.Qt3DRender.Qt3DRender.QFilterKey]: ...
        def graphicsApiFilter(self, /) -> PySide6.Qt3DRender.Qt3DRender.QGraphicsApiFilter: ...
        def parameters(self, /) -> typing.List[PySide6.Qt3DRender.Qt3DRender.QParameter]: ...
        def removeFilterKey(self, filterKey: PySide6.Qt3DRender.Qt3DRender.QFilterKey, /) -> None: ...
        def removeParameter(self, p: PySide6.Qt3DRender.Qt3DRender.QParameter, /) -> None: ...
        def removeRenderPass(self, pass_: PySide6.Qt3DRender.Qt3DRender.QRenderPass, /) -> None: ...
        def renderPasses(self, /) -> typing.List[PySide6.Qt3DRender.Qt3DRender.QRenderPass]: ...

    class QTechniqueFilter(PySide6.Qt3DRender.Qt3DRender.QFrameGraphNode):
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...) -> None: ...

        def addMatch(self, filterKey: PySide6.Qt3DRender.Qt3DRender.QFilterKey, /) -> None: ...
        def addParameter(self, p: PySide6.Qt3DRender.Qt3DRender.QParameter, /) -> None: ...
        def matchAll(self, /) -> typing.List[PySide6.Qt3DRender.Qt3DRender.QFilterKey]: ...
        def parameters(self, /) -> typing.List[PySide6.Qt3DRender.Qt3DRender.QParameter]: ...
        def removeMatch(self, filterKey: PySide6.Qt3DRender.Qt3DRender.QFilterKey, /) -> None: ...
        def removeParameter(self, p: PySide6.Qt3DRender.Qt3DRender.QParameter, /) -> None: ...

    class QTexture1D(PySide6.Qt3DRender.Qt3DRender.QAbstractTexture):
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...) -> None: ...

    class QTexture1DArray(PySide6.Qt3DRender.Qt3DRender.QAbstractTexture):
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...) -> None: ...

    class QTexture2D(PySide6.Qt3DRender.Qt3DRender.QAbstractTexture):
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...) -> None: ...

    class QTexture2DArray(PySide6.Qt3DRender.Qt3DRender.QAbstractTexture):
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...) -> None: ...

    class QTexture2DMultisample(PySide6.Qt3DRender.Qt3DRender.QAbstractTexture):
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...) -> None: ...

    class QTexture2DMultisampleArray(PySide6.Qt3DRender.Qt3DRender.QAbstractTexture):
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...) -> None: ...

    class QTexture3D(PySide6.Qt3DRender.Qt3DRender.QAbstractTexture):
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...) -> None: ...

    class QTextureBuffer(PySide6.Qt3DRender.Qt3DRender.QAbstractTexture):
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...) -> None: ...

    class QTextureCubeMap(PySide6.Qt3DRender.Qt3DRender.QAbstractTexture):
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...) -> None: ...

    class QTextureCubeMapArray(PySide6.Qt3DRender.Qt3DRender.QAbstractTexture):
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...) -> None: ...

    class QTextureData(shiboken6.Shiboken.Object):
        def __init__(self, /) -> None: ...

        def addImageData(self, imageData: PySide6.Qt3DRender.Qt3DRender.QTextureImageDataPtr, /) -> None: ...
        def comparisonFunction(self, /) -> PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.ComparisonFunction: ...
        def comparisonMode(self, /) -> PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.ComparisonMode: ...
        def depth(self, /) -> int: ...
        def format(self, /) -> PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.TextureFormat: ...
        def height(self, /) -> int: ...
        def imageData(self, /) -> typing.List[typing.Tuple[PySide6.Qt3DRender.Qt3DRender.QTextureImageData]]: ...
        def isAutoMipMapGenerationEnabled(self, /) -> bool: ...
        def layers(self, /) -> int: ...
        def magnificationFilter(self, /) -> PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.Filter: ...
        def maximumAnisotropy(self, /) -> float: ...
        def minificationFilter(self, /) -> PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.Filter: ...
        def setAutoMipMapGenerationEnabled(self, isAutoMipMapGenerationEnabled: bool, /) -> None: ...
        def setComparisonFunction(self, comparisonFunction: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.ComparisonFunction, /) -> None: ...
        def setComparisonMode(self, comparisonMode: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.ComparisonMode, /) -> None: ...
        def setDepth(self, depth: int, /) -> None: ...
        def setFormat(self, arg__1: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.TextureFormat, /) -> None: ...
        def setHeight(self, height: int, /) -> None: ...
        def setLayers(self, layers: int, /) -> None: ...
        def setMagnificationFilter(self, filter: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.Filter, /) -> None: ...
        def setMaximumAnisotropy(self, maximumAnisotropy: float, /) -> None: ...
        def setMinificationFilter(self, filter: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.Filter, /) -> None: ...
        def setTarget(self, target: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.Target, /) -> None: ...
        def setWidth(self, width: int, /) -> None: ...
        def setWrapModeX(self, wrapModeX: PySide6.Qt3DRender.Qt3DRender.QTextureWrapMode.WrapMode, /) -> None: ...
        def setWrapModeY(self, wrapModeY: PySide6.Qt3DRender.Qt3DRender.QTextureWrapMode.WrapMode, /) -> None: ...
        def setWrapModeZ(self, wrapModeZ: PySide6.Qt3DRender.Qt3DRender.QTextureWrapMode.WrapMode, /) -> None: ...
        def target(self, /) -> PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.Target: ...
        def width(self, /) -> int: ...
        def wrapModeX(self, /) -> PySide6.Qt3DRender.Qt3DRender.QTextureWrapMode.WrapMode: ...
        def wrapModeY(self, /) -> PySide6.Qt3DRender.Qt3DRender.QTextureWrapMode.WrapMode: ...
        def wrapModeZ(self, /) -> PySide6.Qt3DRender.Qt3DRender.QTextureWrapMode.WrapMode: ...

    class QTextureDataUpdate(shiboken6.Shiboken.Object):
        @typing.overload
        def __init__(self, /) -> None: ...
        @typing.overload
        def __init__(self, other: PySide6.Qt3DRender.Qt3DRender.QTextureDataUpdate, /) -> None: ...

        def __copy__(self, /) -> PySide6.Qt3DRender.Qt3DRender.QTextureDataUpdate: ...
        def __eq__(self, rhs: PySide6.Qt3DRender.Qt3DRender.QTextureDataUpdate, /) -> bool: ...
        def __ne__(self, rhs: PySide6.Qt3DRender.Qt3DRender.QTextureDataUpdate, /) -> bool: ...
        def data(self, /) -> PySide6.Qt3DRender.Qt3DRender.QTextureImageDataPtr: ...
        def face(self, /) -> PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.CubeMapFace: ...
        def layer(self, /) -> int: ...
        def mipLevel(self, /) -> int: ...
        def setData(self, data: PySide6.Qt3DRender.Qt3DRender.QTextureImageDataPtr, /) -> None: ...
        def setFace(self, face: PySide6.Qt3DRender.Qt3DRender.QAbstractTexture.CubeMapFace, /) -> None: ...
        def setLayer(self, layer: int, /) -> None: ...
        def setMipLevel(self, mipLevel: int, /) -> None: ...
        def setX(self, x: int, /) -> None: ...
        def setY(self, y: int, /) -> None: ...
        def setZ(self, z: int, /) -> None: ...
        def swap(self, other: PySide6.Qt3DRender.Qt3DRender.QTextureDataUpdate, /) -> None: ...
        def x(self, /) -> int: ...
        def y(self, /) -> int: ...
        def z(self, /) -> int: ...

    class QTextureImage(PySide6.Qt3DRender.Qt3DRender.QAbstractTextureImage):
        # mirroredChanged(bool)
        mirroredChanged: typing.ClassVar[Signal[
            [bool], [], [], [], [], [], [], [],
            [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
        ]]
        # sourceChanged(QUrl)
        sourceChanged: typing.ClassVar[Signal[
            [PySide6.QtCore.QUrl], [], [], [], [], [], [], [],
            [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl]
        ]]
        # statusChanged(Status)
        statusChanged: typing.ClassVar[Signal[
            [Status], [], [], [], [], [], [], [],
            [Status], [Status], [Status], [Status], [Status], [Status], [Status], [Status]
        ]]

        class Status(enum.Enum):
            None_                     = 0x0
            Loading                   = 0x1
            Ready                     = 0x2
            Error                     = 0x3

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, source: PySide6.QtCore.QUrl | None = ..., status: PySide6.Qt3DRender.Qt3DRender.QTextureImage.Status | None = ..., mirrored: bool | None = ...) -> None: ...

        def dataGenerator(self, /) -> PySide6.Qt3DRender.Qt3DRender.QTextureImageDataGeneratorPtr: ...
        def isMirrored(self, /) -> bool: ...
        def setMirrored(self, mirrored: bool, /) -> None: ...
        def setSource(self, source: PySide6.QtCore.QUrl | str, /) -> None: ...
        def setStatus(self, status: PySide6.Qt3DRender.Qt3DRender.QTextureImage.Status, /) -> None: ...
        def source(self, /) -> PySide6.QtCore.QUrl: ...
        def status(self, /) -> PySide6.Qt3DRender.Qt3DRender.QTextureImage.Status: ...

    class QTextureImageData(shiboken6.Shiboken.Object):
        def __init__(self, /) -> None: ...

        def alignment(self, /) -> int: ...
        def cleanup(self, /) -> None: ...
        def data(self, /, layer: int | None = ..., face: int | None = ..., mipmapLevel: int | None = ...) -> PySide6.QtCore.QByteArray: ...
        def depth(self, /) -> int: ...
        def faces(self, /) -> int: ...
        def format(self, /) -> PySide6.QtOpenGL.QOpenGLTexture.TextureFormat: ...
        def height(self, /) -> int: ...
        def isCompressed(self, /) -> bool: ...
        def layers(self, /) -> int: ...
        def mipLevels(self, /) -> int: ...
        def pixelFormat(self, /) -> PySide6.QtOpenGL.QOpenGLTexture.PixelFormat: ...
        def pixelType(self, /) -> PySide6.QtOpenGL.QOpenGLTexture.PixelType: ...
        def setAlignment(self, alignment: int, /) -> None: ...
        def setData(self, data: PySide6.QtCore.QByteArray | bytes | bytearray | str, blockSize: int, /, isCompressed: bool = ...) -> None: ...
        def setDepth(self, depth: int, /) -> None: ...
        def setFaces(self, faces: int, /) -> None: ...
        def setFormat(self, format: PySide6.QtOpenGL.QOpenGLTexture.TextureFormat, /) -> None: ...
        def setHeight(self, height: int, /) -> None: ...
        def setImage(self, arg__1: PySide6.QtGui.QImage, /) -> None: ...
        def setLayers(self, layers: int, /) -> None: ...
        def setMipLevels(self, mipLevels: int, /) -> None: ...
        def setPixelFormat(self, pixelFormat: PySide6.QtOpenGL.QOpenGLTexture.PixelFormat, /) -> None: ...
        def setPixelType(self, pixelType: PySide6.QtOpenGL.QOpenGLTexture.PixelType, /) -> None: ...
        def setTarget(self, target: PySide6.QtOpenGL.QOpenGLTexture.Target, /) -> None: ...
        def setWidth(self, width: int, /) -> None: ...
        def target(self, /) -> PySide6.QtOpenGL.QOpenGLTexture.Target: ...
        def width(self, /) -> int: ...

    class QTextureImageDataGenerator(PySide6.Qt3DCore.Qt3DCore.QAbstractFunctor):
        def __init__(self, /) -> None: ...

        def __call__(self, /) -> PySide6.Qt3DRender.Qt3DRender.QTextureImageDataPtr: ...
        def __eq__(self, other: PySide6.Qt3DRender.Qt3DRender.QTextureImageDataGenerator, /) -> bool: ...

    class QTextureImageDataGeneratorPtr(shiboken6.Shiboken.Object):
        @typing.overload
        def __init__(self, /) -> None: ...
        @typing.overload
        def __init__(self, pointee: PySide6.Qt3DRender.Qt3DRender.QTextureImageDataGenerator, /) -> None: ...

        def __copy__(self, /) -> PySide6.Qt3DRender.Qt3DRender.QTextureImageDataGeneratorPtr: ...
        def __dir__(self, /) -> collections.abc.Iterable[str]: ...
        def __repr__(self, /) -> str: ...
        def data(self, /) -> PySide6.Qt3DRender.Qt3DRender.QTextureImageDataGenerator: ...
        @typing.overload
        def reset(self, /) -> None: ...
        @typing.overload
        def reset(self, t: PySide6.Qt3DRender.Qt3DRender.QTextureImageDataGenerator, /) -> None: ...

    class QTextureImageDataPtr(shiboken6.Shiboken.Object):
        @typing.overload
        def __init__(self, /) -> None: ...
        @typing.overload
        def __init__(self, pointee: PySide6.Qt3DRender.Qt3DRender.QTextureImageData, /) -> None: ...

        def __copy__(self, /) -> PySide6.Qt3DRender.Qt3DRender.QTextureImageDataPtr: ...
        def __dir__(self, /) -> collections.abc.Iterable[str]: ...
        def __repr__(self, /) -> str: ...
        def data(self, /) -> PySide6.Qt3DRender.Qt3DRender.QTextureImageData: ...
        @typing.overload
        def reset(self, /) -> None: ...
        @typing.overload
        def reset(self, t: PySide6.Qt3DRender.Qt3DRender.QTextureImageData, /) -> None: ...

    class QTextureLoader(PySide6.Qt3DRender.Qt3DRender.QAbstractTexture):
        # mirroredChanged(bool)
        mirroredChanged: typing.ClassVar[Signal[
            [bool], [], [], [], [], [], [], [],
            [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
        ]]
        # sourceChanged(QUrl)
        sourceChanged: typing.ClassVar[Signal[
            [PySide6.QtCore.QUrl], [], [], [], [], [], [], [],
            [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl], [PySide6.QtCore.QUrl]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, source: PySide6.QtCore.QUrl | None = ..., mirrored: bool | None = ...) -> None: ...

        def isMirrored(self, /) -> bool: ...
        def setMirrored(self, mirrored: bool, /) -> None: ...
        def setSource(self, source: PySide6.QtCore.QUrl | str, /) -> None: ...
        def source(self, /) -> PySide6.QtCore.QUrl: ...

    class QTextureRectangle(PySide6.Qt3DRender.Qt3DRender.QAbstractTexture):
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ...) -> None: ...

    class QTextureWrapMode(PySide6.QtCore.QObject):
        # xChanged(WrapMode)
        xChanged: typing.ClassVar[Signal[
            [WrapMode], [], [], [], [], [], [], [],
            [WrapMode], [WrapMode], [WrapMode], [WrapMode], [WrapMode], [WrapMode], [WrapMode], [WrapMode]
        ]]
        # yChanged(WrapMode)
        yChanged: typing.ClassVar[Signal[
            [WrapMode], [], [], [], [], [], [], [],
            [WrapMode], [WrapMode], [WrapMode], [WrapMode], [WrapMode], [WrapMode], [WrapMode], [WrapMode]
        ]]
        # zChanged(WrapMode)
        zChanged: typing.ClassVar[Signal[
            [WrapMode], [], [], [], [], [], [], [],
            [WrapMode], [WrapMode], [WrapMode], [WrapMode], [WrapMode], [WrapMode], [WrapMode], [WrapMode]
        ]]

        class WrapMode(enum.Enum):
            Repeat                    = 0x2901
            ClampToBorder             = 0x812d
            ClampToEdge               = 0x812f
            MirroredRepeat            = 0x8370

        @typing.overload
        def __init__(self, x: PySide6.Qt3DRender.Qt3DRender.QTextureWrapMode.WrapMode, y: PySide6.Qt3DRender.Qt3DRender.QTextureWrapMode.WrapMode, z: PySide6.Qt3DRender.Qt3DRender.QTextureWrapMode.WrapMode, /, parent: PySide6.QtCore.QObject | None = ...) -> None: ...
        @typing.overload
        def __init__(self, /, wrapMode: PySide6.Qt3DRender.Qt3DRender.QTextureWrapMode.WrapMode = ..., parent: PySide6.QtCore.QObject | None = ..., *, x: PySide6.Qt3DRender.Qt3DRender.QTextureWrapMode.WrapMode | None = ..., y: PySide6.Qt3DRender.Qt3DRender.QTextureWrapMode.WrapMode | None = ..., z: PySide6.Qt3DRender.Qt3DRender.QTextureWrapMode.WrapMode | None = ...) -> None: ...

        def setX(self, x: PySide6.Qt3DRender.Qt3DRender.QTextureWrapMode.WrapMode, /) -> None: ...
        def setY(self, y: PySide6.Qt3DRender.Qt3DRender.QTextureWrapMode.WrapMode, /) -> None: ...
        def setZ(self, z: PySide6.Qt3DRender.Qt3DRender.QTextureWrapMode.WrapMode, /) -> None: ...
        def x(self, /) -> PySide6.Qt3DRender.Qt3DRender.QTextureWrapMode.WrapMode: ...
        def y(self, /) -> PySide6.Qt3DRender.Qt3DRender.QTextureWrapMode.WrapMode: ...
        def z(self, /) -> PySide6.Qt3DRender.Qt3DRender.QTextureWrapMode.WrapMode: ...

    class QViewport(PySide6.Qt3DRender.Qt3DRender.QFrameGraphNode):
        # gammaChanged(float)
        gammaChanged: typing.ClassVar[Signal[
            [float], [], [], [], [], [], [], [],
            [float], [float], [float], [float], [float], [float], [float], [float]
        ]]
        # normalizedRectChanged(QRectF)
        normalizedRectChanged: typing.ClassVar[Signal[
            [PySide6.QtCore.QRectF], [], [], [], [], [], [], [],
            [PySide6.QtCore.QRectF], [PySide6.QtCore.QRectF], [PySide6.QtCore.QRectF], [PySide6.QtCore.QRectF], [PySide6.QtCore.QRectF], [PySide6.QtCore.QRectF], [PySide6.QtCore.QRectF], [PySide6.QtCore.QRectF]
        ]]

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, normalizedRect: PySide6.QtCore.QRectF | None = ..., gamma: float | None = ...) -> None: ...

        def gamma(self, /) -> float: ...
        def normalizedRect(self, /) -> PySide6.QtCore.QRectF: ...
        def setGamma(self, gamma: float, /) -> None: ...
        def setNormalizedRect(self, normalizedRect: PySide6.QtCore.QRectF | PySide6.QtCore.QRect, /) -> None: ...

    class QWaitFence(PySide6.Qt3DRender.Qt3DRender.QFrameGraphNode):
        # handleChanged(QVariant)
        handleChanged: typing.ClassVar[Signal[
            [typing.Any], [], [], [], [], [], [], [],
            [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any]
        ]]
        # handleTypeChanged(HandleType)
        handleTypeChanged: typing.ClassVar[Signal[
            [HandleType], [], [], [], [], [], [], [],
            [HandleType], [HandleType], [HandleType], [HandleType], [HandleType], [HandleType], [HandleType], [HandleType]
        ]]
        # timeoutChanged(qulonglong)
        timeoutChanged: typing.ClassVar[Signal[
            [int], [], [], [], [], [], [], [],
            [int], [int], [int], [int], [int], [int], [int], [int]
        ]]
        # waitOnCPUChanged(bool)
        waitOnCPUChanged: typing.ClassVar[Signal[
            [bool], [], [], [], [], [], [], [],
            [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
        ]]

        class HandleType(enum.Enum):
            NoHandle                  = 0x0
            OpenGLFenceId             = 0x1

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None = ..., *, handleType: PySide6.Qt3DRender.Qt3DRender.QWaitFence.HandleType | None = ..., handle: typing.Any | None = ..., waitOnCPU: bool | None = ..., timeout: int | None = ...) -> None: ...

        def handle(self, /) -> typing.Any: ...
        def handleType(self, /) -> PySide6.Qt3DRender.Qt3DRender.QWaitFence.HandleType: ...
        def setHandle(self, handle: typing.Any, /) -> None: ...
        def setHandleType(self, type: PySide6.Qt3DRender.Qt3DRender.QWaitFence.HandleType, /) -> None: ...
        def setTimeout(self, timeout: int, /) -> None: ...
        def setWaitOnCPU(self, waitOnCPU: bool, /) -> None: ...
        def timeout(self, /) -> int: ...
        def waitOnCPU(self, /) -> bool: ...

    @staticmethod
    def swap(lhs: PySide6.Qt3DRender.Qt3DRender.QTextureDataUpdate, rhs: PySide6.Qt3DRender.Qt3DRender.QTextureDataUpdate, /) -> None: ...


# eof
