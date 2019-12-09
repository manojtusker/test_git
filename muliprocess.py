from multiprocessing import Process,freeze_support
import os
import math


def calc():
    for i in range(0, 4000000):
        math.sqrt(i)

if __name__ =='__main__':
    # freeze_support()      # If the freeze_support() line is omitted then trying to run the frozen executable will raise RuntimeError.



    processes = []

    for i in range(os.cpu_count()):
        print('registering process %d' % i)
        processes.append(Process(target=calc))

    for process in processes:
        process.start()

    for process in processes:
        process.join()