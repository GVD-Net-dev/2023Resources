#include "overridetest.h"

MainClass::MainClass()
{

}

MainClass::~MainClass()
{
    mThread->quit();///! 可正常终止线程（结束线程的事件循环）
    ///! 在执行quit()后，调用wait()来等待QThread子线程的结束。
    ///! 这样就能保证在清除QThread时，子线程已经停止运行。
    mThread->wait();

}

void MainClass::StartWorkThread()
{
    mThread = new WorkerThread();

    ///! 子线程可以发信号给其他线程进行处理
    connect(mThread,&WorkerThread::resultReady,this,&MainClass::handleResults);

    ///! 如果线程完成了，则删除这个线程
    connect(mThread,&WorkerThread::finished,mThread,&QObject::deleteLater);

    ///! 启动这个线程
    mThread->start();
}

void MainClass::handleResults(QString result)
{
    qDebug()<<"I have receive the child thread result: "<<result;
}
