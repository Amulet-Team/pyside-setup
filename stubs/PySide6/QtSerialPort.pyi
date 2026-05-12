# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
"""
This file contains the exact signatures for all functions in module
PySide6.QtSerialPort, except for defaults which are replaced by "...".
"""

# mypy: disable-error-code="override, overload-overlap"
# Module `PySide6.QtSerialPort`

import PySide6.QtSerialPort
import PySide6.QtCore

import enum
import typing
from PySide6.QtCore import Signal
from shiboken6 import Shiboken


class QIntList:
    ...


class QSerialPort(PySide6.QtCore.QIODevice):
    # baudRateChanged(int,QSerialPort::Directions)
    baudRateChanged: typing.ClassVar[Signal[
        [int, PySide6.QtSerialPort.QSerialPort.Direction], [int], [], [], [], [], [], [],
        [int, PySide6.QtSerialPort.QSerialPort.Direction], [int, PySide6.QtSerialPort.QSerialPort.Direction], [int, PySide6.QtSerialPort.QSerialPort.Direction], [int, PySide6.QtSerialPort.QSerialPort.Direction], [int, PySide6.QtSerialPort.QSerialPort.Direction], [int, PySide6.QtSerialPort.QSerialPort.Direction], [int, PySide6.QtSerialPort.QSerialPort.Direction], [int, PySide6.QtSerialPort.QSerialPort.Direction]
    ]]
    # breakEnabledChanged(bool)
    breakEnabledChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # dataBitsChanged(QSerialPort::DataBits)
    dataBitsChanged: typing.ClassVar[Signal[
        [PySide6.QtSerialPort.QSerialPort.DataBits], [], [], [], [], [], [], [],
        [PySide6.QtSerialPort.QSerialPort.DataBits], [PySide6.QtSerialPort.QSerialPort.DataBits], [PySide6.QtSerialPort.QSerialPort.DataBits], [PySide6.QtSerialPort.QSerialPort.DataBits], [PySide6.QtSerialPort.QSerialPort.DataBits], [PySide6.QtSerialPort.QSerialPort.DataBits], [PySide6.QtSerialPort.QSerialPort.DataBits], [PySide6.QtSerialPort.QSerialPort.DataBits]
    ]]
    # dataTerminalReadyChanged(bool)
    dataTerminalReadyChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # errorOccurred(QSerialPort::SerialPortError)
    errorOccurred: typing.ClassVar[Signal[
        [PySide6.QtSerialPort.QSerialPort.SerialPortError], [], [], [], [], [], [], [],
        [PySide6.QtSerialPort.QSerialPort.SerialPortError], [PySide6.QtSerialPort.QSerialPort.SerialPortError], [PySide6.QtSerialPort.QSerialPort.SerialPortError], [PySide6.QtSerialPort.QSerialPort.SerialPortError], [PySide6.QtSerialPort.QSerialPort.SerialPortError], [PySide6.QtSerialPort.QSerialPort.SerialPortError], [PySide6.QtSerialPort.QSerialPort.SerialPortError], [PySide6.QtSerialPort.QSerialPort.SerialPortError]
    ]]
    # flowControlChanged(QSerialPort::FlowControl)
    flowControlChanged: typing.ClassVar[Signal[
        [PySide6.QtSerialPort.QSerialPort.FlowControl], [], [], [], [], [], [], [],
        [PySide6.QtSerialPort.QSerialPort.FlowControl], [PySide6.QtSerialPort.QSerialPort.FlowControl], [PySide6.QtSerialPort.QSerialPort.FlowControl], [PySide6.QtSerialPort.QSerialPort.FlowControl], [PySide6.QtSerialPort.QSerialPort.FlowControl], [PySide6.QtSerialPort.QSerialPort.FlowControl], [PySide6.QtSerialPort.QSerialPort.FlowControl], [PySide6.QtSerialPort.QSerialPort.FlowControl]
    ]]
    # parityChanged(QSerialPort::Parity)
    parityChanged: typing.ClassVar[Signal[
        [PySide6.QtSerialPort.QSerialPort.Parity], [], [], [], [], [], [], [],
        [PySide6.QtSerialPort.QSerialPort.Parity], [PySide6.QtSerialPort.QSerialPort.Parity], [PySide6.QtSerialPort.QSerialPort.Parity], [PySide6.QtSerialPort.QSerialPort.Parity], [PySide6.QtSerialPort.QSerialPort.Parity], [PySide6.QtSerialPort.QSerialPort.Parity], [PySide6.QtSerialPort.QSerialPort.Parity], [PySide6.QtSerialPort.QSerialPort.Parity]
    ]]
    # requestToSendChanged(bool)
    requestToSendChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # settingsRestoredOnCloseChanged(bool)
    settingsRestoredOnCloseChanged: typing.ClassVar[Signal[
        [bool], [], [], [], [], [], [], [],
        [bool], [bool], [bool], [bool], [bool], [bool], [bool], [bool]
    ]]
    # stopBitsChanged(QSerialPort::StopBits)
    stopBitsChanged: typing.ClassVar[Signal[
        [PySide6.QtSerialPort.QSerialPort.StopBits], [], [], [], [], [], [], [],
        [PySide6.QtSerialPort.QSerialPort.StopBits], [PySide6.QtSerialPort.QSerialPort.StopBits], [PySide6.QtSerialPort.QSerialPort.StopBits], [PySide6.QtSerialPort.QSerialPort.StopBits], [PySide6.QtSerialPort.QSerialPort.StopBits], [PySide6.QtSerialPort.QSerialPort.StopBits], [PySide6.QtSerialPort.QSerialPort.StopBits], [PySide6.QtSerialPort.QSerialPort.StopBits]
    ]]

    class BaudRate(enum.IntEnum):
        Baud1200                  = 0x4b0
        Baud2400                  = 0x960
        Baud4800                  = 0x12c0
        Baud9600                  = 0x2580
        Baud19200                 = 0x4b00
        Baud38400                 = 0x9600
        Baud57600                 = 0xe100
        Baud115200                = 0x1c200

    class DataBits(enum.Enum):
        Data5                     = 0x5
        Data6                     = 0x6
        Data7                     = 0x7
        Data8                     = 0x8

    class Direction(enum.Flag):
        Input                     = 0x1
        Output                    = 0x2
        AllDirections             = 0x3

    class FlowControl(enum.Enum):
        NoFlowControl             = 0x0
        HardwareControl           = 0x1
        SoftwareControl           = 0x2

    class Parity(enum.Enum):
        NoParity                  = 0x0
        EvenParity                = 0x2
        OddParity                 = 0x3
        SpaceParity               = 0x4
        MarkParity                = 0x5

    class PinoutSignal(enum.Flag):
        NoSignal                  = 0x0
        DataTerminalReadySignal   = 0x4
        DataCarrierDetectSignal   = 0x8
        DataSetReadySignal        = 0x10
        RingIndicatorSignal       = 0x20
        RequestToSendSignal       = 0x40
        ClearToSendSignal         = 0x80
        SecondaryTransmittedDataSignal = 0x100
        SecondaryReceivedDataSignal = 0x200

    class SerialPortError(enum.Enum):
        NoError                   = 0x0
        DeviceNotFoundError       = 0x1
        PermissionError           = 0x2
        OpenError                 = 0x3
        WriteError                = 0x4
        ReadError                 = 0x5
        ResourceError             = 0x6
        UnsupportedOperationError = 0x7
        UnknownError              = 0x8
        TimeoutError              = 0x9
        NotOpenError              = 0xa

    class StopBits(enum.Enum):
        OneStop                   = 0x1
        TwoStop                   = 0x2
        OneAndHalfStop            = 0x3

    @typing.overload
    def __init__(self, info: PySide6.QtSerialPort.QSerialPortInfo, /, parent: PySide6.QtCore.QObject | None = ..., *, baudRate: int | None = ..., dataBits: PySide6.QtSerialPort.QSerialPort.DataBits | None = ..., parity: PySide6.QtSerialPort.QSerialPort.Parity | None = ..., stopBits: PySide6.QtSerialPort.QSerialPort.StopBits | None = ..., flowControl: PySide6.QtSerialPort.QSerialPort.FlowControl | None = ..., dataTerminalReady: bool | None = ..., requestToSend: bool | None = ..., error: PySide6.QtSerialPort.QSerialPort.SerialPortError | None = ..., breakEnabled: bool | None = ..., settingsRestoredOnClose: bool | None = ...) -> None: ...
    @typing.overload
    def __init__(self, name: str, /, parent: PySide6.QtCore.QObject | None = ..., *, baudRate: int | None = ..., dataBits: PySide6.QtSerialPort.QSerialPort.DataBits | None = ..., parity: PySide6.QtSerialPort.QSerialPort.Parity | None = ..., stopBits: PySide6.QtSerialPort.QSerialPort.StopBits | None = ..., flowControl: PySide6.QtSerialPort.QSerialPort.FlowControl | None = ..., dataTerminalReady: bool | None = ..., requestToSend: bool | None = ..., error: PySide6.QtSerialPort.QSerialPort.SerialPortError | None = ..., breakEnabled: bool | None = ..., settingsRestoredOnClose: bool | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., *, baudRate: int | None = ..., dataBits: PySide6.QtSerialPort.QSerialPort.DataBits | None = ..., parity: PySide6.QtSerialPort.QSerialPort.Parity | None = ..., stopBits: PySide6.QtSerialPort.QSerialPort.StopBits | None = ..., flowControl: PySide6.QtSerialPort.QSerialPort.FlowControl | None = ..., dataTerminalReady: bool | None = ..., requestToSend: bool | None = ..., error: PySide6.QtSerialPort.QSerialPort.SerialPortError | None = ..., breakEnabled: bool | None = ..., settingsRestoredOnClose: bool | None = ...) -> None: ...

    def baudRate(self, /, directions: PySide6.QtSerialPort.QSerialPort.Direction = ...) -> int: ...
    def bytesAvailable(self, /) -> int: ...
    def bytesToWrite(self, /) -> int: ...
    def canReadLine(self, /) -> bool: ...
    def clear(self, /, directions: PySide6.QtSerialPort.QSerialPort.Direction = ...) -> bool: ...
    def clearError(self, /) -> None: ...
    def close(self, /) -> None: ...
    def dataBits(self, /) -> PySide6.QtSerialPort.QSerialPort.DataBits: ...
    def error(self, /) -> PySide6.QtSerialPort.QSerialPort.SerialPortError: ...
    def flowControl(self, /) -> PySide6.QtSerialPort.QSerialPort.FlowControl: ...
    def flush(self, /) -> bool: ...
    def handle(self, /) -> shiboken6.Shiboken.VoidPtr | None: ...
    def isBreakEnabled(self, /) -> bool: ...
    def isDataTerminalReady(self, /) -> bool: ...
    def isRequestToSend(self, /) -> bool: ...
    def isSequential(self, /) -> bool: ...
    def open(self, mode: PySide6.QtCore.QIODeviceBase.OpenModeFlag, /) -> bool: ...
    def parity(self, /) -> PySide6.QtSerialPort.QSerialPort.Parity: ...
    def pinoutSignals(self, /) -> PySide6.QtSerialPort.QSerialPort.PinoutSignal: ...
    def portName(self, /) -> str: ...
    def readBufferSize(self, /) -> int: ...
    def readData(self, maxSize: int, /) -> object: ...
    def readLineData(self, maxSize: int, /) -> object: ...
    def setBaudRate(self, baudRate: int, /, directions: PySide6.QtSerialPort.QSerialPort.Direction = ...) -> bool: ...
    def setBreakEnabled(self, /, set: bool = ...) -> bool: ...
    def setDataBits(self, dataBits: PySide6.QtSerialPort.QSerialPort.DataBits, /) -> bool: ...
    def setDataTerminalReady(self, set: bool, /) -> bool: ...
    def setFlowControl(self, flowControl: PySide6.QtSerialPort.QSerialPort.FlowControl, /) -> bool: ...
    def setParity(self, parity: PySide6.QtSerialPort.QSerialPort.Parity, /) -> bool: ...
    def setPort(self, info: PySide6.QtSerialPort.QSerialPortInfo, /) -> None: ...
    def setPortName(self, name: str, /) -> None: ...
    def setReadBufferSize(self, size: int, /) -> None: ...
    def setRequestToSend(self, set: bool, /) -> bool: ...
    def setSettingsRestoredOnClose(self, restore: bool, /) -> None: ...
    def setStopBits(self, stopBits: PySide6.QtSerialPort.QSerialPort.StopBits, /) -> bool: ...
    def setWriteBufferSize(self, size: int, /) -> None: ...
    def settingsRestoredOnClose(self, /) -> bool: ...
    def stopBits(self, /) -> PySide6.QtSerialPort.QSerialPort.StopBits: ...
    def waitForBytesWritten(self, /, msecs: int = ...) -> bool: ...
    def waitForReadyRead(self, /, msecs: int = ...) -> bool: ...
    def writeBufferSize(self, /) -> int: ...
    def writeData(self, data: str, maxSize: int, /) -> int: ...


class QSerialPortInfo(Shiboken.Object):
    @typing.overload
    def __init__(self, /) -> None: ...
    @typing.overload
    def __init__(self, port: PySide6.QtSerialPort.QSerialPort, /) -> None: ...
    @typing.overload
    def __init__(self, other: PySide6.QtSerialPort.QSerialPortInfo, /) -> None: ...
    @typing.overload
    def __init__(self, name: str, /) -> None: ...

    def __copy__(self, /) -> PySide6.QtSerialPort.QSerialPortInfo: ...
    @staticmethod
    def availablePorts() -> typing.List[PySide6.QtSerialPort.QSerialPortInfo]: ...
    def description(self, /) -> str: ...
    def hasProductIdentifier(self, /) -> bool: ...
    def hasVendorIdentifier(self, /) -> bool: ...
    def isNull(self, /) -> bool: ...
    def manufacturer(self, /) -> str: ...
    def portName(self, /) -> str: ...
    def productIdentifier(self, /) -> int: ...
    def serialNumber(self, /) -> str: ...
    @staticmethod
    def standardBaudRates() -> typing.List[int]: ...
    def swap(self, other: PySide6.QtSerialPort.QSerialPortInfo, /) -> None: ...
    def systemLocation(self, /) -> str: ...
    def vendorIdentifier(self, /) -> int: ...


# eof
