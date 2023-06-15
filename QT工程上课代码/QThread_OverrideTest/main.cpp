#include "overridetest.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainClass w;
    w.StartWorkThread();
    return a.exec();
}
