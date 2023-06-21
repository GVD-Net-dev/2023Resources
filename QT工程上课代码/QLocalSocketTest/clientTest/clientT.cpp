#include "clientT.h"

ClientT::ClientT()
{
}

ClientT::~ClientT()
{


}

void ClientT::UseService()
{
    m_client = new QLocalSocket(this);
    connect(m_client,SIGNAL(connected()),this,SLOT(on_connected()));
    connect(m_client,SIGNAL(disconnected()),this,SLOT(on_disconnected));
    m_client->connectToServer(clientName);///! 绑定在一个指定的服务器名字上

}

void ClientT::testFun()
{

    qDebug()<<"client Test";

}

void ClientT::setClientName(QString _name)
{
    clientName = _name;
}

void ClientT::SendData(QString _data)
{
    m_client->write(_data.toLatin1());
    m_client->flush();
}

void ClientT::on_connected()
{
    QString m_text(" clientT: I am client!");
    m_client->write(m_text.toLatin1());
    m_client->flush();
}

void ClientT::on_disconnected()
{
    qDebug()<<"clientT: disconnected!";
}
