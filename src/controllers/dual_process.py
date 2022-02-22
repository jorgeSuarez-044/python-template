"""This script contains the structure to multiprocessing and threads"""
from multiprocessing import Process
from rq import Worker, Queue, Connection
from redis import Redis

# Creation of the connection
redis_conn = Redis()

listen = ['high', 'default', 'low']


def job_test(id_call, id_instruction, id_type, url_bucket):
    if id_type == 'play':
        print('Calling', ' - ', 'Id_call: ', id_call, ' - ', 'Id_instruction: ', id_instruction,
              ' - ', 'Resource: ', url_bucket)
    else:
        print('Waiting....')


def streaming():
    """Counting until 100"""
    count = 0
    while count < 100:
        count += 1
        print('Process:',
              Process(),
              'Count:', count)


def redis_listener():
    """Test process"""
    with Connection(redis_conn):
        worker = Worker(map(Queue, listen))
        worker.work()


process_streaming = Process(target=streaming)
process_redis = Process(target=redis_listener)
# Start of processes
# process_streaming.start()
# process_redis.start()
