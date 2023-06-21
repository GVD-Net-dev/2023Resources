#ifndef SERVERT_H
#define SERVERT_H

#include <QDebug>
#include <QObject>
#include <QLocalServer>
#include <QLocalSocket>
#include <QByteArray>
#include <QString>

class ServerT:public QObject
{
    Q_OBJECT
public:
    ServerT();
    ~ServerT();

    void testF();

    void UseService();
    void setServerName(QString _name);

public:
    QString serverName;
private:
    QLocalServer *m_server;

private slots:
    void on_connected();
    void on_readyread();
};

#endif // SERVERT_H
