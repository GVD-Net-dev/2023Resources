# 新建文件要添加的内容
QT += core gui
QT += xml
QT +=network
greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

CONFIG += c++11

####################################
# 设置编译成动态库
TARGET = clientT
TEMPLATE = lib
DEFINES +=CLIENTT_LIBRARY

####################################


HEADERS += \
    clientT.h \
    clientT_global.h

SOURCES += \
    clientT.cpp
