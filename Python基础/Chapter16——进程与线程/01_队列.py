# coding:utf-8

# 进程间通信，队列
from multiprocessing import Process,Queue
import  time

# 向队列中写入数据
def write_task(q):
    if not q.full():
        for i in range(5):
            message = "消息"+str(i)
            q.put(message)
            print('写入:%s'%message)


# 从队列中读取数据
def read_task(q):
    time.sleep(1)  # 休眠1秒
    while not q.empty():
        print('读取%s' %q.get(True,2)) #等待2秒，如果还没有读取到任何消息，则抛出"Queue Empty"异常


if __name__ == '__main__':
    print('-----父进程开始-----')
    q=Queue()
    pw = Process(target=write_task,args=(q,))
    pr = Process(target=read_task,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.join()
    print('-----父进程结束-----')