# 新建文件要添加的内容
QT += core gui
QT += xml
QT +=network
greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

CONFIG += c++11

#######################################################

HEADERS += \
    serverT.h

SOURCES += \
    main.cpp \
    serverT.cpp

########################################################
# 引用了clientTest这个插件



win32:CONFIG(release, debug|release): LIBS += -L$$OUT_PWD/../clientTest/release/ -lclientT
else:win32:CONFIG(debug, debug|release): LIBS += -L$$OUT_PWD/../clientTest/debug/ -lclientT
else:unix: LIBS += -L$$OUT_PWD/../clientTest/ -lclientT

INCLUDEPATH += $$PWD/../clientTest
DEPENDPATH += $$PWD/../clientTest
