#ifndef OVERRIDETEST_H
#define OVERRIDETEST_H

#include<QThread>///! 多线程头文件
#include<QDebug>
#include<QObject>
#include<QDebug>

///! 定义一个子线程
class WorkerThread : public QThread
{
    Q_OBJECT
    ///! 重写run函数
    void run() override {
        QString result;
        qDebug()<<"child thread!";
        result="childThread";

        emit resultReady(result);///! 发出信号，可以跨线程调用
    }
signals:
    void resultReady(const QString &s);
};

class MainClass:public QObject
{
    Q_OBJECT
public:
    MainClass();
    ~MainClass();

    ///! 关联信号槽、启动子线程
    void StartWorkThread();
public slots:
    ///! 处理子线程的信号的槽函数
    void handleResults(QString result);

private:
    WorkerThread *mThread; ///! 子线程

};
#endif // OVERRIDETEST_H
