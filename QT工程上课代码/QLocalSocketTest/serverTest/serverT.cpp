#include"serverT.h"

ServerT::ServerT()
{

}

ServerT::~ServerT()
{

}

void ServerT::testF()
{
    qDebug()<<"hello world!";
}

void ServerT::UseService()
{
    m_server = new QLocalServer(this);
    connect(m_server,SIGNAL(newConnection()),this,SLOT(on_connected()));
    ///! 设置监听状态
    m_server->listen(serverName);
}

void ServerT::setServerName(QString _name)
{
    serverName = _name;
}

///! 连接上
void ServerT::on_connected()
{
    qDebug()<<"Server: on connected!";
    QLocalSocket *client = m_server->nextPendingConnection();
    connect(client,SIGNAL(readyRead()),this,SLOT(on_readyread()));

}

void ServerT::on_readyread()
{
    QLocalSocket *client = static_cast<QLocalSocket*>(sender());
    qDebug()<<"server has readyread!";
    QByteArray read_data =  client->readAll();///! 读取到的是字节数据
    qDebug()<<read_data;
    qDebug()<<"*********************************************";
}
