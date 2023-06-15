#include "CThread.h"

CTHread::CTHread(QObject *parent):QThread(parent)
{
    m_mutex = new QMutex;///! new当前线程的线程锁
    m_currentCondition = new QWaitCondition;///! new 当前线程的条件变量

}

CTHread::~CTHread()
{
    delete m_currentCondition;
    delete m_mutex;
}

void CTHread::run()
{
    ///! 循环输出八次
    for(int index=0;index<8;index++)
    {
        ///! 将线程上锁
        m_mutex->lock();
        ///! 阻塞并暂时释放指定的线程锁（等待wakeAll函数或wakeOne函数将其唤醒)
        m_currentCondition->wait(m_mutex);
        ///! 输出当前线程的标识符和线程ID
        qDebug()<<m_flag<<QThread::currentThreadId();
        QThread::usleep(300000);///! 使线程睡眠一段时间（单位：微秒）
        ///! 线程锁解锁
        m_mutex->unlock();
        ///! 唤醒m_nextCondition中所有正在等待的线程
        ///! wakeOne函数也能唤醒等待的线程，不过好像不能指定，除非有不同的条件变量
        ///! （wakeOne唤醒的线程取决于操作系统的调度策略，无法控制或预测）
        m_nextCondition->wakeAll();
    }
}

void CTHread::setFlag(char flag)
{
    m_flag = flag;
}

void CTHread::setNextCondition(QWaitCondition *nextCondition)
{
    m_nextCondition = nextCondition;
}

QWaitCondition *CTHread::currentCondition() const
{
    return m_currentCondition;
}
