# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
"""
This file contains the exact signatures for all functions in module
PySide6.QtGraphs, except for defaults which are replaced by "...".
"""

# mypy: disable-error-code="override, overload-overlap"
# Module `PySide6.QtGraphs`

import PySide6.QtGraphs
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtQml
import PySide6.QtQuick

import os
import enum
import typing
import collections.abc
from PySide6.QtCore import Signal
from shiboken6 import Shiboken


class Q3DScene(PySide6.QtCore.QObject):
    # devicePixelRatioChanged(double)
    devicePixelRatioChanged: typing.ClassVar[Signal[
        [float], [], [], [], [], [], [], [],
        [float], [float], [float], [float], [float], [float], [float], [float]
    ]]
    # graphPositionQueryChanged(QPoint)
    graphPositionQueryChanged: typing.ClassVar[Signal[
        [PySide6.QtCore.QPoint], [], [], [], [], [], [], [],
        [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint]
    ]]
    # needRender()
    needRender: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # primarySubViewportChanged(QRect)
    primarySubViewportChanged: typing.ClassVar[Signal[
        [PySide6.QtCore.QRect], [], [], [], [], [], [], [],
        [PySide6.QtCore.QRect], [PySide6.QtCore.QRect], [PySide6.QtCore.QRect], [PySide6.QtCore.QRect], [PySide6.QtCore.QRect], [PySide6.QtCore.QRect], [PySide6.QtCore.QRect], [PySide6.QtCore.QRect]
    ]]
    # secondarySubViewportChanged(QRect)
    secondarySubViewportChanged: typing.ClassVar[Signal[
        [PySide6.QtCore.QRect], [], [], [], [], [], [], [],
        [PySide6.QtCore.QRect], [PySide6.QtCore.QRect], [PySide6.QtCore.QRect], [PySide6.QtCore.QRect], [PySide6.QtCore.QRect], [PySide6.QtCore.QRect], [PySide6.QtCore.QRect], [PySide6.QtCore.QRect]
    ]]
    # secondarySubviewOnTopChanged(bool)
    secondarySubviewOnTopChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # selectionQueryPositionChanged(QPoint)
    selectionQueryPositionChanged: typing.ClassVar[Signal[
        [PySide6.QtCore.QPoint], [], [], [], [], [], [], [],
        [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint]
    ]]
    # slicingActiveChanged(bool)
    slicingActiveChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # viewportChanged(QRect)
    viewportChanged: typing.ClassVar[Signal[
        [PySide6.QtCore.QRect], [], [], [], [], [], [], [],
        [PySide6.QtCore.QRect], [PySide6.QtCore.QRect], [PySide6.QtCore.QRect], [PySide6.QtCore.QRect], [PySide6.QtCore.QRect], [PySide6.QtCore.QRect], [PySide6.QtCore.QRect], [PySide6.QtCore.QRect]
    ]]

    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., *, viewport: PySide6.QtCore.QRect | None = ..., primarySubViewport: PySide6.QtCore.QRect | None = ..., secondarySubViewport: PySide6.QtCore.QRect | None = ..., selectionQueryPosition: PySide6.QtCore.QPoint | None = ..., secondarySubviewOnTop: bool | None = ..., slicingActive: bool | None = ..., devicePixelRatio: float | None = ..., graphPositionQuery: PySide6.QtCore.QPoint | None = ..., invalidSelectionPoint: PySide6.QtCore.QPoint | None = ...) -> None: ...

    def devicePixelRatio(self, /) -> float: ...
    def graphPositionQuery(self, /) -> PySide6.QtCore.QPoint: ...
    def invalidSelectionPoint(self, /) -> PySide6.QtCore.QPoint: ...
    def isPointInPrimarySubView(self, point: PySide6.QtCore.QPoint, /) -> bool: ...
    def isPointInSecondarySubView(self, point: PySide6.QtCore.QPoint, /) -> bool: ...
    def isSecondarySubviewOnTop(self, /) -> bool: ...
    def isSlicingActive(self, /) -> bool: ...
    def primarySubViewport(self, /) -> PySide6.QtCore.QRect: ...
    def secondarySubViewport(self, /) -> PySide6.QtCore.QRect: ...
    def selectionQueryPosition(self, /) -> PySide6.QtCore.QPoint: ...
    def setDevicePixelRatio(self, pixelRatio: float, /) -> None: ...
    def setGraphPositionQuery(self, point: PySide6.QtCore.QPoint, /) -> None: ...
    def setPrimarySubViewport(self, primarySubViewport: PySide6.QtCore.QRect, /) -> None: ...
    def setSecondarySubViewport(self, secondarySubViewport: PySide6.QtCore.QRect, /) -> None: ...
    def setSecondarySubviewOnTop(self, isSecondaryOnTop: bool, /) -> None: ...
    def setSelectionQueryPosition(self, point: PySide6.QtCore.QPoint, /) -> None: ...
    def setSlicingActive(self, isSlicing: bool, /) -> None: ...
    def viewport(self, /) -> PySide6.QtCore.QRect: ...


class QAbstract3DAxis(PySide6.QtCore.QObject):
    # autoAdjustRangeChanged(bool)
    autoAdjustRangeChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # labelAutoAngleChanged(float)
    labelAutoAngleChanged: typing.ClassVar[Signal[
        [float], [], [], [], [], [], [], [],
        [float], [float], [float], [float], [float], [float], [float], [float]
    ]]
    # labelSizeChanged(double)
    labelSizeChanged: typing.ClassVar[Signal[
        [float], [], [], [], [], [], [], [],
        [float], [float], [float], [float], [float], [float], [float], [float]
    ]]
    # labelVisibleChanged(bool)
    labelVisibleChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # labelsChanged()
    labelsChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # maxChanged(float)
    maxChanged: typing.ClassVar[Signal[
        [float], [], [], [], [], [], [], [],
        [float], [float], [float], [float], [float], [float], [float], [float]
    ]]
    # minChanged(float)
    minChanged: typing.ClassVar[Signal[
        [float], [], [], [], [], [], [], [],
        [float], [float], [float], [float], [float], [float], [float], [float]
    ]]
    # orientationChanged(QAbstract3DAxis::AxisOrientation)
    orientationChanged: typing.ClassVar[Signal[
        [PySide6.QtGraphs.QAbstract3DAxis.AxisOrientation], [], [], [], [], [], [], [],
        [PySide6.QtGraphs.QAbstract3DAxis.AxisOrientation], [PySide6.QtGraphs.QAbstract3DAxis.AxisOrientation], [PySide6.QtGraphs.QAbstract3DAxis.AxisOrientation], [PySide6.QtGraphs.QAbstract3DAxis.AxisOrientation], [PySide6.QtGraphs.QAbstract3DAxis.AxisOrientation], [PySide6.QtGraphs.QAbstract3DAxis.AxisOrientation], [PySide6.QtGraphs.QAbstract3DAxis.AxisOrientation], [PySide6.QtGraphs.QAbstract3DAxis.AxisOrientation]
    ]]
    # rangeChanged(float,float)
    rangeChanged: typing.ClassVar[Signal[
        [float, float], [float], [], [], [], [], [], [],
        [float, float], [float, float], [float, float], [float, float], [float, float], [float, float], [float, float], [float, float]
    ]]
    # scaleLabelsByCountChanged(bool)
    scaleLabelsByCountChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # titleChanged(QString)
    titleChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # titleFixedChanged(bool)
    titleFixedChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # titleOffsetChanged(float)
    titleOffsetChanged: typing.ClassVar[Signal[
        [float], [], [], [], [], [], [], [],
        [float], [float], [float], [float], [float], [float], [float], [float]
    ]]
    # titleVisibleChanged(bool)
    titleVisibleChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]

    class AxisOrientation(enum.Enum):
        None_                     = 0x0
        X                         = 0x1
        Y                         = 0x2
        Z                         = 0x3

    class AxisType(enum.Enum):
        None_                     = 0x0
        Category                  = 0x1
        Value                     = 0x2

    def isAutoAdjustRange(self, /) -> bool: ...
    def isScaleLabelsByCount(self, /) -> bool: ...
    def isTitleFixed(self, /) -> bool: ...
    def isTitleVisible(self, /) -> bool: ...
    def labelAutoAngle(self, /) -> float: ...
    def labelSize(self, /) -> float: ...
    def labels(self, /) -> typing.List[str]: ...
    def labelsVisible(self, /) -> bool: ...
    def max(self, /) -> float: ...
    def min(self, /) -> float: ...
    def orientation(self, /) -> PySide6.QtGraphs.QAbstract3DAxis.AxisOrientation: ...
    def setAutoAdjustRange(self, autoAdjust: bool, /) -> None: ...
    def setLabelAutoAngle(self, degree: float, /) -> None: ...
    def setLabelSize(self, size: float, /) -> None: ...
    def setLabels(self, labels: collections.abc.Sequence[str], /) -> None: ...
    def setLabelsVisible(self, visible: bool, /) -> None: ...
    def setMax(self, max: float, /) -> None: ...
    def setMin(self, min: float, /) -> None: ...
    def setRange(self, min: float, max: float, /) -> None: ...
    def setScaleLabelsByCount(self, adjust: bool, /) -> None: ...
    def setTitle(self, title: str, /) -> None: ...
    def setTitleFixed(self, fixed: bool, /) -> None: ...
    def setTitleOffset(self, offset: float, /) -> None: ...
    def setTitleVisible(self, visible: bool, /) -> None: ...
    def title(self, /) -> str: ...
    def titleOffset(self, /) -> float: ...
    def type(self, /) -> PySide6.QtGraphs.QAbstract3DAxis.AxisType: ...


class QAbstract3DSeries(PySide6.QtCore.QObject):
    # baseColorChanged(QColor)
    baseColorChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QColor], [], [], [], [], [], [], [],
        [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor]
    ]]
    # baseGradientChanged(QLinearGradient)
    baseGradientChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QLinearGradient], [], [], [], [], [], [], [],
        [PySide6.QtGui.QLinearGradient], [PySide6.QtGui.QLinearGradient], [PySide6.QtGui.QLinearGradient], [PySide6.QtGui.QLinearGradient], [PySide6.QtGui.QLinearGradient], [PySide6.QtGui.QLinearGradient], [PySide6.QtGui.QLinearGradient], [PySide6.QtGui.QLinearGradient]
    ]]
    # colorStyleChanged(QGraphsTheme::ColorStyle)
    colorStyleChanged: typing.ClassVar[Signal[
        [PySide6.QtGraphs.QGraphsTheme.ColorStyle], [], [], [], [], [], [], [],
        [PySide6.QtGraphs.QGraphsTheme.ColorStyle], [PySide6.QtGraphs.QGraphsTheme.ColorStyle], [PySide6.QtGraphs.QGraphsTheme.ColorStyle], [PySide6.QtGraphs.QGraphsTheme.ColorStyle], [PySide6.QtGraphs.QGraphsTheme.ColorStyle], [PySide6.QtGraphs.QGraphsTheme.ColorStyle], [PySide6.QtGraphs.QGraphsTheme.ColorStyle], [PySide6.QtGraphs.QGraphsTheme.ColorStyle]
    ]]
    # itemLabelChanged(QString)
    itemLabelChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # itemLabelFormatChanged(QString)
    itemLabelFormatChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # itemLabelVisibleChanged(bool)
    itemLabelVisibleChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # lightingModeChanged(QAbstract3DSeries::LightingMode)
    lightingModeChanged: typing.ClassVar[Signal[
        [PySide6.QtGraphs.QAbstract3DSeries.LightingMode], [], [], [], [], [], [], [],
        [PySide6.QtGraphs.QAbstract3DSeries.LightingMode], [PySide6.QtGraphs.QAbstract3DSeries.LightingMode], [PySide6.QtGraphs.QAbstract3DSeries.LightingMode], [PySide6.QtGraphs.QAbstract3DSeries.LightingMode], [PySide6.QtGraphs.QAbstract3DSeries.LightingMode], [PySide6.QtGraphs.QAbstract3DSeries.LightingMode], [PySide6.QtGraphs.QAbstract3DSeries.LightingMode], [PySide6.QtGraphs.QAbstract3DSeries.LightingMode]
    ]]
    # meshChanged(QAbstract3DSeries::Mesh)
    meshChanged: typing.ClassVar[Signal[
        [PySide6.QtGraphs.QAbstract3DSeries.Mesh], [], [], [], [], [], [], [],
        [PySide6.QtGraphs.QAbstract3DSeries.Mesh], [PySide6.QtGraphs.QAbstract3DSeries.Mesh], [PySide6.QtGraphs.QAbstract3DSeries.Mesh], [PySide6.QtGraphs.QAbstract3DSeries.Mesh], [PySide6.QtGraphs.QAbstract3DSeries.Mesh], [PySide6.QtGraphs.QAbstract3DSeries.Mesh], [PySide6.QtGraphs.QAbstract3DSeries.Mesh], [PySide6.QtGraphs.QAbstract3DSeries.Mesh]
    ]]
    # meshRotationChanged(QQuaternion)
    meshRotationChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QQuaternion], [], [], [], [], [], [], [],
        [PySide6.QtGui.QQuaternion], [PySide6.QtGui.QQuaternion], [PySide6.QtGui.QQuaternion], [PySide6.QtGui.QQuaternion], [PySide6.QtGui.QQuaternion], [PySide6.QtGui.QQuaternion], [PySide6.QtGui.QQuaternion], [PySide6.QtGui.QQuaternion]
    ]]
    # meshSmoothChanged(bool)
    meshSmoothChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # multiHighlightColorChanged(QColor)
    multiHighlightColorChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QColor], [], [], [], [], [], [], [],
        [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor]
    ]]
    # multiHighlightGradientChanged(QLinearGradient)
    multiHighlightGradientChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QLinearGradient], [], [], [], [], [], [], [],
        [PySide6.QtGui.QLinearGradient], [PySide6.QtGui.QLinearGradient], [PySide6.QtGui.QLinearGradient], [PySide6.QtGui.QLinearGradient], [PySide6.QtGui.QLinearGradient], [PySide6.QtGui.QLinearGradient], [PySide6.QtGui.QLinearGradient], [PySide6.QtGui.QLinearGradient]
    ]]
    # nameChanged(QString)
    nameChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # singleHighlightColorChanged(QColor)
    singleHighlightColorChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QColor], [], [], [], [], [], [], [],
        [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor]
    ]]
    # singleHighlightGradientChanged(QLinearGradient)
    singleHighlightGradientChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QLinearGradient], [], [], [], [], [], [], [],
        [PySide6.QtGui.QLinearGradient], [PySide6.QtGui.QLinearGradient], [PySide6.QtGui.QLinearGradient], [PySide6.QtGui.QLinearGradient], [PySide6.QtGui.QLinearGradient], [PySide6.QtGui.QLinearGradient], [PySide6.QtGui.QLinearGradient], [PySide6.QtGui.QLinearGradient]
    ]]
    # userDefinedMeshChanged(QString)
    userDefinedMeshChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # visibleChanged(bool)
    visibleChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]

    class LightingMode(enum.Enum):
        Shaded                    = 0x0
        Unshaded                  = 0x1

    class Mesh(enum.Enum):
        UserDefined               = 0x0
        Bar                       = 0x1
        Cube                      = 0x2
        Pyramid                   = 0x3
        Cone                      = 0x4
        Cylinder                  = 0x5
        BevelBar                  = 0x6
        BevelCube                 = 0x7
        Sphere                    = 0x8
        Minimal                   = 0x9
        Arrow                     = 0xa
        Point                     = 0xb

    class SeriesType(enum.Enum):
        None_                     = 0x0
        Bar                       = 0x1
        Scatter                   = 0x2
        Surface                   = 0x3

    def baseColor(self, /) -> PySide6.QtGui.QColor: ...
    def baseGradient(self, /) -> PySide6.QtGui.QLinearGradient: ...
    def colorStyle(self, /) -> PySide6.QtGraphs.QGraphsTheme.ColorStyle: ...
    def isItemLabelVisible(self, /) -> bool: ...
    def isMeshSmooth(self, /) -> bool: ...
    def isVisible(self, /) -> bool: ...
    def itemLabel(self, /) -> str: ...
    def itemLabelFormat(self, /) -> str: ...
    def lightingMode(self, /) -> PySide6.QtGraphs.QAbstract3DSeries.LightingMode: ...
    def mesh(self, /) -> PySide6.QtGraphs.QAbstract3DSeries.Mesh: ...
    def meshRotation(self, /) -> PySide6.QtGui.QQuaternion: ...
    def multiHighlightColor(self, /) -> PySide6.QtGui.QColor: ...
    def multiHighlightGradient(self, /) -> PySide6.QtGui.QLinearGradient: ...
    def name(self, /) -> str: ...
    def setBaseColor(self, color: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setBaseGradient(self, gradient: PySide6.QtGui.QLinearGradient, /) -> None: ...
    def setColorStyle(self, style: PySide6.QtGraphs.QGraphsTheme.ColorStyle, /) -> None: ...
    def setItemLabelFormat(self, format: str, /) -> None: ...
    def setItemLabelVisible(self, visible: bool, /) -> None: ...
    def setLightingMode(self, lightingMode: PySide6.QtGraphs.QAbstract3DSeries.LightingMode, /) -> None: ...
    def setMesh(self, mesh: PySide6.QtGraphs.QAbstract3DSeries.Mesh, /) -> None: ...
    def setMeshAxisAndAngle(self, axis: PySide6.QtGui.QVector3D, angle: float, /) -> None: ...
    def setMeshRotation(self, rotation: PySide6.QtGui.QQuaternion, /) -> None: ...
    def setMeshSmooth(self, enable: bool, /) -> None: ...
    def setMultiHighlightColor(self, color: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setMultiHighlightGradient(self, gradient: PySide6.QtGui.QLinearGradient, /) -> None: ...
    def setName(self, name: str, /) -> None: ...
    def setSingleHighlightColor(self, color: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setSingleHighlightGradient(self, gradient: PySide6.QtGui.QLinearGradient, /) -> None: ...
    def setUserDefinedMesh(self, fileName: str, /) -> None: ...
    def setVisible(self, visible: bool, /) -> None: ...
    def singleHighlightColor(self, /) -> PySide6.QtGui.QColor: ...
    def singleHighlightGradient(self, /) -> PySide6.QtGui.QLinearGradient: ...
    def type(self, /) -> PySide6.QtGraphs.QAbstract3DSeries.SeriesType: ...
    def userDefinedMesh(self, /) -> str: ...


class QAbstractAxis(PySide6.QtCore.QObject):
    # alignmentChanged(Qt::Alignment)
    alignmentChanged: typing.ClassVar[Signal[
        [PySide6.QtCore.Qt.AlignmentFlag], [], [], [], [], [], [], [],
        [PySide6.QtCore.Qt.AlignmentFlag], [PySide6.QtCore.Qt.AlignmentFlag], [PySide6.QtCore.Qt.AlignmentFlag], [PySide6.QtCore.Qt.AlignmentFlag], [PySide6.QtCore.Qt.AlignmentFlag], [PySide6.QtCore.Qt.AlignmentFlag], [PySide6.QtCore.Qt.AlignmentFlag], [PySide6.QtCore.Qt.AlignmentFlag]
    ]]
    # colorChanged(QColor)
    colorChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QColor], [], [], [], [], [], [], [],
        [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor]
    ]]
    # gridVisibleChanged(bool)
    gridVisibleChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # labelDelegateChanged()
    labelDelegateChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # labelsAngleChanged(double)
    labelsAngleChanged: typing.ClassVar[Signal[
        [float], [], [], [], [], [], [], [],
        [float], [float], [float], [float], [float], [float], [float], [float]
    ]]
    # labelsVisibleChanged(bool)
    labelsVisibleChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # lineVisibleChanged(bool)
    lineVisibleChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # rangeChanged(double,double)
    rangeChanged: typing.ClassVar[Signal[
        [float, float], [float], [], [], [], [], [], [],
        [float, float], [float, float], [float, float], [float, float], [float, float], [float, float], [float, float], [float, float]
    ]]
    # subColorChanged(QColor)
    subColorChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QColor], [], [], [], [], [], [], [],
        [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor]
    ]]
    # subGridVisibleChanged(bool)
    subGridVisibleChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # textElideModeChanged(Qt::TextElideMode)
    textElideModeChanged: typing.ClassVar[Signal[
        [PySide6.QtCore.Qt.TextElideMode], [], [], [], [], [], [], [],
        [PySide6.QtCore.Qt.TextElideMode], [PySide6.QtCore.Qt.TextElideMode], [PySide6.QtCore.Qt.TextElideMode], [PySide6.QtCore.Qt.TextElideMode], [PySide6.QtCore.Qt.TextElideMode], [PySide6.QtCore.Qt.TextElideMode], [PySide6.QtCore.Qt.TextElideMode], [PySide6.QtCore.Qt.TextElideMode]
    ]]
    # titleColorChanged(QColor)
    titleColorChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QColor], [], [], [], [], [], [], [],
        [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor]
    ]]
    # titleFontChanged(QFont)
    titleFontChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QFont], [], [], [], [], [], [], [],
        [PySide6.QtGui.QFont], [PySide6.QtGui.QFont], [PySide6.QtGui.QFont], [PySide6.QtGui.QFont], [PySide6.QtGui.QFont], [PySide6.QtGui.QFont], [PySide6.QtGui.QFont], [PySide6.QtGui.QFont]
    ]]
    # titleTextChanged(QString)
    titleTextChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # titleVisibleChanged(bool)
    titleVisibleChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # update()
    update: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # visibleChanged(bool)
    visibleChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]

    class AxisType(enum.Enum):
        Value                     = 0x0
        BarCategory               = 0x1
        DateTime                  = 0x2

    def alignment(self, /) -> PySide6.QtCore.Qt.AlignmentFlag: ...
    def color(self, /) -> PySide6.QtGui.QColor: ...
    def hide(self, /) -> None: ...
    def isGridVisible(self, /) -> bool: ...
    def isLineVisible(self, /) -> bool: ...
    def isSubGridVisible(self, /) -> bool: ...
    def isTitleVisible(self, /) -> bool: ...
    def isVisible(self, /) -> bool: ...
    def labelDelegate(self, /) -> PySide6.QtQml.QQmlComponent: ...
    def labelsAngle(self, /) -> float: ...
    def labelsVisible(self, /) -> bool: ...
    def setAlignment(self, alignment: PySide6.QtCore.Qt.AlignmentFlag, /) -> None: ...
    def setColor(self, color: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setGridVisible(self, /, visible: bool = ...) -> None: ...
    def setLabelDelegate(self, newLabelDelegate: PySide6.QtQml.QQmlComponent, /) -> None: ...
    def setLabelsAngle(self, angle: float, /) -> None: ...
    def setLabelsVisible(self, /, visible: bool = ...) -> None: ...
    def setLineVisible(self, /, visible: bool = ...) -> None: ...
    def setMax(self, max: typing.Any, /) -> None: ...
    def setMin(self, min: typing.Any, /) -> None: ...
    def setRange(self, min: typing.Any, max: typing.Any, /) -> None: ...
    def setSubColor(self, color: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setSubGridVisible(self, /, visible: bool = ...) -> None: ...
    def setTextElideMode(self, elideMode: PySide6.QtCore.Qt.TextElideMode, /) -> None: ...
    def setTitleColor(self, color: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setTitleFont(self, font: PySide6.QtGui.QFont | str | collections.abc.Sequence[str], /) -> None: ...
    def setTitleText(self, title: str, /) -> None: ...
    def setTitleVisible(self, /, visible: bool = ...) -> None: ...
    def setVisible(self, /, visible: bool = ...) -> None: ...
    def show(self, /) -> None: ...
    def subColor(self, /) -> PySide6.QtGui.QColor: ...
    def textElideMode(self, /) -> PySide6.QtCore.Qt.TextElideMode: ...
    def titleColor(self, /) -> PySide6.QtGui.QColor: ...
    def titleFont(self, /) -> PySide6.QtGui.QFont: ...
    def titleText(self, /) -> str: ...
    def type(self, /) -> PySide6.QtGraphs.QAbstractAxis.AxisType: ...


class QAbstractDataProxy(PySide6.QtCore.QObject):
    class DataType(enum.Enum):
        None_                     = 0x0
        Bar                       = 0x1
        Scatter                   = 0x2
        Surface                   = 0x3

    def type(self, /) -> PySide6.QtGraphs.QAbstractDataProxy.DataType: ...


class QAbstractSeries(PySide6.QtCore.QObject, PySide6.QtQml.QQmlParserStatus):
    # axisXChanged(QAbstractAxis*)
    axisXChanged: typing.ClassVar[Signal[
        [PySide6.QtGraphs.QAbstractAxis], [], [], [], [], [], [], [],
        [PySide6.QtGraphs.QAbstractAxis], [PySide6.QtGraphs.QAbstractAxis], [PySide6.QtGraphs.QAbstractAxis], [PySide6.QtGraphs.QAbstractAxis], [PySide6.QtGraphs.QAbstractAxis], [PySide6.QtGraphs.QAbstractAxis], [PySide6.QtGraphs.QAbstractAxis], [PySide6.QtGraphs.QAbstractAxis]
    ]]
    # axisYChanged(QAbstractAxis*)
    axisYChanged: typing.ClassVar[Signal[
        [PySide6.QtGraphs.QAbstractAxis], [], [], [], [], [], [], [],
        [PySide6.QtGraphs.QAbstractAxis], [PySide6.QtGraphs.QAbstractAxis], [PySide6.QtGraphs.QAbstractAxis], [PySide6.QtGraphs.QAbstractAxis], [PySide6.QtGraphs.QAbstractAxis], [PySide6.QtGraphs.QAbstractAxis], [PySide6.QtGraphs.QAbstractAxis], [PySide6.QtGraphs.QAbstractAxis]
    ]]
    # hover(QString,QPointF,QPointF)
    hover: typing.ClassVar[Signal[
        [str, PySide6.QtCore.QPointF, PySide6.QtCore.QPointF], [str, PySide6.QtCore.QPointF], [str], [], [], [], [], [],
        [str, PySide6.QtCore.QPointF, PySide6.QtCore.QPointF], [str, PySide6.QtCore.QPointF, PySide6.QtCore.QPointF], [str, PySide6.QtCore.QPointF, PySide6.QtCore.QPointF], [str, PySide6.QtCore.QPointF, PySide6.QtCore.QPointF], [str, PySide6.QtCore.QPointF, PySide6.QtCore.QPointF], [str, PySide6.QtCore.QPointF, PySide6.QtCore.QPointF], [str, PySide6.QtCore.QPointF, PySide6.QtCore.QPointF], [str, PySide6.QtCore.QPointF, PySide6.QtCore.QPointF]
    ]]
    # hoverEnter(QString,QPointF,QPointF)
    hoverEnter: typing.ClassVar[Signal[
        [str, PySide6.QtCore.QPointF, PySide6.QtCore.QPointF], [str, PySide6.QtCore.QPointF], [str], [], [], [], [], [],
        [str, PySide6.QtCore.QPointF, PySide6.QtCore.QPointF], [str, PySide6.QtCore.QPointF, PySide6.QtCore.QPointF], [str, PySide6.QtCore.QPointF, PySide6.QtCore.QPointF], [str, PySide6.QtCore.QPointF, PySide6.QtCore.QPointF], [str, PySide6.QtCore.QPointF, PySide6.QtCore.QPointF], [str, PySide6.QtCore.QPointF, PySide6.QtCore.QPointF], [str, PySide6.QtCore.QPointF, PySide6.QtCore.QPointF], [str, PySide6.QtCore.QPointF, PySide6.QtCore.QPointF]
    ]]
    # hoverExit(QString,QPointF)
    hoverExit: typing.ClassVar[Signal[
        [str, PySide6.QtCore.QPointF], [str], [], [], [], [], [], [],
        [str, PySide6.QtCore.QPointF], [str, PySide6.QtCore.QPointF], [str, PySide6.QtCore.QPointF], [str, PySide6.QtCore.QPointF], [str, PySide6.QtCore.QPointF], [str, PySide6.QtCore.QPointF], [str, PySide6.QtCore.QPointF], [str, PySide6.QtCore.QPointF]
    ]]
    # hoverableChanged()
    hoverableChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # hoveredChanged(bool)
    hoveredChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # legendDataChanged()
    legendDataChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # nameChanged()
    nameChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # opacityChanged()
    opacityChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # selectableChanged()
    selectableChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # update()
    update: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # valuesMultiplierChanged()
    valuesMultiplierChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # visibleChanged()
    visibleChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # zValueChanged(int)
    zValueChanged: typing.ClassVar[Signal[
        [int], [], [], [], [], [], [], [],
        [int], [int], [int], [int], [int], [int], [int], [int]
    ]]

    class SeriesType(enum.Enum):
        Line                      = 0x0
        Area                      = 0x1
        Bar                       = 0x2
        Pie                       = 0x3
        Scatter                   = 0x4
        Spline                    = 0x5
        Custom                    = 0x6

    def axisX(self, /) -> PySide6.QtGraphs.QAbstractAxis: ...
    def axisY(self, /) -> PySide6.QtGraphs.QAbstractAxis: ...
    def classBegin(self, /) -> None: ...
    def componentComplete(self, /) -> None: ...
    def hasLoaded(self, /) -> bool: ...
    def hide(self, /) -> None: ...
    def isHoverable(self, /) -> bool: ...
    def isHovered(self, /) -> bool: ...
    def isSelectable(self, /) -> bool: ...
    def isVisible(self, /) -> bool: ...
    def legendData(self, /) -> typing.List[PySide6.QtGraphs.QLegendData]: ...
    def name(self, /) -> str: ...
    def opacity(self, /) -> float: ...
    def setAxisX(self, newAxisX: PySide6.QtGraphs.QAbstractAxis, /) -> None: ...
    def setAxisY(self, newAxisY: PySide6.QtGraphs.QAbstractAxis, /) -> None: ...
    def setHoverable(self, newHoverable: bool, /) -> None: ...
    def setHovered(self, enabled: bool, /) -> None: ...
    def setName(self, name: str, /) -> None: ...
    def setOpacity(self, opacity: float, /) -> None: ...
    def setSelectable(self, selectable: bool, /) -> None: ...
    def setValuesMultiplier(self, valuesMultiplier: float, /) -> None: ...
    def setVisible(self, /, visible: bool = ...) -> None: ...
    def setZValue(self, newDrawOrder: int, /) -> None: ...
    def show(self, /) -> None: ...
    def type(self, /) -> PySide6.QtGraphs.QAbstractSeries.SeriesType: ...
    def valuesMultiplier(self, /) -> float: ...
    def zValue(self, /) -> int: ...


class QAreaSeries(PySide6.QtGraphs.QAbstractSeries):
    # borderColorChanged(QColor)
    borderColorChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QColor], [], [], [], [], [], [], [],
        [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor]
    ]]
    # borderWidthChanged()
    borderWidthChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # clicked(QPoint)
    clicked: typing.ClassVar[Signal[
        [PySide6.QtCore.QPoint], [], [], [], [], [], [], [],
        [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint]
    ]]
    # colorChanged(QColor)
    colorChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QColor], [], [], [], [], [], [], [],
        [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor]
    ]]
    # doubleClicked(QPoint)
    doubleClicked: typing.ClassVar[Signal[
        [PySide6.QtCore.QPoint], [], [], [], [], [], [], [],
        [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint]
    ]]
    # gradientChanged(QQuickShapeGradient*)
    gradientChanged: typing.ClassVar[Signal[
        [typing.Any], [], [], [], [], [], [], [],
        [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any]
    ]]
    # lowerSeriesChanged()
    lowerSeriesChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # pressed(QPoint)
    pressed: typing.ClassVar[Signal[
        [PySide6.QtCore.QPoint], [], [], [], [], [], [], [],
        [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint]
    ]]
    # released(QPoint)
    released: typing.ClassVar[Signal[
        [PySide6.QtCore.QPoint], [], [], [], [], [], [], [],
        [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint]
    ]]
    # selectedBorderColorChanged(QColor)
    selectedBorderColorChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QColor], [], [], [], [], [], [], [],
        [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor]
    ]]
    # selectedChanged()
    selectedChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # selectedColorChanged(QColor)
    selectedColorChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QColor], [], [], [], [], [], [], [],
        [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor]
    ]]
    # selectedGradientChanged(QQuickShapeGradient*)
    selectedGradientChanged: typing.ClassVar[Signal[
        [typing.Any], [], [], [], [], [], [], [],
        [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any]
    ]]
    # upperSeriesChanged()
    upperSeriesChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]

    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., *, color: PySide6.QtGui.QColor | None = ..., selectedColor: PySide6.QtGui.QColor | None = ..., borderColor: PySide6.QtGui.QColor | None = ..., selectedBorderColor: PySide6.QtGui.QColor | None = ..., borderWidth: float | None = ..., selected: bool | None = ..., upperSeries: PySide6.QtGraphs.QXYSeries | None = ..., lowerSeries: PySide6.QtGraphs.QXYSeries | None = ...) -> None: ...

    def borderColor(self, /) -> PySide6.QtGui.QColor: ...
    def borderWidth(self, /) -> float: ...
    def color(self, /) -> PySide6.QtGui.QColor: ...
    def isSelected(self, /) -> bool: ...
    def lowerSeries(self, /) -> PySide6.QtGraphs.QXYSeries: ...
    def selectedBorderColor(self, /) -> PySide6.QtGui.QColor: ...
    def selectedColor(self, /) -> PySide6.QtGui.QColor: ...
    def setBorderColor(self, newBorderColor: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setBorderWidth(self, newBorderWidth: float, /) -> None: ...
    def setColor(self, newColor: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setLowerSeries(self, newLowerSeries: PySide6.QtGraphs.QXYSeries, /) -> None: ...
    def setSelected(self, newSelected: bool, /) -> None: ...
    def setSelectedBorderColor(self, newSelectedBorderColor: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setSelectedColor(self, newColor: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setUpperSeries(self, newUpperSeries: PySide6.QtGraphs.QXYSeries, /) -> None: ...
    def type(self, /) -> PySide6.QtGraphs.QAbstractSeries.SeriesType: ...
    def upperSeries(self, /) -> PySide6.QtGraphs.QXYSeries: ...


class QBar3DSeries(PySide6.QtGraphs.QAbstract3DSeries):
    # columnAxisChanged(QCategory3DAxis*)
    columnAxisChanged: typing.ClassVar[Signal[
        [PySide6.QtGraphs.QCategory3DAxis], [], [], [], [], [], [], [],
        [PySide6.QtGraphs.QCategory3DAxis], [PySide6.QtGraphs.QCategory3DAxis], [PySide6.QtGraphs.QCategory3DAxis], [PySide6.QtGraphs.QCategory3DAxis], [PySide6.QtGraphs.QCategory3DAxis], [PySide6.QtGraphs.QCategory3DAxis], [PySide6.QtGraphs.QCategory3DAxis], [PySide6.QtGraphs.QCategory3DAxis]
    ]]
    # columnLabelsChanged()
    columnLabelsChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # customColumnLabelsChanged(QStringList)
    customColumnLabelsChanged: typing.ClassVar[Signal[
        [typing.List[str]], [], [], [], [], [], [], [],
        [typing.List[str]], [typing.List[str]], [typing.List[str]], [typing.List[str]], [typing.List[str]], [typing.List[str]], [typing.List[str]], [typing.List[str]]
    ]]
    # customRowLabelsChanged(QStringList)
    customRowLabelsChanged: typing.ClassVar[Signal[
        [typing.List[str]], [], [], [], [], [], [], [],
        [typing.List[str]], [typing.List[str]], [typing.List[str]], [typing.List[str]], [typing.List[str]], [typing.List[str]], [typing.List[str]], [typing.List[str]]
    ]]
    # dataArrayChanged(QBarDataArray)
    dataArrayChanged: typing.ClassVar[Signal[
        [collections.abc.Sequence[collections.abc.Sequence[QBarDataItem]]], [], [], [], [], [], [], [],
        [collections.abc.Sequence[collections.abc.Sequence[QBarDataItem]]], [collections.abc.Sequence[collections.abc.Sequence[QBarDataItem]]], [collections.abc.Sequence[collections.abc.Sequence[QBarDataItem]]], [collections.abc.Sequence[collections.abc.Sequence[QBarDataItem]]], [collections.abc.Sequence[collections.abc.Sequence[QBarDataItem]]], [collections.abc.Sequence[collections.abc.Sequence[QBarDataItem]]], [collections.abc.Sequence[collections.abc.Sequence[QBarDataItem]]], [collections.abc.Sequence[collections.abc.Sequence[QBarDataItem]]]
    ]]
    # dataProxyChanged(QBarDataProxy*)
    dataProxyChanged: typing.ClassVar[Signal[
        [PySide6.QtGraphs.QBarDataProxy], [], [], [], [], [], [], [],
        [PySide6.QtGraphs.QBarDataProxy], [PySide6.QtGraphs.QBarDataProxy], [PySide6.QtGraphs.QBarDataProxy], [PySide6.QtGraphs.QBarDataProxy], [PySide6.QtGraphs.QBarDataProxy], [PySide6.QtGraphs.QBarDataProxy], [PySide6.QtGraphs.QBarDataProxy], [PySide6.QtGraphs.QBarDataProxy]
    ]]
    # meshAngleChanged(float)
    meshAngleChanged: typing.ClassVar[Signal[
        [float], [], [], [], [], [], [], [],
        [float], [float], [float], [float], [float], [float], [float], [float]
    ]]
    # rowAxisChanged(QCategory3DAxis*)
    rowAxisChanged: typing.ClassVar[Signal[
        [PySide6.QtGraphs.QCategory3DAxis], [], [], [], [], [], [], [],
        [PySide6.QtGraphs.QCategory3DAxis], [PySide6.QtGraphs.QCategory3DAxis], [PySide6.QtGraphs.QCategory3DAxis], [PySide6.QtGraphs.QCategory3DAxis], [PySide6.QtGraphs.QCategory3DAxis], [PySide6.QtGraphs.QCategory3DAxis], [PySide6.QtGraphs.QCategory3DAxis], [PySide6.QtGraphs.QCategory3DAxis]
    ]]
    # rowColorsChanged(QList<QColor>)
    rowColorsChanged: typing.ClassVar[Signal[
        [collections.abc.Sequence[PySide6.QtGui.QColor]], [], [], [], [], [], [], [],
        [collections.abc.Sequence[PySide6.QtGui.QColor]], [collections.abc.Sequence[PySide6.QtGui.QColor]], [collections.abc.Sequence[PySide6.QtGui.QColor]], [collections.abc.Sequence[PySide6.QtGui.QColor]], [collections.abc.Sequence[PySide6.QtGui.QColor]], [collections.abc.Sequence[PySide6.QtGui.QColor]], [collections.abc.Sequence[PySide6.QtGui.QColor]], [collections.abc.Sequence[PySide6.QtGui.QColor]]
    ]]
    # rowLabelsChanged()
    rowLabelsChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # selectedBarChanged(QPoint)
    selectedBarChanged: typing.ClassVar[Signal[
        [PySide6.QtCore.QPoint], [], [], [], [], [], [], [],
        [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint]
    ]]
    # valueAxisChanged(QValue3DAxis*)
    valueAxisChanged: typing.ClassVar[Signal[
        [PySide6.QtGraphs.QValue3DAxis], [], [], [], [], [], [], [],
        [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis]
    ]]
    # valueColoringEnabledChanged(bool)
    valueColoringEnabledChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]

    @typing.overload
    def __init__(self, dataProxy: PySide6.QtGraphs.QBarDataProxy, /, parent: PySide6.QtCore.QObject | None = ..., *, selectedBar: PySide6.QtCore.QPoint | None = ..., meshAngle: float | None = ..., rowColors: collections.abc.Sequence[PySide6.QtGui.QColor] | None = ..., rowLabels: collections.abc.Sequence[str] | None = ..., columnLabels: collections.abc.Sequence[str] | None = ..., customRowLabels: collections.abc.Sequence[str] | None = ..., customColumnLabels: collections.abc.Sequence[str] | None = ..., dataArray: collections.abc.Sequence[collections.abc.Sequence[PySide6.QtGraphs.QBarDataItem]] | None = ..., valueColoringEnabled: bool | None = ..., rowAxis: PySide6.QtGraphs.QCategory3DAxis | None = ..., valueAxis: PySide6.QtGraphs.QValue3DAxis | None = ..., columnAxis: PySide6.QtGraphs.QCategory3DAxis | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., *, dataProxy: PySide6.QtGraphs.QBarDataProxy | None = ..., selectedBar: PySide6.QtCore.QPoint | None = ..., meshAngle: float | None = ..., rowColors: collections.abc.Sequence[PySide6.QtGui.QColor] | None = ..., rowLabels: collections.abc.Sequence[str] | None = ..., columnLabels: collections.abc.Sequence[str] | None = ..., customRowLabels: collections.abc.Sequence[str] | None = ..., customColumnLabels: collections.abc.Sequence[str] | None = ..., dataArray: collections.abc.Sequence[collections.abc.Sequence[PySide6.QtGraphs.QBarDataItem]] | None = ..., valueColoringEnabled: bool | None = ..., rowAxis: PySide6.QtGraphs.QCategory3DAxis | None = ..., valueAxis: PySide6.QtGraphs.QValue3DAxis | None = ..., columnAxis: PySide6.QtGraphs.QCategory3DAxis | None = ...) -> None: ...

    def clearArray(self, /) -> None: ...
    def clearRow(self, rowIndex: int, /) -> None: ...
    def columnAxis(self, /) -> PySide6.QtGraphs.QCategory3DAxis: ...
    def columnLabels(self, /) -> typing.List[str]: ...
    def customColumnLabels(self, /) -> typing.List[str]: ...
    def customRowLabels(self, /) -> typing.List[str]: ...
    def dataArray(self, /) -> typing.List[typing.List[PySide6.QtGraphs.QBarDataItem]]: ...
    def dataProxy(self, /) -> PySide6.QtGraphs.QBarDataProxy: ...
    @staticmethod
    def invalidSelectionPosition() -> PySide6.QtCore.QPoint: ...
    def isValueColoringEnabled(self, /) -> bool: ...
    def meshAngle(self, /) -> float: ...
    def resetColumnAxis(self, /) -> None: ...
    def resetRowAxis(self, /) -> None: ...
    def resetValueAxis(self, /) -> None: ...
    def rowAxis(self, /) -> PySide6.QtGraphs.QCategory3DAxis: ...
    def rowColors(self, /) -> typing.List[PySide6.QtGui.QColor]: ...
    def rowLabels(self, /) -> typing.List[str]: ...
    def selectedBar(self, /) -> PySide6.QtCore.QPoint: ...
    def setColumnAxis(self, axis: PySide6.QtGraphs.QCategory3DAxis, /) -> None: ...
    def setColumnLabels(self, labels: collections.abc.Sequence[str], /) -> None: ...
    def setCustomColumnLabels(self, labels: collections.abc.Sequence[str], /) -> None: ...
    def setCustomRowLabels(self, labels: collections.abc.Sequence[str], /) -> None: ...
    def setDataArray(self, newDataArray: collections.abc.Sequence[collections.abc.Sequence[PySide6.QtGraphs.QBarDataItem]], /) -> None: ...
    def setDataProxy(self, proxy: PySide6.QtGraphs.QBarDataProxy, /) -> None: ...
    def setMeshAngle(self, angle: float, /) -> None: ...
    def setRowAxis(self, axis: PySide6.QtGraphs.QCategory3DAxis, /) -> None: ...
    def setRowColors(self, colors: collections.abc.Sequence[PySide6.QtGui.QColor], /) -> None: ...
    def setRowLabels(self, labels: collections.abc.Sequence[str], /) -> None: ...
    def setSelectedBar(self, position: PySide6.QtCore.QPoint, /) -> None: ...
    def setValueAxis(self, axis: PySide6.QtGraphs.QValue3DAxis, /) -> None: ...
    def setValueColoringEnabled(self, enabled: bool, /) -> None: ...
    def valueAxis(self, /) -> PySide6.QtGraphs.QValue3DAxis: ...


class QBarCategoryAxis(PySide6.QtGraphs.QAbstractAxis):
    # categoriesChanged()
    categoriesChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # categoryRangeChanged(QString,QString)
    categoryRangeChanged: typing.ClassVar[Signal[
        [str, str], [str], [], [], [], [], [], [],
        [str, str], [str, str], [str, str], [str, str], [str, str], [str, str], [str, str], [str, str]
    ]]
    # countChanged()
    countChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # labelPositionChanged(LabelPosition)
    labelPositionChanged: typing.ClassVar[Signal[
        [LabelPosition], [], [], [], [], [], [], [],
        [LabelPosition], [LabelPosition], [LabelPosition], [LabelPosition], [LabelPosition], [LabelPosition], [LabelPosition], [LabelPosition]
    ]]
    # maxChanged(QString)
    maxChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # minChanged(QString)
    minChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]

    class LabelPosition(enum.Enum):
        Center                    = 0x0
        OnValue                   = 0x1

    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., *, categories: collections.abc.Sequence[str] | None = ..., min: str | None = ..., max: str | None = ..., count: int | None = ..., labelPosition: PySide6.QtGraphs.QBarCategoryAxis.LabelPosition | None = ...) -> None: ...

    @typing.overload
    def append(self, category: str, /) -> None: ...
    @typing.overload
    def append(self, categories: collections.abc.Sequence[str], /) -> None: ...
    def at(self, index: int, /) -> str: ...
    def categories(self, /) -> typing.List[str]: ...
    def clear(self, /) -> None: ...
    def count(self, /) -> int: ...
    def insert(self, index: int, category: str, /) -> None: ...
    def labelPosition(self, /) -> PySide6.QtGraphs.QBarCategoryAxis.LabelPosition: ...
    def max(self, /) -> str: ...
    def min(self, /) -> str: ...
    @typing.overload
    def remove(self, category: str, /) -> None: ...
    @typing.overload
    def remove(self, index: int, /) -> None: ...
    def replace(self, oldCategory: str, newCategory: str, /) -> None: ...
    def setCategories(self, categories: collections.abc.Sequence[str], /) -> None: ...
    def setLabelPosition(self, position: PySide6.QtGraphs.QBarCategoryAxis.LabelPosition, /) -> None: ...
    def setMax(self, maxCategory: str, /) -> None: ...
    def setMin(self, minCategory: str, /) -> None: ...
    def setRange(self, minCategory: str, maxCategory: str, /) -> None: ...
    def type(self, /) -> PySide6.QtGraphs.QAbstractAxis.AxisType: ...


class QBarDataItem(Shiboken.Object):
    @typing.overload
    def __init__(self, /) -> None: ...
    @typing.overload
    def __init__(self, QBarDataItem: PySide6.QtGraphs.QBarDataItem, /) -> None: ...
    @typing.overload
    def __init__(self, value: float, /) -> None: ...
    @typing.overload
    def __init__(self, value: float, angle: float, /) -> None: ...

    def __copy__(self, /) -> typing.Self: ...
    def rotation(self, /) -> float: ...
    def setRotation(self, angle: float, /) -> None: ...
    def setValue(self, val: float, /) -> None: ...
    def value(self, /) -> float: ...


class QBarDataProxy(PySide6.QtGraphs.QAbstractDataProxy):
    # arrayReset()
    arrayReset: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # colCountChanged(qsizetype)
    colCountChanged: typing.ClassVar[Signal[
        [int], [], [], [], [], [], [], [],
        [int], [int], [int], [int], [int], [int], [int], [int]
    ]]
    # itemChanged(qsizetype,qsizetype)
    itemChanged: typing.ClassVar[Signal[
        [int, int], [int], [], [], [], [], [], [],
        [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int]
    ]]
    # rowCountChanged(qsizetype)
    rowCountChanged: typing.ClassVar[Signal[
        [int], [], [], [], [], [], [], [],
        [int], [int], [int], [int], [int], [int], [int], [int]
    ]]
    # rowsAdded(qsizetype,qsizetype)
    rowsAdded: typing.ClassVar[Signal[
        [int, int], [int], [], [], [], [], [], [],
        [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int]
    ]]
    # rowsChanged(qsizetype,qsizetype)
    rowsChanged: typing.ClassVar[Signal[
        [int, int], [int], [], [], [], [], [], [],
        [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int]
    ]]
    # rowsInserted(qsizetype,qsizetype)
    rowsInserted: typing.ClassVar[Signal[
        [int, int], [int], [], [], [], [], [], [],
        [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int]
    ]]
    # rowsRemoved(qsizetype,qsizetype)
    rowsRemoved: typing.ClassVar[Signal[
        [int, int], [int], [], [], [], [], [], [],
        [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int]
    ]]
    # seriesChanged(QBar3DSeries*)
    seriesChanged: typing.ClassVar[Signal[
        [PySide6.QtGraphs.QBar3DSeries], [], [], [], [], [], [], [],
        [PySide6.QtGraphs.QBar3DSeries], [PySide6.QtGraphs.QBar3DSeries], [PySide6.QtGraphs.QBar3DSeries], [PySide6.QtGraphs.QBar3DSeries], [PySide6.QtGraphs.QBar3DSeries], [PySide6.QtGraphs.QBar3DSeries], [PySide6.QtGraphs.QBar3DSeries], [PySide6.QtGraphs.QBar3DSeries]
    ]]

    class RemoveLabels(enum.Enum):
        No                        = 0x0
        Yes                       = 0x1

    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., *, rowCount: int | None = ..., colCount: int | None = ..., series: PySide6.QtGraphs.QBar3DSeries | None = ...) -> None: ...

    @typing.overload
    def addRow(self, row: collections.abc.Sequence[PySide6.QtGraphs.QBarDataItem], /) -> int: ...
    @typing.overload
    def addRow(self, row: collections.abc.Sequence[PySide6.QtGraphs.QBarDataItem], label: str, /) -> int: ...
    @typing.overload
    def addRows(self, rows: collections.abc.Sequence[collections.abc.Sequence[PySide6.QtGraphs.QBarDataItem]], /) -> int: ...
    @typing.overload
    def addRows(self, rows: collections.abc.Sequence[collections.abc.Sequence[PySide6.QtGraphs.QBarDataItem]], labels: collections.abc.Sequence[str], /) -> int: ...
    def colCount(self, /) -> int: ...
    @typing.overload
    def insertRow(self, rowIndex: int, row: collections.abc.Sequence[PySide6.QtGraphs.QBarDataItem], /) -> None: ...
    @typing.overload
    def insertRow(self, rowIndex: int, row: collections.abc.Sequence[PySide6.QtGraphs.QBarDataItem], label: str, /) -> None: ...
    @typing.overload
    def insertRows(self, rowIndex: int, rows: collections.abc.Sequence[collections.abc.Sequence[PySide6.QtGraphs.QBarDataItem]], /) -> None: ...
    @typing.overload
    def insertRows(self, rowIndex: int, rows: collections.abc.Sequence[collections.abc.Sequence[PySide6.QtGraphs.QBarDataItem]], labels: collections.abc.Sequence[str], /) -> None: ...
    @typing.overload
    def itemAt(self, position: PySide6.QtCore.QPoint, /) -> PySide6.QtGraphs.QBarDataItem: ...
    @typing.overload
    def itemAt(self, rowIndex: int, columnIndex: int, /) -> PySide6.QtGraphs.QBarDataItem: ...
    def removeRows(self, rowIndex: int, removeCount: int, /, removeLabels: PySide6.QtGraphs.QBarDataProxy.RemoveLabels = ...) -> None: ...
    @typing.overload
    def resetArray(self, /) -> None: ...
    @typing.overload
    def resetArray(self, newArray: collections.abc.Sequence[collections.abc.Sequence[PySide6.QtGraphs.QBarDataItem]], /) -> None: ...
    @typing.overload
    def resetArray(self, newArray: collections.abc.Sequence[collections.abc.Sequence[PySide6.QtGraphs.QBarDataItem]], rowLabels: collections.abc.Sequence[str], columnLabels: collections.abc.Sequence[str], /) -> None: ...
    def rowAt(self, rowIndex: int, /) -> typing.List[PySide6.QtGraphs.QBarDataItem]: ...
    def rowCount(self, /) -> int: ...
    def series(self, /) -> PySide6.QtGraphs.QBar3DSeries: ...
    @typing.overload
    def setItem(self, position: PySide6.QtCore.QPoint, item: PySide6.QtGraphs.QBarDataItem, /) -> None: ...
    @typing.overload
    def setItem(self, rowIndex: int, columnIndex: int, item: PySide6.QtGraphs.QBarDataItem, /) -> None: ...
    @typing.overload
    def setRow(self, rowIndex: int, row: collections.abc.Sequence[PySide6.QtGraphs.QBarDataItem], /) -> None: ...
    @typing.overload
    def setRow(self, rowIndex: int, row: collections.abc.Sequence[PySide6.QtGraphs.QBarDataItem], label: str, /) -> None: ...
    @typing.overload
    def setRows(self, rowIndex: int, rows: collections.abc.Sequence[collections.abc.Sequence[PySide6.QtGraphs.QBarDataItem]], /) -> None: ...
    @typing.overload
    def setRows(self, rowIndex: int, rows: collections.abc.Sequence[collections.abc.Sequence[PySide6.QtGraphs.QBarDataItem]], labels: collections.abc.Sequence[str], /) -> None: ...


class QBarModelMapper(PySide6.QtCore.QObject):
    # countChanged()
    countChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # firstBarSetSectionChanged()
    firstBarSetSectionChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # firstChanged()
    firstChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # lastBarSetSectionChanged()
    lastBarSetSectionChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # modelChanged()
    modelChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # orientationChanged()
    orientationChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # seriesChanged()
    seriesChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]

    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., *, series: PySide6.QtGraphs.QBarSeries | None = ..., model: PySide6.QtCore.QAbstractItemModel | None = ..., firstBarSetSection: int | None = ..., lastBarSetSection: int | None = ..., first: int | None = ..., count: int | None = ..., orientation: PySide6.QtCore.Qt.Orientation | None = ...) -> None: ...

    def count(self, /) -> int: ...
    def first(self, /) -> int: ...
    def firstBarSetSection(self, /) -> int: ...
    def lastBarSetSection(self, /) -> int: ...
    def model(self, /) -> PySide6.QtCore.QAbstractItemModel: ...
    def orientation(self, /) -> PySide6.QtCore.Qt.Orientation: ...
    def series(self, /) -> PySide6.QtGraphs.QBarSeries: ...
    def setCount(self, newCount: int, /) -> None: ...
    def setFirst(self, newFirst: int, /) -> None: ...
    def setFirstBarSetSection(self, newFirstBarSetSection: int, /) -> None: ...
    def setLastBarSetSection(self, newLastBarSetSection: int, /) -> None: ...
    def setModel(self, model: PySide6.QtCore.QAbstractItemModel, /) -> None: ...
    def setOrientation(self, orientation: PySide6.QtCore.Qt.Orientation, /) -> None: ...
    def setSeries(self, series: PySide6.QtGraphs.QBarSeries, /) -> None: ...


class QBarSeries(PySide6.QtGraphs.QAbstractSeries):
    # barDelegateChanged()
    barDelegateChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # barSetsChanged()
    barSetsChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # barWidthChanged()
    barWidthChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # barsTypeChanged(QBarSeries::BarsType)
    barsTypeChanged: typing.ClassVar[Signal[
        [PySide6.QtGraphs.QBarSeries.BarsType], [], [], [], [], [], [], [],
        [PySide6.QtGraphs.QBarSeries.BarsType], [PySide6.QtGraphs.QBarSeries.BarsType], [PySide6.QtGraphs.QBarSeries.BarsType], [PySide6.QtGraphs.QBarSeries.BarsType], [PySide6.QtGraphs.QBarSeries.BarsType], [PySide6.QtGraphs.QBarSeries.BarsType], [PySide6.QtGraphs.QBarSeries.BarsType], [PySide6.QtGraphs.QBarSeries.BarsType]
    ]]
    # barsetsAdded(QList<QBarSet*>)
    barsetsAdded: typing.ClassVar[Signal[
        [collections.abc.Sequence[PySide6.QtGraphs.QBarSet]], [], [], [], [], [], [], [],
        [collections.abc.Sequence[PySide6.QtGraphs.QBarSet]], [collections.abc.Sequence[PySide6.QtGraphs.QBarSet]], [collections.abc.Sequence[PySide6.QtGraphs.QBarSet]], [collections.abc.Sequence[PySide6.QtGraphs.QBarSet]], [collections.abc.Sequence[PySide6.QtGraphs.QBarSet]], [collections.abc.Sequence[PySide6.QtGraphs.QBarSet]], [collections.abc.Sequence[PySide6.QtGraphs.QBarSet]], [collections.abc.Sequence[PySide6.QtGraphs.QBarSet]]
    ]]
    # barsetsRemoved(QList<QBarSet*>)
    barsetsRemoved: typing.ClassVar[Signal[
        [collections.abc.Sequence[PySide6.QtGraphs.QBarSet]], [], [], [], [], [], [], [],
        [collections.abc.Sequence[PySide6.QtGraphs.QBarSet]], [collections.abc.Sequence[PySide6.QtGraphs.QBarSet]], [collections.abc.Sequence[PySide6.QtGraphs.QBarSet]], [collections.abc.Sequence[PySide6.QtGraphs.QBarSet]], [collections.abc.Sequence[PySide6.QtGraphs.QBarSet]], [collections.abc.Sequence[PySide6.QtGraphs.QBarSet]], [collections.abc.Sequence[PySide6.QtGraphs.QBarSet]], [collections.abc.Sequence[PySide6.QtGraphs.QBarSet]]
    ]]
    # barsetsReplaced(QList<QBarSet*>)
    barsetsReplaced: typing.ClassVar[Signal[
        [collections.abc.Sequence[PySide6.QtGraphs.QBarSet]], [], [], [], [], [], [], [],
        [collections.abc.Sequence[PySide6.QtGraphs.QBarSet]], [collections.abc.Sequence[PySide6.QtGraphs.QBarSet]], [collections.abc.Sequence[PySide6.QtGraphs.QBarSet]], [collections.abc.Sequence[PySide6.QtGraphs.QBarSet]], [collections.abc.Sequence[PySide6.QtGraphs.QBarSet]], [collections.abc.Sequence[PySide6.QtGraphs.QBarSet]], [collections.abc.Sequence[PySide6.QtGraphs.QBarSet]], [collections.abc.Sequence[PySide6.QtGraphs.QBarSet]]
    ]]
    # borderColorsChanged()
    borderColorsChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # clicked(qsizetype,QBarSet*)
    clicked: typing.ClassVar[Signal[
        [int, PySide6.QtGraphs.QBarSet], [int], [], [], [], [], [], [],
        [int, PySide6.QtGraphs.QBarSet], [int, PySide6.QtGraphs.QBarSet], [int, PySide6.QtGraphs.QBarSet], [int, PySide6.QtGraphs.QBarSet], [int, PySide6.QtGraphs.QBarSet], [int, PySide6.QtGraphs.QBarSet], [int, PySide6.QtGraphs.QBarSet], [int, PySide6.QtGraphs.QBarSet]
    ]]
    # countChanged()
    countChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # doubleClicked(qsizetype,QBarSet*)
    doubleClicked: typing.ClassVar[Signal[
        [int, PySide6.QtGraphs.QBarSet], [int], [], [], [], [], [], [],
        [int, PySide6.QtGraphs.QBarSet], [int, PySide6.QtGraphs.QBarSet], [int, PySide6.QtGraphs.QBarSet], [int, PySide6.QtGraphs.QBarSet], [int, PySide6.QtGraphs.QBarSet], [int, PySide6.QtGraphs.QBarSet], [int, PySide6.QtGraphs.QBarSet], [int, PySide6.QtGraphs.QBarSet]
    ]]
    # labelsAngleChanged(double)
    labelsAngleChanged: typing.ClassVar[Signal[
        [float], [], [], [], [], [], [], [],
        [float], [float], [float], [float], [float], [float], [float], [float]
    ]]
    # labelsFormatChanged(QString)
    labelsFormatChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # labelsMarginChanged(double)
    labelsMarginChanged: typing.ClassVar[Signal[
        [float], [], [], [], [], [], [], [],
        [float], [float], [float], [float], [float], [float], [float], [float]
    ]]
    # labelsPositionChanged(QBarSeries::LabelsPosition)
    labelsPositionChanged: typing.ClassVar[Signal[
        [PySide6.QtGraphs.QBarSeries.LabelsPosition], [], [], [], [], [], [], [],
        [PySide6.QtGraphs.QBarSeries.LabelsPosition], [PySide6.QtGraphs.QBarSeries.LabelsPosition], [PySide6.QtGraphs.QBarSeries.LabelsPosition], [PySide6.QtGraphs.QBarSeries.LabelsPosition], [PySide6.QtGraphs.QBarSeries.LabelsPosition], [PySide6.QtGraphs.QBarSeries.LabelsPosition], [PySide6.QtGraphs.QBarSeries.LabelsPosition], [PySide6.QtGraphs.QBarSeries.LabelsPosition]
    ]]
    # labelsPrecisionChanged(int)
    labelsPrecisionChanged: typing.ClassVar[Signal[
        [int], [], [], [], [], [], [], [],
        [int], [int], [int], [int], [int], [int], [int], [int]
    ]]
    # labelsVisibleChanged(bool)
    labelsVisibleChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # pressed(qsizetype,QBarSet*)
    pressed: typing.ClassVar[Signal[
        [int, PySide6.QtGraphs.QBarSet], [int], [], [], [], [], [], [],
        [int, PySide6.QtGraphs.QBarSet], [int, PySide6.QtGraphs.QBarSet], [int, PySide6.QtGraphs.QBarSet], [int, PySide6.QtGraphs.QBarSet], [int, PySide6.QtGraphs.QBarSet], [int, PySide6.QtGraphs.QBarSet], [int, PySide6.QtGraphs.QBarSet], [int, PySide6.QtGraphs.QBarSet]
    ]]
    # released(qsizetype,QBarSet*)
    released: typing.ClassVar[Signal[
        [int, PySide6.QtGraphs.QBarSet], [int], [], [], [], [], [], [],
        [int, PySide6.QtGraphs.QBarSet], [int, PySide6.QtGraphs.QBarSet], [int, PySide6.QtGraphs.QBarSet], [int, PySide6.QtGraphs.QBarSet], [int, PySide6.QtGraphs.QBarSet], [int, PySide6.QtGraphs.QBarSet], [int, PySide6.QtGraphs.QBarSet], [int, PySide6.QtGraphs.QBarSet]
    ]]
    # seriesColorsChanged()
    seriesColorsChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # setValueAdded(qsizetype,qsizetype,QBarSet*)
    setValueAdded: typing.ClassVar[Signal[
        [int, int, PySide6.QtGraphs.QBarSet], [int, int], [int], [], [], [], [], [],
        [int, int, PySide6.QtGraphs.QBarSet], [int, int, PySide6.QtGraphs.QBarSet], [int, int, PySide6.QtGraphs.QBarSet], [int, int, PySide6.QtGraphs.QBarSet], [int, int, PySide6.QtGraphs.QBarSet], [int, int, PySide6.QtGraphs.QBarSet], [int, int, PySide6.QtGraphs.QBarSet], [int, int, PySide6.QtGraphs.QBarSet]
    ]]
    # setValueChanged(qsizetype,QBarSet*)
    setValueChanged: typing.ClassVar[Signal[
        [int, PySide6.QtGraphs.QBarSet], [int], [], [], [], [], [], [],
        [int, PySide6.QtGraphs.QBarSet], [int, PySide6.QtGraphs.QBarSet], [int, PySide6.QtGraphs.QBarSet], [int, PySide6.QtGraphs.QBarSet], [int, PySide6.QtGraphs.QBarSet], [int, PySide6.QtGraphs.QBarSet], [int, PySide6.QtGraphs.QBarSet], [int, PySide6.QtGraphs.QBarSet]
    ]]
    # setValueRemoved(qsizetype,qsizetype,QBarSet*)
    setValueRemoved: typing.ClassVar[Signal[
        [int, int, PySide6.QtGraphs.QBarSet], [int, int], [int], [], [], [], [], [],
        [int, int, PySide6.QtGraphs.QBarSet], [int, int, PySide6.QtGraphs.QBarSet], [int, int, PySide6.QtGraphs.QBarSet], [int, int, PySide6.QtGraphs.QBarSet], [int, int, PySide6.QtGraphs.QBarSet], [int, int, PySide6.QtGraphs.QBarSet], [int, int, PySide6.QtGraphs.QBarSet], [int, int, PySide6.QtGraphs.QBarSet]
    ]]
    # updatedBars()
    updatedBars: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]

    class BarsType(enum.Enum):
        Groups                    = 0x0
        Stacked                   = 0x1
        StackedPercent            = 0x2

    class LabelsPosition(enum.Enum):
        Center                    = 0x0
        InsideEnd                 = 0x1
        InsideBase                = 0x2
        OutsideEnd                = 0x3

    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., *, seriesColors: collections.abc.Sequence[PySide6.QtGui.QColor] | None = ..., borderColors: collections.abc.Sequence[PySide6.QtGui.QColor] | None = ..., barsType: PySide6.QtGraphs.QBarSeries.BarsType | None = ..., barWidth: float | None = ..., count: int | None = ..., labelsVisible: bool | None = ..., labelsFormat: str | None = ..., labelsPosition: PySide6.QtGraphs.QBarSeries.LabelsPosition | None = ..., labelsMargin: float | None = ..., labelsAngle: float | None = ..., labelsPrecision: int | None = ..., barDelegate: PySide6.QtQml.QQmlComponent | None = ..., barSets: collections.abc.Sequence[PySide6.QtGraphs.QBarSet] | None = ...) -> None: ...

    @typing.overload
    def append(self, set: PySide6.QtGraphs.QBarSet, /) -> bool: ...
    @typing.overload
    def append(self, sets: collections.abc.Sequence[PySide6.QtGraphs.QBarSet], /) -> bool: ...
    def at(self, index: int, /) -> PySide6.QtGraphs.QBarSet: ...
    def barDelegate(self, /) -> PySide6.QtQml.QQmlComponent: ...
    def barSets(self, /) -> typing.List[PySide6.QtGraphs.QBarSet]: ...
    def barWidth(self, /) -> float: ...
    def barsType(self, /) -> PySide6.QtGraphs.QBarSeries.BarsType: ...
    def borderColors(self, /) -> typing.List[PySide6.QtGui.QColor]: ...
    def clear(self, /) -> None: ...
    def componentComplete(self, /) -> None: ...
    def count(self, /) -> int: ...
    def deselectAll(self, /) -> None: ...
    def find(self, set: PySide6.QtGraphs.QBarSet, /) -> int: ...
    def insert(self, index: int, set: PySide6.QtGraphs.QBarSet, /) -> bool: ...
    def labelsAngle(self, /) -> float: ...
    def labelsFormat(self, /) -> str: ...
    def labelsMargin(self, /) -> float: ...
    def labelsPosition(self, /) -> PySide6.QtGraphs.QBarSeries.LabelsPosition: ...
    def labelsPrecision(self, /) -> int: ...
    def labelsVisible(self, /) -> bool: ...
    @typing.overload
    def remove(self, set: PySide6.QtGraphs.QBarSet, /) -> bool: ...
    @typing.overload
    def remove(self, index: int, /) -> bool: ...
    def removeMultiple(self, index: int, count: int, /) -> None: ...
    @typing.overload
    def replace(self, oldValue: PySide6.QtGraphs.QBarSet, newValue: PySide6.QtGraphs.QBarSet, /) -> bool: ...
    @typing.overload
    def replace(self, sets: collections.abc.Sequence[PySide6.QtGraphs.QBarSet], /) -> bool: ...
    @typing.overload
    def replace(self, index: int, set: PySide6.QtGraphs.QBarSet, /) -> None: ...
    def selectAll(self, /) -> None: ...
    def seriesColors(self, /) -> typing.List[PySide6.QtGui.QColor]: ...
    def setBarDelegate(self, newBarDelegate: PySide6.QtQml.QQmlComponent, /) -> None: ...
    def setBarWidth(self, width: float, /) -> None: ...
    def setBarsType(self, type: PySide6.QtGraphs.QBarSeries.BarsType, /) -> None: ...
    def setBorderColors(self, newBorderColors: collections.abc.Sequence[PySide6.QtGui.QColor], /) -> None: ...
    def setLabelsAngle(self, angle: float, /) -> None: ...
    def setLabelsFormat(self, format: str, /) -> None: ...
    def setLabelsMargin(self, margin: float, /) -> None: ...
    def setLabelsPosition(self, position: PySide6.QtGraphs.QBarSeries.LabelsPosition, /) -> None: ...
    def setLabelsPrecision(self, precision: int, /) -> None: ...
    def setLabelsVisible(self, /, visible: bool = ...) -> None: ...
    def setSeriesColors(self, newSeriesColors: collections.abc.Sequence[PySide6.QtGui.QColor], /) -> None: ...
    def take(self, set: PySide6.QtGraphs.QBarSet, /) -> bool: ...
    def type(self, /) -> PySide6.QtGraphs.QAbstractSeries.SeriesType: ...


class QBarSet(PySide6.QtCore.QObject):
    # borderColorChanged(QColor)
    borderColorChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QColor], [], [], [], [], [], [], [],
        [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor]
    ]]
    # borderWidthChanged(double)
    borderWidthChanged: typing.ClassVar[Signal[
        [float], [], [], [], [], [], [], [],
        [float], [float], [float], [float], [float], [float], [float], [float]
    ]]
    # colorChanged(QColor)
    colorChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QColor], [], [], [], [], [], [], [],
        [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor]
    ]]
    # countChanged()
    countChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # labelChanged()
    labelChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # labelColorChanged(QColor)
    labelColorChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QColor], [], [], [], [], [], [], [],
        [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor]
    ]]
    # selectedBarsChanged(QList<qsizetype>)
    selectedBarsChanged: typing.ClassVar[Signal[
        [collections.abc.Sequence[int]], [], [], [], [], [], [], [],
        [collections.abc.Sequence[int]], [collections.abc.Sequence[int]], [collections.abc.Sequence[int]], [collections.abc.Sequence[int]], [collections.abc.Sequence[int]], [collections.abc.Sequence[int]], [collections.abc.Sequence[int]], [collections.abc.Sequence[int]]
    ]]
    # selectedColorChanged(QColor)
    selectedColorChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QColor], [], [], [], [], [], [], [],
        [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor]
    ]]
    # update()
    update: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # updatedBars()
    updatedBars: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # valueAdded(qsizetype,qsizetype)
    valueAdded: typing.ClassVar[Signal[
        [int, int], [int], [], [], [], [], [], [],
        [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int]
    ]]
    # valueChanged(qsizetype)
    valueChanged: typing.ClassVar[Signal[
        [int], [], [], [], [], [], [], [],
        [int], [int], [int], [int], [int], [int], [int], [int]
    ]]
    # valueRemoved(qsizetype,qsizetype)
    valueRemoved: typing.ClassVar[Signal[
        [int, int], [int], [], [], [], [], [], [],
        [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int]
    ]]
    # valuesAdded(qsizetype,qsizetype)
    valuesAdded: typing.ClassVar[Signal[
        [int, int], [int], [], [], [], [], [], [],
        [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int]
    ]]
    # valuesChanged()
    valuesChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # valuesRemoved(qsizetype,qsizetype)
    valuesRemoved: typing.ClassVar[Signal[
        [int, int], [int], [], [], [], [], [], [],
        [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int]
    ]]

    @typing.overload
    def __init__(self, label: str, /, parent: PySide6.QtCore.QObject | None = ..., *, color: PySide6.QtGui.QColor | None = ..., selectedColor: PySide6.QtGui.QColor | None = ..., borderColor: PySide6.QtGui.QColor | None = ..., labelColor: PySide6.QtGui.QColor | None = ..., values: collections.abc.Sequence[typing.Any] | None = ..., borderWidth: float | None = ..., count: int | None = ..., selectedBars: collections.abc.Sequence[int] | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., *, label: str | None = ..., color: PySide6.QtGui.QColor | None = ..., selectedColor: PySide6.QtGui.QColor | None = ..., borderColor: PySide6.QtGui.QColor | None = ..., labelColor: PySide6.QtGui.QColor | None = ..., values: collections.abc.Sequence[typing.Any] | None = ..., borderWidth: float | None = ..., count: int | None = ..., selectedBars: collections.abc.Sequence[int] | None = ...) -> None: ...

    def __lshift__(self, value: float, /) -> PySide6.QtGraphs.QBarSet: ...
    @typing.overload
    def append(self, values: collections.abc.Sequence[float], /) -> None: ...
    @typing.overload
    def append(self, value: float, /) -> None: ...
    def at(self, index: int, /) -> float: ...
    def borderColor(self, /) -> PySide6.QtGui.QColor: ...
    def borderWidth(self, /) -> float: ...
    def clear(self, /) -> None: ...
    def color(self, /) -> PySide6.QtGui.QColor: ...
    def count(self, /) -> int: ...
    def deselectAllBars(self, /) -> None: ...
    def deselectBar(self, index: int, /) -> None: ...
    def deselectBars(self, indexes: collections.abc.Sequence[int], /) -> None: ...
    def insert(self, index: int, value: float, /) -> None: ...
    def isBarSelected(self, index: int, /) -> bool: ...
    def label(self, /) -> str: ...
    def labelColor(self, /) -> PySide6.QtGui.QColor: ...
    def remove(self, index: int, /, count: int = ...) -> None: ...
    def replace(self, index: int, value: float, /) -> None: ...
    def selectAllBars(self, /) -> None: ...
    def selectBar(self, index: int, /) -> None: ...
    def selectBars(self, indexes: collections.abc.Sequence[int], /) -> None: ...
    def selectedBars(self, /) -> typing.List[int]: ...
    def selectedColor(self, /) -> PySide6.QtGui.QColor: ...
    def setBarSelected(self, index: int, selected: bool, /) -> None: ...
    def setBorderColor(self, color: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setBorderWidth(self, borderWidth: float, /) -> None: ...
    def setColor(self, color: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setLabel(self, label: str, /) -> None: ...
    def setLabelColor(self, color: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setSelectedColor(self, color: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setValues(self, values: collections.abc.Sequence[typing.Any], /) -> None: ...
    def sum(self, /) -> float: ...
    def toggleSelection(self, indexes: collections.abc.Sequence[int], /) -> None: ...
    def values(self, /) -> typing.List[typing.Any]: ...


class QCategory3DAxis(PySide6.QtGraphs.QAbstract3DAxis):
    # columnLabelsChanged()
    columnLabelsChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # rowLabelsChanged()
    rowLabelsChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]

    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., *, labels: collections.abc.Sequence[str] | None = ...) -> None: ...

    def labels(self, /) -> typing.List[str]: ...
    def setLabels(self, labels: collections.abc.Sequence[str], /) -> None: ...


class QCustom3DItem(PySide6.QtCore.QObject):
    # meshFileChanged(QString)
    meshFileChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # needUpdate()
    needUpdate: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # positionAbsoluteChanged(bool)
    positionAbsoluteChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # positionChanged(QVector3D)
    positionChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QVector3D], [], [], [], [], [], [], [],
        [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D]
    ]]
    # rotationAbsoluteChanged(bool)
    rotationAbsoluteChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # rotationChanged(QQuaternion)
    rotationChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QQuaternion], [], [], [], [], [], [], [],
        [PySide6.QtGui.QQuaternion], [PySide6.QtGui.QQuaternion], [PySide6.QtGui.QQuaternion], [PySide6.QtGui.QQuaternion], [PySide6.QtGui.QQuaternion], [PySide6.QtGui.QQuaternion], [PySide6.QtGui.QQuaternion], [PySide6.QtGui.QQuaternion]
    ]]
    # scalingAbsoluteChanged(bool)
    scalingAbsoluteChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # scalingChanged(QVector3D)
    scalingChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QVector3D], [], [], [], [], [], [], [],
        [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D]
    ]]
    # shadowCastingChanged(bool)
    shadowCastingChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # textureFileChanged(QString)
    textureFileChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # visibleChanged(bool)
    visibleChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]

    @typing.overload
    def __init__(self, meshFile: str, position: PySide6.QtGui.QVector3D, scaling: PySide6.QtGui.QVector3D, rotation: PySide6.QtGui.QQuaternion, texture: PySide6.QtGui.QImage, /, parent: PySide6.QtCore.QObject | None = ..., *, textureFile: str | None = ..., positionAbsolute: bool | None = ..., visible: bool | None = ..., shadowCasting: bool | None = ..., scalingAbsolute: bool | None = ..., rotationAbsolute: bool | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., *, meshFile: str | None = ..., textureFile: str | None = ..., position: PySide6.QtGui.QVector3D | None = ..., positionAbsolute: bool | None = ..., scaling: PySide6.QtGui.QVector3D | None = ..., rotation: PySide6.QtGui.QQuaternion | None = ..., visible: bool | None = ..., shadowCasting: bool | None = ..., scalingAbsolute: bool | None = ..., rotationAbsolute: bool | None = ...) -> None: ...

    def isPositionAbsolute(self, /) -> bool: ...
    def isRotationAbsolute(self, /) -> bool: ...
    def isScalingAbsolute(self, /) -> bool: ...
    def isShadowCasting(self, /) -> bool: ...
    def isVisible(self, /) -> bool: ...
    def meshFile(self, /) -> str: ...
    def position(self, /) -> PySide6.QtGui.QVector3D: ...
    def rotation(self, /) -> PySide6.QtGui.QQuaternion: ...
    def scaling(self, /) -> PySide6.QtGui.QVector3D: ...
    def setMeshFile(self, meshFile: str, /) -> None: ...
    def setPosition(self, position: PySide6.QtGui.QVector3D, /) -> None: ...
    def setPositionAbsolute(self, positionAbsolute: bool, /) -> None: ...
    def setRotation(self, rotation: PySide6.QtGui.QQuaternion, /) -> None: ...
    def setRotationAbsolute(self, rotationAbsolute: bool, /) -> None: ...
    def setRotationAxisAndAngle(self, axis: PySide6.QtGui.QVector3D, angle: float, /) -> None: ...
    def setScaling(self, scaling: PySide6.QtGui.QVector3D, /) -> None: ...
    def setScalingAbsolute(self, scalingAbsolute: bool, /) -> None: ...
    def setShadowCasting(self, enabled: bool, /) -> None: ...
    def setTextureFile(self, textureFile: str, /) -> None: ...
    def setTextureImage(self, textureImage: PySide6.QtGui.QImage, /) -> None: ...
    def setVisible(self, visible: bool, /) -> None: ...
    def textureFile(self, /) -> str: ...


class QCustom3DLabel(PySide6.QtGraphs.QCustom3DItem):
    # backgroundColorChanged(QColor)
    backgroundColorChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QColor], [], [], [], [], [], [], [],
        [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor]
    ]]
    # backgroundVisibleChanged(bool)
    backgroundVisibleChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # borderVisibleChanged(bool)
    borderVisibleChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # facingCameraChanged(bool)
    facingCameraChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # fontChanged(QFont)
    fontChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QFont], [], [], [], [], [], [], [],
        [PySide6.QtGui.QFont], [PySide6.QtGui.QFont], [PySide6.QtGui.QFont], [PySide6.QtGui.QFont], [PySide6.QtGui.QFont], [PySide6.QtGui.QFont], [PySide6.QtGui.QFont], [PySide6.QtGui.QFont]
    ]]
    # textChanged(QString)
    textChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # textColorChanged(QColor)
    textColorChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QColor], [], [], [], [], [], [], [],
        [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor]
    ]]

    @typing.overload
    def __init__(self, text: str, font: PySide6.QtGui.QFont | str | collections.abc.Sequence[str], position: PySide6.QtGui.QVector3D, scaling: PySide6.QtGui.QVector3D, rotation: PySide6.QtGui.QQuaternion, /, parent: PySide6.QtCore.QObject | None = ..., *, textColor: PySide6.QtGui.QColor | None = ..., backgroundColor: PySide6.QtGui.QColor | None = ..., borderVisible: bool | None = ..., backgroundVisible: bool | None = ..., facingCamera: bool | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., *, text: str | None = ..., font: PySide6.QtGui.QFont | None = ..., textColor: PySide6.QtGui.QColor | None = ..., backgroundColor: PySide6.QtGui.QColor | None = ..., borderVisible: bool | None = ..., backgroundVisible: bool | None = ..., facingCamera: bool | None = ...) -> None: ...

    def backgroundColor(self, /) -> PySide6.QtGui.QColor: ...
    def font(self, /) -> PySide6.QtGui.QFont: ...
    def isBackgroundVisible(self, /) -> bool: ...
    def isBorderVisible(self, /) -> bool: ...
    def isFacingCamera(self, /) -> bool: ...
    def setBackgroundColor(self, color: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setBackgroundVisible(self, visible: bool, /) -> None: ...
    def setBorderVisible(self, visible: bool, /) -> None: ...
    def setFacingCamera(self, enabled: bool, /) -> None: ...
    def setFont(self, font: PySide6.QtGui.QFont | str | collections.abc.Sequence[str], /) -> None: ...
    def setText(self, text: str, /) -> None: ...
    def setTextColor(self, color: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def text(self, /) -> str: ...
    def textColor(self, /) -> PySide6.QtGui.QColor: ...


class QCustom3DVolume(PySide6.QtGraphs.QCustom3DItem):
    # alphaMultiplierChanged(float)
    alphaMultiplierChanged: typing.ClassVar[Signal[
        [float], [], [], [], [], [], [], [],
        [float], [float], [float], [float], [float], [float], [float], [float]
    ]]
    # colorTableChanged()
    colorTableChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # drawSliceFramesChanged(bool)
    drawSliceFramesChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # drawSlicesChanged(bool)
    drawSlicesChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # preserveOpacityChanged(bool)
    preserveOpacityChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # sliceFrameColorChanged(QColor)
    sliceFrameColorChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QColor], [], [], [], [], [], [], [],
        [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor]
    ]]
    # sliceFrameGapsChanged(QVector3D)
    sliceFrameGapsChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QVector3D], [], [], [], [], [], [], [],
        [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D]
    ]]
    # sliceFrameThicknessesChanged(QVector3D)
    sliceFrameThicknessesChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QVector3D], [], [], [], [], [], [], [],
        [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D]
    ]]
    # sliceFrameWidthsChanged(QVector3D)
    sliceFrameWidthsChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QVector3D], [], [], [], [], [], [], [],
        [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D], [PySide6.QtGui.QVector3D]
    ]]
    # sliceIndexXChanged(int)
    sliceIndexXChanged: typing.ClassVar[Signal[
        [int], [], [], [], [], [], [], [],
        [int], [int], [int], [int], [int], [int], [int], [int]
    ]]
    # sliceIndexYChanged(int)
    sliceIndexYChanged: typing.ClassVar[Signal[
        [int], [], [], [], [], [], [], [],
        [int], [int], [int], [int], [int], [int], [int], [int]
    ]]
    # sliceIndexZChanged(int)
    sliceIndexZChanged: typing.ClassVar[Signal[
        [int], [], [], [], [], [], [], [],
        [int], [int], [int], [int], [int], [int], [int], [int]
    ]]
    # textureDataChanged(QList<uchar>*)
    textureDataChanged: typing.ClassVar[Signal[
        [collections.abc.Sequence[int]], [], [], [], [], [], [], [],
        [collections.abc.Sequence[int]], [collections.abc.Sequence[int]], [collections.abc.Sequence[int]], [collections.abc.Sequence[int]], [collections.abc.Sequence[int]], [collections.abc.Sequence[int]], [collections.abc.Sequence[int]], [collections.abc.Sequence[int]]
    ]]
    # textureDepthChanged(int)
    textureDepthChanged: typing.ClassVar[Signal[
        [int], [], [], [], [], [], [], [],
        [int], [int], [int], [int], [int], [int], [int], [int]
    ]]
    # textureFormatChanged(QImage::Format)
    textureFormatChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QImage.Format], [], [], [], [], [], [], [],
        [PySide6.QtGui.QImage.Format], [PySide6.QtGui.QImage.Format], [PySide6.QtGui.QImage.Format], [PySide6.QtGui.QImage.Format], [PySide6.QtGui.QImage.Format], [PySide6.QtGui.QImage.Format], [PySide6.QtGui.QImage.Format], [PySide6.QtGui.QImage.Format]
    ]]
    # textureHeightChanged(int)
    textureHeightChanged: typing.ClassVar[Signal[
        [int], [], [], [], [], [], [], [],
        [int], [int], [int], [int], [int], [int], [int], [int]
    ]]
    # textureWidthChanged(int)
    textureWidthChanged: typing.ClassVar[Signal[
        [int], [], [], [], [], [], [], [],
        [int], [int], [int], [int], [int], [int], [int], [int]
    ]]
    # useHighDefShaderChanged(bool)
    useHighDefShaderChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]

    @typing.overload
    def __init__(self, position: PySide6.QtGui.QVector3D, scaling: PySide6.QtGui.QVector3D, rotation: PySide6.QtGui.QQuaternion, textureWidth: int, textureHeight: int, textureDepth: int, textureData: collections.abc.Sequence[int], textureFormat: PySide6.QtGui.QImage.Format, colorTable: collections.abc.Sequence[int], /, parent: PySide6.QtCore.QObject | None = ..., *, sliceIndexX: int | None = ..., sliceIndexY: int | None = ..., sliceIndexZ: int | None = ..., alphaMultiplier: float | None = ..., preserveOpacity: bool | None = ..., useHighDefShader: bool | None = ..., drawSlices: bool | None = ..., drawSliceFrames: bool | None = ..., sliceFrameColor: PySide6.QtGui.QColor | None = ..., sliceFrameWidths: PySide6.QtGui.QVector3D | None = ..., sliceFrameGaps: PySide6.QtGui.QVector3D | None = ..., sliceFrameThicknesses: PySide6.QtGui.QVector3D | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., *, textureWidth: int | None = ..., textureHeight: int | None = ..., textureDepth: int | None = ..., sliceIndexX: int | None = ..., sliceIndexY: int | None = ..., sliceIndexZ: int | None = ..., colorTable: collections.abc.Sequence[int] | None = ..., textureData: collections.abc.Sequence[int] | None = ..., alphaMultiplier: float | None = ..., preserveOpacity: bool | None = ..., useHighDefShader: bool | None = ..., drawSlices: bool | None = ..., drawSliceFrames: bool | None = ..., sliceFrameColor: PySide6.QtGui.QColor | None = ..., sliceFrameWidths: PySide6.QtGui.QVector3D | None = ..., sliceFrameGaps: PySide6.QtGui.QVector3D | None = ..., sliceFrameThicknesses: PySide6.QtGui.QVector3D | None = ...) -> None: ...

    def alphaMultiplier(self, /) -> float: ...
    def colorTable(self, /) -> typing.List[int]: ...
    def createTextureData(self, images: collections.abc.Sequence[PySide6.QtGui.QImage], /) -> typing.List[int]: ...
    def drawSliceFrames(self, /) -> bool: ...
    def drawSlices(self, /) -> bool: ...
    def preserveOpacity(self, /) -> bool: ...
    def renderSlice(self, axis: PySide6.QtCore.Qt.Axis, index: int, /) -> PySide6.QtGui.QImage: ...
    def setAlphaMultiplier(self, mult: float, /) -> None: ...
    def setColorTable(self, colors: collections.abc.Sequence[int], /) -> None: ...
    def setDrawSliceFrames(self, enable: bool, /) -> None: ...
    def setDrawSlices(self, enable: bool, /) -> None: ...
    def setPreserveOpacity(self, enable: bool, /) -> None: ...
    def setSliceFrameColor(self, color: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setSliceFrameGaps(self, values: PySide6.QtGui.QVector3D, /) -> None: ...
    def setSliceFrameThicknesses(self, values: PySide6.QtGui.QVector3D, /) -> None: ...
    def setSliceFrameWidths(self, values: PySide6.QtGui.QVector3D, /) -> None: ...
    def setSliceIndexX(self, value: int, /) -> None: ...
    def setSliceIndexY(self, value: int, /) -> None: ...
    def setSliceIndexZ(self, value: int, /) -> None: ...
    def setSliceIndices(self, x: int, y: int, z: int, /) -> None: ...
    @typing.overload
    def setSubTextureData(self, axis: PySide6.QtCore.Qt.Axis, index: int, image: PySide6.QtGui.QImage, /) -> None: ...
    @typing.overload
    def setSubTextureData(self, axis: PySide6.QtCore.Qt.Axis, index: int, data: bytes | bytearray | memoryview, /) -> None: ...
    def setTextureData(self, arg__1: collections.abc.Sequence[int], /) -> None: ...
    def setTextureDepth(self, value: int, /) -> None: ...
    def setTextureDimensions(self, width: int, height: int, depth: int, /) -> None: ...
    def setTextureFormat(self, format: PySide6.QtGui.QImage.Format, /) -> None: ...
    def setTextureHeight(self, value: int, /) -> None: ...
    def setTextureWidth(self, value: int, /) -> None: ...
    def setUseHighDefShader(self, enable: bool, /) -> None: ...
    def sliceFrameColor(self, /) -> PySide6.QtGui.QColor: ...
    def sliceFrameGaps(self, /) -> PySide6.QtGui.QVector3D: ...
    def sliceFrameThicknesses(self, /) -> PySide6.QtGui.QVector3D: ...
    def sliceFrameWidths(self, /) -> PySide6.QtGui.QVector3D: ...
    def sliceIndexX(self, /) -> int: ...
    def sliceIndexY(self, /) -> int: ...
    def sliceIndexZ(self, /) -> int: ...
    def textureData(self, /) -> typing.List[int]: ...
    def textureDataWidth(self, /) -> int: ...
    def textureDepth(self, /) -> int: ...
    def textureFormat(self, /) -> PySide6.QtGui.QImage.Format: ...
    def textureHeight(self, /) -> int: ...
    def textureWidth(self, /) -> int: ...
    def useHighDefShader(self, /) -> bool: ...


class QCustomSeries(PySide6.QtGraphs.QAbstractSeries):
    # delegateChanged()
    delegateChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]

    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., *, delegate: PySide6.QtQml.QQmlComponent | None = ...) -> None: ...

    @typing.overload
    def append(self, /) -> None: ...
    @typing.overload
    def append(self, data: typing.Dict[str, typing.Any], /) -> None: ...
    def clear(self, /) -> None: ...
    def componentComplete(self, /) -> None: ...
    def delegate(self, /) -> PySide6.QtQml.QQmlComponent: ...
    def event(self, event: PySide6.QtCore.QEvent, /) -> bool: ...
    @typing.overload
    def insert(self, index: int, /) -> None: ...
    @typing.overload
    def insert(self, index: int, data: typing.Dict[str, typing.Any], /) -> None: ...
    def mapX(self, x: float, /) -> float: ...
    def mapY(self, y: float, /) -> float: ...
    def remove(self, index: int, /) -> None: ...
    def setDelegate(self, newDelegate: PySide6.QtQml.QQmlComponent, /) -> None: ...
    def type(self, /) -> PySide6.QtGraphs.QAbstractSeries.SeriesType: ...
    def updateDelegate(self, item: PySide6.QtQuick.QQuickItem, index: int, /) -> None: ...


class QDateTimeAxis(PySide6.QtGraphs.QAbstractAxis):
    # labelFormatChanged(QString)
    labelFormatChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # maxChanged(QDateTime)
    maxChanged: typing.ClassVar[Signal[
        [PySide6.QtCore.QDateTime], [], [], [], [], [], [], [],
        [PySide6.QtCore.QDateTime], [PySide6.QtCore.QDateTime], [PySide6.QtCore.QDateTime], [PySide6.QtCore.QDateTime], [PySide6.QtCore.QDateTime], [PySide6.QtCore.QDateTime], [PySide6.QtCore.QDateTime], [PySide6.QtCore.QDateTime]
    ]]
    # minChanged(QDateTime)
    minChanged: typing.ClassVar[Signal[
        [PySide6.QtCore.QDateTime], [], [], [], [], [], [], [],
        [PySide6.QtCore.QDateTime], [PySide6.QtCore.QDateTime], [PySide6.QtCore.QDateTime], [PySide6.QtCore.QDateTime], [PySide6.QtCore.QDateTime], [PySide6.QtCore.QDateTime], [PySide6.QtCore.QDateTime], [PySide6.QtCore.QDateTime]
    ]]
    # panChanged(double)
    panChanged: typing.ClassVar[Signal[
        [float], [], [], [], [], [], [], [],
        [float], [float], [float], [float], [float], [float], [float], [float]
    ]]
    # subTickCountChanged()
    subTickCountChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # tickIntervalChanged()
    tickIntervalChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # timeZoneChanged(QTimeZone)
    timeZoneChanged: typing.ClassVar[Signal[
        [PySide6.QtCore.QTimeZone], [], [], [], [], [], [], [],
        [PySide6.QtCore.QTimeZone], [PySide6.QtCore.QTimeZone], [PySide6.QtCore.QTimeZone], [PySide6.QtCore.QTimeZone], [PySide6.QtCore.QTimeZone], [PySide6.QtCore.QTimeZone], [PySide6.QtCore.QTimeZone], [PySide6.QtCore.QTimeZone]
    ]]
    # visualMaxChanged(QDateTime)
    visualMaxChanged: typing.ClassVar[Signal[
        [PySide6.QtCore.QDateTime], [], [], [], [], [], [], [],
        [PySide6.QtCore.QDateTime], [PySide6.QtCore.QDateTime], [PySide6.QtCore.QDateTime], [PySide6.QtCore.QDateTime], [PySide6.QtCore.QDateTime], [PySide6.QtCore.QDateTime], [PySide6.QtCore.QDateTime], [PySide6.QtCore.QDateTime]
    ]]
    # visualMinChanged(QDateTime)
    visualMinChanged: typing.ClassVar[Signal[
        [PySide6.QtCore.QDateTime], [], [], [], [], [], [], [],
        [PySide6.QtCore.QDateTime], [PySide6.QtCore.QDateTime], [PySide6.QtCore.QDateTime], [PySide6.QtCore.QDateTime], [PySide6.QtCore.QDateTime], [PySide6.QtCore.QDateTime], [PySide6.QtCore.QDateTime], [PySide6.QtCore.QDateTime]
    ]]
    # zoomChanged(double)
    zoomChanged: typing.ClassVar[Signal[
        [float], [], [], [], [], [], [], [],
        [float], [float], [float], [float], [float], [float], [float], [float]
    ]]

    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., *, min: PySide6.QtCore.QDateTime | None = ..., max: PySide6.QtCore.QDateTime | None = ..., labelFormat: str | None = ..., subTickCount: int | None = ..., tickInterval: float | None = ..., timeZone: PySide6.QtCore.QTimeZone | None = ..., zoom: float | None = ..., pan: float | None = ..., visualMin: PySide6.QtCore.QDateTime | None = ..., visualMax: PySide6.QtCore.QDateTime | None = ...) -> None: ...

    def labelFormat(self, /) -> str: ...
    def max(self, /) -> PySide6.QtCore.QDateTime: ...
    def min(self, /) -> PySide6.QtCore.QDateTime: ...
    def pan(self, /) -> float: ...
    def setLabelFormat(self, format: str, /) -> None: ...
    def setMax(self, max: PySide6.QtCore.QDateTime, /) -> None: ...
    def setMin(self, min: PySide6.QtCore.QDateTime, /) -> None: ...
    def setPan(self, pan: float, /) -> None: ...
    def setSubTickCount(self, newSubTickCount: int, /) -> None: ...
    def setTickInterval(self, newTickInterval: float, /) -> None: ...
    def setTimeZone(self, zoneId: PySide6.QtCore.QTimeZone | PySide6.QtCore.QTimeZone.Initialization, /) -> None: ...
    def setZoom(self, zoom: float, /) -> None: ...
    def subTickCount(self, /) -> int: ...
    def tickInterval(self, /) -> float: ...
    def timeZone(self, /) -> PySide6.QtCore.QTimeZone: ...
    def timeZoneAsString(self, /) -> str: ...
    def timeZoneFromString(self, zoneId: str, /) -> PySide6.QtCore.QTimeZone: ...
    def type(self, /) -> PySide6.QtGraphs.QAbstractAxis.AxisType: ...
    def visualMax(self, /) -> PySide6.QtCore.QDateTime: ...
    def visualMin(self, /) -> PySide6.QtCore.QDateTime: ...
    def zoom(self, /) -> float: ...


class QGraphsLine(Shiboken.Object):
    @typing.overload
    def __init__(self, other: PySide6.QtGraphs.QGraphsLine, /, *, mainColor: PySide6.QtGui.QColor | None = ..., subColor: PySide6.QtGui.QColor | None = ..., mainWidth: float | None = ..., subWidth: float | None = ..., labelTextColor: PySide6.QtGui.QColor | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, *, mainColor: PySide6.QtGui.QColor | None = ..., subColor: PySide6.QtGui.QColor | None = ..., mainWidth: float | None = ..., subWidth: float | None = ..., labelTextColor: PySide6.QtGui.QColor | None = ...) -> None: ...

    def __copy__(self, /) -> typing.Self: ...
    def __eq__(self, rhs: PySide6.QtGraphs.QGraphsLine, /) -> bool: ...
    def __ne__(self, rhs: PySide6.QtGraphs.QGraphsLine, /) -> bool: ...
    def labelTextColor(self, /) -> PySide6.QtGui.QColor: ...
    def mainColor(self, /) -> PySide6.QtGui.QColor: ...
    def mainWidth(self, /) -> float: ...
    def setLabelTextColor(self, newColor: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setMainColor(self, newColor: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setMainWidth(self, newWidth: float, /) -> None: ...
    def setSubColor(self, newColor: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setSubWidth(self, newWidth: float, /) -> None: ...
    def subColor(self, /) -> PySide6.QtGui.QColor: ...
    def subWidth(self, /) -> float: ...


class QGraphsTheme(PySide6.QtCore.QObject, PySide6.QtQml.QQmlParserStatus):
    # axisXChanged()
    axisXChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # axisXLabelFontChanged()
    axisXLabelFontChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # axisYChanged()
    axisYChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # axisYLabelFontChanged()
    axisYLabelFontChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # axisZChanged()
    axisZChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # axisZLabelFontChanged()
    axisZLabelFontChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # backgroundColorChanged()
    backgroundColorChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # backgroundVisibleChanged()
    backgroundVisibleChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # borderColorsChanged()
    borderColorsChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # borderWidthChanged()
    borderWidthChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # colorSchemeChanged()
    colorSchemeChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # colorStyleChanged(QGraphsTheme::ColorStyle)
    colorStyleChanged: typing.ClassVar[Signal[
        [PySide6.QtGraphs.QGraphsTheme.ColorStyle], [], [], [], [], [], [], [],
        [PySide6.QtGraphs.QGraphsTheme.ColorStyle], [PySide6.QtGraphs.QGraphsTheme.ColorStyle], [PySide6.QtGraphs.QGraphsTheme.ColorStyle], [PySide6.QtGraphs.QGraphsTheme.ColorStyle], [PySide6.QtGraphs.QGraphsTheme.ColorStyle], [PySide6.QtGraphs.QGraphsTheme.ColorStyle], [PySide6.QtGraphs.QGraphsTheme.ColorStyle], [PySide6.QtGraphs.QGraphsTheme.ColorStyle]
    ]]
    # gridChanged()
    gridChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # gridVisibleChanged()
    gridVisibleChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # labelBackgroundColorChanged()
    labelBackgroundColorChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # labelBackgroundVisibleChanged()
    labelBackgroundVisibleChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # labelBorderVisibleChanged()
    labelBorderVisibleChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # labelFontChanged()
    labelFontChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # labelTextColorChanged()
    labelTextColorChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # labelsVisibleChanged()
    labelsVisibleChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # multiHighlightColorChanged(QColor)
    multiHighlightColorChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QColor], [], [], [], [], [], [], [],
        [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor]
    ]]
    # multiHighlightGradientChanged(QLinearGradient)
    multiHighlightGradientChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QLinearGradient], [], [], [], [], [], [], [],
        [PySide6.QtGui.QLinearGradient], [PySide6.QtGui.QLinearGradient], [PySide6.QtGui.QLinearGradient], [PySide6.QtGui.QLinearGradient], [PySide6.QtGui.QLinearGradient], [PySide6.QtGui.QLinearGradient], [PySide6.QtGui.QLinearGradient], [PySide6.QtGui.QLinearGradient]
    ]]
    # multiHighlightGradientQMLChanged()
    multiHighlightGradientQMLChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # plotAreaBackgroundColorChanged()
    plotAreaBackgroundColorChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # plotAreaBackgroundVisibleChanged()
    plotAreaBackgroundVisibleChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # seriesColorsChanged(QList<QColor>)
    seriesColorsChanged: typing.ClassVar[Signal[
        [collections.abc.Sequence[PySide6.QtGui.QColor]], [], [], [], [], [], [], [],
        [collections.abc.Sequence[PySide6.QtGui.QColor]], [collections.abc.Sequence[PySide6.QtGui.QColor]], [collections.abc.Sequence[PySide6.QtGui.QColor]], [collections.abc.Sequence[PySide6.QtGui.QColor]], [collections.abc.Sequence[PySide6.QtGui.QColor]], [collections.abc.Sequence[PySide6.QtGui.QColor]], [collections.abc.Sequence[PySide6.QtGui.QColor]], [collections.abc.Sequence[PySide6.QtGui.QColor]]
    ]]
    # seriesGradientsChanged(QList<QLinearGradient>)
    seriesGradientsChanged: typing.ClassVar[Signal[
        [collections.abc.Sequence[PySide6.QtGui.QLinearGradient]], [], [], [], [], [], [], [],
        [collections.abc.Sequence[PySide6.QtGui.QLinearGradient]], [collections.abc.Sequence[PySide6.QtGui.QLinearGradient]], [collections.abc.Sequence[PySide6.QtGui.QLinearGradient]], [collections.abc.Sequence[PySide6.QtGui.QLinearGradient]], [collections.abc.Sequence[PySide6.QtGui.QLinearGradient]], [collections.abc.Sequence[PySide6.QtGui.QLinearGradient]], [collections.abc.Sequence[PySide6.QtGui.QLinearGradient]], [collections.abc.Sequence[PySide6.QtGui.QLinearGradient]]
    ]]
    # singleHighlightColorChanged(QColor)
    singleHighlightColorChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QColor], [], [], [], [], [], [], [],
        [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor]
    ]]
    # singleHighlightGradientChanged(QLinearGradient)
    singleHighlightGradientChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QLinearGradient], [], [], [], [], [], [], [],
        [PySide6.QtGui.QLinearGradient], [PySide6.QtGui.QLinearGradient], [PySide6.QtGui.QLinearGradient], [PySide6.QtGui.QLinearGradient], [PySide6.QtGui.QLinearGradient], [PySide6.QtGui.QLinearGradient], [PySide6.QtGui.QLinearGradient], [PySide6.QtGui.QLinearGradient]
    ]]
    # singleHighlightGradientQMLChanged()
    singleHighlightGradientQMLChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # themeChanged(QGraphsTheme::Theme)
    themeChanged: typing.ClassVar[Signal[
        [PySide6.QtGraphs.QGraphsTheme.Theme], [], [], [], [], [], [], [],
        [PySide6.QtGraphs.QGraphsTheme.Theme], [PySide6.QtGraphs.QGraphsTheme.Theme], [PySide6.QtGraphs.QGraphsTheme.Theme], [PySide6.QtGraphs.QGraphsTheme.Theme], [PySide6.QtGraphs.QGraphsTheme.Theme], [PySide6.QtGraphs.QGraphsTheme.Theme], [PySide6.QtGraphs.QGraphsTheme.Theme], [PySide6.QtGraphs.QGraphsTheme.Theme]
    ]]
    # update()
    update: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]

    class ColorScheme(enum.Enum):
        Automatic                 = 0x0
        Light                     = 0x1
        Dark                      = 0x2

    class ColorStyle(enum.Enum):
        Uniform                   = 0x0
        ObjectGradient            = 0x1
        RangeGradient             = 0x2

    class ForceTheme(enum.Enum):
        No                        = 0x0
        Yes                       = 0x1

    class Theme(enum.Enum):
        QtGreen                   = 0x0
        QtGreenNeon               = 0x1
        MixSeries                 = 0x2
        OrangeSeries              = 0x3
        YellowSeries              = 0x4
        BlueSeries                = 0x5
        PurpleSeries              = 0x6
        GreySeries                = 0x7
        UserDefined               = 0x8

    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., *, colorScheme: PySide6.QtGraphs.QGraphsTheme.ColorScheme | None = ..., theme: PySide6.QtGraphs.QGraphsTheme.Theme | None = ..., colorStyle: PySide6.QtGraphs.QGraphsTheme.ColorStyle | None = ..., backgroundColor: PySide6.QtGui.QColor | None = ..., backgroundVisible: bool | None = ..., plotAreaBackgroundColor: PySide6.QtGui.QColor | None = ..., plotAreaBackgroundVisible: bool | None = ..., gridVisible: bool | None = ..., axisXLabelFont: PySide6.QtGui.QFont | None = ..., axisYLabelFont: PySide6.QtGui.QFont | None = ..., axisZLabelFont: PySide6.QtGui.QFont | None = ..., grid: PySide6.QtGraphs.QGraphsLine | None = ..., axisX: PySide6.QtGraphs.QGraphsLine | None = ..., axisY: PySide6.QtGraphs.QGraphsLine | None = ..., axisZ: PySide6.QtGraphs.QGraphsLine | None = ..., labelFont: PySide6.QtGui.QFont | None = ..., labelsVisible: bool | None = ..., labelBackgroundColor: PySide6.QtGui.QColor | None = ..., labelTextColor: PySide6.QtGui.QColor | None = ..., labelBackgroundVisible: bool | None = ..., labelBorderVisible: bool | None = ..., seriesColors: collections.abc.Sequence[PySide6.QtGui.QColor] | None = ..., borderColors: collections.abc.Sequence[PySide6.QtGui.QColor] | None = ..., borderWidth: float | None = ..., singleHighlightColor: PySide6.QtGui.QColor | None = ..., multiHighlightColor: PySide6.QtGui.QColor | None = ...) -> None: ...

    def axisX(self, /) -> PySide6.QtGraphs.QGraphsLine: ...
    def axisXLabelFont(self, /) -> PySide6.QtGui.QFont: ...
    def axisY(self, /) -> PySide6.QtGraphs.QGraphsLine: ...
    def axisYLabelFont(self, /) -> PySide6.QtGui.QFont: ...
    def axisZ(self, /) -> PySide6.QtGraphs.QGraphsLine: ...
    def axisZLabelFont(self, /) -> PySide6.QtGui.QFont: ...
    def backgroundColor(self, /) -> PySide6.QtGui.QColor: ...
    def borderColors(self, /) -> typing.List[PySide6.QtGui.QColor]: ...
    def borderWidth(self, /) -> float: ...
    def classBegin(self, /) -> None: ...
    def colorScheme(self, /) -> PySide6.QtGraphs.QGraphsTheme.ColorScheme: ...
    def colorStyle(self, /) -> PySide6.QtGraphs.QGraphsTheme.ColorStyle: ...
    def componentComplete(self, /) -> None: ...
    def dirtyBits(self, /) -> PySide6.QtGraphs.QGraphsThemeDirtyBitField: ...
    def grid(self, /) -> PySide6.QtGraphs.QGraphsLine: ...
    def handleBaseColorUpdate(self, /) -> None: ...
    def handleBaseGradientUpdate(self, /) -> None: ...
    def isBackgroundVisible(self, /) -> bool: ...
    def isGridVisible(self, /) -> bool: ...
    def isLabelBackgroundVisible(self, /) -> bool: ...
    def isLabelBorderVisible(self, /) -> bool: ...
    def isPlotAreaBackgroundVisible(self, /) -> bool: ...
    def labelBackgroundColor(self, /) -> PySide6.QtGui.QColor: ...
    def labelFont(self, /) -> PySide6.QtGui.QFont: ...
    def labelTextColor(self, /) -> PySide6.QtGui.QColor: ...
    def labelsVisible(self, /) -> bool: ...
    def multiHighlightColor(self, /) -> PySide6.QtGui.QColor: ...
    def multiHighlightGradient(self, /) -> PySide6.QtGui.QLinearGradient: ...
    def plotAreaBackgroundColor(self, /) -> PySide6.QtGui.QColor: ...
    def resetColorTheme(self, /) -> None: ...
    def resetDirtyBits(self, /) -> None: ...
    def resetThemeDirty(self, /) -> None: ...
    def seriesColors(self, /) -> typing.List[PySide6.QtGui.QColor]: ...
    def seriesGradients(self, /) -> typing.List[PySide6.QtGui.QLinearGradient]: ...
    def setAxisX(self, newAxisX: PySide6.QtGraphs.QGraphsLine, /) -> None: ...
    def setAxisXLabelFont(self, newAxisXLabelFont: PySide6.QtGui.QFont | str | collections.abc.Sequence[str], /) -> None: ...
    def setAxisY(self, newAxisY: PySide6.QtGraphs.QGraphsLine, /) -> None: ...
    def setAxisYLabelFont(self, newAxisYLabelFont: PySide6.QtGui.QFont | str | collections.abc.Sequence[str], /) -> None: ...
    def setAxisZ(self, newAxisZ: PySide6.QtGraphs.QGraphsLine, /) -> None: ...
    def setAxisZLabelFont(self, newAxisZLabelFont: PySide6.QtGui.QFont | str | collections.abc.Sequence[str], /) -> None: ...
    def setBackgroundColor(self, newBackgroundColor: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setBackgroundVisible(self, newBackgroundVisible: bool, /) -> None: ...
    def setBorderColors(self, newBorderColors: collections.abc.Sequence[PySide6.QtGui.QColor], /) -> None: ...
    def setBorderWidth(self, newBorderWidth: float, /) -> None: ...
    def setColorScheme(self, newColorScheme: PySide6.QtGraphs.QGraphsTheme.ColorScheme, /) -> None: ...
    def setColorStyle(self, newColorStyle: PySide6.QtGraphs.QGraphsTheme.ColorStyle, /) -> None: ...
    def setGrid(self, newGrid: PySide6.QtGraphs.QGraphsLine, /) -> None: ...
    def setGridVisible(self, newGridVisibility: bool, /) -> None: ...
    def setLabelBackgroundColor(self, newLabelBackgroundColor: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setLabelBackgroundVisible(self, newLabelBackgroundVisibility: bool, /) -> None: ...
    def setLabelBorderVisible(self, newLabelBorderVisibility: bool, /) -> None: ...
    def setLabelFont(self, newFont: PySide6.QtGui.QFont | str | collections.abc.Sequence[str], /) -> None: ...
    def setLabelTextColor(self, newLabelTextColor: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setLabelsVisible(self, newLabelsVisibility: bool, /) -> None: ...
    def setMultiHighlightColor(self, newMultiHighlightColor: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setMultiHighlightGradient(self, gradient: PySide6.QtGui.QLinearGradient, /) -> None: ...
    def setPlotAreaBackgroundColor(self, newBackgroundColor: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setPlotAreaBackgroundVisible(self, newBackgroundVisibility: bool, /) -> None: ...
    def setSeriesColors(self, newSeriesColors: collections.abc.Sequence[PySide6.QtGui.QColor], /) -> None: ...
    def setSeriesGradients(self, newSeriesGradients: collections.abc.Sequence[PySide6.QtGui.QLinearGradient], /) -> None: ...
    def setSingleHighlightColor(self, newSingleHighlightColor: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setSingleHighlightGradient(self, gradient: PySide6.QtGui.QLinearGradient, /) -> None: ...
    def setTheme(self, newTheme: PySide6.QtGraphs.QGraphsTheme.Theme, /, force: PySide6.QtGraphs.QGraphsTheme.ForceTheme = ...) -> None: ...
    def singleHighlightColor(self, /) -> PySide6.QtGui.QColor: ...
    def singleHighlightGradient(self, /) -> PySide6.QtGui.QLinearGradient: ...
    def theme(self, /) -> PySide6.QtGraphs.QGraphsTheme.Theme: ...
    def themeDirty(self, /) -> bool: ...


class QGraphsThemeDirtyBitField(Shiboken.Object):
    @property
    def axisXDirty(self) -> bool: ...
    @axisXDirty.setter
    def axisXDirty(self, axisXDirty: bool) -> None: ...
    @property
    def axisYDirty(self) -> bool: ...
    @axisYDirty.setter
    def axisYDirty(self, axisYDirty: bool) -> None: ...
    @property
    def axisZDirty(self) -> bool: ...
    @axisZDirty.setter
    def axisZDirty(self, axisZDirty: bool) -> None: ...
    @property
    def backgroundColorDirty(self) -> bool: ...
    @backgroundColorDirty.setter
    def backgroundColorDirty(self, backgroundColorDirty: bool) -> None: ...
    @property
    def backgroundVisibilityDirty(self) -> bool: ...
    @backgroundVisibilityDirty.setter
    def backgroundVisibilityDirty(self, backgroundVisibilityDirty: bool) -> None: ...
    @property
    def colorSchemeDirty(self) -> bool: ...
    @colorSchemeDirty.setter
    def colorSchemeDirty(self, colorSchemeDirty: bool) -> None: ...
    @property
    def colorStyleDirty(self) -> bool: ...
    @colorStyleDirty.setter
    def colorStyleDirty(self, colorStyleDirty: bool) -> None: ...
    @property
    def gridDirty(self) -> bool: ...
    @gridDirty.setter
    def gridDirty(self, gridDirty: bool) -> None: ...
    @property
    def gridVisibilityDirty(self) -> bool: ...
    @gridVisibilityDirty.setter
    def gridVisibilityDirty(self, gridVisibilityDirty: bool) -> None: ...
    @property
    def labelBackgroundColorDirty(self) -> bool: ...
    @labelBackgroundColorDirty.setter
    def labelBackgroundColorDirty(self, labelBackgroundColorDirty: bool) -> None: ...
    @property
    def labelBackgroundVisibilityDirty(self) -> bool: ...
    @labelBackgroundVisibilityDirty.setter
    def labelBackgroundVisibilityDirty(self, labelBackgroundVisibilityDirty: bool) -> None: ...
    @property
    def labelBorderVisibilityDirty(self) -> bool: ...
    @labelBorderVisibilityDirty.setter
    def labelBorderVisibilityDirty(self, labelBorderVisibilityDirty: bool) -> None: ...
    @property
    def labelFontDirty(self) -> bool: ...
    @labelFontDirty.setter
    def labelFontDirty(self, labelFontDirty: bool) -> None: ...
    @property
    def labelTextColorDirty(self) -> bool: ...
    @labelTextColorDirty.setter
    def labelTextColorDirty(self, labelTextColorDirty: bool) -> None: ...
    @property
    def labelsVisibilityDirty(self) -> bool: ...
    @labelsVisibilityDirty.setter
    def labelsVisibilityDirty(self, labelsVisibilityDirty: bool) -> None: ...
    @property
    def multiHighlightColorDirty(self) -> bool: ...
    @multiHighlightColorDirty.setter
    def multiHighlightColorDirty(self, multiHighlightColorDirty: bool) -> None: ...
    @property
    def multiHighlightGradientDirty(self) -> bool: ...
    @multiHighlightGradientDirty.setter
    def multiHighlightGradientDirty(self, multiHighlightGradientDirty: bool) -> None: ...
    @property
    def plotAreaBackgroundColorDirty(self) -> bool: ...
    @plotAreaBackgroundColorDirty.setter
    def plotAreaBackgroundColorDirty(self, plotAreaBackgroundColorDirty: bool) -> None: ...
    @property
    def plotAreaBackgroundVisibilityDirty(self) -> bool: ...
    @plotAreaBackgroundVisibilityDirty.setter
    def plotAreaBackgroundVisibilityDirty(self, plotAreaBackgroundVisibilityDirty: bool) -> None: ...
    @property
    def seriesColorsDirty(self) -> bool: ...
    @seriesColorsDirty.setter
    def seriesColorsDirty(self, seriesColorsDirty: bool) -> None: ...
    @property
    def seriesGradientDirty(self) -> bool: ...
    @seriesGradientDirty.setter
    def seriesGradientDirty(self, seriesGradientDirty: bool) -> None: ...
    @property
    def singleHighlightColorDirty(self) -> bool: ...
    @singleHighlightColorDirty.setter
    def singleHighlightColorDirty(self, singleHighlightColorDirty: bool) -> None: ...
    @property
    def singleHighlightGradientDirty(self) -> bool: ...
    @singleHighlightGradientDirty.setter
    def singleHighlightGradientDirty(self, singleHighlightGradientDirty: bool) -> None: ...
    @property
    def themeDirty(self) -> bool: ...
    @themeDirty.setter
    def themeDirty(self, themeDirty: bool) -> None: ...

    @typing.overload
    def __init__(self, /) -> None: ...
    @typing.overload
    def __init__(self, QGraphsThemeDirtyBitField: PySide6.QtGraphs.QGraphsThemeDirtyBitField, /) -> None: ...

    def __copy__(self, /) -> typing.Self: ...


class QHeightMapSurfaceDataProxy(PySide6.QtGraphs.QSurfaceDataProxy):
    # autoScaleYChanged(bool)
    autoScaleYChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # heightMapChanged(QImage)
    heightMapChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QImage], [], [], [], [], [], [], [],
        [PySide6.QtGui.QImage], [PySide6.QtGui.QImage], [PySide6.QtGui.QImage], [PySide6.QtGui.QImage], [PySide6.QtGui.QImage], [PySide6.QtGui.QImage], [PySide6.QtGui.QImage], [PySide6.QtGui.QImage]
    ]]
    # heightMapFileChanged(QString)
    heightMapFileChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # maxXValueChanged(float)
    maxXValueChanged: typing.ClassVar[Signal[
        [float], [], [], [], [], [], [], [],
        [float], [float], [float], [float], [float], [float], [float], [float]
    ]]
    # maxYValueChanged(float)
    maxYValueChanged: typing.ClassVar[Signal[
        [float], [], [], [], [], [], [], [],
        [float], [float], [float], [float], [float], [float], [float], [float]
    ]]
    # maxZValueChanged(float)
    maxZValueChanged: typing.ClassVar[Signal[
        [float], [], [], [], [], [], [], [],
        [float], [float], [float], [float], [float], [float], [float], [float]
    ]]
    # minXValueChanged(float)
    minXValueChanged: typing.ClassVar[Signal[
        [float], [], [], [], [], [], [], [],
        [float], [float], [float], [float], [float], [float], [float], [float]
    ]]
    # minYValueChanged(float)
    minYValueChanged: typing.ClassVar[Signal[
        [float], [], [], [], [], [], [], [],
        [float], [float], [float], [float], [float], [float], [float], [float]
    ]]
    # minZValueChanged(float)
    minZValueChanged: typing.ClassVar[Signal[
        [float], [], [], [], [], [], [], [],
        [float], [float], [float], [float], [float], [float], [float], [float]
    ]]

    @typing.overload
    def __init__(self, image: PySide6.QtGui.QImage, /, parent: PySide6.QtCore.QObject | None = ..., *, heightMap: PySide6.QtGui.QImage | None = ..., heightMapFile: str | None = ..., minXValue: float | None = ..., maxXValue: float | None = ..., minZValue: float | None = ..., maxZValue: float | None = ..., minYValue: float | None = ..., maxYValue: float | None = ..., autoScaleY: bool | None = ...) -> None: ...
    @typing.overload
    def __init__(self, filename: str, /, parent: PySide6.QtCore.QObject | None = ..., *, heightMap: PySide6.QtGui.QImage | None = ..., heightMapFile: str | None = ..., minXValue: float | None = ..., maxXValue: float | None = ..., minZValue: float | None = ..., maxZValue: float | None = ..., minYValue: float | None = ..., maxYValue: float | None = ..., autoScaleY: bool | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., *, heightMap: PySide6.QtGui.QImage | None = ..., heightMapFile: str | None = ..., minXValue: float | None = ..., maxXValue: float | None = ..., minZValue: float | None = ..., maxZValue: float | None = ..., minYValue: float | None = ..., maxYValue: float | None = ..., autoScaleY: bool | None = ...) -> None: ...

    def autoScaleY(self, /) -> bool: ...
    def handlePendingResolve(self, /) -> None: ...
    def heightMap(self, /) -> PySide6.QtGui.QImage: ...
    def heightMapFile(self, /) -> str: ...
    def maxXValue(self, /) -> float: ...
    def maxYValue(self, /) -> float: ...
    def maxZValue(self, /) -> float: ...
    def minXValue(self, /) -> float: ...
    def minYValue(self, /) -> float: ...
    def minZValue(self, /) -> float: ...
    def setAutoScaleY(self, enabled: bool, /) -> None: ...
    def setHeightMap(self, image: PySide6.QtGui.QImage, /) -> None: ...
    def setHeightMapFile(self, filename: str, /) -> None: ...
    def setMaxXValue(self, max: float, /) -> None: ...
    def setMaxYValue(self, max: float, /) -> None: ...
    def setMaxZValue(self, max: float, /) -> None: ...
    def setMinXValue(self, min: float, /) -> None: ...
    def setMinYValue(self, min: float, /) -> None: ...
    def setMinZValue(self, min: float, /) -> None: ...
    def setValueRanges(self, minX: float, maxX: float, minZ: float, maxZ: float, /) -> None: ...


class QIntList:
    ...


class QItemModelBarDataProxy(PySide6.QtGraphs.QBarDataProxy):
    # autoColumnCategoriesChanged(bool)
    autoColumnCategoriesChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # autoRowCategoriesChanged(bool)
    autoRowCategoriesChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # columnCategoriesChanged()
    columnCategoriesChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # columnRoleChanged(QString)
    columnRoleChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # columnRolePatternChanged(QRegularExpression)
    columnRolePatternChanged: typing.ClassVar[Signal[
        [PySide6.QtCore.QRegularExpression], [], [], [], [], [], [], [],
        [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression]
    ]]
    # columnRoleReplaceChanged(QString)
    columnRoleReplaceChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # itemModelChanged(const QAbstractItemModel*)
    itemModelChanged: typing.ClassVar[Signal[
        [typing.Any], [], [], [], [], [], [], [],
        [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any]
    ]]
    # multiMatchBehaviorChanged(QItemModelBarDataProxy::MultiMatchBehavior)
    multiMatchBehaviorChanged: typing.ClassVar[Signal[
        [PySide6.QtGraphs.QItemModelBarDataProxy.MultiMatchBehavior], [], [], [], [], [], [], [],
        [PySide6.QtGraphs.QItemModelBarDataProxy.MultiMatchBehavior], [PySide6.QtGraphs.QItemModelBarDataProxy.MultiMatchBehavior], [PySide6.QtGraphs.QItemModelBarDataProxy.MultiMatchBehavior], [PySide6.QtGraphs.QItemModelBarDataProxy.MultiMatchBehavior], [PySide6.QtGraphs.QItemModelBarDataProxy.MultiMatchBehavior], [PySide6.QtGraphs.QItemModelBarDataProxy.MultiMatchBehavior], [PySide6.QtGraphs.QItemModelBarDataProxy.MultiMatchBehavior], [PySide6.QtGraphs.QItemModelBarDataProxy.MultiMatchBehavior]
    ]]
    # rotationRoleChanged(QString)
    rotationRoleChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # rotationRolePatternChanged(QRegularExpression)
    rotationRolePatternChanged: typing.ClassVar[Signal[
        [PySide6.QtCore.QRegularExpression], [], [], [], [], [], [], [],
        [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression]
    ]]
    # rotationRoleReplaceChanged(QString)
    rotationRoleReplaceChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # rowCategoriesChanged()
    rowCategoriesChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # rowRoleChanged(QString)
    rowRoleChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # rowRolePatternChanged(QRegularExpression)
    rowRolePatternChanged: typing.ClassVar[Signal[
        [PySide6.QtCore.QRegularExpression], [], [], [], [], [], [], [],
        [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression]
    ]]
    # rowRoleReplaceChanged(QString)
    rowRoleReplaceChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # useModelCategoriesChanged(bool)
    useModelCategoriesChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # valueRoleChanged(QString)
    valueRoleChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # valueRolePatternChanged(QRegularExpression)
    valueRolePatternChanged: typing.ClassVar[Signal[
        [PySide6.QtCore.QRegularExpression], [], [], [], [], [], [], [],
        [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression]
    ]]
    # valueRoleReplaceChanged(QString)
    valueRoleReplaceChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]

    class MultiMatchBehavior(enum.Enum):
        First                     = 0x0
        Last                      = 0x1
        Average                   = 0x2
        Cumulative                = 0x3

    @typing.overload
    def __init__(self, itemModel: PySide6.QtCore.QAbstractItemModel, rowRole: str, columnRole: str, valueRole: str, rotationRole: str, rowCategories: collections.abc.Sequence[str], columnCategories: collections.abc.Sequence[str], /, parent: PySide6.QtCore.QObject | None = ..., *, useModelCategories: bool | None = ..., autoRowCategories: bool | None = ..., autoColumnCategories: bool | None = ..., rowRolePattern: PySide6.QtCore.QRegularExpression | None = ..., columnRolePattern: PySide6.QtCore.QRegularExpression | None = ..., valueRolePattern: PySide6.QtCore.QRegularExpression | None = ..., rotationRolePattern: PySide6.QtCore.QRegularExpression | None = ..., rowRoleReplace: str | None = ..., columnRoleReplace: str | None = ..., valueRoleReplace: str | None = ..., rotationRoleReplace: str | None = ..., multiMatchBehavior: PySide6.QtGraphs.QItemModelBarDataProxy.MultiMatchBehavior | None = ...) -> None: ...
    @typing.overload
    def __init__(self, itemModel: PySide6.QtCore.QAbstractItemModel, rowRole: str, columnRole: str, valueRole: str, rotationRole: str, /, parent: PySide6.QtCore.QObject | None = ..., *, rowCategories: collections.abc.Sequence[str] | None = ..., columnCategories: collections.abc.Sequence[str] | None = ..., useModelCategories: bool | None = ..., autoRowCategories: bool | None = ..., autoColumnCategories: bool | None = ..., rowRolePattern: PySide6.QtCore.QRegularExpression | None = ..., columnRolePattern: PySide6.QtCore.QRegularExpression | None = ..., valueRolePattern: PySide6.QtCore.QRegularExpression | None = ..., rotationRolePattern: PySide6.QtCore.QRegularExpression | None = ..., rowRoleReplace: str | None = ..., columnRoleReplace: str | None = ..., valueRoleReplace: str | None = ..., rotationRoleReplace: str | None = ..., multiMatchBehavior: PySide6.QtGraphs.QItemModelBarDataProxy.MultiMatchBehavior | None = ...) -> None: ...
    @typing.overload
    def __init__(self, itemModel: PySide6.QtCore.QAbstractItemModel, rowRole: str, columnRole: str, valueRole: str, rowCategories: collections.abc.Sequence[str], columnCategories: collections.abc.Sequence[str], /, parent: PySide6.QtCore.QObject | None = ..., *, rotationRole: str | None = ..., useModelCategories: bool | None = ..., autoRowCategories: bool | None = ..., autoColumnCategories: bool | None = ..., rowRolePattern: PySide6.QtCore.QRegularExpression | None = ..., columnRolePattern: PySide6.QtCore.QRegularExpression | None = ..., valueRolePattern: PySide6.QtCore.QRegularExpression | None = ..., rotationRolePattern: PySide6.QtCore.QRegularExpression | None = ..., rowRoleReplace: str | None = ..., columnRoleReplace: str | None = ..., valueRoleReplace: str | None = ..., rotationRoleReplace: str | None = ..., multiMatchBehavior: PySide6.QtGraphs.QItemModelBarDataProxy.MultiMatchBehavior | None = ...) -> None: ...
    @typing.overload
    def __init__(self, itemModel: PySide6.QtCore.QAbstractItemModel, rowRole: str, columnRole: str, valueRole: str, /, parent: PySide6.QtCore.QObject | None = ..., *, rotationRole: str | None = ..., rowCategories: collections.abc.Sequence[str] | None = ..., columnCategories: collections.abc.Sequence[str] | None = ..., useModelCategories: bool | None = ..., autoRowCategories: bool | None = ..., autoColumnCategories: bool | None = ..., rowRolePattern: PySide6.QtCore.QRegularExpression | None = ..., columnRolePattern: PySide6.QtCore.QRegularExpression | None = ..., valueRolePattern: PySide6.QtCore.QRegularExpression | None = ..., rotationRolePattern: PySide6.QtCore.QRegularExpression | None = ..., rowRoleReplace: str | None = ..., columnRoleReplace: str | None = ..., valueRoleReplace: str | None = ..., rotationRoleReplace: str | None = ..., multiMatchBehavior: PySide6.QtGraphs.QItemModelBarDataProxy.MultiMatchBehavior | None = ...) -> None: ...
    @typing.overload
    def __init__(self, itemModel: PySide6.QtCore.QAbstractItemModel, valueRole: str, /, parent: PySide6.QtCore.QObject | None = ..., *, rowRole: str | None = ..., columnRole: str | None = ..., rotationRole: str | None = ..., rowCategories: collections.abc.Sequence[str] | None = ..., columnCategories: collections.abc.Sequence[str] | None = ..., useModelCategories: bool | None = ..., autoRowCategories: bool | None = ..., autoColumnCategories: bool | None = ..., rowRolePattern: PySide6.QtCore.QRegularExpression | None = ..., columnRolePattern: PySide6.QtCore.QRegularExpression | None = ..., valueRolePattern: PySide6.QtCore.QRegularExpression | None = ..., rotationRolePattern: PySide6.QtCore.QRegularExpression | None = ..., rowRoleReplace: str | None = ..., columnRoleReplace: str | None = ..., valueRoleReplace: str | None = ..., rotationRoleReplace: str | None = ..., multiMatchBehavior: PySide6.QtGraphs.QItemModelBarDataProxy.MultiMatchBehavior | None = ...) -> None: ...
    @typing.overload
    def __init__(self, itemModel: PySide6.QtCore.QAbstractItemModel, /, parent: PySide6.QtCore.QObject | None = ..., *, rowRole: str | None = ..., columnRole: str | None = ..., valueRole: str | None = ..., rotationRole: str | None = ..., rowCategories: collections.abc.Sequence[str] | None = ..., columnCategories: collections.abc.Sequence[str] | None = ..., useModelCategories: bool | None = ..., autoRowCategories: bool | None = ..., autoColumnCategories: bool | None = ..., rowRolePattern: PySide6.QtCore.QRegularExpression | None = ..., columnRolePattern: PySide6.QtCore.QRegularExpression | None = ..., valueRolePattern: PySide6.QtCore.QRegularExpression | None = ..., rotationRolePattern: PySide6.QtCore.QRegularExpression | None = ..., rowRoleReplace: str | None = ..., columnRoleReplace: str | None = ..., valueRoleReplace: str | None = ..., rotationRoleReplace: str | None = ..., multiMatchBehavior: PySide6.QtGraphs.QItemModelBarDataProxy.MultiMatchBehavior | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., *, itemModel: PySide6.QtCore.QAbstractItemModel | None = ..., rowRole: str | None = ..., columnRole: str | None = ..., valueRole: str | None = ..., rotationRole: str | None = ..., rowCategories: collections.abc.Sequence[str] | None = ..., columnCategories: collections.abc.Sequence[str] | None = ..., useModelCategories: bool | None = ..., autoRowCategories: bool | None = ..., autoColumnCategories: bool | None = ..., rowRolePattern: PySide6.QtCore.QRegularExpression | None = ..., columnRolePattern: PySide6.QtCore.QRegularExpression | None = ..., valueRolePattern: PySide6.QtCore.QRegularExpression | None = ..., rotationRolePattern: PySide6.QtCore.QRegularExpression | None = ..., rowRoleReplace: str | None = ..., columnRoleReplace: str | None = ..., valueRoleReplace: str | None = ..., rotationRoleReplace: str | None = ..., multiMatchBehavior: PySide6.QtGraphs.QItemModelBarDataProxy.MultiMatchBehavior | None = ...) -> None: ...

    def autoColumnCategories(self, /) -> bool: ...
    def autoRowCategories(self, /) -> bool: ...
    def columnCategories(self, /) -> typing.List[str]: ...
    def columnCategoryIndex(self, category: str, /) -> int: ...
    def columnRole(self, /) -> str: ...
    def columnRolePattern(self, /) -> PySide6.QtCore.QRegularExpression: ...
    def columnRoleReplace(self, /) -> str: ...
    def itemModel(self, /) -> PySide6.QtCore.QAbstractItemModel: ...
    def multiMatchBehavior(self, /) -> PySide6.QtGraphs.QItemModelBarDataProxy.MultiMatchBehavior: ...
    def remap(self, rowRole: str, columnRole: str, valueRole: str, rotationRole: str, rowCategories: collections.abc.Sequence[str], columnCategories: collections.abc.Sequence[str], /) -> None: ...
    def rotationRole(self, /) -> str: ...
    def rotationRolePattern(self, /) -> PySide6.QtCore.QRegularExpression: ...
    def rotationRoleReplace(self, /) -> str: ...
    def rowCategories(self, /) -> typing.List[str]: ...
    def rowCategoryIndex(self, category: str, /) -> int: ...
    def rowRole(self, /) -> str: ...
    def rowRolePattern(self, /) -> PySide6.QtCore.QRegularExpression: ...
    def rowRoleReplace(self, /) -> str: ...
    def setAutoColumnCategories(self, enable: bool, /) -> None: ...
    def setAutoRowCategories(self, enable: bool, /) -> None: ...
    def setColumnCategories(self, categories: collections.abc.Sequence[str], /) -> None: ...
    def setColumnRole(self, role: str, /) -> None: ...
    def setColumnRolePattern(self, pattern: PySide6.QtCore.QRegularExpression | str, /) -> None: ...
    def setColumnRoleReplace(self, replace: str, /) -> None: ...
    def setItemModel(self, itemModel: PySide6.QtCore.QAbstractItemModel, /) -> None: ...
    def setMultiMatchBehavior(self, behavior: PySide6.QtGraphs.QItemModelBarDataProxy.MultiMatchBehavior, /) -> None: ...
    def setRotationRole(self, role: str, /) -> None: ...
    def setRotationRolePattern(self, pattern: PySide6.QtCore.QRegularExpression | str, /) -> None: ...
    def setRotationRoleReplace(self, replace: str, /) -> None: ...
    def setRowCategories(self, categories: collections.abc.Sequence[str], /) -> None: ...
    def setRowRole(self, role: str, /) -> None: ...
    def setRowRolePattern(self, pattern: PySide6.QtCore.QRegularExpression | str, /) -> None: ...
    def setRowRoleReplace(self, replace: str, /) -> None: ...
    def setUseModelCategories(self, enable: bool, /) -> None: ...
    def setValueRole(self, role: str, /) -> None: ...
    def setValueRolePattern(self, pattern: PySide6.QtCore.QRegularExpression | str, /) -> None: ...
    def setValueRoleReplace(self, replace: str, /) -> None: ...
    def useModelCategories(self, /) -> bool: ...
    def valueRole(self, /) -> str: ...
    def valueRolePattern(self, /) -> PySide6.QtCore.QRegularExpression: ...
    def valueRoleReplace(self, /) -> str: ...


class QItemModelScatterDataProxy(PySide6.QtGraphs.QScatterDataProxy):
    # itemModelChanged(const QAbstractItemModel*)
    itemModelChanged: typing.ClassVar[Signal[
        [typing.Any], [], [], [], [], [], [], [],
        [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any]
    ]]
    # rotationRoleChanged(QString)
    rotationRoleChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # rotationRolePatternChanged(QRegularExpression)
    rotationRolePatternChanged: typing.ClassVar[Signal[
        [PySide6.QtCore.QRegularExpression], [], [], [], [], [], [], [],
        [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression]
    ]]
    # rotationRoleReplaceChanged(QString)
    rotationRoleReplaceChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # scaleRoleChanged(QString)
    scaleRoleChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # scaleRolePatternChanged(QRegularExpression)
    scaleRolePatternChanged: typing.ClassVar[Signal[
        [PySide6.QtCore.QRegularExpression], [], [], [], [], [], [], [],
        [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression]
    ]]
    # scaleRoleReplaceChanged(QString)
    scaleRoleReplaceChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # xPosRoleChanged(QString)
    xPosRoleChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # xPosRolePatternChanged(QRegularExpression)
    xPosRolePatternChanged: typing.ClassVar[Signal[
        [PySide6.QtCore.QRegularExpression], [], [], [], [], [], [], [],
        [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression]
    ]]
    # xPosRoleReplaceChanged(QString)
    xPosRoleReplaceChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # yPosRoleChanged(QString)
    yPosRoleChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # yPosRolePatternChanged(QRegularExpression)
    yPosRolePatternChanged: typing.ClassVar[Signal[
        [PySide6.QtCore.QRegularExpression], [], [], [], [], [], [], [],
        [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression]
    ]]
    # yPosRoleReplaceChanged(QString)
    yPosRoleReplaceChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # zPosRoleChanged(QString)
    zPosRoleChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # zPosRolePatternChanged(QRegularExpression)
    zPosRolePatternChanged: typing.ClassVar[Signal[
        [PySide6.QtCore.QRegularExpression], [], [], [], [], [], [], [],
        [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression]
    ]]
    # zPosRoleReplaceChanged(QString)
    zPosRoleReplaceChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]

    @typing.overload
    def __init__(self, itemModel: PySide6.QtCore.QAbstractItemModel, xPosRole: str, yPosRole: str, zPosRole: str, rotationRole: str, /, parent: PySide6.QtCore.QObject | None = ..., *, scaleRole: str | None = ..., xPosRolePattern: PySide6.QtCore.QRegularExpression | None = ..., yPosRolePattern: PySide6.QtCore.QRegularExpression | None = ..., zPosRolePattern: PySide6.QtCore.QRegularExpression | None = ..., rotationRolePattern: PySide6.QtCore.QRegularExpression | None = ..., scaleRolePattern: PySide6.QtCore.QRegularExpression | None = ..., xPosRoleReplace: str | None = ..., yPosRoleReplace: str | None = ..., zPosRoleReplace: str | None = ..., rotationRoleReplace: str | None = ..., scaleRoleReplace: str | None = ...) -> None: ...
    @typing.overload
    def __init__(self, itemModel: PySide6.QtCore.QAbstractItemModel, xPosRole: str, yPosRole: str, zPosRole: str, /, parent: PySide6.QtCore.QObject | None = ..., *, rotationRole: str | None = ..., scaleRole: str | None = ..., xPosRolePattern: PySide6.QtCore.QRegularExpression | None = ..., yPosRolePattern: PySide6.QtCore.QRegularExpression | None = ..., zPosRolePattern: PySide6.QtCore.QRegularExpression | None = ..., rotationRolePattern: PySide6.QtCore.QRegularExpression | None = ..., scaleRolePattern: PySide6.QtCore.QRegularExpression | None = ..., xPosRoleReplace: str | None = ..., yPosRoleReplace: str | None = ..., zPosRoleReplace: str | None = ..., rotationRoleReplace: str | None = ..., scaleRoleReplace: str | None = ...) -> None: ...
    @typing.overload
    def __init__(self, itemModel: PySide6.QtCore.QAbstractItemModel, /, parent: PySide6.QtCore.QObject | None = ..., *, xPosRole: str | None = ..., yPosRole: str | None = ..., zPosRole: str | None = ..., rotationRole: str | None = ..., scaleRole: str | None = ..., xPosRolePattern: PySide6.QtCore.QRegularExpression | None = ..., yPosRolePattern: PySide6.QtCore.QRegularExpression | None = ..., zPosRolePattern: PySide6.QtCore.QRegularExpression | None = ..., rotationRolePattern: PySide6.QtCore.QRegularExpression | None = ..., scaleRolePattern: PySide6.QtCore.QRegularExpression | None = ..., xPosRoleReplace: str | None = ..., yPosRoleReplace: str | None = ..., zPosRoleReplace: str | None = ..., rotationRoleReplace: str | None = ..., scaleRoleReplace: str | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., *, itemModel: PySide6.QtCore.QAbstractItemModel | None = ..., xPosRole: str | None = ..., yPosRole: str | None = ..., zPosRole: str | None = ..., rotationRole: str | None = ..., scaleRole: str | None = ..., xPosRolePattern: PySide6.QtCore.QRegularExpression | None = ..., yPosRolePattern: PySide6.QtCore.QRegularExpression | None = ..., zPosRolePattern: PySide6.QtCore.QRegularExpression | None = ..., rotationRolePattern: PySide6.QtCore.QRegularExpression | None = ..., scaleRolePattern: PySide6.QtCore.QRegularExpression | None = ..., xPosRoleReplace: str | None = ..., yPosRoleReplace: str | None = ..., zPosRoleReplace: str | None = ..., rotationRoleReplace: str | None = ..., scaleRoleReplace: str | None = ...) -> None: ...

    def itemModel(self, /) -> PySide6.QtCore.QAbstractItemModel: ...
    @typing.overload
    def remap(self, xPosRole: str, yPosRole: str, zPosRole: str, rotationRole: str, /) -> None: ...
    @typing.overload
    def remap(self, xPosRole: str, yPosRole: str, zPosRole: str, rotationRole: str, scaleRole: str, /) -> None: ...
    def rotationRole(self, /) -> str: ...
    def rotationRolePattern(self, /) -> PySide6.QtCore.QRegularExpression: ...
    def rotationRoleReplace(self, /) -> str: ...
    def scaleRole(self, /) -> str: ...
    def scaleRolePattern(self, /) -> PySide6.QtCore.QRegularExpression: ...
    def scaleRoleReplace(self, /) -> str: ...
    def setItemModel(self, itemModel: PySide6.QtCore.QAbstractItemModel, /) -> None: ...
    def setRotationRole(self, role: str, /) -> None: ...
    def setRotationRolePattern(self, pattern: PySide6.QtCore.QRegularExpression | str, /) -> None: ...
    def setRotationRoleReplace(self, replace: str, /) -> None: ...
    def setScaleRole(self, role: str, /) -> None: ...
    def setScaleRolePattern(self, pattern: PySide6.QtCore.QRegularExpression | str, /) -> None: ...
    def setScaleRoleReplace(self, replace: str, /) -> None: ...
    def setXPosRole(self, role: str, /) -> None: ...
    def setXPosRolePattern(self, pattern: PySide6.QtCore.QRegularExpression | str, /) -> None: ...
    def setXPosRoleReplace(self, replace: str, /) -> None: ...
    def setYPosRole(self, role: str, /) -> None: ...
    def setYPosRolePattern(self, pattern: PySide6.QtCore.QRegularExpression | str, /) -> None: ...
    def setYPosRoleReplace(self, replace: str, /) -> None: ...
    def setZPosRole(self, role: str, /) -> None: ...
    def setZPosRolePattern(self, pattern: PySide6.QtCore.QRegularExpression | str, /) -> None: ...
    def setZPosRoleReplace(self, replace: str, /) -> None: ...
    def xPosRole(self, /) -> str: ...
    def xPosRolePattern(self, /) -> PySide6.QtCore.QRegularExpression: ...
    def xPosRoleReplace(self, /) -> str: ...
    def yPosRole(self, /) -> str: ...
    def yPosRolePattern(self, /) -> PySide6.QtCore.QRegularExpression: ...
    def yPosRoleReplace(self, /) -> str: ...
    def zPosRole(self, /) -> str: ...
    def zPosRolePattern(self, /) -> PySide6.QtCore.QRegularExpression: ...
    def zPosRoleReplace(self, /) -> str: ...


class QItemModelSurfaceDataProxy(PySide6.QtGraphs.QSurfaceDataProxy):
    # autoColumnCategoriesChanged(bool)
    autoColumnCategoriesChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # autoRowCategoriesChanged(bool)
    autoRowCategoriesChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # columnCategoriesChanged()
    columnCategoriesChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # columnRoleChanged(QString)
    columnRoleChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # columnRolePatternChanged(QRegularExpression)
    columnRolePatternChanged: typing.ClassVar[Signal[
        [PySide6.QtCore.QRegularExpression], [], [], [], [], [], [], [],
        [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression]
    ]]
    # columnRoleReplaceChanged(QString)
    columnRoleReplaceChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # itemModelChanged(const QAbstractItemModel*)
    itemModelChanged: typing.ClassVar[Signal[
        [typing.Any], [], [], [], [], [], [], [],
        [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any], [typing.Any]
    ]]
    # multiMatchBehaviorChanged(QItemModelSurfaceDataProxy::MultiMatchBehavior)
    multiMatchBehaviorChanged: typing.ClassVar[Signal[
        [PySide6.QtGraphs.QItemModelSurfaceDataProxy.MultiMatchBehavior], [], [], [], [], [], [], [],
        [PySide6.QtGraphs.QItemModelSurfaceDataProxy.MultiMatchBehavior], [PySide6.QtGraphs.QItemModelSurfaceDataProxy.MultiMatchBehavior], [PySide6.QtGraphs.QItemModelSurfaceDataProxy.MultiMatchBehavior], [PySide6.QtGraphs.QItemModelSurfaceDataProxy.MultiMatchBehavior], [PySide6.QtGraphs.QItemModelSurfaceDataProxy.MultiMatchBehavior], [PySide6.QtGraphs.QItemModelSurfaceDataProxy.MultiMatchBehavior], [PySide6.QtGraphs.QItemModelSurfaceDataProxy.MultiMatchBehavior], [PySide6.QtGraphs.QItemModelSurfaceDataProxy.MultiMatchBehavior]
    ]]
    # rowCategoriesChanged()
    rowCategoriesChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # rowRoleChanged(QString)
    rowRoleChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # rowRolePatternChanged(QRegularExpression)
    rowRolePatternChanged: typing.ClassVar[Signal[
        [PySide6.QtCore.QRegularExpression], [], [], [], [], [], [], [],
        [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression]
    ]]
    # rowRoleReplaceChanged(QString)
    rowRoleReplaceChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # useModelCategoriesChanged(bool)
    useModelCategoriesChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # xPosRoleChanged(QString)
    xPosRoleChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # xPosRolePatternChanged(QRegularExpression)
    xPosRolePatternChanged: typing.ClassVar[Signal[
        [PySide6.QtCore.QRegularExpression], [], [], [], [], [], [], [],
        [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression]
    ]]
    # xPosRoleReplaceChanged(QString)
    xPosRoleReplaceChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # yPosRoleChanged(QString)
    yPosRoleChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # yPosRolePatternChanged(QRegularExpression)
    yPosRolePatternChanged: typing.ClassVar[Signal[
        [PySide6.QtCore.QRegularExpression], [], [], [], [], [], [], [],
        [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression]
    ]]
    # yPosRoleReplaceChanged(QString)
    yPosRoleReplaceChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # zPosRoleChanged(QString)
    zPosRoleChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # zPosRolePatternChanged(QRegularExpression)
    zPosRolePatternChanged: typing.ClassVar[Signal[
        [PySide6.QtCore.QRegularExpression], [], [], [], [], [], [], [],
        [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression], [PySide6.QtCore.QRegularExpression]
    ]]
    # zPosRoleReplaceChanged(QString)
    zPosRoleReplaceChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]

    class MultiMatchBehavior(enum.Enum):
        First                     = 0x0
        Last                      = 0x1
        Average                   = 0x2
        CumulativeY               = 0x3

    @typing.overload
    def __init__(self, itemModel: PySide6.QtCore.QAbstractItemModel, rowRole: str, columnRole: str, xPosRole: str, yPosRole: str, zPosRole: str, rowCategories: collections.abc.Sequence[str], columnCategories: collections.abc.Sequence[str], /, parent: PySide6.QtCore.QObject | None = ..., *, useModelCategories: bool | None = ..., autoRowCategories: bool | None = ..., autoColumnCategories: bool | None = ..., rowRolePattern: PySide6.QtCore.QRegularExpression | None = ..., columnRolePattern: PySide6.QtCore.QRegularExpression | None = ..., xPosRolePattern: PySide6.QtCore.QRegularExpression | None = ..., yPosRolePattern: PySide6.QtCore.QRegularExpression | None = ..., zPosRolePattern: PySide6.QtCore.QRegularExpression | None = ..., rowRoleReplace: str | None = ..., columnRoleReplace: str | None = ..., xPosRoleReplace: str | None = ..., yPosRoleReplace: str | None = ..., zPosRoleReplace: str | None = ..., multiMatchBehavior: PySide6.QtGraphs.QItemModelSurfaceDataProxy.MultiMatchBehavior | None = ...) -> None: ...
    @typing.overload
    def __init__(self, itemModel: PySide6.QtCore.QAbstractItemModel, rowRole: str, columnRole: str, xPosRole: str, yPosRole: str, zPosRole: str, /, parent: PySide6.QtCore.QObject | None = ..., *, rowCategories: collections.abc.Sequence[str] | None = ..., columnCategories: collections.abc.Sequence[str] | None = ..., useModelCategories: bool | None = ..., autoRowCategories: bool | None = ..., autoColumnCategories: bool | None = ..., rowRolePattern: PySide6.QtCore.QRegularExpression | None = ..., columnRolePattern: PySide6.QtCore.QRegularExpression | None = ..., xPosRolePattern: PySide6.QtCore.QRegularExpression | None = ..., yPosRolePattern: PySide6.QtCore.QRegularExpression | None = ..., zPosRolePattern: PySide6.QtCore.QRegularExpression | None = ..., rowRoleReplace: str | None = ..., columnRoleReplace: str | None = ..., xPosRoleReplace: str | None = ..., yPosRoleReplace: str | None = ..., zPosRoleReplace: str | None = ..., multiMatchBehavior: PySide6.QtGraphs.QItemModelSurfaceDataProxy.MultiMatchBehavior | None = ...) -> None: ...
    @typing.overload
    def __init__(self, itemModel: PySide6.QtCore.QAbstractItemModel, rowRole: str, columnRole: str, yPosRole: str, rowCategories: collections.abc.Sequence[str], columnCategories: collections.abc.Sequence[str], /, parent: PySide6.QtCore.QObject | None = ..., *, xPosRole: str | None = ..., zPosRole: str | None = ..., useModelCategories: bool | None = ..., autoRowCategories: bool | None = ..., autoColumnCategories: bool | None = ..., rowRolePattern: PySide6.QtCore.QRegularExpression | None = ..., columnRolePattern: PySide6.QtCore.QRegularExpression | None = ..., xPosRolePattern: PySide6.QtCore.QRegularExpression | None = ..., yPosRolePattern: PySide6.QtCore.QRegularExpression | None = ..., zPosRolePattern: PySide6.QtCore.QRegularExpression | None = ..., rowRoleReplace: str | None = ..., columnRoleReplace: str | None = ..., xPosRoleReplace: str | None = ..., yPosRoleReplace: str | None = ..., zPosRoleReplace: str | None = ..., multiMatchBehavior: PySide6.QtGraphs.QItemModelSurfaceDataProxy.MultiMatchBehavior | None = ...) -> None: ...
    @typing.overload
    def __init__(self, itemModel: PySide6.QtCore.QAbstractItemModel, rowRole: str, columnRole: str, yPosRole: str, /, parent: PySide6.QtCore.QObject | None = ..., *, xPosRole: str | None = ..., zPosRole: str | None = ..., rowCategories: collections.abc.Sequence[str] | None = ..., columnCategories: collections.abc.Sequence[str] | None = ..., useModelCategories: bool | None = ..., autoRowCategories: bool | None = ..., autoColumnCategories: bool | None = ..., rowRolePattern: PySide6.QtCore.QRegularExpression | None = ..., columnRolePattern: PySide6.QtCore.QRegularExpression | None = ..., xPosRolePattern: PySide6.QtCore.QRegularExpression | None = ..., yPosRolePattern: PySide6.QtCore.QRegularExpression | None = ..., zPosRolePattern: PySide6.QtCore.QRegularExpression | None = ..., rowRoleReplace: str | None = ..., columnRoleReplace: str | None = ..., xPosRoleReplace: str | None = ..., yPosRoleReplace: str | None = ..., zPosRoleReplace: str | None = ..., multiMatchBehavior: PySide6.QtGraphs.QItemModelSurfaceDataProxy.MultiMatchBehavior | None = ...) -> None: ...
    @typing.overload
    def __init__(self, itemModel: PySide6.QtCore.QAbstractItemModel, yPosRole: str, /, parent: PySide6.QtCore.QObject | None = ..., *, rowRole: str | None = ..., columnRole: str | None = ..., xPosRole: str | None = ..., zPosRole: str | None = ..., rowCategories: collections.abc.Sequence[str] | None = ..., columnCategories: collections.abc.Sequence[str] | None = ..., useModelCategories: bool | None = ..., autoRowCategories: bool | None = ..., autoColumnCategories: bool | None = ..., rowRolePattern: PySide6.QtCore.QRegularExpression | None = ..., columnRolePattern: PySide6.QtCore.QRegularExpression | None = ..., xPosRolePattern: PySide6.QtCore.QRegularExpression | None = ..., yPosRolePattern: PySide6.QtCore.QRegularExpression | None = ..., zPosRolePattern: PySide6.QtCore.QRegularExpression | None = ..., rowRoleReplace: str | None = ..., columnRoleReplace: str | None = ..., xPosRoleReplace: str | None = ..., yPosRoleReplace: str | None = ..., zPosRoleReplace: str | None = ..., multiMatchBehavior: PySide6.QtGraphs.QItemModelSurfaceDataProxy.MultiMatchBehavior | None = ...) -> None: ...
    @typing.overload
    def __init__(self, itemModel: PySide6.QtCore.QAbstractItemModel, /, parent: PySide6.QtCore.QObject | None = ..., *, rowRole: str | None = ..., columnRole: str | None = ..., xPosRole: str | None = ..., yPosRole: str | None = ..., zPosRole: str | None = ..., rowCategories: collections.abc.Sequence[str] | None = ..., columnCategories: collections.abc.Sequence[str] | None = ..., useModelCategories: bool | None = ..., autoRowCategories: bool | None = ..., autoColumnCategories: bool | None = ..., rowRolePattern: PySide6.QtCore.QRegularExpression | None = ..., columnRolePattern: PySide6.QtCore.QRegularExpression | None = ..., xPosRolePattern: PySide6.QtCore.QRegularExpression | None = ..., yPosRolePattern: PySide6.QtCore.QRegularExpression | None = ..., zPosRolePattern: PySide6.QtCore.QRegularExpression | None = ..., rowRoleReplace: str | None = ..., columnRoleReplace: str | None = ..., xPosRoleReplace: str | None = ..., yPosRoleReplace: str | None = ..., zPosRoleReplace: str | None = ..., multiMatchBehavior: PySide6.QtGraphs.QItemModelSurfaceDataProxy.MultiMatchBehavior | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., *, itemModel: PySide6.QtCore.QAbstractItemModel | None = ..., rowRole: str | None = ..., columnRole: str | None = ..., xPosRole: str | None = ..., yPosRole: str | None = ..., zPosRole: str | None = ..., rowCategories: collections.abc.Sequence[str] | None = ..., columnCategories: collections.abc.Sequence[str] | None = ..., useModelCategories: bool | None = ..., autoRowCategories: bool | None = ..., autoColumnCategories: bool | None = ..., rowRolePattern: PySide6.QtCore.QRegularExpression | None = ..., columnRolePattern: PySide6.QtCore.QRegularExpression | None = ..., xPosRolePattern: PySide6.QtCore.QRegularExpression | None = ..., yPosRolePattern: PySide6.QtCore.QRegularExpression | None = ..., zPosRolePattern: PySide6.QtCore.QRegularExpression | None = ..., rowRoleReplace: str | None = ..., columnRoleReplace: str | None = ..., xPosRoleReplace: str | None = ..., yPosRoleReplace: str | None = ..., zPosRoleReplace: str | None = ..., multiMatchBehavior: PySide6.QtGraphs.QItemModelSurfaceDataProxy.MultiMatchBehavior | None = ...) -> None: ...

    def autoColumnCategories(self, /) -> bool: ...
    def autoRowCategories(self, /) -> bool: ...
    def columnCategories(self, /) -> typing.List[str]: ...
    def columnCategoryIndex(self, category: str, /) -> int: ...
    def columnRole(self, /) -> str: ...
    def columnRolePattern(self, /) -> PySide6.QtCore.QRegularExpression: ...
    def columnRoleReplace(self, /) -> str: ...
    def itemModel(self, /) -> PySide6.QtCore.QAbstractItemModel: ...
    def multiMatchBehavior(self, /) -> PySide6.QtGraphs.QItemModelSurfaceDataProxy.MultiMatchBehavior: ...
    def remap(self, rowRole: str, columnRole: str, xPosRole: str, yPosRole: str, zPosRole: str, rowCategories: collections.abc.Sequence[str], columnCategories: collections.abc.Sequence[str], /) -> None: ...
    def rowCategories(self, /) -> typing.List[str]: ...
    def rowCategoryIndex(self, category: str, /) -> int: ...
    def rowRole(self, /) -> str: ...
    def rowRolePattern(self, /) -> PySide6.QtCore.QRegularExpression: ...
    def rowRoleReplace(self, /) -> str: ...
    def setAutoColumnCategories(self, enable: bool, /) -> None: ...
    def setAutoRowCategories(self, enable: bool, /) -> None: ...
    def setColumnCategories(self, categories: collections.abc.Sequence[str], /) -> None: ...
    def setColumnRole(self, role: str, /) -> None: ...
    def setColumnRolePattern(self, pattern: PySide6.QtCore.QRegularExpression | str, /) -> None: ...
    def setColumnRoleReplace(self, replace: str, /) -> None: ...
    def setItemModel(self, itemModel: PySide6.QtCore.QAbstractItemModel, /) -> None: ...
    def setMultiMatchBehavior(self, behavior: PySide6.QtGraphs.QItemModelSurfaceDataProxy.MultiMatchBehavior, /) -> None: ...
    def setRowCategories(self, categories: collections.abc.Sequence[str], /) -> None: ...
    def setRowRole(self, role: str, /) -> None: ...
    def setRowRolePattern(self, pattern: PySide6.QtCore.QRegularExpression | str, /) -> None: ...
    def setRowRoleReplace(self, replace: str, /) -> None: ...
    def setUseModelCategories(self, enable: bool, /) -> None: ...
    def setXPosRole(self, role: str, /) -> None: ...
    def setXPosRolePattern(self, pattern: PySide6.QtCore.QRegularExpression | str, /) -> None: ...
    def setXPosRoleReplace(self, replace: str, /) -> None: ...
    def setYPosRole(self, role: str, /) -> None: ...
    def setYPosRolePattern(self, pattern: PySide6.QtCore.QRegularExpression | str, /) -> None: ...
    def setYPosRoleReplace(self, replace: str, /) -> None: ...
    def setZPosRole(self, role: str, /) -> None: ...
    def setZPosRolePattern(self, pattern: PySide6.QtCore.QRegularExpression | str, /) -> None: ...
    def setZPosRoleReplace(self, replace: str, /) -> None: ...
    def useModelCategories(self, /) -> bool: ...
    def xPosRole(self, /) -> str: ...
    def xPosRolePattern(self, /) -> PySide6.QtCore.QRegularExpression: ...
    def xPosRoleReplace(self, /) -> str: ...
    def yPosRole(self, /) -> str: ...
    def yPosRolePattern(self, /) -> PySide6.QtCore.QRegularExpression: ...
    def yPosRoleReplace(self, /) -> str: ...
    def zPosRole(self, /) -> str: ...
    def zPosRolePattern(self, /) -> PySide6.QtCore.QRegularExpression: ...
    def zPosRoleReplace(self, /) -> str: ...


class QLegendData(Shiboken.Object):
    @property
    def borderColor(self) -> PySide6.QtGui.QColor: ...
    @borderColor.setter
    def borderColor(self, borderColor: PySide6.QtGui.QColor) -> None: ...
    @property
    def color(self) -> PySide6.QtGui.QColor: ...
    @color.setter
    def color(self, color: PySide6.QtGui.QColor) -> None: ...
    @property
    def label(self) -> str: ...
    @label.setter
    def label(self, label: str) -> None: ...

    @typing.overload
    def __init__(self, /) -> None: ...
    @typing.overload
    def __init__(self, QLegendData: PySide6.QtGraphs.QLegendData, /) -> None: ...

    def __copy__(self, /) -> typing.Self: ...


class QLineSeries(PySide6.QtGraphs.QXYSeries):
    # capStyleChanged()
    capStyleChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # dashOffsetChanged(double)
    dashOffsetChanged: typing.ClassVar[Signal[
        [float], [], [], [], [], [], [], [],
        [float], [float], [float], [float], [float], [float], [float], [float]
    ]]
    # dashPatternChanged(QList<qreal>)
    dashPatternChanged: typing.ClassVar[Signal[
        [collections.abc.Sequence[float]], [], [], [], [], [], [], [],
        [collections.abc.Sequence[float]], [collections.abc.Sequence[float]], [collections.abc.Sequence[float]], [collections.abc.Sequence[float]], [collections.abc.Sequence[float]], [collections.abc.Sequence[float]], [collections.abc.Sequence[float]], [collections.abc.Sequence[float]]
    ]]
    # joinStyleChanged(Qt::PenJoinStyle)
    joinStyleChanged: typing.ClassVar[Signal[
        [PySide6.QtCore.Qt.PenJoinStyle], [], [], [], [], [], [], [],
        [PySide6.QtCore.Qt.PenJoinStyle], [PySide6.QtCore.Qt.PenJoinStyle], [PySide6.QtCore.Qt.PenJoinStyle], [PySide6.QtCore.Qt.PenJoinStyle], [PySide6.QtCore.Qt.PenJoinStyle], [PySide6.QtCore.Qt.PenJoinStyle], [PySide6.QtCore.Qt.PenJoinStyle], [PySide6.QtCore.Qt.PenJoinStyle]
    ]]
    # lineStyleChanged(QLineSeries::LineStyle)
    lineStyleChanged: typing.ClassVar[Signal[
        [PySide6.QtGraphs.QLineSeries.LineStyle], [], [], [], [], [], [], [],
        [PySide6.QtGraphs.QLineSeries.LineStyle], [PySide6.QtGraphs.QLineSeries.LineStyle], [PySide6.QtGraphs.QLineSeries.LineStyle], [PySide6.QtGraphs.QLineSeries.LineStyle], [PySide6.QtGraphs.QLineSeries.LineStyle], [PySide6.QtGraphs.QLineSeries.LineStyle], [PySide6.QtGraphs.QLineSeries.LineStyle], [PySide6.QtGraphs.QLineSeries.LineStyle]
    ]]
    # strokeStyleChanged(QLineSeries::StrokeStyle)
    strokeStyleChanged: typing.ClassVar[Signal[
        [PySide6.QtGraphs.QLineSeries.StrokeStyle], [], [], [], [], [], [], [],
        [PySide6.QtGraphs.QLineSeries.StrokeStyle], [PySide6.QtGraphs.QLineSeries.StrokeStyle], [PySide6.QtGraphs.QLineSeries.StrokeStyle], [PySide6.QtGraphs.QLineSeries.StrokeStyle], [PySide6.QtGraphs.QLineSeries.StrokeStyle], [PySide6.QtGraphs.QLineSeries.StrokeStyle], [PySide6.QtGraphs.QLineSeries.StrokeStyle], [PySide6.QtGraphs.QLineSeries.StrokeStyle]
    ]]
    # widthChanged()
    widthChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]

    class LineStyle(enum.Enum):
        Straight                  = 0x0
        StepLeft                  = 0x1
        StepRight                 = 0x2
        StepCenter                = 0x3

    class StrokeStyle(enum.Enum):
        SolidLine                 = 0x1
        DashLine                  = 0x2

    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., *, width: float | None = ..., capStyle: PySide6.QtCore.Qt.PenCapStyle | None = ..., joinStyle: PySide6.QtCore.Qt.PenJoinStyle | None = ..., lineStyle: PySide6.QtGraphs.QLineSeries.LineStyle | None = ..., strokeStyle: PySide6.QtGraphs.QLineSeries.StrokeStyle | None = ..., dashOffset: float | None = ..., dashPattern: collections.abc.Sequence[float] | None = ...) -> None: ...

    def capStyle(self, /) -> PySide6.QtCore.Qt.PenCapStyle: ...
    def componentComplete(self, /) -> None: ...
    def dashOffset(self, /) -> float: ...
    def dashPattern(self, /) -> typing.List[float]: ...
    def dataPointCoordinatesAt(self, x: float, y: float, /) -> PySide6.QtCore.QPointF: ...
    def joinStyle(self, /) -> PySide6.QtCore.Qt.PenJoinStyle: ...
    def lineStyle(self, /) -> PySide6.QtGraphs.QLineSeries.LineStyle: ...
    def setCapStyle(self, newCapStyle: PySide6.QtCore.Qt.PenCapStyle, /) -> None: ...
    def setDashOffset(self, newDashOffset: float, /) -> None: ...
    def setDashPattern(self, pattern: collections.abc.Sequence[float], /) -> None: ...
    def setJoinStyle(self, newJoinStyle: PySide6.QtCore.Qt.PenJoinStyle, /) -> None: ...
    def setLineStyle(self, newLineStyle: PySide6.QtGraphs.QLineSeries.LineStyle, /) -> None: ...
    def setStrokeStyle(self, newStrokeStyle: PySide6.QtGraphs.QLineSeries.StrokeStyle, /) -> None: ...
    def setWidth(self, newWidth: float, /) -> None: ...
    def strokeStyle(self, /) -> PySide6.QtGraphs.QLineSeries.StrokeStyle: ...
    def type(self, /) -> PySide6.QtGraphs.QAbstractSeries.SeriesType: ...
    def width(self, /) -> float: ...


class QLogValue3DAxisFormatter(PySide6.QtGraphs.QValue3DAxisFormatter):
    # autoSubGridChanged(bool)
    autoSubGridChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # baseChanged(double)
    baseChanged: typing.ClassVar[Signal[
        [float], [], [], [], [], [], [], [],
        [float], [float], [float], [float], [float], [float], [float], [float]
    ]]
    # edgeLabelsVisibleChanged(bool)
    edgeLabelsVisibleChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]

    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., *, base: float | None = ..., autoSubGrid: bool | None = ..., edgeLabelsVisible: bool | None = ...) -> None: ...

    def autoSubGrid(self, /) -> bool: ...
    def base(self, /) -> float: ...
    def createNewInstance(self, /) -> PySide6.QtGraphs.QValue3DAxisFormatter: ...
    def edgeLabelsVisible(self, /) -> bool: ...
    def populateCopy(self, copy: PySide6.QtGraphs.QValue3DAxisFormatter, /) -> None: ...
    def positionAt(self, value: float, /) -> float: ...
    def recalculate(self, /) -> None: ...
    def setAutoSubGrid(self, enabled: bool, /) -> None: ...
    def setBase(self, base: float, /) -> None: ...
    def setEdgeLabelsVisible(self, enabled: bool, /) -> None: ...
    def valueAt(self, position: float, /) -> float: ...


class QPieModelMapper(PySide6.QtCore.QObject):
    # countChanged()
    countChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # firstChanged()
    firstChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # labelsSectionChanged()
    labelsSectionChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # modelChanged()
    modelChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # orientationChanged()
    orientationChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # seriesChanged()
    seriesChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # valuesSectionChanged()
    valuesSectionChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]

    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., *, series: PySide6.QtGraphs.QPieSeries | None = ..., model: PySide6.QtCore.QAbstractItemModel | None = ..., valuesSection: int | None = ..., labelsSection: int | None = ..., first: int | None = ..., count: int | None = ..., orientation: PySide6.QtCore.Qt.Orientation | None = ...) -> None: ...

    def count(self, /) -> int: ...
    def first(self, /) -> int: ...
    def labelsSection(self, /) -> int: ...
    def model(self, /) -> PySide6.QtCore.QAbstractItemModel: ...
    def onSliceLabelChanged(self, /) -> None: ...
    def onSliceValueChanged(self, /) -> None: ...
    def orientation(self, /) -> PySide6.QtCore.Qt.Orientation: ...
    def series(self, /) -> PySide6.QtGraphs.QPieSeries: ...
    def setCount(self, count: int, /) -> None: ...
    def setFirst(self, first: int, /) -> None: ...
    def setLabelsSection(self, labelsSection: int, /) -> None: ...
    def setModel(self, model: PySide6.QtCore.QAbstractItemModel, /) -> None: ...
    def setOrientation(self, orientation: PySide6.QtCore.Qt.Orientation, /) -> None: ...
    def setSeries(self, series: PySide6.QtGraphs.QPieSeries, /) -> None: ...
    def setValuesSection(self, valuesSection: int, /) -> None: ...
    def valuesSection(self, /) -> int: ...


class QPieSeries(PySide6.QtGraphs.QAbstractSeries):
    # added(QList<QPieSlice*>)
    added: typing.ClassVar[Signal[
        [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [], [], [], [], [], [], [],
        [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]]
    ]]
    # angleSpanLabelVisibilityChanged(LabelVisibility)
    angleSpanLabelVisibilityChanged: typing.ClassVar[Signal[
        [LabelVisibility], [], [], [], [], [], [], [],
        [LabelVisibility], [LabelVisibility], [LabelVisibility], [LabelVisibility], [LabelVisibility], [LabelVisibility], [LabelVisibility], [LabelVisibility]
    ]]
    # angleSpanVisibleLimitChanged(double)
    angleSpanVisibleLimitChanged: typing.ClassVar[Signal[
        [float], [], [], [], [], [], [], [],
        [float], [float], [float], [float], [float], [float], [float], [float]
    ]]
    # clicked(QPieSlice*)
    clicked: typing.ClassVar[Signal[
        [PySide6.QtGraphs.QPieSlice], [], [], [], [], [], [], [],
        [PySide6.QtGraphs.QPieSlice], [PySide6.QtGraphs.QPieSlice], [PySide6.QtGraphs.QPieSlice], [PySide6.QtGraphs.QPieSlice], [PySide6.QtGraphs.QPieSlice], [PySide6.QtGraphs.QPieSlice], [PySide6.QtGraphs.QPieSlice], [PySide6.QtGraphs.QPieSlice]
    ]]
    # countChanged()
    countChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # doubleClicked(QPieSlice*)
    doubleClicked: typing.ClassVar[Signal[
        [PySide6.QtGraphs.QPieSlice], [], [], [], [], [], [], [],
        [PySide6.QtGraphs.QPieSlice], [PySide6.QtGraphs.QPieSlice], [PySide6.QtGraphs.QPieSlice], [PySide6.QtGraphs.QPieSlice], [PySide6.QtGraphs.QPieSlice], [PySide6.QtGraphs.QPieSlice], [PySide6.QtGraphs.QPieSlice], [PySide6.QtGraphs.QPieSlice]
    ]]
    # endAngleChanged()
    endAngleChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # holeSizeChanged()
    holeSizeChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # horizontalPositionChanged()
    horizontalPositionChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # pieSizeChanged()
    pieSizeChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # pressed(QPieSlice*)
    pressed: typing.ClassVar[Signal[
        [PySide6.QtGraphs.QPieSlice], [], [], [], [], [], [], [],
        [PySide6.QtGraphs.QPieSlice], [PySide6.QtGraphs.QPieSlice], [PySide6.QtGraphs.QPieSlice], [PySide6.QtGraphs.QPieSlice], [PySide6.QtGraphs.QPieSlice], [PySide6.QtGraphs.QPieSlice], [PySide6.QtGraphs.QPieSlice], [PySide6.QtGraphs.QPieSlice]
    ]]
    # released(QPieSlice*)
    released: typing.ClassVar[Signal[
        [PySide6.QtGraphs.QPieSlice], [], [], [], [], [], [], [],
        [PySide6.QtGraphs.QPieSlice], [PySide6.QtGraphs.QPieSlice], [PySide6.QtGraphs.QPieSlice], [PySide6.QtGraphs.QPieSlice], [PySide6.QtGraphs.QPieSlice], [PySide6.QtGraphs.QPieSlice], [PySide6.QtGraphs.QPieSlice], [PySide6.QtGraphs.QPieSlice]
    ]]
    # removed(QList<QPieSlice*>)
    removed: typing.ClassVar[Signal[
        [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [], [], [], [], [], [], [],
        [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]]
    ]]
    # replaced(QList<QPieSlice*>)
    replaced: typing.ClassVar[Signal[
        [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [], [], [], [], [], [], [],
        [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]]
    ]]
    # startAngleChanged()
    startAngleChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # sumChanged()
    sumChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # verticalPositionChanged()
    verticalPositionChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]

    class LabelVisibility(enum.Enum):
        None_                     = 0x0
        First                     = 0x1
        Even                      = 0x2
        Odd                       = 0x3

    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., *, horizontalPosition: float | None = ..., verticalPosition: float | None = ..., pieSize: float | None = ..., startAngle: float | None = ..., endAngle: float | None = ..., count: int | None = ..., sum: float | None = ..., holeSize: float | None = ..., angleSpanVisibleLimit: float | None = ..., angleSpanLabelVisibility: PySide6.QtGraphs.QPieSeries.LabelVisibility | None = ...) -> None: ...

    def __lshift__(self, slice: PySide6.QtGraphs.QPieSlice, /) -> PySide6.QtGraphs.QPieSeries: ...
    def angleSpanLabelVisibility(self, /) -> PySide6.QtGraphs.QPieSeries.LabelVisibility: ...
    def angleSpanVisibleLimit(self, /) -> float: ...
    @typing.overload
    def append(self, slice: PySide6.QtGraphs.QPieSlice, /) -> bool: ...
    @typing.overload
    def append(self, label: str, value: float, /) -> PySide6.QtGraphs.QPieSlice: ...
    @typing.overload
    def append(self, slices: collections.abc.Sequence[PySide6.QtGraphs.QPieSlice], /) -> bool: ...
    def at(self, index: int, /) -> PySide6.QtGraphs.QPieSlice: ...
    def clear(self, /) -> None: ...
    def componentComplete(self, /) -> None: ...
    def count(self, /) -> int: ...
    def endAngle(self, /) -> float: ...
    def find(self, label: str, /) -> PySide6.QtGraphs.QPieSlice: ...
    def handleSliceChange(self, /) -> None: ...
    def holeSize(self, /) -> float: ...
    def horizontalPosition(self, /) -> float: ...
    def insert(self, index: int, slice: PySide6.QtGraphs.QPieSlice, /) -> bool: ...
    def isEmpty(self, /) -> bool: ...
    def pieSize(self, /) -> float: ...
    @typing.overload
    def remove(self, slice: PySide6.QtGraphs.QPieSlice, /) -> bool: ...
    @typing.overload
    def remove(self, index: int, /) -> bool: ...
    def removeMultiple(self, index: int, count: int, /) -> None: ...
    @typing.overload
    def replace(self, oldSlice: PySide6.QtGraphs.QPieSlice, newSlice: PySide6.QtGraphs.QPieSlice, /) -> bool: ...
    @typing.overload
    def replace(self, slices: collections.abc.Sequence[PySide6.QtGraphs.QPieSlice], /) -> bool: ...
    @typing.overload
    def replace(self, index: int, slice: PySide6.QtGraphs.QPieSlice, /) -> bool: ...
    def setAngleSpanLabelVisibility(self, newAngleSpanVisibleMode: PySide6.QtGraphs.QPieSeries.LabelVisibility, /) -> None: ...
    def setAngleSpanVisibleLimit(self, newAngleSpanVisibleLimit: float, /) -> None: ...
    def setEndAngle(self, endAngle: float, /) -> None: ...
    def setHoleSize(self, holeSize: float, /) -> None: ...
    def setHorizontalPosition(self, relativePosition: float, /) -> None: ...
    def setLabelsPosition(self, position: PySide6.QtGraphs.QPieSlice.LabelPosition, /) -> None: ...
    def setLabelsVisible(self, visible: bool, /) -> None: ...
    def setPieSize(self, relativeSize: float, /) -> None: ...
    def setStartAngle(self, startAngle: float, /) -> None: ...
    def setVerticalPosition(self, relativePosition: float, /) -> None: ...
    def slices(self, /) -> typing.List[PySide6.QtGraphs.QPieSlice]: ...
    def startAngle(self, /) -> float: ...
    def sum(self, /) -> float: ...
    def take(self, slice: PySide6.QtGraphs.QPieSlice, /) -> bool: ...
    def type(self, /) -> PySide6.QtGraphs.QAbstractSeries.SeriesType: ...
    def verticalPosition(self, /) -> float: ...


class QPieSlice(PySide6.QtCore.QObject):
    # angleSpanChanged()
    angleSpanChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # borderColorChanged()
    borderColorChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # borderWidthChanged()
    borderWidthChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # colorChanged()
    colorChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # explodeDistanceFactorChanged()
    explodeDistanceFactorChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # explodedChanged()
    explodedChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # labelArmLengthFactorChanged()
    labelArmLengthFactorChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # labelChanged()
    labelChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # labelColorChanged()
    labelColorChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # labelFontChanged()
    labelFontChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # labelPositionChanged()
    labelPositionChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # labelVisibleChanged()
    labelVisibleChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # percentageChanged()
    percentageChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # sliceChanged()
    sliceChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # startAngleChanged()
    startAngleChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # subSlicesAdded(QList<QPieSlice*>)
    subSlicesAdded: typing.ClassVar[Signal[
        [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [], [], [], [], [], [], [],
        [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]]
    ]]
    # subSlicesCountChanged(qsizetype)
    subSlicesCountChanged: typing.ClassVar[Signal[
        [int], [], [], [], [], [], [], [],
        [int], [int], [int], [int], [int], [int], [int], [int]
    ]]
    # subSlicesRatioChanged(double)
    subSlicesRatioChanged: typing.ClassVar[Signal[
        [float], [], [], [], [], [], [], [],
        [float], [float], [float], [float], [float], [float], [float], [float]
    ]]
    # subSlicesRemoved(QList<QPieSlice*>)
    subSlicesRemoved: typing.ClassVar[Signal[
        [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [], [], [], [], [], [], [],
        [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]]
    ]]
    # subSlicesReplaced(QList<QPieSlice*>)
    subSlicesReplaced: typing.ClassVar[Signal[
        [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [], [], [], [], [], [], [],
        [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]], [collections.abc.Sequence[PySide6.QtGraphs.QPieSlice]]
    ]]
    # subSlicesSumChanged(double)
    subSlicesSumChanged: typing.ClassVar[Signal[
        [float], [], [], [], [], [], [], [],
        [float], [float], [float], [float], [float], [float], [float], [float]
    ]]
    # valueChanged()
    valueChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]

    class LabelPosition(enum.Enum):
        Outside                   = 0x0
        InsideHorizontal          = 0x1
        InsideTangential          = 0x2
        InsideNormal              = 0x3

    @typing.overload
    def __init__(self, label: str, value: float, /, parent: PySide6.QtCore.QObject | None = ..., *, labelVisible: bool | None = ..., labelPosition: PySide6.QtGraphs.QPieSlice.LabelPosition | None = ..., labelColor: PySide6.QtGui.QColor | None = ..., labelFont: PySide6.QtGui.QFont | None = ..., labelArmLengthFactor: float | None = ..., color: PySide6.QtGui.QColor | None = ..., borderColor: PySide6.QtGui.QColor | None = ..., borderWidth: float | None = ..., exploded: bool | None = ..., explodeDistanceFactor: float | None = ..., percentage: float | None = ..., startAngle: float | None = ..., angleSpan: float | None = ..., subSlicesCount: int | None = ..., subSlicesSum: float | None = ..., subSlicesRatio: float | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., *, label: str | None = ..., labelVisible: bool | None = ..., labelPosition: PySide6.QtGraphs.QPieSlice.LabelPosition | None = ..., labelColor: PySide6.QtGui.QColor | None = ..., labelFont: PySide6.QtGui.QFont | None = ..., labelArmLengthFactor: float | None = ..., color: PySide6.QtGui.QColor | None = ..., borderColor: PySide6.QtGui.QColor | None = ..., borderWidth: float | None = ..., value: float | None = ..., exploded: bool | None = ..., explodeDistanceFactor: float | None = ..., percentage: float | None = ..., startAngle: float | None = ..., angleSpan: float | None = ..., subSlicesCount: int | None = ..., subSlicesSum: float | None = ..., subSlicesRatio: float | None = ...) -> None: ...

    def angleSpan(self, /) -> float: ...
    @typing.overload
    def append(self, slice: PySide6.QtGraphs.QPieSlice, /) -> bool: ...
    @typing.overload
    def append(self, label: str, value: float, /) -> PySide6.QtGraphs.QPieSlice: ...
    @typing.overload
    def append(self, slices: collections.abc.Sequence[PySide6.QtGraphs.QPieSlice], /) -> bool: ...
    def at(self, index: int, /) -> PySide6.QtGraphs.QPieSlice: ...
    def borderColor(self, /) -> PySide6.QtGui.QColor: ...
    def borderWidth(self, /) -> float: ...
    def clear(self, /) -> None: ...
    def color(self, /) -> PySide6.QtGui.QColor: ...
    def explodeDistanceFactor(self, /) -> float: ...
    def find(self, label: str, /) -> PySide6.QtGraphs.QPieSlice: ...
    def insert(self, index: int, slice: PySide6.QtGraphs.QPieSlice, /) -> bool: ...
    def isEmpty(self, /) -> bool: ...
    def isExploded(self, /) -> bool: ...
    def isLabelVisible(self, /) -> bool: ...
    def label(self, /) -> str: ...
    def labelArmLengthFactor(self, /) -> float: ...
    def labelColor(self, /) -> PySide6.QtGui.QColor: ...
    def labelFont(self, /) -> PySide6.QtGui.QFont: ...
    def labelPosition(self, /) -> PySide6.QtGraphs.QPieSlice.LabelPosition: ...
    def percentage(self, /) -> float: ...
    @typing.overload
    def remove(self, slice: PySide6.QtGraphs.QPieSlice, /) -> bool: ...
    @typing.overload
    def remove(self, index: int, /) -> bool: ...
    def removeMultiple(self, index: int, count: int, /) -> None: ...
    @typing.overload
    def replace(self, oldSlice: PySide6.QtGraphs.QPieSlice, newSlice: PySide6.QtGraphs.QPieSlice, /) -> bool: ...
    @typing.overload
    def replace(self, index: int, slice: PySide6.QtGraphs.QPieSlice, /) -> bool: ...
    def replaceAll(self, slices: collections.abc.Sequence[PySide6.QtGraphs.QPieSlice], /) -> bool: ...
    def series(self, /) -> PySide6.QtGraphs.QPieSeries: ...
    def setBorderColor(self, color: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setBorderWidth(self, borderWidth: float, /) -> None: ...
    def setColor(self, color: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setExplodeDistanceFactor(self, factor: float, /) -> None: ...
    def setExploded(self, exploded: bool, /) -> None: ...
    def setLabel(self, label: str, /) -> None: ...
    def setLabelArmLengthFactor(self, factor: float, /) -> None: ...
    def setLabelColor(self, color: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setLabelFont(self, font: PySide6.QtGui.QFont | str | collections.abc.Sequence[str], /) -> None: ...
    def setLabelPosition(self, position: PySide6.QtGraphs.QPieSlice.LabelPosition, /) -> None: ...
    def setLabelVisible(self, /, visible: bool = ...) -> None: ...
    def setSubSlicesRatio(self, subSlicesRatio: float, /) -> None: ...
    def setValue(self, value: float, /) -> None: ...
    def startAngle(self, /) -> float: ...
    def subSlices(self, /) -> typing.List[PySide6.QtGraphs.QPieSlice]: ...
    def subSlicesCount(self, /) -> int: ...
    def subSlicesRatio(self, /) -> float: ...
    def subSlicesSum(self, /) -> float: ...
    def take(self, slice: PySide6.QtGraphs.QPieSlice, /) -> bool: ...
    def value(self, /) -> float: ...


class QPointFList:
    ...


class QScatter3DSeries(PySide6.QtGraphs.QAbstract3DSeries):
    # axisXChanged(QValue3DAxis*)
    axisXChanged: typing.ClassVar[Signal[
        [PySide6.QtGraphs.QValue3DAxis], [], [], [], [], [], [], [],
        [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis]
    ]]
    # axisYChanged(QValue3DAxis*)
    axisYChanged: typing.ClassVar[Signal[
        [PySide6.QtGraphs.QValue3DAxis], [], [], [], [], [], [], [],
        [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis]
    ]]
    # axisZChanged(QValue3DAxis*)
    axisZChanged: typing.ClassVar[Signal[
        [PySide6.QtGraphs.QValue3DAxis], [], [], [], [], [], [], [],
        [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis]
    ]]
    # dataArrayChanged(QScatterDataArray)
    dataArrayChanged: typing.ClassVar[Signal[
        [collections.abc.Sequence[PySide6.QtGraphs.QScatterDataItem]], [], [], [], [], [], [], [],
        [collections.abc.Sequence[PySide6.QtGraphs.QScatterDataItem]], [collections.abc.Sequence[PySide6.QtGraphs.QScatterDataItem]], [collections.abc.Sequence[PySide6.QtGraphs.QScatterDataItem]], [collections.abc.Sequence[PySide6.QtGraphs.QScatterDataItem]], [collections.abc.Sequence[PySide6.QtGraphs.QScatterDataItem]], [collections.abc.Sequence[PySide6.QtGraphs.QScatterDataItem]], [collections.abc.Sequence[PySide6.QtGraphs.QScatterDataItem]], [collections.abc.Sequence[PySide6.QtGraphs.QScatterDataItem]]
    ]]
    # dataProxyChanged(QScatterDataProxy*)
    dataProxyChanged: typing.ClassVar[Signal[
        [PySide6.QtGraphs.QScatterDataProxy], [], [], [], [], [], [], [],
        [PySide6.QtGraphs.QScatterDataProxy], [PySide6.QtGraphs.QScatterDataProxy], [PySide6.QtGraphs.QScatterDataProxy], [PySide6.QtGraphs.QScatterDataProxy], [PySide6.QtGraphs.QScatterDataProxy], [PySide6.QtGraphs.QScatterDataProxy], [PySide6.QtGraphs.QScatterDataProxy], [PySide6.QtGraphs.QScatterDataProxy]
    ]]
    # itemSizeChanged(float)
    itemSizeChanged: typing.ClassVar[Signal[
        [float], [], [], [], [], [], [], [],
        [float], [float], [float], [float], [float], [float], [float], [float]
    ]]
    # scaleArrayChanged(QList<QVector3D>)
    scaleArrayChanged: typing.ClassVar[Signal[
        [collections.abc.Sequence[PySide6.QtGui.QVector3D]], [], [], [], [], [], [], [],
        [collections.abc.Sequence[PySide6.QtGui.QVector3D]], [collections.abc.Sequence[PySide6.QtGui.QVector3D]], [collections.abc.Sequence[PySide6.QtGui.QVector3D]], [collections.abc.Sequence[PySide6.QtGui.QVector3D]], [collections.abc.Sequence[PySide6.QtGui.QVector3D]], [collections.abc.Sequence[PySide6.QtGui.QVector3D]], [collections.abc.Sequence[PySide6.QtGui.QVector3D]], [collections.abc.Sequence[PySide6.QtGui.QVector3D]]
    ]]
    # selectedItemChanged(qsizetype)
    selectedItemChanged: typing.ClassVar[Signal[
        [int], [], [], [], [], [], [], [],
        [int], [int], [int], [int], [int], [int], [int], [int]
    ]]

    @typing.overload
    def __init__(self, dataProxy: PySide6.QtGraphs.QScatterDataProxy, /, parent: PySide6.QtCore.QObject | None = ..., *, selectedItem: int | None = ..., itemSize: float | None = ..., dataArray: collections.abc.Sequence[PySide6.QtGraphs.QScatterDataItem] | None = ..., scaleArray: collections.abc.Sequence[PySide6.QtGui.QVector3D] | None = ..., axisX: PySide6.QtGraphs.QValue3DAxis | None = ..., axisY: PySide6.QtGraphs.QValue3DAxis | None = ..., axisZ: PySide6.QtGraphs.QValue3DAxis | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., *, dataProxy: PySide6.QtGraphs.QScatterDataProxy | None = ..., selectedItem: int | None = ..., itemSize: float | None = ..., dataArray: collections.abc.Sequence[PySide6.QtGraphs.QScatterDataItem] | None = ..., scaleArray: collections.abc.Sequence[PySide6.QtGui.QVector3D] | None = ..., axisX: PySide6.QtGraphs.QValue3DAxis | None = ..., axisY: PySide6.QtGraphs.QValue3DAxis | None = ..., axisZ: PySide6.QtGraphs.QValue3DAxis | None = ...) -> None: ...

    def axisX(self, /) -> PySide6.QtGraphs.QValue3DAxis: ...
    def axisY(self, /) -> PySide6.QtGraphs.QValue3DAxis: ...
    def axisZ(self, /) -> PySide6.QtGraphs.QValue3DAxis: ...
    def clearArray(self, /) -> None: ...
    def clearScaleArray(self, /) -> None: ...
    def dataArray(self, /) -> typing.List[PySide6.QtGraphs.QScatterDataItem]: ...
    def dataProxy(self, /) -> PySide6.QtGraphs.QScatterDataProxy: ...
    @staticmethod
    def invalidSelectionIndex() -> int: ...
    def itemSize(self, /) -> float: ...
    def resetAxisX(self, /) -> None: ...
    def resetAxisY(self, /) -> None: ...
    def resetAxisZ(self, /) -> None: ...
    def scaleArray(self, /) -> typing.List[PySide6.QtGui.QVector3D]: ...
    def selectedItem(self, /) -> int: ...
    def setAxisX(self, axis: PySide6.QtGraphs.QValue3DAxis, /) -> None: ...
    def setAxisY(self, axis: PySide6.QtGraphs.QValue3DAxis, /) -> None: ...
    def setAxisZ(self, axis: PySide6.QtGraphs.QValue3DAxis, /) -> None: ...
    def setDataArray(self, newDataArray: collections.abc.Sequence[PySide6.QtGraphs.QScatterDataItem], /) -> None: ...
    def setDataProxy(self, proxy: PySide6.QtGraphs.QScatterDataProxy, /) -> None: ...
    def setItemSize(self, size: float, /) -> None: ...
    def setScaleArray(self, newScaleArray: collections.abc.Sequence[PySide6.QtGui.QVector3D], /) -> None: ...
    def setSelectedItem(self, index: int, /) -> None: ...


class QScatterDataItem(Shiboken.Object):
    @typing.overload
    def __init__(self, /) -> None: ...
    @typing.overload
    def __init__(self, QScatterDataItem: PySide6.QtGraphs.QScatterDataItem, /) -> None: ...
    @typing.overload
    def __init__(self, position: PySide6.QtGui.QVector3D, /) -> None: ...
    @typing.overload
    def __init__(self, position: PySide6.QtGui.QVector3D, rotation: PySide6.QtGui.QQuaternion, /) -> None: ...
    @typing.overload
    def __init__(self, x: float, y: float, z: float, /) -> None: ...

    def __copy__(self, /) -> typing.Self: ...
    def position(self, /) -> PySide6.QtGui.QVector3D: ...
    def rotation(self, /) -> PySide6.QtGui.QQuaternion: ...
    def setPosition(self, pos: PySide6.QtGui.QVector3D, /) -> None: ...
    def setRotation(self, rot: PySide6.QtGui.QQuaternion, /) -> None: ...
    def setX(self, value: float, /) -> None: ...
    def setY(self, value: float, /) -> None: ...
    def setZ(self, value: float, /) -> None: ...
    def x(self, /) -> float: ...
    def y(self, /) -> float: ...
    def z(self, /) -> float: ...


class QScatterDataProxy(PySide6.QtGraphs.QAbstractDataProxy):
    # arrayReset()
    arrayReset: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # itemCountChanged(qsizetype)
    itemCountChanged: typing.ClassVar[Signal[
        [int], [], [], [], [], [], [], [],
        [int], [int], [int], [int], [int], [int], [int], [int]
    ]]
    # itemsAdded(qsizetype,qsizetype)
    itemsAdded: typing.ClassVar[Signal[
        [int, int], [int], [], [], [], [], [], [],
        [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int]
    ]]
    # itemsChanged(qsizetype,qsizetype)
    itemsChanged: typing.ClassVar[Signal[
        [int, int], [int], [], [], [], [], [], [],
        [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int]
    ]]
    # itemsInserted(qsizetype,qsizetype)
    itemsInserted: typing.ClassVar[Signal[
        [int, int], [int], [], [], [], [], [], [],
        [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int]
    ]]
    # itemsRemoved(qsizetype,qsizetype)
    itemsRemoved: typing.ClassVar[Signal[
        [int, int], [int], [], [], [], [], [], [],
        [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int]
    ]]
    # scaleArrayReset()
    scaleArrayReset: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # seriesChanged(QScatter3DSeries*)
    seriesChanged: typing.ClassVar[Signal[
        [PySide6.QtGraphs.QScatter3DSeries], [], [], [], [], [], [], [],
        [PySide6.QtGraphs.QScatter3DSeries], [PySide6.QtGraphs.QScatter3DSeries], [PySide6.QtGraphs.QScatter3DSeries], [PySide6.QtGraphs.QScatter3DSeries], [PySide6.QtGraphs.QScatter3DSeries], [PySide6.QtGraphs.QScatter3DSeries], [PySide6.QtGraphs.QScatter3DSeries], [PySide6.QtGraphs.QScatter3DSeries]
    ]]

    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., *, itemCount: int | None = ..., series: PySide6.QtGraphs.QScatter3DSeries | None = ...) -> None: ...

    def addItem(self, item: PySide6.QtGraphs.QScatterDataItem, /) -> int: ...
    def addItems(self, items: collections.abc.Sequence[PySide6.QtGraphs.QScatterDataItem], /) -> int: ...
    def insertItem(self, index: int, item: PySide6.QtGraphs.QScatterDataItem, /) -> None: ...
    def insertItems(self, index: int, items: collections.abc.Sequence[PySide6.QtGraphs.QScatterDataItem], /) -> None: ...
    def itemAt(self, index: int, /) -> PySide6.QtGraphs.QScatterDataItem: ...
    def itemCount(self, /) -> int: ...
    def removeItems(self, index: int, removeCount: int, /) -> None: ...
    @typing.overload
    def resetArray(self, /) -> None: ...
    @typing.overload
    def resetArray(self, newArray: collections.abc.Sequence[PySide6.QtGraphs.QScatterDataItem], /) -> None: ...
    def resetScaleArray(self, newArray: collections.abc.Sequence[PySide6.QtGui.QVector3D], /) -> None: ...
    def scaleAt(self, index: int, /) -> PySide6.QtGui.QVector3D: ...
    def series(self, /) -> PySide6.QtGraphs.QScatter3DSeries: ...
    def setItem(self, index: int, item: PySide6.QtGraphs.QScatterDataItem, /) -> None: ...
    def setItems(self, index: int, items: collections.abc.Sequence[PySide6.QtGraphs.QScatterDataItem], /) -> None: ...


class QScatterSeries(PySide6.QtGraphs.QXYSeries):
    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ...) -> None: ...

    def componentComplete(self, /) -> None: ...
    def type(self, /) -> PySide6.QtGraphs.QAbstractSeries.SeriesType: ...


class QSpline3DSeries(PySide6.QtGraphs.QScatter3DSeries):
    # splineColorChanged(QColor)
    splineColorChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QColor], [], [], [], [], [], [], [],
        [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor]
    ]]
    # splineKnottingChanged(double)
    splineKnottingChanged: typing.ClassVar[Signal[
        [float], [], [], [], [], [], [], [],
        [float], [float], [float], [float], [float], [float], [float], [float]
    ]]
    # splineLoopingChanged(bool)
    splineLoopingChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # splineResolutionChanged(int)
    splineResolutionChanged: typing.ClassVar[Signal[
        [int], [], [], [], [], [], [], [],
        [int], [int], [int], [int], [int], [int], [int], [int]
    ]]
    # splineTensionChanged(double)
    splineTensionChanged: typing.ClassVar[Signal[
        [float], [], [], [], [], [], [], [],
        [float], [float], [float], [float], [float], [float], [float], [float]
    ]]
    # splineVisibilityChanged(bool)
    splineVisibilityChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]

    @typing.overload
    def __init__(self, dataProxy: PySide6.QtGraphs.QScatterDataProxy, /, parent: PySide6.QtCore.QObject | None = ..., *, splineVisible: bool | None = ..., splineTension: float | None = ..., splineKnotting: float | None = ..., splineLooping: bool | None = ..., splineColor: PySide6.QtGui.QColor | None = ..., splineResolution: int | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., *, splineVisible: bool | None = ..., splineTension: float | None = ..., splineKnotting: float | None = ..., splineLooping: bool | None = ..., splineColor: PySide6.QtGui.QColor | None = ..., splineResolution: int | None = ...) -> None: ...

    def isSplineLooping(self, /) -> bool: ...
    def isSplineVisible(self, /) -> bool: ...
    def setSplineColor(self, color: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setSplineKnotting(self, knotting: float, /) -> None: ...
    def setSplineLooping(self, looping: bool, /) -> None: ...
    def setSplineResolution(self, resolution: int, /) -> None: ...
    def setSplineTension(self, tension: float, /) -> None: ...
    def setSplineVisible(self, draw: bool, /) -> None: ...
    def splineColor(self, /) -> PySide6.QtGui.QColor: ...
    def splineKnotting(self, /) -> float: ...
    def splineResolution(self, /) -> int: ...
    def splineTension(self, /) -> float: ...


class QSplineSeries(PySide6.QtGraphs.QXYSeries):
    # capStyleChanged()
    capStyleChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # optimizedChanged(bool)
    optimizedChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # widthChanged()
    widthChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]

    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., *, width: float | None = ..., capStyle: PySide6.QtCore.Qt.PenCapStyle | None = ..., optimized: bool | None = ...) -> None: ...

    def capStyle(self, /) -> PySide6.QtCore.Qt.PenCapStyle: ...
    def componentComplete(self, /) -> None: ...
    def getControlPoints(self, /) -> typing.List[PySide6.QtCore.QPointF]: ...
    def isOptimized(self, /) -> bool: ...
    def setCapStyle(self, newCapStyle: PySide6.QtCore.Qt.PenCapStyle, /) -> None: ...
    def setOptimized(self, optimized: bool, /) -> None: ...
    def setWidth(self, newWidth: float, /) -> None: ...
    def type(self, /) -> PySide6.QtGraphs.QAbstractSeries.SeriesType: ...
    def width(self, /) -> float: ...


class QSurface3DSeries(PySide6.QtGraphs.QAbstract3DSeries):
    # axisXChanged(QValue3DAxis*)
    axisXChanged: typing.ClassVar[Signal[
        [PySide6.QtGraphs.QValue3DAxis], [], [], [], [], [], [], [],
        [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis]
    ]]
    # axisYChanged(QValue3DAxis*)
    axisYChanged: typing.ClassVar[Signal[
        [PySide6.QtGraphs.QValue3DAxis], [], [], [], [], [], [], [],
        [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis]
    ]]
    # axisZChanged(QValue3DAxis*)
    axisZChanged: typing.ClassVar[Signal[
        [PySide6.QtGraphs.QValue3DAxis], [], [], [], [], [], [], [],
        [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis], [PySide6.QtGraphs.QValue3DAxis]
    ]]
    # dataArrayChanged(QSurfaceDataArray)
    dataArrayChanged: typing.ClassVar[Signal[
        [collections.abc.Sequence[collections.abc.Sequence[PySide6.QtGraphs.QSurfaceDataItem]]], [], [], [], [], [], [], [],
        [collections.abc.Sequence[collections.abc.Sequence[PySide6.QtGraphs.QSurfaceDataItem]]], [collections.abc.Sequence[collections.abc.Sequence[PySide6.QtGraphs.QSurfaceDataItem]]], [collections.abc.Sequence[collections.abc.Sequence[PySide6.QtGraphs.QSurfaceDataItem]]], [collections.abc.Sequence[collections.abc.Sequence[PySide6.QtGraphs.QSurfaceDataItem]]], [collections.abc.Sequence[collections.abc.Sequence[PySide6.QtGraphs.QSurfaceDataItem]]], [collections.abc.Sequence[collections.abc.Sequence[PySide6.QtGraphs.QSurfaceDataItem]]], [collections.abc.Sequence[collections.abc.Sequence[PySide6.QtGraphs.QSurfaceDataItem]]], [collections.abc.Sequence[collections.abc.Sequence[PySide6.QtGraphs.QSurfaceDataItem]]]
    ]]
    # dataProxyChanged(QSurfaceDataProxy*)
    dataProxyChanged: typing.ClassVar[Signal[
        [PySide6.QtGraphs.QSurfaceDataProxy], [], [], [], [], [], [], [],
        [PySide6.QtGraphs.QSurfaceDataProxy], [PySide6.QtGraphs.QSurfaceDataProxy], [PySide6.QtGraphs.QSurfaceDataProxy], [PySide6.QtGraphs.QSurfaceDataProxy], [PySide6.QtGraphs.QSurfaceDataProxy], [PySide6.QtGraphs.QSurfaceDataProxy], [PySide6.QtGraphs.QSurfaceDataProxy], [PySide6.QtGraphs.QSurfaceDataProxy]
    ]]
    # drawModeChanged(QSurface3DSeries::DrawFlags)
    drawModeChanged: typing.ClassVar[Signal[
        [PySide6.QtGraphs.QSurface3DSeries.DrawFlag], [], [], [], [], [], [], [],
        [PySide6.QtGraphs.QSurface3DSeries.DrawFlag], [PySide6.QtGraphs.QSurface3DSeries.DrawFlag], [PySide6.QtGraphs.QSurface3DSeries.DrawFlag], [PySide6.QtGraphs.QSurface3DSeries.DrawFlag], [PySide6.QtGraphs.QSurface3DSeries.DrawFlag], [PySide6.QtGraphs.QSurface3DSeries.DrawFlag], [PySide6.QtGraphs.QSurface3DSeries.DrawFlag], [PySide6.QtGraphs.QSurface3DSeries.DrawFlag]
    ]]
    # flatShadingSupportedChanged(bool)
    flatShadingSupportedChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # rowsSanitizedChanged(bool)
    rowsSanitizedChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # selectedPointChanged(QPoint)
    selectedPointChanged: typing.ClassVar[Signal[
        [PySide6.QtCore.QPoint], [], [], [], [], [], [], [],
        [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint]
    ]]
    # shadingChanged(Shading)
    shadingChanged: typing.ClassVar[Signal[
        [Shading], [], [], [], [], [], [], [],
        [Shading], [Shading], [Shading], [Shading], [Shading], [Shading], [Shading], [Shading]
    ]]
    # textureChanged(QImage)
    textureChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QImage], [], [], [], [], [], [], [],
        [PySide6.QtGui.QImage], [PySide6.QtGui.QImage], [PySide6.QtGui.QImage], [PySide6.QtGui.QImage], [PySide6.QtGui.QImage], [PySide6.QtGui.QImage], [PySide6.QtGui.QImage], [PySide6.QtGui.QImage]
    ]]
    # textureFileChanged(QString)
    textureFileChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # wireframeColorChanged(QColor)
    wireframeColorChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QColor], [], [], [], [], [], [], [],
        [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor]
    ]]

    class DrawFlag(enum.Flag):
        DrawWireframe             = 0x1
        DrawSurface               = 0x2
        DrawSurfaceAndWireframe   = 0x3
        DrawFilledSurface         = 0x4

    class Shading(enum.Enum):
        Smooth                    = 0x0
        Flat                      = 0x1

    @typing.overload
    def __init__(self, dataProxy: PySide6.QtGraphs.QSurfaceDataProxy, /, parent: PySide6.QtCore.QObject | None = ..., *, selectedPoint: PySide6.QtCore.QPoint | None = ..., flatShadingSupported: bool | None = ..., drawMode: PySide6.QtGraphs.QSurface3DSeries.DrawFlag | None = ..., shading: PySide6.QtGraphs.QSurface3DSeries.Shading | None = ..., texture: PySide6.QtGui.QImage | None = ..., textureFile: str | None = ..., wireframeColor: PySide6.QtGui.QColor | None = ..., dataArray: collections.abc.Sequence[collections.abc.Sequence[PySide6.QtGraphs.QSurfaceDataItem]] | None = ..., rowsSanitized: bool | None = ..., axisX: PySide6.QtGraphs.QValue3DAxis | None = ..., axisY: PySide6.QtGraphs.QValue3DAxis | None = ..., axisZ: PySide6.QtGraphs.QValue3DAxis | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., *, dataProxy: PySide6.QtGraphs.QSurfaceDataProxy | None = ..., selectedPoint: PySide6.QtCore.QPoint | None = ..., flatShadingSupported: bool | None = ..., drawMode: PySide6.QtGraphs.QSurface3DSeries.DrawFlag | None = ..., shading: PySide6.QtGraphs.QSurface3DSeries.Shading | None = ..., texture: PySide6.QtGui.QImage | None = ..., textureFile: str | None = ..., wireframeColor: PySide6.QtGui.QColor | None = ..., dataArray: collections.abc.Sequence[collections.abc.Sequence[PySide6.QtGraphs.QSurfaceDataItem]] | None = ..., rowsSanitized: bool | None = ..., axisX: PySide6.QtGraphs.QValue3DAxis | None = ..., axisY: PySide6.QtGraphs.QValue3DAxis | None = ..., axisZ: PySide6.QtGraphs.QValue3DAxis | None = ...) -> None: ...

    def axisX(self, /) -> PySide6.QtGraphs.QValue3DAxis: ...
    def axisY(self, /) -> PySide6.QtGraphs.QValue3DAxis: ...
    def axisZ(self, /) -> PySide6.QtGraphs.QValue3DAxis: ...
    def clearArray(self, /) -> None: ...
    def clearRow(self, rowIndex: int, /) -> None: ...
    def dataArray(self, /) -> typing.List[typing.List[PySide6.QtGraphs.QSurfaceDataItem]]: ...
    def dataProxy(self, /) -> PySide6.QtGraphs.QSurfaceDataProxy: ...
    def drawMode(self, /) -> PySide6.QtGraphs.QSurface3DSeries.DrawFlag: ...
    @staticmethod
    def invalidSelectionPosition() -> PySide6.QtCore.QPoint: ...
    def isFlatShadingSupported(self, /) -> bool: ...
    def resetAxisX(self, /) -> None: ...
    def resetAxisY(self, /) -> None: ...
    def resetAxisZ(self, /) -> None: ...
    def rowsSanitized(self, /) -> bool: ...
    def selectedPoint(self, /) -> PySide6.QtCore.QPoint: ...
    def setAxisX(self, axis: PySide6.QtGraphs.QValue3DAxis, /) -> None: ...
    def setAxisY(self, axis: PySide6.QtGraphs.QValue3DAxis, /) -> None: ...
    def setAxisZ(self, axis: PySide6.QtGraphs.QValue3DAxis, /) -> None: ...
    def setDataArray(self, newDataArray: collections.abc.Sequence[collections.abc.Sequence[PySide6.QtGraphs.QSurfaceDataItem]], /) -> None: ...
    def setDataProxy(self, proxy: PySide6.QtGraphs.QSurfaceDataProxy, /) -> None: ...
    def setDrawMode(self, mode: PySide6.QtGraphs.QSurface3DSeries.DrawFlag, /) -> None: ...
    def setRowsSanitized(self, sanitized: bool, /) -> None: ...
    def setSelectedPoint(self, position: PySide6.QtCore.QPoint, /) -> None: ...
    def setShading(self, shading: PySide6.QtGraphs.QSurface3DSeries.Shading, /) -> None: ...
    def setTexture(self, texture: PySide6.QtGui.QImage, /) -> None: ...
    def setTextureFile(self, filename: str, /) -> None: ...
    def setWireframeColor(self, color: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def shading(self, /) -> PySide6.QtGraphs.QSurface3DSeries.Shading: ...
    def texture(self, /) -> PySide6.QtGui.QImage: ...
    def textureFile(self, /) -> str: ...
    def wireframeColor(self, /) -> PySide6.QtGui.QColor: ...


class QSurfaceDataItem(Shiboken.Object):
    @typing.overload
    def __init__(self, /) -> None: ...
    @typing.overload
    def __init__(self, QSurfaceDataItem: PySide6.QtGraphs.QSurfaceDataItem, /) -> None: ...
    @typing.overload
    def __init__(self, position: PySide6.QtGui.QVector3D, /) -> None: ...
    @typing.overload
    def __init__(self, x: float, y: float, z: float, /) -> None: ...

    def __copy__(self, /) -> typing.Self: ...
    def position(self, /) -> PySide6.QtGui.QVector3D: ...
    def setPosition(self, pos: PySide6.QtGui.QVector3D, /) -> None: ...
    def setX(self, value: float, /) -> None: ...
    def setY(self, value: float, /) -> None: ...
    def setZ(self, value: float, /) -> None: ...
    def x(self, /) -> float: ...
    def y(self, /) -> float: ...
    def z(self, /) -> float: ...


class QSurfaceDataProxy(PySide6.QtGraphs.QAbstractDataProxy):
    # arrayReset()
    arrayReset: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # columnCountChanged(qsizetype)
    columnCountChanged: typing.ClassVar[Signal[
        [int], [], [], [], [], [], [], [],
        [int], [int], [int], [int], [int], [int], [int], [int]
    ]]
    # itemChanged(qsizetype,qsizetype)
    itemChanged: typing.ClassVar[Signal[
        [int, int], [int], [], [], [], [], [], [],
        [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int]
    ]]
    # rowCountChanged(qsizetype)
    rowCountChanged: typing.ClassVar[Signal[
        [int], [], [], [], [], [], [], [],
        [int], [int], [int], [int], [int], [int], [int], [int]
    ]]
    # rowsAdded(qsizetype,qsizetype)
    rowsAdded: typing.ClassVar[Signal[
        [int, int], [int], [], [], [], [], [], [],
        [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int]
    ]]
    # rowsChanged(qsizetype,qsizetype)
    rowsChanged: typing.ClassVar[Signal[
        [int, int], [int], [], [], [], [], [], [],
        [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int]
    ]]
    # rowsInserted(qsizetype,qsizetype)
    rowsInserted: typing.ClassVar[Signal[
        [int, int], [int], [], [], [], [], [], [],
        [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int]
    ]]
    # rowsRemoved(qsizetype,qsizetype)
    rowsRemoved: typing.ClassVar[Signal[
        [int, int], [int], [], [], [], [], [], [],
        [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int]
    ]]
    # seriesChanged(QSurface3DSeries*)
    seriesChanged: typing.ClassVar[Signal[
        [PySide6.QtGraphs.QSurface3DSeries], [], [], [], [], [], [], [],
        [PySide6.QtGraphs.QSurface3DSeries], [PySide6.QtGraphs.QSurface3DSeries], [PySide6.QtGraphs.QSurface3DSeries], [PySide6.QtGraphs.QSurface3DSeries], [PySide6.QtGraphs.QSurface3DSeries], [PySide6.QtGraphs.QSurface3DSeries], [PySide6.QtGraphs.QSurface3DSeries], [PySide6.QtGraphs.QSurface3DSeries]
    ]]

    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., *, rowCount: int | None = ..., columnCount: int | None = ..., series: PySide6.QtGraphs.QSurface3DSeries | None = ...) -> None: ...

    def addRow(self, row: collections.abc.Sequence[PySide6.QtGraphs.QSurfaceDataItem], /) -> int: ...
    def addRows(self, rows: collections.abc.Sequence[collections.abc.Sequence[PySide6.QtGraphs.QSurfaceDataItem]], /) -> int: ...
    def columnCount(self, /) -> int: ...
    def insertRow(self, rowIndex: int, row: collections.abc.Sequence[PySide6.QtGraphs.QSurfaceDataItem], /) -> None: ...
    def insertRows(self, rowIndex: int, rows: collections.abc.Sequence[collections.abc.Sequence[PySide6.QtGraphs.QSurfaceDataItem]], /) -> None: ...
    @typing.overload
    def itemAt(self, position: PySide6.QtCore.QPoint, /) -> PySide6.QtGraphs.QSurfaceDataItem: ...
    @typing.overload
    def itemAt(self, rowIndex: int, columnIndex: int, /) -> PySide6.QtGraphs.QSurfaceDataItem: ...
    def removeRows(self, rowIndex: int, removeCount: int, /) -> None: ...
    @typing.overload
    def resetArray(self, /) -> None: ...
    @typing.overload
    def resetArray(self, newArray: collections.abc.Sequence[collections.abc.Sequence[PySide6.QtGraphs.QSurfaceDataItem]], /) -> None: ...
    def resetArrayNp(self, x: float, deltaX: float, z: float, deltaZ: float, data: collections.abc.Sequence[typing.Any], /) -> None: ...
    def rowCount(self, /) -> int: ...
    def series(self, /) -> PySide6.QtGraphs.QSurface3DSeries: ...
    @typing.overload
    def setItem(self, position: PySide6.QtCore.QPoint, item: PySide6.QtGraphs.QSurfaceDataItem, /) -> None: ...
    @typing.overload
    def setItem(self, rowIndex: int, columnIndex: int, item: PySide6.QtGraphs.QSurfaceDataItem, /) -> None: ...
    def setRow(self, rowIndex: int, row: collections.abc.Sequence[PySide6.QtGraphs.QSurfaceDataItem], /) -> None: ...
    def setRows(self, rowIndex: int, rows: collections.abc.Sequence[collections.abc.Sequence[PySide6.QtGraphs.QSurfaceDataItem]], /) -> None: ...


class QValue3DAxis(PySide6.QtGraphs.QAbstract3DAxis):
    # formatterChanged(QValue3DAxisFormatter*)
    formatterChanged: typing.ClassVar[Signal[
        [PySide6.QtGraphs.QValue3DAxisFormatter], [], [], [], [], [], [], [],
        [PySide6.QtGraphs.QValue3DAxisFormatter], [PySide6.QtGraphs.QValue3DAxisFormatter], [PySide6.QtGraphs.QValue3DAxisFormatter], [PySide6.QtGraphs.QValue3DAxisFormatter], [PySide6.QtGraphs.QValue3DAxisFormatter], [PySide6.QtGraphs.QValue3DAxisFormatter], [PySide6.QtGraphs.QValue3DAxisFormatter], [PySide6.QtGraphs.QValue3DAxisFormatter]
    ]]
    # formatterDirty()
    formatterDirty: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # labelFormatChanged(QString)
    labelFormatChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # reversedChanged(bool)
    reversedChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # segmentCountChanged(qsizetype)
    segmentCountChanged: typing.ClassVar[Signal[
        [int], [], [], [], [], [], [], [],
        [int], [int], [int], [int], [int], [int], [int], [int]
    ]]
    # subSegmentCountChanged(qsizetype)
    subSegmentCountChanged: typing.ClassVar[Signal[
        [int], [], [], [], [], [], [], [],
        [int], [int], [int], [int], [int], [int], [int], [int]
    ]]

    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., *, segmentCount: int | None = ..., subSegmentCount: int | None = ..., labelFormat: str | None = ..., formatter: PySide6.QtGraphs.QValue3DAxisFormatter | None = ..., reversed: bool | None = ...) -> None: ...

    def formatter(self, /) -> PySide6.QtGraphs.QValue3DAxisFormatter: ...
    def gridPositionAt(self, gridLine: int, /) -> float: ...
    def gridSize(self, /) -> int: ...
    def labelFormat(self, /) -> str: ...
    def labelPositionAt(self, index: int, /) -> float: ...
    def positionAt(self, x: float, /) -> float: ...
    def recalculate(self, /) -> None: ...
    def reversed(self, /) -> bool: ...
    def segmentCount(self, /) -> int: ...
    def setFormatter(self, formatter: PySide6.QtGraphs.QValue3DAxisFormatter, /) -> None: ...
    def setLabelFormat(self, format: str, /) -> None: ...
    def setReversed(self, enable: bool, /) -> None: ...
    def setSegmentCount(self, count: int, /) -> None: ...
    def setSubSegmentCount(self, count: int, /) -> None: ...
    def stringForValue(self, x: float, /) -> str: ...
    def subGridPositionAt(self, gridLine: int, /) -> float: ...
    def subGridSize(self, /) -> int: ...
    def subSegmentCount(self, /) -> int: ...


class QValue3DAxisFormatter(PySide6.QtCore.QObject):
    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ...) -> None: ...

    def allowNegatives(self, /) -> bool: ...
    def allowZero(self, /) -> bool: ...
    def axis(self, /) -> PySide6.QtGraphs.QValue3DAxis: ...
    def createNewInstance(self, /) -> PySide6.QtGraphs.QValue3DAxisFormatter: ...
    def gridPositions(self, /) -> typing.List[float]: ...
    def labelPositions(self, /) -> typing.List[float]: ...
    def labelStrings(self, /) -> typing.List[str]: ...
    def locale(self, /) -> PySide6.QtCore.QLocale: ...
    def markDirty(self, /, labelsChange: bool = ...) -> None: ...
    def populateCopy(self, copy: PySide6.QtGraphs.QValue3DAxisFormatter, /) -> None: ...
    def positionAt(self, value: float, /) -> float: ...
    def recalculate(self, /) -> None: ...
    def setAllowNegatives(self, allow: bool, /) -> None: ...
    def setAllowZero(self, allow: bool, /) -> None: ...
    def setAxis(self, axis: PySide6.QtGraphs.QValue3DAxis, /) -> None: ...
    def setGridPoitions(self, gridPositions: collections.abc.Sequence[float], /) -> None: ...
    def setLabelStrings(self, labelStrings: collections.abc.Sequence[str], /) -> None: ...
    def setLocale(self, locale: PySide6.QtCore.QLocale | PySide6.QtCore.QLocale.Language, /) -> None: ...
    def setSubGridPositions(self, subGridPositions: collections.abc.Sequence[float], /) -> None: ...
    def setlabelPositions(self, labelPositions: collections.abc.Sequence[float], /) -> None: ...
    def stringForValue(self, value: float, format: str, /) -> str: ...
    def subGridPositions(self, /) -> typing.List[float]: ...
    def valueAt(self, position: float, /) -> float: ...


class QValueAxis(PySide6.QtGraphs.QAbstractAxis):
    # labelDecimalsChanged(int)
    labelDecimalsChanged: typing.ClassVar[Signal[
        [int], [], [], [], [], [], [], [],
        [int], [int], [int], [int], [int], [int], [int], [int]
    ]]
    # labelFormatChanged(QString)
    labelFormatChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # maxChanged(double)
    maxChanged: typing.ClassVar[Signal[
        [float], [], [], [], [], [], [], [],
        [float], [float], [float], [float], [float], [float], [float], [float]
    ]]
    # minChanged(double)
    minChanged: typing.ClassVar[Signal[
        [float], [], [], [], [], [], [], [],
        [float], [float], [float], [float], [float], [float], [float], [float]
    ]]
    # panChanged(double)
    panChanged: typing.ClassVar[Signal[
        [float], [], [], [], [], [], [], [],
        [float], [float], [float], [float], [float], [float], [float], [float]
    ]]
    # rangeChanged(double,double)
    rangeChanged: typing.ClassVar[Signal[
        [float, float], [float], [], [], [], [], [], [],
        [float, float], [float, float], [float, float], [float, float], [float, float], [float, float], [float, float], [float, float]
    ]]
    # subTickCountChanged(qsizetype)
    subTickCountChanged: typing.ClassVar[Signal[
        [int], [], [], [], [], [], [], [],
        [int], [int], [int], [int], [int], [int], [int], [int]
    ]]
    # tickAnchorChanged(double)
    tickAnchorChanged: typing.ClassVar[Signal[
        [float], [], [], [], [], [], [], [],
        [float], [float], [float], [float], [float], [float], [float], [float]
    ]]
    # tickIntervalChanged(double)
    tickIntervalChanged: typing.ClassVar[Signal[
        [float], [], [], [], [], [], [], [],
        [float], [float], [float], [float], [float], [float], [float], [float]
    ]]
    # visualMaxChanged(double)
    visualMaxChanged: typing.ClassVar[Signal[
        [float], [], [], [], [], [], [], [],
        [float], [float], [float], [float], [float], [float], [float], [float]
    ]]
    # visualMinChanged(double)
    visualMinChanged: typing.ClassVar[Signal[
        [float], [], [], [], [], [], [], [],
        [float], [float], [float], [float], [float], [float], [float], [float]
    ]]
    # zoomChanged(double)
    zoomChanged: typing.ClassVar[Signal[
        [float], [], [], [], [], [], [], [],
        [float], [float], [float], [float], [float], [float], [float], [float]
    ]]

    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., *, min: float | None = ..., max: float | None = ..., labelFormat: str | None = ..., labelDecimals: int | None = ..., subTickCount: int | None = ..., tickAnchor: float | None = ..., tickInterval: float | None = ..., zoom: float | None = ..., pan: float | None = ..., visualMin: float | None = ..., visualMax: float | None = ...) -> None: ...

    def labelDecimals(self, /) -> int: ...
    def labelFormat(self, /) -> str: ...
    def max(self, /) -> float: ...
    def min(self, /) -> float: ...
    def pan(self, /) -> float: ...
    def setLabelDecimals(self, decimals: int, /) -> None: ...
    def setLabelFormat(self, format: str, /) -> None: ...
    def setMax(self, max: float, /) -> None: ...
    def setMin(self, min: float, /) -> None: ...
    def setPan(self, pan: float, /) -> None: ...
    def setRange(self, min: float, max: float, /) -> None: ...
    def setSubTickCount(self, count: int, /) -> None: ...
    def setTickAnchor(self, anchor: float, /) -> None: ...
    def setTickInterval(self, interval: float, /) -> None: ...
    def setZoom(self, zoom: float, /) -> None: ...
    def subTickCount(self, /) -> int: ...
    def tickAnchor(self, /) -> float: ...
    def tickInterval(self, /) -> float: ...
    def type(self, /) -> PySide6.QtGraphs.QAbstractAxis.AxisType: ...
    def visualMax(self, /) -> float: ...
    def visualMin(self, /) -> float: ...
    def zoom(self, /) -> float: ...


class QVector3DList:
    ...


class QXYModelMapper(PySide6.QtCore.QObject):
    # countChanged()
    countChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # firstChanged()
    firstChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # modelChanged()
    modelChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # orientationChanged()
    orientationChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # seriesChanged()
    seriesChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # xSectionChanged()
    xSectionChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # ySectionChanged()
    ySectionChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]

    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., *, series: PySide6.QtGraphs.QXYSeries | None = ..., model: PySide6.QtCore.QAbstractItemModel | None = ..., xSection: int | None = ..., ySection: int | None = ..., first: int | None = ..., count: int | None = ..., orientation: PySide6.QtCore.Qt.Orientation | None = ...) -> None: ...

    def count(self, /) -> int: ...
    def first(self, /) -> int: ...
    def model(self, /) -> PySide6.QtCore.QAbstractItemModel: ...
    def orientation(self, /) -> PySide6.QtCore.Qt.Orientation: ...
    def series(self, /) -> PySide6.QtGraphs.QXYSeries: ...
    def setCount(self, count: int, /) -> None: ...
    def setFirst(self, first: int, /) -> None: ...
    def setModel(self, model: PySide6.QtCore.QAbstractItemModel, /) -> None: ...
    def setOrientation(self, orientation: PySide6.QtCore.Qt.Orientation, /) -> None: ...
    def setSeries(self, series: PySide6.QtGraphs.QXYSeries, /) -> None: ...
    def setXSection(self, xSection: int, /) -> None: ...
    def setYSection(self, ySection: int, /) -> None: ...
    def xSection(self, /) -> int: ...
    def ySection(self, /) -> int: ...


class QXYSeries(PySide6.QtGraphs.QAbstractSeries):
    # clicked(QPoint)
    clicked: typing.ClassVar[Signal[
        [PySide6.QtCore.QPoint], [], [], [], [], [], [], [],
        [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint]
    ]]
    # colorChanged(QColor)
    colorChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QColor], [], [], [], [], [], [], [],
        [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor]
    ]]
    # countChanged()
    countChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # doubleClicked(QPoint)
    doubleClicked: typing.ClassVar[Signal[
        [PySide6.QtCore.QPoint], [], [], [], [], [], [], [],
        [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint]
    ]]
    # draggableChanged()
    draggableChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # pointAdded(qsizetype)
    pointAdded: typing.ClassVar[Signal[
        [int], [], [], [], [], [], [], [],
        [int], [int], [int], [int], [int], [int], [int], [int]
    ]]
    # pointDelegateChanged()
    pointDelegateChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # pointRemoved(qsizetype)
    pointRemoved: typing.ClassVar[Signal[
        [int], [], [], [], [], [], [], [],
        [int], [int], [int], [int], [int], [int], [int], [int]
    ]]
    # pointReplaced(qsizetype)
    pointReplaced: typing.ClassVar[Signal[
        [int], [], [], [], [], [], [], [],
        [int], [int], [int], [int], [int], [int], [int], [int]
    ]]
    # pointsAdded(qsizetype,qsizetype)
    pointsAdded: typing.ClassVar[Signal[
        [int, int], [int], [], [], [], [], [], [],
        [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int]
    ]]
    # pointsRemoved(qsizetype,qsizetype)
    pointsRemoved: typing.ClassVar[Signal[
        [int, int], [int], [], [], [], [], [], [],
        [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int], [int, int]
    ]]
    # pointsReplaced()
    pointsReplaced: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # pressed(QPoint)
    pressed: typing.ClassVar[Signal[
        [PySide6.QtCore.QPoint], [], [], [], [], [], [], [],
        [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint]
    ]]
    # released(QPoint)
    released: typing.ClassVar[Signal[
        [PySide6.QtCore.QPoint], [], [], [], [], [], [], [],
        [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint], [PySide6.QtCore.QPoint]
    ]]
    # selectedColorChanged(QColor)
    selectedColorChanged: typing.ClassVar[Signal[
        [PySide6.QtGui.QColor], [], [], [], [], [], [], [],
        [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor], [PySide6.QtGui.QColor]
    ]]
    # selectedPointsChanged()
    selectedPointsChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # seriesUpdated()
    seriesUpdated: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]

    @typing.overload
    def __lshift__(self, points: collections.abc.Sequence[PySide6.QtCore.QPointF], /) -> PySide6.QtGraphs.QXYSeries: ...
    @typing.overload
    def __lshift__(self, point: PySide6.QtCore.QPointF | PySide6.QtCore.QPoint | PySide6.QtGui.QPainterPath.Element, /) -> PySide6.QtGraphs.QXYSeries: ...
    @typing.overload
    def append(self, points: collections.abc.Sequence[PySide6.QtCore.QPointF], /) -> None: ...
    @typing.overload
    def append(self, point: PySide6.QtCore.QPointF | PySide6.QtCore.QPoint | PySide6.QtGui.QPainterPath.Element, /) -> None: ...
    @typing.overload
    def append(self, x: float, y: float, /) -> None: ...
    def appendNp(self, x: collections.abc.Sequence[typing.Any], y: collections.abc.Sequence[typing.Any], /) -> None: ...
    def at(self, index: int, /) -> PySide6.QtCore.QPointF: ...
    def clear(self, /) -> None: ...
    def color(self, /) -> PySide6.QtGui.QColor: ...
    def count(self, /) -> int: ...
    def deselectAllPoints(self, /) -> None: ...
    def deselectPoint(self, index: int, /) -> None: ...
    def deselectPoints(self, indexes: collections.abc.Sequence[int], /) -> None: ...
    def find(self, point: PySide6.QtCore.QPointF | PySide6.QtCore.QPoint | PySide6.QtGui.QPainterPath.Element, /) -> int: ...
    def insert(self, index: int, point: PySide6.QtCore.QPointF | PySide6.QtCore.QPoint | PySide6.QtGui.QPainterPath.Element, /) -> None: ...
    def isDraggable(self, /) -> bool: ...
    def isPointSelected(self, index: int, /) -> bool: ...
    def pointDelegate(self, /) -> PySide6.QtQml.QQmlComponent: ...
    def points(self, /) -> typing.List[PySide6.QtCore.QPointF]: ...
    def qt_qmlMarker_uncreatable(self, /) -> None: ...
    @typing.overload
    def remove(self, point: PySide6.QtCore.QPointF | PySide6.QtCore.QPoint | PySide6.QtGui.QPainterPath.Element, /) -> None: ...
    @typing.overload
    def remove(self, index: int, /) -> None: ...
    @typing.overload
    def remove(self, x: float, y: float, /) -> None: ...
    def removeMultiple(self, index: int, count: int, /) -> None: ...
    @typing.overload
    def replace(self, points: collections.abc.Sequence[PySide6.QtCore.QPointF], /) -> None: ...
    @typing.overload
    def replace(self, oldPoint: PySide6.QtCore.QPointF | PySide6.QtCore.QPoint | PySide6.QtGui.QPainterPath.Element, newPoint: PySide6.QtCore.QPointF | PySide6.QtCore.QPoint | PySide6.QtGui.QPainterPath.Element, /) -> None: ...
    @typing.overload
    def replace(self, index: int, newPoint: PySide6.QtCore.QPointF | PySide6.QtCore.QPoint | PySide6.QtGui.QPainterPath.Element, /) -> None: ...
    @typing.overload
    def replace(self, index: int, newX: float, newY: float, /) -> None: ...
    @typing.overload
    def replace(self, oldX: float, oldY: float, newX: float, newY: float, /) -> None: ...
    def replaceNp(self, x: collections.abc.Sequence[typing.Any], y: collections.abc.Sequence[typing.Any], /) -> None: ...
    def selectAllPoints(self, /) -> None: ...
    def selectPoint(self, index: int, /) -> None: ...
    def selectPoints(self, indexes: collections.abc.Sequence[int], /) -> None: ...
    def selectedColor(self, /) -> PySide6.QtGui.QColor: ...
    def selectedPoints(self, /) -> typing.List[int]: ...
    def setColor(self, newColor: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def setDraggable(self, newDraggable: bool, /) -> None: ...
    def setPointDelegate(self, newPointDelegate: PySide6.QtQml.QQmlComponent, /) -> None: ...
    def setPointSelected(self, index: int, selected: bool, /) -> None: ...
    def setSelectedColor(self, color: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None: ...
    def take(self, point: PySide6.QtCore.QPointF | PySide6.QtCore.QPoint | PySide6.QtGui.QPainterPath.Element, /) -> bool: ...
    def toggleSelection(self, indexes: collections.abc.Sequence[int], /) -> None: ...


class QtGraphs3D(Shiboken.Object):
    class CameraPreset(enum.Enum):
        NoPreset                  = 0x0
        FrontLow                  = 0x1
        Front                     = 0x2
        FrontHigh                 = 0x3
        LeftLow                   = 0x4
        Left                      = 0x5
        LeftHigh                  = 0x6
        RightLow                  = 0x7
        Right                     = 0x8
        RightHigh                 = 0x9
        BehindLow                 = 0xa
        Behind                    = 0xb
        BehindHigh                = 0xc
        IsometricLeft             = 0xd
        IsometricLeftHigh         = 0xe
        IsometricRight            = 0xf
        IsometricRightHigh        = 0x10
        DirectlyAbove             = 0x11
        DirectlyAboveCW45         = 0x12
        DirectlyAboveCCW45        = 0x13
        FrontBelow                = 0x14
        LeftBelow                 = 0x15
        RightBelow                = 0x16
        BehindBelow               = 0x17
        DirectlyBelow             = 0x18

    class ElementType(enum.Enum):
        None_                     = 0x0
        Series                    = 0x1
        AxisXLabel                = 0x2
        AxisYLabel                = 0x3
        AxisZLabel                = 0x4
        CustomItem                = 0x5

    class GridLineType(enum.Enum):
        Shader                    = 0x0
        Geometry                  = 0x1

    class OptimizationHint(enum.Flag):
        Default                   = 0x0
        Legacy                    = 0x1

    class RenderingMode(enum.Enum):
        DirectToBackground        = 0x0
        Indirect                  = 0x1

    class SelectionFlag(enum.Flag):
        None_                     = 0x0
        Item                      = 0x1
        Row                       = 0x2
        ItemAndRow                = 0x3
        Column                    = 0x4
        ItemAndColumn             = 0x5
        RowAndColumn              = 0x6
        ItemRowAndColumn          = 0x7
        Slice                     = 0x8
        MultiSeries               = 0x10

    class ShadowQuality(enum.Enum):
        None_                     = 0x0
        Low                       = 0x1
        Medium                    = 0x2
        High                      = 0x3
        SoftLow                   = 0x4
        SoftMedium                = 0x5
        SoftHigh                  = 0x6

    class SliceCaptureType(enum.Enum):
        NoImage                   = 0x0
        RowImage                  = 0x1
        ColumnImage               = 0x2

    class TransparencyTechnique(enum.Enum):
        Default                   = 0x0
        Approximate               = 0x1
        Accurate                  = 0x2


def qDefaultSurfaceFormat(antialias: bool, /) -> PySide6.QtGui.QSurfaceFormat: ...

# eof
