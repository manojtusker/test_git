


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



# Threading vs Multiprocessing
############################### Multiprocessing: ###########################################

# - A new process is started independent from the first process
# - Starting a process is slower than starting a thread
# - Process switch needs interaction with os - context switch
# - Memory is not shared between processes
# - Mutexes not necessary (unless threading in the new process)
# - One GIL (Global Interpreter Lock) for each process
# - Independent , blocking one process will not affect other process



from multiprocessing import Process,freeze_support
import os
import math


def calc():
    for i in range(0, 400000000):
        math.sqrt(i)

if __name__=='__main__':
    freeze_support()
    processes = []

    for i in range(os.cpu_count()):
        print('registering process %d' % i)
        processes.append(Process(target=calc))

    for pro in processes:
        pro.start()

    for pr in processes:
        pr.join()


############################### Threading: #################################################

# - A new thread is spawned within the existing process
# - Starting a thread is faster than starting a process
# - Thread switch is faster ,no need to interact with os ,as it interacts with in the processor
# - Memory is shared between all threads
# - Mutexes often necessary to control access to shared data
# - One GIL (Global Interpreter Lock) for all threads
# - Interdependent , blocking one thread will block other threads also - due to shred memory

lst=[None,None,None,None,None]

def f1():
    with open(r'C:\Users\act9kor\Desktop\temp_multi\function1.txt','w') as file:
        for each in reversed(lst[1:]):
            file.write(each+'\n')

def f2():
    content_needed=''
    with open(r'C:\Users\act9kor\Desktop\temp_multi\function2.txt') as file:
        for line in file.readlines():
            time.sleep(2)
            content_needed=line+f'time stamp ={time.time()}'
            break
    lst[1]=content_needed

def f3():
    content_needed=''
    with open(r'C:\Users\act9kor\Desktop\temp_multi\function 3.txt') as file:
        for line in file.readlines():
            time.sleep(3)
            content_needed=line+f'time stamp ={time.time()}'
            break
    lst[2] = content_needed

def f4():
    content_needed=''
    with open(r'C:\Users\act9kor\Desktop\temp_multi\function 4.txt') as file:
        for line in file.readlines():
            time.sleep(4)
            content_needed=line+f'time stamp ={time.time()}'
            break
    lst[3] = content_needed



def f5():
    content_needed=''
    with open(r'C:\Users\act9kor\Desktop\temp_multi\function 5.txt') as file:
        for line in file.readlines():
            time.sleep(5)
            content_needed=line+f'time stamp ={time.time()}'
            break
    lst[4] = content_needed

# - locks

account_balance=0

def deposite(times):
    global account_balance
    for i in range(times):
        account_balance+=1111


def withdraw(times):
    global account_balance
    for i in range(times):
        account_balance-=1111


def deposite_lock(times,lock):
    global account_balance
    for i in range(times):
        lock.acquire()
        account_balance+=1111
        lock.release()

def withdraw_lock(times,lock):
    global account_balance
    for i in range(times):
        lock.acquire()
        account_balance-=1111
        lock.release()


def multiple_data():
    import threading
    import time
    t1 = threading.Thread(target=f1,args='')        # write file
    t2 = threading.Thread(target=f2, args='')       # reading file
    t3 = threading.Thread(target=f3, args='')       # reading file
    t4 = threading.Thread(target=f4, args='')       # reading file
    t5 = threading.Thread(target=f5, args='')       # reading file

    for each_thread in [t1,t2,t3,t4,t5]:
        if each_thread != t1:
            each_thread.start()
    for each_thread in [t1,t2,t3,t4,t5]:
        if each_thread != t1:
            each_thread.join()
    t1.start()
    t1.join()

def bank():
    num = 100000
    time1 = time.time()
    withdraw(num)
    deposite(num)
    print('without threading -->', account_balance)
    print('without threading time-->', time.time() - time1)


def bank_without_lock():
    import threading
    import time
    num = 100000

    # -with threading

    thread_time = time.time()
    t1=threading.Thread(target=deposite,args=(num,))
    t2=threading.Thread(target=withdraw,args=(num,))


    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print('with threading and without lock -->', account_balance)
    print('without threading time-->', time.time() - thread_time)

def bank_with_lock():
    import threading
    import time
    num = 100000

    # -with threading
    # lock
    lok = threading.Lock()

    thread_time = time.time()

    # -with locks
    t1 = threading.Thread(target=deposite_lock, args=(num, lok))
    t2 = threading.Thread(target=withdraw_lock, args=(num, lok))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print('with threading and with lock -->', account_balance)
    print('without threading time -->', time.time() - thread_time)

# if __name__=='__main__':
#     # - multithreading files read and write
#     multiple_data()

# if __name__ == '__main__':
    # bank()
    # account_balance=0
    # bank_without_lock()
    # account_balance = 0
    # bank_with_lock()
    # account_balance = 0
