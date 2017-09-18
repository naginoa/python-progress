import random, time, queue
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()
result_queue = queue.Queue()

class QueueManager(BaseManager):
    pass

def task_q():
    return task_queue
def result_q():
    return result_queue
QueueManager.register('get_task_queue', callable=task_q)
QueueManager.register('get_result_queue', callable=result_q)

manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')

if __name__ =='__main__':
    manager.start()

    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)

    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=10)
        print('Result: %s' % r)

    manager.shutdown()