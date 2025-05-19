# Simulate Stopwatch Program
# a. Desc -> Write a Stopwatch Program for measuring the time that elapses between
# the start and end clicks
# b. I/P -> Start the Stopwatch and End the Stopwatch
# c. Logic -> Measure the elapsed time between start and end
# d. O/P -> Print the elapsed time.

import time

def calculate_time(start_time, end_time):
    result = end_time - start_time
    print("Time elapsed between start and end click is:", result, "seconds")

input("Press Enter to start the stopwatch")
start_time = time.time()

input("Press Enter to stp the stopwatch")
end_time = time.time()

calculate_time(start_time, end_time)
