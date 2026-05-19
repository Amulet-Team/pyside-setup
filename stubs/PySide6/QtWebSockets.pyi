# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
"""
This file contains the exact signatures for all functions in module
PySide6.QtWebSockets, except for defaults which are replaced by "...".
"""

# mypy: disable-error-code="override, overload-overlap"
# Module `PySide6.QtWebSockets`

import PySide6.QtWebSockets
import PySide6.QtCore
import PySide6.QtNetwork

import os
import enum
import typing
import collections.abc
from PySide6.QtCore import Signal
import shiboken6


class QIntList:
    ...


class QMaskGenerator(PySide6.QtCore.QObject):
    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ...) -> None: ...

    def nextMask(self, /) -> int: ...
    def seed(self, /) -> bool: ...


class QWebSocket(PySide6.QtCore.QObject):
    # aboutToClose()
    aboutToClose: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # alertReceived(QSsl::AlertLevel,QSsl::AlertType,QString)
    alertReceived: typing.ClassVar[Signal[
        [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType, str], [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType], [PySide6.QtNetwork.QSsl.AlertLevel], [], [], [], [], [],
        [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType, str], [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType, str], [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType, str], [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType, str], [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType, str], [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType, str], [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType, str], [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType, str]
    ]]
    # alertSent(QSsl::AlertLevel,QSsl::AlertType,QString)
    alertSent: typing.ClassVar[Signal[
        [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType, str], [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType], [PySide6.QtNetwork.QSsl.AlertLevel], [], [], [], [], [],
        [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType, str], [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType, str], [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType, str], [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType, str], [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType, str], [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType, str], [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType, str], [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType, str]
    ]]
    # authenticationRequired(QAuthenticator*)
    authenticationRequired: typing.ClassVar[Signal[
        [PySide6.QtNetwork.QAuthenticator], [], [], [], [], [], [], [],
        [PySide6.QtNetwork.QAuthenticator], [PySide6.QtNetwork.QAuthenticator], [PySide6.QtNetwork.QAuthenticator], [PySide6.QtNetwork.QAuthenticator], [PySide6.QtNetwork.QAuthenticator], [PySide6.QtNetwork.QAuthenticator], [PySide6.QtNetwork.QAuthenticator], [PySide6.QtNetwork.QAuthenticator]
    ]]
    # binaryFrameReceived(QByteArray,bool)
    binaryFrameReceived: typing.ClassVar[Signal[
        [PySide6.QtCore.QByteArray, bool], [PySide6.QtCore.QByteArray], [], [], [], [], [], [],
        [PySide6.QtCore.QByteArray, bool], [PySide6.QtCore.QByteArray, bool], [PySide6.QtCore.QByteArray, bool], [PySide6.QtCore.QByteArray, bool], [PySide6.QtCore.QByteArray, bool], [PySide6.QtCore.QByteArray, bool], [PySide6.QtCore.QByteArray, bool], [PySide6.QtCore.QByteArray, bool]
    ]]
    # binaryMessageReceived(QByteArray)
    binaryMessageReceived: typing.ClassVar[Signal[
        [PySide6.QtCore.QByteArray], [], [], [], [], [], [], [],
        [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray], [PySide6.QtCore.QByteArray]
    ]]
    # bytesWritten(qlonglong)
    bytesWritten: typing.ClassVar[Signal[
        [int], [], [], [], [], [], [], [],
        [int], [int], [int], [int], [int], [int], [int], [int]
    ]]
    # connected()
    connected: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # disconnected()
    disconnected: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # error(QAbstractSocket::SocketError)
    error: typing.ClassVar[Signal[
        [PySide6.QtNetwork.QAbstractSocket.SocketError], [], [], [], [], [], [], [],
        [PySide6.QtNetwork.QAbstractSocket.SocketError], [PySide6.QtNetwork.QAbstractSocket.SocketError], [PySide6.QtNetwork.QAbstractSocket.SocketError], [PySide6.QtNetwork.QAbstractSocket.SocketError], [PySide6.QtNetwork.QAbstractSocket.SocketError], [PySide6.QtNetwork.QAbstractSocket.SocketError], [PySide6.QtNetwork.QAbstractSocket.SocketError], [PySide6.QtNetwork.QAbstractSocket.SocketError]
    ]]
    # errorOccurred(QAbstractSocket::SocketError)
    errorOccurred: typing.ClassVar[Signal[
        [PySide6.QtNetwork.QAbstractSocket.SocketError], [], [], [], [], [], [], [],
        [PySide6.QtNetwork.QAbstractSocket.SocketError], [PySide6.QtNetwork.QAbstractSocket.SocketError], [PySide6.QtNetwork.QAbstractSocket.SocketError], [PySide6.QtNetwork.QAbstractSocket.SocketError], [PySide6.QtNetwork.QAbstractSocket.SocketError], [PySide6.QtNetwork.QAbstractSocket.SocketError], [PySide6.QtNetwork.QAbstractSocket.SocketError], [PySide6.QtNetwork.QAbstractSocket.SocketError]
    ]]
    # handshakeInterruptedOnError(QSslError)
    handshakeInterruptedOnError: typing.ClassVar[Signal[
        [PySide6.QtNetwork.QSslError], [], [], [], [], [], [], [],
        [PySide6.QtNetwork.QSslError], [PySide6.QtNetwork.QSslError], [PySide6.QtNetwork.QSslError], [PySide6.QtNetwork.QSslError], [PySide6.QtNetwork.QSslError], [PySide6.QtNetwork.QSslError], [PySide6.QtNetwork.QSslError], [PySide6.QtNetwork.QSslError]
    ]]
    # peerVerifyError(QSslError)
    peerVerifyError: typing.ClassVar[Signal[
        [PySide6.QtNetwork.QSslError], [], [], [], [], [], [], [],
        [PySide6.QtNetwork.QSslError], [PySide6.QtNetwork.QSslError], [PySide6.QtNetwork.QSslError], [PySide6.QtNetwork.QSslError], [PySide6.QtNetwork.QSslError], [PySide6.QtNetwork.QSslError], [PySide6.QtNetwork.QSslError], [PySide6.QtNetwork.QSslError]
    ]]
    # pong(qulonglong,QByteArray)
    pong: typing.ClassVar[Signal[
        [int, PySide6.QtCore.QByteArray], [int], [], [], [], [], [], [],
        [int, PySide6.QtCore.QByteArray], [int, PySide6.QtCore.QByteArray], [int, PySide6.QtCore.QByteArray], [int, PySide6.QtCore.QByteArray], [int, PySide6.QtCore.QByteArray], [int, PySide6.QtCore.QByteArray], [int, PySide6.QtCore.QByteArray], [int, PySide6.QtCore.QByteArray]
    ]]
    # preSharedKeyAuthenticationRequired(QSslPreSharedKeyAuthenticator*)
    preSharedKeyAuthenticationRequired: typing.ClassVar[Signal[
        [PySide6.QtNetwork.QSslPreSharedKeyAuthenticator], [], [], [], [], [], [], [],
        [PySide6.QtNetwork.QSslPreSharedKeyAuthenticator], [PySide6.QtNetwork.QSslPreSharedKeyAuthenticator], [PySide6.QtNetwork.QSslPreSharedKeyAuthenticator], [PySide6.QtNetwork.QSslPreSharedKeyAuthenticator], [PySide6.QtNetwork.QSslPreSharedKeyAuthenticator], [PySide6.QtNetwork.QSslPreSharedKeyAuthenticator], [PySide6.QtNetwork.QSslPreSharedKeyAuthenticator], [PySide6.QtNetwork.QSslPreSharedKeyAuthenticator]
    ]]
    # proxyAuthenticationRequired(QNetworkProxy,QAuthenticator*)
    proxyAuthenticationRequired: typing.ClassVar[Signal[
        [PySide6.QtNetwork.QNetworkProxy, PySide6.QtNetwork.QAuthenticator], [PySide6.QtNetwork.QNetworkProxy], [], [], [], [], [], [],
        [PySide6.QtNetwork.QNetworkProxy, PySide6.QtNetwork.QAuthenticator], [PySide6.QtNetwork.QNetworkProxy, PySide6.QtNetwork.QAuthenticator], [PySide6.QtNetwork.QNetworkProxy, PySide6.QtNetwork.QAuthenticator], [PySide6.QtNetwork.QNetworkProxy, PySide6.QtNetwork.QAuthenticator], [PySide6.QtNetwork.QNetworkProxy, PySide6.QtNetwork.QAuthenticator], [PySide6.QtNetwork.QNetworkProxy, PySide6.QtNetwork.QAuthenticator], [PySide6.QtNetwork.QNetworkProxy, PySide6.QtNetwork.QAuthenticator], [PySide6.QtNetwork.QNetworkProxy, PySide6.QtNetwork.QAuthenticator]
    ]]
    # readChannelFinished()
    readChannelFinished: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # sslErrors(QList<QSslError>)
    sslErrors: typing.ClassVar[Signal[
        [collections.abc.Sequence[PySide6.QtNetwork.QSslError]], [], [], [], [], [], [], [],
        [collections.abc.Sequence[PySide6.QtNetwork.QSslError]], [collections.abc.Sequence[PySide6.QtNetwork.QSslError]], [collections.abc.Sequence[PySide6.QtNetwork.QSslError]], [collections.abc.Sequence[PySide6.QtNetwork.QSslError]], [collections.abc.Sequence[PySide6.QtNetwork.QSslError]], [collections.abc.Sequence[PySide6.QtNetwork.QSslError]], [collections.abc.Sequence[PySide6.QtNetwork.QSslError]], [collections.abc.Sequence[PySide6.QtNetwork.QSslError]]
    ]]
    # stateChanged(QAbstractSocket::SocketState)
    stateChanged: typing.ClassVar[Signal[
        [PySide6.QtNetwork.QAbstractSocket.SocketState], [], [], [], [], [], [], [],
        [PySide6.QtNetwork.QAbstractSocket.SocketState], [PySide6.QtNetwork.QAbstractSocket.SocketState], [PySide6.QtNetwork.QAbstractSocket.SocketState], [PySide6.QtNetwork.QAbstractSocket.SocketState], [PySide6.QtNetwork.QAbstractSocket.SocketState], [PySide6.QtNetwork.QAbstractSocket.SocketState], [PySide6.QtNetwork.QAbstractSocket.SocketState], [PySide6.QtNetwork.QAbstractSocket.SocketState]
    ]]
    # textFrameReceived(QString,bool)
    textFrameReceived: typing.ClassVar[Signal[
        [str, bool], [str], [], [], [], [], [], [],
        [str, bool], [str, bool], [str, bool], [str, bool], [str, bool], [str, bool], [str, bool], [str, bool]
    ]]
    # textMessageReceived(QString)
    textMessageReceived: typing.ClassVar[Signal[
        [str], [], [], [], [], [], [], [],
        [str], [str], [str], [str], [str], [str], [str], [str]
    ]]

    def __init__(self, /, origin: str = ..., version: PySide6.QtWebSockets.QWebSocketProtocol.Version = ..., parent: PySide6.QtCore.QObject | None = ...) -> None: ...

    def abort(self, /) -> None: ...
    def bytesToWrite(self, /) -> int: ...
    def close(self, /, closeCode: PySide6.QtWebSockets.QWebSocketProtocol.CloseCode = ..., reason: str = ...) -> None: ...
    def closeCode(self, /) -> PySide6.QtWebSockets.QWebSocketProtocol.CloseCode: ...
    def closeReason(self, /) -> str: ...
    def continueInterruptedHandshake(self, /) -> None: ...
    def errorString(self, /) -> str: ...
    def flush(self, /) -> bool: ...
    def handshakeOptions(self, /) -> PySide6.QtWebSockets.QWebSocketHandshakeOptions: ...
    @typing.overload
    def ignoreSslErrors(self, /) -> None: ...
    @typing.overload
    def ignoreSslErrors(self, errors: collections.abc.Sequence[PySide6.QtNetwork.QSslError], /) -> None: ...
    def isValid(self, /) -> bool: ...
    def localAddress(self, /) -> PySide6.QtNetwork.QHostAddress: ...
    def localPort(self, /) -> int: ...
    def maskGenerator(self, /) -> PySide6.QtWebSockets.QMaskGenerator: ...
    def maxAllowedIncomingFrameSize(self, /) -> int: ...
    def maxAllowedIncomingMessageSize(self, /) -> int: ...
    @staticmethod
    def maxIncomingFrameSize() -> int: ...
    @staticmethod
    def maxIncomingMessageSize() -> int: ...
    @staticmethod
    def maxOutgoingFrameSize() -> int: ...
    @typing.overload
    def open(self, request: PySide6.QtNetwork.QNetworkRequest, /) -> None: ...
    @typing.overload
    def open(self, request: PySide6.QtNetwork.QNetworkRequest, options: PySide6.QtWebSockets.QWebSocketHandshakeOptions, /) -> None: ...
    @typing.overload
    def open(self, url: PySide6.QtCore.QUrl | str, /) -> None: ...
    @typing.overload
    def open(self, url: PySide6.QtCore.QUrl | str, options: PySide6.QtWebSockets.QWebSocketHandshakeOptions, /) -> None: ...
    def origin(self, /) -> str: ...
    def outgoingFrameSize(self, /) -> int: ...
    def pauseMode(self, /) -> PySide6.QtNetwork.QAbstractSocket.PauseMode: ...
    def peerAddress(self, /) -> PySide6.QtNetwork.QHostAddress: ...
    def peerName(self, /) -> str: ...
    def peerPort(self, /) -> int: ...
    def ping(self, /, payload: PySide6.QtCore.QByteArray | bytes | bytearray | str = ...) -> None: ...
    def proxy(self, /) -> PySide6.QtNetwork.QNetworkProxy: ...
    def readBufferSize(self, /) -> int: ...
    def request(self, /) -> PySide6.QtNetwork.QNetworkRequest: ...
    def requestUrl(self, /) -> PySide6.QtCore.QUrl: ...
    def resourceName(self, /) -> str: ...
    def resume(self, /) -> None: ...
    def sendBinaryMessage(self, data: PySide6.QtCore.QByteArray | bytes | bytearray | str, /) -> int: ...
    def sendTextMessage(self, message: str, /) -> int: ...
    def setMaskGenerator(self, maskGenerator: PySide6.QtWebSockets.QMaskGenerator, /) -> None: ...
    def setMaxAllowedIncomingFrameSize(self, maxAllowedIncomingFrameSize: int, /) -> None: ...
    def setMaxAllowedIncomingMessageSize(self, maxAllowedIncomingMessageSize: int, /) -> None: ...
    def setOutgoingFrameSize(self, outgoingFrameSize: int, /) -> None: ...
    def setPauseMode(self, pauseMode: PySide6.QtNetwork.QAbstractSocket.PauseMode, /) -> None: ...
    def setProxy(self, networkProxy: PySide6.QtNetwork.QNetworkProxy | PySide6.QtNetwork.QNetworkProxy.ProxyType, /) -> None: ...
    def setReadBufferSize(self, size: int, /) -> None: ...
    def setSslConfiguration(self, sslConfiguration: PySide6.QtNetwork.QSslConfiguration, /) -> None: ...
    def sslConfiguration(self, /) -> PySide6.QtNetwork.QSslConfiguration: ...
    def state(self, /) -> PySide6.QtNetwork.QAbstractSocket.SocketState: ...
    def subprotocol(self, /) -> str: ...
    def version(self, /) -> PySide6.QtWebSockets.QWebSocketProtocol.Version: ...


class QWebSocketCorsAuthenticator(shiboken6.Shiboken.Object):
    @typing.overload
    def __init__(self, other: PySide6.QtWebSockets.QWebSocketCorsAuthenticator, /) -> None: ...
    @typing.overload
    def __init__(self, origin: str, /) -> None: ...

    def allowed(self, /) -> bool: ...
    def origin(self, /) -> str: ...
    def setAllowed(self, allowed: bool, /) -> None: ...
    def swap(self, other: PySide6.QtWebSockets.QWebSocketCorsAuthenticator, /) -> None: ...


class QWebSocketHandshakeOptions(shiboken6.Shiboken.Object):
    @typing.overload
    def __init__(self, /) -> None: ...
    @typing.overload
    def __init__(self, other: PySide6.QtWebSockets.QWebSocketHandshakeOptions, /) -> None: ...

    def __copy__(self, /) -> PySide6.QtWebSockets.QWebSocketHandshakeOptions: ...
    def __eq__(self, rhs: PySide6.QtWebSockets.QWebSocketHandshakeOptions, /) -> bool: ...
    def __ne__(self, rhs: PySide6.QtWebSockets.QWebSocketHandshakeOptions, /) -> bool: ...
    def setSubprotocols(self, protocols: collections.abc.Sequence[str], /) -> None: ...
    def subprotocols(self, /) -> typing.List[str]: ...
    def swap(self, other: PySide6.QtWebSockets.QWebSocketHandshakeOptions, /) -> None: ...


class QWebSocketProtocol(shiboken6.Shiboken.Object):
    class CloseCode(enum.Enum):
        CloseCodeNormal           = 0x3e8
        CloseCodeGoingAway        = 0x3e9
        CloseCodeProtocolError    = 0x3ea
        CloseCodeDatatypeNotSupported = 0x3eb
        CloseCodeReserved1004     = 0x3ec
        CloseCodeMissingStatusCode = 0x3ed
        CloseCodeAbnormalDisconnection = 0x3ee
        CloseCodeWrongDatatype    = 0x3ef
        CloseCodePolicyViolated   = 0x3f0
        CloseCodeTooMuchData      = 0x3f1
        CloseCodeMissingExtension = 0x3f2
        CloseCodeBadOperation     = 0x3f3
        CloseCodeTlsHandshakeFailed = 0x3f7

    class Version(enum.Enum):
        VersionUnknown            = -1
        Version0                  = 0x0
        Version4                  = 0x4
        Version5                  = 0x5
        Version6                  = 0x6
        Version7                  = 0x7
        Version8                  = 0x8
        Version13                 = 0xd
        VersionLatest             = 0xd


class QWebSocketServer(PySide6.QtCore.QObject):
    # acceptError(QAbstractSocket::SocketError)
    acceptError: typing.ClassVar[Signal[
        [PySide6.QtNetwork.QAbstractSocket.SocketError], [], [], [], [], [], [], [],
        [PySide6.QtNetwork.QAbstractSocket.SocketError], [PySide6.QtNetwork.QAbstractSocket.SocketError], [PySide6.QtNetwork.QAbstractSocket.SocketError], [PySide6.QtNetwork.QAbstractSocket.SocketError], [PySide6.QtNetwork.QAbstractSocket.SocketError], [PySide6.QtNetwork.QAbstractSocket.SocketError], [PySide6.QtNetwork.QAbstractSocket.SocketError], [PySide6.QtNetwork.QAbstractSocket.SocketError]
    ]]
    # alertReceived(QSsl::AlertLevel,QSsl::AlertType,QString)
    alertReceived: typing.ClassVar[Signal[
        [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType, str], [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType], [PySide6.QtNetwork.QSsl.AlertLevel], [], [], [], [], [],
        [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType, str], [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType, str], [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType, str], [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType, str], [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType, str], [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType, str], [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType, str], [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType, str]
    ]]
    # alertSent(QSsl::AlertLevel,QSsl::AlertType,QString)
    alertSent: typing.ClassVar[Signal[
        [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType, str], [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType], [PySide6.QtNetwork.QSsl.AlertLevel], [], [], [], [], [],
        [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType, str], [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType, str], [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType, str], [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType, str], [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType, str], [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType, str], [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType, str], [PySide6.QtNetwork.QSsl.AlertLevel, PySide6.QtNetwork.QSsl.AlertType, str]
    ]]
    # closed()
    closed: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # handshakeInterruptedOnError(QSslError)
    handshakeInterruptedOnError: typing.ClassVar[Signal[
        [PySide6.QtNetwork.QSslError], [], [], [], [], [], [], [],
        [PySide6.QtNetwork.QSslError], [PySide6.QtNetwork.QSslError], [PySide6.QtNetwork.QSslError], [PySide6.QtNetwork.QSslError], [PySide6.QtNetwork.QSslError], [PySide6.QtNetwork.QSslError], [PySide6.QtNetwork.QSslError], [PySide6.QtNetwork.QSslError]
    ]]
    # newConnection()
    newConnection: typing.ClassVar[Signal[
        [], [], [], [], [], [], [], [],
        [], [], [], [], [], [], [], []
    ]]
    # originAuthenticationRequired(QWebSocketCorsAuthenticator*)
    originAuthenticationRequired: typing.ClassVar[Signal[
        [PySide6.QtWebSockets.QWebSocketCorsAuthenticator], [], [], [], [], [], [], [],
        [PySide6.QtWebSockets.QWebSocketCorsAuthenticator], [PySide6.QtWebSockets.QWebSocketCorsAuthenticator], [PySide6.QtWebSockets.QWebSocketCorsAuthenticator], [PySide6.QtWebSockets.QWebSocketCorsAuthenticator], [PySide6.QtWebSockets.QWebSocketCorsAuthenticator], [PySide6.QtWebSockets.QWebSocketCorsAuthenticator], [PySide6.QtWebSockets.QWebSocketCorsAuthenticator], [PySide6.QtWebSockets.QWebSocketCorsAuthenticator]
    ]]
    # peerVerifyError(QSslError)
    peerVerifyError: typing.ClassVar[Signal[
        [PySide6.QtNetwork.QSslError], [], [], [], [], [], [], [],
        [PySide6.QtNetwork.QSslError], [PySide6.QtNetwork.QSslError], [PySide6.QtNetwork.QSslError], [PySide6.QtNetwork.QSslError], [PySide6.QtNetwork.QSslError], [PySide6.QtNetwork.QSslError], [PySide6.QtNetwork.QSslError], [PySide6.QtNetwork.QSslError]
    ]]
    # preSharedKeyAuthenticationRequired(QSslPreSharedKeyAuthenticator*)
    preSharedKeyAuthenticationRequired: typing.ClassVar[Signal[
        [PySide6.QtNetwork.QSslPreSharedKeyAuthenticator], [], [], [], [], [], [], [],
        [PySide6.QtNetwork.QSslPreSharedKeyAuthenticator], [PySide6.QtNetwork.QSslPreSharedKeyAuthenticator], [PySide6.QtNetwork.QSslPreSharedKeyAuthenticator], [PySide6.QtNetwork.QSslPreSharedKeyAuthenticator], [PySide6.QtNetwork.QSslPreSharedKeyAuthenticator], [PySide6.QtNetwork.QSslPreSharedKeyAuthenticator], [PySide6.QtNetwork.QSslPreSharedKeyAuthenticator], [PySide6.QtNetwork.QSslPreSharedKeyAuthenticator]
    ]]
    # serverError(QWebSocketProtocol::CloseCode)
    serverError: typing.ClassVar[Signal[
        [PySide6.QtWebSockets.QWebSocketProtocol.CloseCode], [], [], [], [], [], [], [],
        [PySide6.QtWebSockets.QWebSocketProtocol.CloseCode], [PySide6.QtWebSockets.QWebSocketProtocol.CloseCode], [PySide6.QtWebSockets.QWebSocketProtocol.CloseCode], [PySide6.QtWebSockets.QWebSocketProtocol.CloseCode], [PySide6.QtWebSockets.QWebSocketProtocol.CloseCode], [PySide6.QtWebSockets.QWebSocketProtocol.CloseCode], [PySide6.QtWebSockets.QWebSocketProtocol.CloseCode], [PySide6.QtWebSockets.QWebSocketProtocol.CloseCode]
    ]]
    # sslErrors(QList<QSslError>)
    sslErrors: typing.ClassVar[Signal[
        [collections.abc.Sequence[PySide6.QtNetwork.QSslError]], [], [], [], [], [], [], [],
        [collections.abc.Sequence[PySide6.QtNetwork.QSslError]], [collections.abc.Sequence[PySide6.QtNetwork.QSslError]], [collections.abc.Sequence[PySide6.QtNetwork.QSslError]], [collections.abc.Sequence[PySide6.QtNetwork.QSslError]], [collections.abc.Sequence[PySide6.QtNetwork.QSslError]], [collections.abc.Sequence[PySide6.QtNetwork.QSslError]], [collections.abc.Sequence[PySide6.QtNetwork.QSslError]], [collections.abc.Sequence[PySide6.QtNetwork.QSslError]]
    ]]
    # sslErrorsOccurred(QSslSocket*,QList<QSslError>)
    sslErrorsOccurred: typing.ClassVar[Signal[
        [PySide6.QtNetwork.QSslSocket, collections.abc.Sequence[PySide6.QtNetwork.QSslError]], [PySide6.QtNetwork.QSslSocket], [], [], [], [], [], [],
        [PySide6.QtNetwork.QSslSocket, collections.abc.Sequence[PySide6.QtNetwork.QSslError]], [PySide6.QtNetwork.QSslSocket, collections.abc.Sequence[PySide6.QtNetwork.QSslError]], [PySide6.QtNetwork.QSslSocket, collections.abc.Sequence[PySide6.QtNetwork.QSslError]], [PySide6.QtNetwork.QSslSocket, collections.abc.Sequence[PySide6.QtNetwork.QSslError]], [PySide6.QtNetwork.QSslSocket, collections.abc.Sequence[PySide6.QtNetwork.QSslError]], [PySide6.QtNetwork.QSslSocket, collections.abc.Sequence[PySide6.QtNetwork.QSslError]], [PySide6.QtNetwork.QSslSocket, collections.abc.Sequence[PySide6.QtNetwork.QSslError]], [PySide6.QtNetwork.QSslSocket, collections.abc.Sequence[PySide6.QtNetwork.QSslError]]
    ]]

    class SslMode(enum.Enum):
        SecureMode                = 0x0
        NonSecureMode             = 0x1

    def __init__(self, serverName: str, secureMode: PySide6.QtWebSockets.QWebSocketServer.SslMode, /, parent: PySide6.QtCore.QObject | None = ...) -> None: ...

    def close(self, /) -> None: ...
    def error(self, /) -> PySide6.QtWebSockets.QWebSocketProtocol.CloseCode: ...
    def errorString(self, /) -> str: ...
    def handleConnection(self, socket: PySide6.QtNetwork.QTcpSocket, /) -> None: ...
    def handshakeTimeout(self, /) -> int: ...
    def handshakeTimeoutMS(self, /) -> int: ...
    def hasPendingConnections(self, /) -> bool: ...
    def isListening(self, /) -> bool: ...
    def listen(self, /, address: PySide6.QtNetwork.QHostAddress | PySide6.QtNetwork.QHostAddress.SpecialAddress = ..., port: int | None = ...) -> bool: ...
    def maxPendingConnections(self, /) -> int: ...
    def nativeDescriptor(self, /) -> int: ...
    def nextPendingConnection(self, /) -> PySide6.QtWebSockets.QWebSocket: ...
    def pauseAccepting(self, /) -> None: ...
    def proxy(self, /) -> PySide6.QtNetwork.QNetworkProxy: ...
    def resumeAccepting(self, /) -> None: ...
    def secureMode(self, /) -> PySide6.QtWebSockets.QWebSocketServer.SslMode: ...
    def serverAddress(self, /) -> PySide6.QtNetwork.QHostAddress: ...
    def serverName(self, /) -> str: ...
    def serverPort(self, /) -> int: ...
    def serverUrl(self, /) -> PySide6.QtCore.QUrl: ...
    def setHandshakeTimeout(self, msec: int, /) -> None: ...
    def setMaxPendingConnections(self, numConnections: int, /) -> None: ...
    def setNativeDescriptor(self, descriptor: int, /) -> bool: ...
    def setProxy(self, networkProxy: PySide6.QtNetwork.QNetworkProxy | PySide6.QtNetwork.QNetworkProxy.ProxyType, /) -> None: ...
    def setServerName(self, serverName: str, /) -> None: ...
    def setSocketDescriptor(self, socketDescriptor: int, /) -> bool: ...
    def setSslConfiguration(self, sslConfiguration: PySide6.QtNetwork.QSslConfiguration, /) -> None: ...
    def setSupportedSubprotocols(self, protocols: collections.abc.Sequence[str], /) -> None: ...
    def socketDescriptor(self, /) -> int: ...
    def sslConfiguration(self, /) -> PySide6.QtNetwork.QSslConfiguration: ...
    def supportedSubprotocols(self, /) -> typing.List[str]: ...
    def supportedVersions(self, /) -> typing.List[PySide6.QtWebSockets.QWebSocketProtocol.Version]: ...


# eof
