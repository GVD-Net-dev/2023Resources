#include "cthreadwidget.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    CThreadWidget w;
    w.show();
    return a.exec();
}
