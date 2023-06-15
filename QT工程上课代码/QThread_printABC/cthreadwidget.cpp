#include "cthreadwidget.h"
#include "ui_cthreadwidget.h"

CThreadWidget::CThreadWidget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::CThreadWidget)
{
    ui->setupUi(this);

    ///! 使用循环为线程链表添加三个线程并运行
    for(int index=0;index<3;index++)
    {
        m_threadList.append(new CTHread);
        m_threadList[index]->setFlag(65+index);///!设置标识符
        m_threadList[index]->start();///!启动线程
    }

    // 将获得各个线程的m_currentCondition设置到对应的存储位置中
    ///! 这里可以如此理解 （0->1：代表0唤醒1）
    ///! 0->1, 1->2, 2->0
    ///! 如此看来形成了环状的唤醒关系
    m_threadList[0]->setNextCondition(m_threadList[1]->currentCondition());
    m_threadList[1]->setNextCondition(m_threadList[2]->currentCondition());
    m_threadList[2]->setNextCondition(m_threadList[0]->currentCondition());
}

CThreadWidget::~CThreadWidget()
{
    foreach(CTHread *thread,m_threadList)
    {
        thread->quit();
        thread->wait(1);
        delete thread;
    }
    delete ui;
}

///! 开始按钮
void CThreadWidget::on_pushButton_clicked()
{
    //如果观察了自定义线程类，会发现线程启动过后都会阻塞在wait函数的位置
    //所以我们需要自己唤醒某一个线程让环形的唤醒关系跑起来
    m_threadList[0]->currentCondition()->wakeAll();
}
