# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
"""
This file contains the exact signatures for all functions in module
PySide6.QtWebEngineQuick, except for defaults which are replaced by "...".
"""

# mypy: disable-error-code="override, overload-overlap"
# Module `PySide6.QtWebEngineQuick`

import PySide6.QtWebEngineQuick
import PySide6.QtCore
import PySide6.QtWebEngineCore

import enum
import typing
import collections.abc
from PySide6.QtCore import Signal
from shiboken6 import Shiboken


class QIntList:
    ...


class QQuickWebEngineDownloadRequest(PySide6.QtWebEngineCore.QWebEngineDownloadRequest):
    def qt_qmlMarker_uncreatable(self, /) -> None: ...


class QQuickWebEngineProfile(PySide6.QtCore.QObject):
    # cachePathChanged()
    cachePathChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # clearHttpCacheCompleted()
    clearHttpCacheCompleted: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # downloadFinished(QQuickWebEngineDownloadRequest*)
    downloadFinished: typing.ClassVar[Signal[
        [PySide6.QtWebEngineQuick.QQuickWebEngineDownloadRequest], [], [], [], [], [], [], [],
        [PySide6.QtWebEngineQuick.QQuickWebEngineDownloadRequest], [PySide6.QtWebEngineQuick.QQuickWebEngineDownloadRequest], [PySide6.QtWebEngineQuick.QQuickWebEngineDownloadRequest], [PySide6.QtWebEngineQuick.QQuickWebEngineDownloadRequest], [PySide6.QtWebEngineQuick.QQuickWebEngineDownloadRequest], [PySide6.QtWebEngineQuick.QQuickWebEngineDownloadRequest], [PySide6.QtWebEngineQuick.QQuickWebEngineDownloadRequest], [PySide6.QtWebEngineQuick.QQuickWebEngineDownloadRequest]
    ]]
    # downloadPathChanged()
    downloadPathChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # downloadRequested(QQuickWebEngineDownloadRequest*)
    downloadRequested: typing.ClassVar[Signal[
        [PySide6.QtWebEngineQuick.QQuickWebEngineDownloadRequest], [], [], [], [], [], [], [],
        [PySide6.QtWebEngineQuick.QQuickWebEngineDownloadRequest], [PySide6.QtWebEngineQuick.QQuickWebEngineDownloadRequest], [PySide6.QtWebEngineQuick.QQuickWebEngineDownloadRequest], [PySide6.QtWebEngineQuick.QQuickWebEngineDownloadRequest], [PySide6.QtWebEngineQuick.QQuickWebEngineDownloadRequest], [PySide6.QtWebEngineQuick.QQuickWebEngineDownloadRequest], [PySide6.QtWebEngineQuick.QQuickWebEngineDownloadRequest], [PySide6.QtWebEngineQuick.QQuickWebEngineDownloadRequest]
    ]]
    # httpAcceptLanguageChanged()
    httpAcceptLanguageChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # httpCacheMaximumSizeChanged()
    httpCacheMaximumSizeChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # httpCacheTypeChanged()
    httpCacheTypeChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # httpUserAgentChanged()
    httpUserAgentChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # offTheRecordChanged()
    offTheRecordChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # persistentCookiesPolicyChanged()
    persistentCookiesPolicyChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # persistentPermissionsPolicyChanged()
    persistentPermissionsPolicyChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # persistentStoragePathChanged()
    persistentStoragePathChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # presentNotification(QWebEngineNotification*)
    presentNotification: typing.ClassVar[Signal[
        [PySide6.QtWebEngineCore.QWebEngineNotification], [], [], [], [], [], [], [],
        [PySide6.QtWebEngineCore.QWebEngineNotification], [PySide6.QtWebEngineCore.QWebEngineNotification], [PySide6.QtWebEngineCore.QWebEngineNotification], [PySide6.QtWebEngineCore.QWebEngineNotification], [PySide6.QtWebEngineCore.QWebEngineNotification], [PySide6.QtWebEngineCore.QWebEngineNotification], [PySide6.QtWebEngineCore.QWebEngineNotification], [PySide6.QtWebEngineCore.QWebEngineNotification]
    ]]
    # pushServiceEnabledChanged()
    pushServiceEnabledChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # spellCheckEnabledChanged()
    spellCheckEnabledChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # spellCheckLanguagesChanged()
    spellCheckLanguagesChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # storageNameChanged()
    storageNameChanged: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]

    class HttpCacheType(enum.Enum):
        MemoryHttpCache           = 0x0
        DiskHttpCache             = 0x1
        NoCache                   = 0x2

    class PersistentCookiesPolicy(enum.Enum):
        NoPersistentCookies       = 0x0
        AllowPersistentCookies    = 0x1
        ForcePersistentCookies    = 0x2
        OnlyPersistentCookies     = 0x3

    class PersistentPermissionsPolicy(enum.Enum):
        AskEveryTime              = 0x0
        StoreInMemory             = 0x1
        StoreOnDisk               = 0x2

    @typing.overload
    def __init__(self, storageName: str, /, parent: PySide6.QtCore.QObject | None = ..., *, offTheRecord: bool | None = ..., persistentStoragePath: str | None = ..., cachePath: str | None = ..., httpUserAgent: str | None = ..., httpCacheType: PySide6.QtWebEngineQuick.QQuickWebEngineProfile.HttpCacheType | None = ..., httpAcceptLanguage: str | None = ..., persistentCookiesPolicy: PySide6.QtWebEngineQuick.QQuickWebEngineProfile.PersistentCookiesPolicy | None = ..., persistentPermissionsPolicy: PySide6.QtWebEngineQuick.QQuickWebEngineProfile.PersistentPermissionsPolicy | None = ..., httpCacheMaximumSize: int | None = ..., spellCheckLanguages: collections.abc.Sequence[str] | None = ..., spellCheckEnabled: bool | None = ..., downloadPath: str | None = ..., isPushServiceEnabled: bool | None = ..., clientHints: PySide6.QtWebEngineCore.QWebEngineClientHints | None = ..., extensionManager: PySide6.QtWebEngineCore.QWebEngineExtensionManager | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., *, storageName: str | None = ..., offTheRecord: bool | None = ..., persistentStoragePath: str | None = ..., cachePath: str | None = ..., httpUserAgent: str | None = ..., httpCacheType: PySide6.QtWebEngineQuick.QQuickWebEngineProfile.HttpCacheType | None = ..., httpAcceptLanguage: str | None = ..., persistentCookiesPolicy: PySide6.QtWebEngineQuick.QQuickWebEngineProfile.PersistentCookiesPolicy | None = ..., persistentPermissionsPolicy: PySide6.QtWebEngineQuick.QQuickWebEngineProfile.PersistentPermissionsPolicy | None = ..., httpCacheMaximumSize: int | None = ..., spellCheckLanguages: collections.abc.Sequence[str] | None = ..., spellCheckEnabled: bool | None = ..., downloadPath: str | None = ..., isPushServiceEnabled: bool | None = ..., clientHints: PySide6.QtWebEngineCore.QWebEngineClientHints | None = ..., extensionManager: PySide6.QtWebEngineCore.QWebEngineExtensionManager | None = ...) -> None: ...

    def cachePath(self, /) -> str: ...
    def clearHttpCache(self, /) -> None: ...
    def clientCertificateStore(self, /) -> PySide6.QtWebEngineCore.QWebEngineClientCertificateStore: ...
    def clientHints(self, /) -> PySide6.QtWebEngineCore.QWebEngineClientHints: ...
    def cookieStore(self, /) -> PySide6.QtWebEngineCore.QWebEngineCookieStore: ...
    @staticmethod
    def defaultProfile() -> PySide6.QtWebEngineQuick.QQuickWebEngineProfile: ...
    def downloadPath(self, /) -> str: ...
    def extensionManager(self, /) -> PySide6.QtWebEngineCore.QWebEngineExtensionManager: ...
    def httpAcceptLanguage(self, /) -> str: ...
    def httpCacheMaximumSize(self, /) -> int: ...
    def httpCacheType(self, /) -> PySide6.QtWebEngineQuick.QQuickWebEngineProfile.HttpCacheType: ...
    def httpUserAgent(self, /) -> str: ...
    def installUrlSchemeHandler(self, scheme: PySide6.QtCore.QByteArray | bytes | bytearray | str, arg__2: PySide6.QtWebEngineCore.QWebEngineUrlSchemeHandler, /) -> None: ...
    def isOffTheRecord(self, /) -> bool: ...
    def isPushServiceEnabled(self, /) -> bool: ...
    def isSpellCheckEnabled(self, /) -> bool: ...
    def listAllPermissions(self, /) -> typing.List[PySide6.QtWebEngineCore.QWebEnginePermission]: ...
    def listPermissionsForOrigin(self, securityOrigin: PySide6.QtCore.QUrl | str, /) -> typing.List[PySide6.QtWebEngineCore.QWebEnginePermission]: ...
    def listPermissionsForPermissionType(self, permissionType: PySide6.QtWebEngineCore.QWebEnginePermission.PermissionType, /) -> typing.List[PySide6.QtWebEngineCore.QWebEnginePermission]: ...
    def persistentCookiesPolicy(self, /) -> PySide6.QtWebEngineQuick.QQuickWebEngineProfile.PersistentCookiesPolicy: ...
    def persistentPermissionsPolicy(self, /) -> PySide6.QtWebEngineQuick.QQuickWebEngineProfile.PersistentPermissionsPolicy: ...
    def persistentStoragePath(self, /) -> str: ...
    def queryPermission(self, securityOrigin: PySide6.QtCore.QUrl | str, permissionType: PySide6.QtWebEngineCore.QWebEnginePermission.PermissionType, /) -> PySide6.QtWebEngineCore.QWebEnginePermission: ...
    def removeAllUrlSchemeHandlers(self, /) -> None: ...
    def removeUrlScheme(self, scheme: PySide6.QtCore.QByteArray | bytes | bytearray | str, /) -> None: ...
    def removeUrlSchemeHandler(self, arg__1: PySide6.QtWebEngineCore.QWebEngineUrlSchemeHandler, /) -> None: ...
    def setCachePath(self, path: str, /) -> None: ...
    def setDownloadPath(self, path: str, /) -> None: ...
    def setHttpAcceptLanguage(self, httpAcceptLanguage: str, /) -> None: ...
    def setHttpCacheMaximumSize(self, maxSize: int, /) -> None: ...
    def setHttpCacheType(self, arg__1: PySide6.QtWebEngineQuick.QQuickWebEngineProfile.HttpCacheType, /) -> None: ...
    def setHttpUserAgent(self, userAgent: str, /) -> None: ...
    def setOffTheRecord(self, offTheRecord: bool, /) -> None: ...
    def setPersistentCookiesPolicy(self, arg__1: PySide6.QtWebEngineQuick.QQuickWebEngineProfile.PersistentCookiesPolicy, /) -> None: ...
    def setPersistentPermissionsPolicy(self, arg__1: PySide6.QtWebEngineQuick.QQuickWebEngineProfile.PersistentPermissionsPolicy, /) -> None: ...
    def setPersistentStoragePath(self, path: str, /) -> None: ...
    def setPushServiceEnabled(self, enable: bool, /) -> None: ...
    def setSpellCheckEnabled(self, enabled: bool, /) -> None: ...
    def setSpellCheckLanguages(self, languages: collections.abc.Sequence[str], /) -> None: ...
    def setStorageName(self, name: str, /) -> None: ...
    def setUrlRequestInterceptor(self, interceptor: PySide6.QtWebEngineCore.QWebEngineUrlRequestInterceptor, /) -> None: ...
    def spellCheckLanguages(self, /) -> typing.List[str]: ...
    def storageName(self, /) -> str: ...
    def urlSchemeHandler(self, arg__1: PySide6.QtCore.QByteArray | bytes | bytearray | str, /) -> PySide6.QtWebEngineCore.QWebEngineUrlSchemeHandler: ...


class QtWebEngineQuick(Shiboken.Object):
    @staticmethod
    def initialize() -> None: ...


# eof
