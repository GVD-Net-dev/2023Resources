#include <QApplication>
#include <QtCore>
#include "serverT.h"
#include "clientT.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    ServerT m_fun;
    m_fun.setServerName("testtestzqy");///! 设置监听对象
    m_fun.UseService();///! 使用服务
    ClientT m_fun2;
    m_fun2.setClientName("testtestzqy");
    m_fun2.UseService();
    m_fun2.SendData("content2!!");
    m_fun2.SendData("content3!!!");///客户端发送第三条消息
    m_fun2.SendData("content4!");///! 客户端发送第四条消息

    return a.exec();
}
