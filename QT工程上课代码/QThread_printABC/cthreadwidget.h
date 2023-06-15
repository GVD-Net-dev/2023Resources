#ifndef CTHREADWIDGET_H
#define CTHREADWIDGET_H

#include <QWidget>
#include <QList>
#include <QThread>
#include "CThread.h"

namespace Ui {
class CThreadWidget;
}

class CThreadWidget : public QWidget
{
    Q_OBJECT

public:
    explicit CThreadWidget(QWidget *parent = nullptr);
    ~CThreadWidget();

private slots:

    ///! 开始按钮
    void on_pushButton_clicked();

private:
    Ui::CThreadWidget *ui;
    QList<CTHread*>  m_threadList;///! 线程指针容器
};

#endif // CTHREADWIDGET_H
