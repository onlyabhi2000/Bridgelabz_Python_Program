# What is multi threading How can you achieve multi-threading in Python?

# Multithreading in Python is a technique that enables a program to execute multiple threads (smaller units of a process) concurrently within a single process. 
# It provides an approach to perform multiple tasks that appear to run simultaneously, though typically not in true parallel on multi-core systems due to Python's Global Interpreter Lock

# Concurrency vs. Parallelism:
# Concurrency means tasks progress in overlapping periods, often by rapidly switching between threads (context switching) on a single CPU core. This is what Python's default interpreter (CPython) achieves with multithreading.
# Parallelism means tasks run at the exact same time on multiple CPU cores. Python's multiprocessing module is used for true parallelism, as each process has its own interpreter and memory space, bypassing the GIL.


# Global Interpreter Lock (GIL): The GIL is a mechanism in CPython that ensures only one thread executes Python bytecode at a time. This prevents race conditions in memory management but limits multithreading's ability to use multiple CPU cores for computationally intensive tasks. 

import threading

def print_numbers():
    for i in range(1, 6):
        print(i)

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(letter)
        

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start()
t2.start()

t1.join()
t2.join()

print("Both threads have finished")