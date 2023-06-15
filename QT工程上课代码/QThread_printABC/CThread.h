#ifndef CTHREAD_H
#define CTHREAD_H

#include <QObject>
#include <QThread>///! 多线程
#include <QMutex>///! 互斥锁
#include <QWaitCondition> ///! 条件变量
#include <QDebug>

class CTHread: public QThread
{
    Q_OBJECT
public:
    ///! explicit: C++中的关键字explicit主要是用来修饰类的构造函数，被修饰的构造函数的类，不能发生相应的隐式类型转换，只能以显示的方式进行类型转换。
    explicit CTHread(QObject *parent = nullptr);
    ~CTHread();

    void run() override;

public:
    void setFlag(char flag);
    void setNextCondition(QWaitCondition *nextCondition);   //设置下次应运行线程的线程锁
    QWaitCondition *currentCondition() const;   //获取当前线程锁函数，用于其他线程设置m_nextMutex

private:
    QMutex *            m_mutex;            //定义一个线程锁变量
    QWaitCondition *    m_currentCondition; //定义一个当前线程的QWaitCondition变量（条件变量）
    QWaitCondition *    m_nextCondition;    //定义一个用于存放下一个运行线程QWaitCondition变量
    char                m_flag;             //定义一个标识符，用于输出

};


#endif // CTHREAD_H
