#ifndef CLIENTT_H
#define CLIENTT_H

#include <QObject>
#include <QLocalServer>
#include <QLocalSocket>
#include <QDebug>
#include <QString>
#include "clientT_global.h"

class CLIENTT_EXPORT ClientT:public QObject
{
    Q_OBJECT
public:
    ClientT();
    ~ClientT();

    void UseService();

    void testFun();
    void setClientName(QString _name);

    void SendData(QString _data);
public:
    QString clientName;
private:
    QLocalSocket *m_client;

private slots:
    void on_connected();
    void on_disconnected();

};

#endif // CLIENTT_H
