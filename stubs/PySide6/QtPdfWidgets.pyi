# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
"""
This file contains the exact signatures for all functions in module
PySide6.QtPdfWidgets, except for defaults which are replaced by "...".
"""

# mypy: disable-error-code="override, overload-overlap"
# Module `PySide6.QtPdfWidgets`

import PySide6.QtPdfWidgets
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets
import PySide6.QtPdf

import enum
import typing
from PySide6.QtCore import Signal


class QIntList:
    ...


class QPdfPageSelector(PySide6.QtWidgets.QWidget):
    # currentPageChanged(int)
    currentPageChanged: typing.ClassVar[Signal[
        [int], [], [], [], [], [], [], [],
        [int], [int], [int], [int], [int], [int], [int], [int]
    ]]
    # currentPageLabelChanged(QString)
    currentPageLabelChanged: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]
    # documentChanged(QPdfDocument*)
    documentChanged: typing.ClassVar[Signal[
        [PySide6.QtPdf.QPdfDocument], [], [], [], [], [], [], [],
        [PySide6.QtPdf.QPdfDocument], [PySide6.QtPdf.QPdfDocument], [PySide6.QtPdf.QPdfDocument], [PySide6.QtPdf.QPdfDocument], [PySide6.QtPdf.QPdfDocument], [PySide6.QtPdf.QPdfDocument], [PySide6.QtPdf.QPdfDocument], [PySide6.QtPdf.QPdfDocument]
    ]]

    @typing.overload
    def __init__(self, parent: PySide6.QtWidgets.QWidget, /, *, document: PySide6.QtPdf.QPdfDocument | None = ..., currentPage: int | None = ..., currentPageLabel: str | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, *, document: PySide6.QtPdf.QPdfDocument | None = ..., currentPage: int | None = ..., currentPageLabel: str | None = ...) -> None: ...

    def currentPage(self, /) -> int: ...
    def currentPageLabel(self, /) -> str: ...
    def document(self, /) -> PySide6.QtPdf.QPdfDocument: ...
    def setCurrentPage(self, index: int, /) -> None: ...
    def setDocument(self, document: PySide6.QtPdf.QPdfDocument, /) -> None: ...


class QPdfView(PySide6.QtWidgets.QAbstractScrollArea):
    # currentSearchResultIndexChanged(int)
    currentSearchResultIndexChanged: typing.ClassVar[Signal[
        [int], [], [], [], [], [], [], [],
        [int], [int], [int], [int], [int], [int], [int], [int]
    ]]
    # documentChanged(QPdfDocument*)
    documentChanged: typing.ClassVar[Signal[
        [PySide6.QtPdf.QPdfDocument], [], [], [], [], [], [], [],
        [PySide6.QtPdf.QPdfDocument], [PySide6.QtPdf.QPdfDocument], [PySide6.QtPdf.QPdfDocument], [PySide6.QtPdf.QPdfDocument], [PySide6.QtPdf.QPdfDocument], [PySide6.QtPdf.QPdfDocument], [PySide6.QtPdf.QPdfDocument], [PySide6.QtPdf.QPdfDocument]
    ]]
    # documentMarginsChanged(QMargins)
    documentMarginsChanged: typing.ClassVar[Signal[
        [PySide6.QtCore.QMargins], [], [], [], [], [], [], [],
        [PySide6.QtCore.QMargins], [PySide6.QtCore.QMargins], [PySide6.QtCore.QMargins], [PySide6.QtCore.QMargins], [PySide6.QtCore.QMargins], [PySide6.QtCore.QMargins], [PySide6.QtCore.QMargins], [PySide6.QtCore.QMargins]
    ]]
    # pageModeChanged(QPdfView::PageMode)
    pageModeChanged: typing.ClassVar[Signal[
        [PySide6.QtPdfWidgets.QPdfView.PageMode], [], [], [], [], [], [], [],
        [PySide6.QtPdfWidgets.QPdfView.PageMode], [PySide6.QtPdfWidgets.QPdfView.PageMode], [PySide6.QtPdfWidgets.QPdfView.PageMode], [PySide6.QtPdfWidgets.QPdfView.PageMode], [PySide6.QtPdfWidgets.QPdfView.PageMode], [PySide6.QtPdfWidgets.QPdfView.PageMode], [PySide6.QtPdfWidgets.QPdfView.PageMode], [PySide6.QtPdfWidgets.QPdfView.PageMode]
    ]]
    # pageSpacingChanged(int)
    pageSpacingChanged: typing.ClassVar[Signal[
        [int], [], [], [], [], [], [], [],
        [int], [int], [int], [int], [int], [int], [int], [int]
    ]]
    # searchModelChanged(QPdfSearchModel*)
    searchModelChanged: typing.ClassVar[Signal[
        [PySide6.QtPdf.QPdfSearchModel], [], [], [], [], [], [], [],
        [PySide6.QtPdf.QPdfSearchModel], [PySide6.QtPdf.QPdfSearchModel], [PySide6.QtPdf.QPdfSearchModel], [PySide6.QtPdf.QPdfSearchModel], [PySide6.QtPdf.QPdfSearchModel], [PySide6.QtPdf.QPdfSearchModel], [PySide6.QtPdf.QPdfSearchModel], [PySide6.QtPdf.QPdfSearchModel]
    ]]
    # zoomFactorChanged(double)
    zoomFactorChanged: typing.ClassVar[Signal[
        [float], [], [], [], [], [], [], [],
        [float], [float], [float], [float], [float], [float], [float], [float]
    ]]
    # zoomModeChanged(QPdfView::ZoomMode)
    zoomModeChanged: typing.ClassVar[Signal[
        [PySide6.QtPdfWidgets.QPdfView.ZoomMode], [], [], [], [], [], [], [],
        [PySide6.QtPdfWidgets.QPdfView.ZoomMode], [PySide6.QtPdfWidgets.QPdfView.ZoomMode], [PySide6.QtPdfWidgets.QPdfView.ZoomMode], [PySide6.QtPdfWidgets.QPdfView.ZoomMode], [PySide6.QtPdfWidgets.QPdfView.ZoomMode], [PySide6.QtPdfWidgets.QPdfView.ZoomMode], [PySide6.QtPdfWidgets.QPdfView.ZoomMode], [PySide6.QtPdfWidgets.QPdfView.ZoomMode]
    ]]

    class PageMode(enum.Enum):
        SinglePage                = 0x0
        MultiPage                 = 0x1

    class ZoomMode(enum.Enum):
        Custom                    = 0x0
        FitToWidth                = 0x1
        FitInView                 = 0x2

    @typing.overload
    def __init__(self, parent: PySide6.QtWidgets.QWidget, /, *, document: PySide6.QtPdf.QPdfDocument | None = ..., pageMode: PySide6.QtPdfWidgets.QPdfView.PageMode | None = ..., zoomMode: PySide6.QtPdfWidgets.QPdfView.ZoomMode | None = ..., zoomFactor: float | None = ..., pageSpacing: int | None = ..., documentMargins: PySide6.QtCore.QMargins | None = ..., searchModel: PySide6.QtPdf.QPdfSearchModel | None = ..., currentSearchResultIndex: int | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, *, document: PySide6.QtPdf.QPdfDocument | None = ..., pageMode: PySide6.QtPdfWidgets.QPdfView.PageMode | None = ..., zoomMode: PySide6.QtPdfWidgets.QPdfView.ZoomMode | None = ..., zoomFactor: float | None = ..., pageSpacing: int | None = ..., documentMargins: PySide6.QtCore.QMargins | None = ..., searchModel: PySide6.QtPdf.QPdfSearchModel | None = ..., currentSearchResultIndex: int | None = ...) -> None: ...

    def currentSearchResultIndex(self, /) -> int: ...
    def document(self, /) -> PySide6.QtPdf.QPdfDocument: ...
    def documentMargins(self, /) -> PySide6.QtCore.QMargins: ...
    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None: ...
    def pageMode(self, /) -> PySide6.QtPdfWidgets.QPdfView.PageMode: ...
    def pageNavigator(self, /) -> PySide6.QtPdf.QPdfPageNavigator: ...
    def pageSpacing(self, /) -> int: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None: ...
    def resizeEvent(self, event: PySide6.QtGui.QResizeEvent, /) -> None: ...
    def scrollContentsBy(self, dx: int, dy: int, /) -> None: ...
    def searchModel(self, /) -> PySide6.QtPdf.QPdfSearchModel: ...
    def setCurrentSearchResultIndex(self, currentResult: int, /) -> None: ...
    def setDocument(self, document: PySide6.QtPdf.QPdfDocument, /) -> None: ...
    def setDocumentMargins(self, margins: PySide6.QtCore.QMargins, /) -> None: ...
    def setPageMode(self, mode: PySide6.QtPdfWidgets.QPdfView.PageMode, /) -> None: ...
    def setPageSpacing(self, spacing: int, /) -> None: ...
    def setSearchModel(self, searchModel: PySide6.QtPdf.QPdfSearchModel, /) -> None: ...
    def setZoomFactor(self, factor: float, /) -> None: ...
    def setZoomMode(self, mode: PySide6.QtPdfWidgets.QPdfView.ZoomMode, /) -> None: ...
    def zoomFactor(self, /) -> float: ...
    def zoomMode(self, /) -> PySide6.QtPdfWidgets.QPdfView.ZoomMode: ...


# eof
