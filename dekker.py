# Author: Alberto Caballero
# Description: Dekker Algorithm implemented in Python

# import multiprocessing library
import multiprocessing as mp

# array of threads wanting to execute
threads = [False, False]

# priority thread
flag = 1

# completed flag
completed = False

# thread number one
def threadOne():
    # while the tasks are not completed
    while not completed:
        threads[0] = True
        print('Thread One', threads[0])

        # while the second thread wants to execute
        while threads[1] == True:
            # and priority is on thread
            if flag == 2:
                threads[0] = False

                # execute until other priority appears
                while flag == 2:
                    threads[0] == True

        # change priority
        flag = 2
        # set first thread to not wanting to execute
        threads[0] = False



# thread number two
def threadTwo():
    # while tasks are not completed
    while not completed:
        threads[1] = True
        print('Thread Two', threads[1])
        
        # check if thread one is executing
        while threads[0] == True:
            # and priority is on thread
            if flag == 1:
                threads[1] = False

                # execute until other priority apperas
                while flag == 1:
                    threads[1] = True

        # change priority
        flag = 1
        # ser second thread to not wanting to execute
        threads[1] = False


# multy processing stuff

# check how many cores can be used
pool = mp.Pool(mp.cpu_count())

# execute and save results of execution
results = [pool.apply(threadOne(), threadTwo())]

# close all executions
pool.close()

# show results
print(results)

