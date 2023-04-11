"""
Produces load on all available CPU cores.
Requires system environment var STRESS_MINS to be set.
"""

from multiprocessing import Pool
from multiprocessing import cpu_count
import time
import os

def f(x):
    set_time = 60
    timeout = time.time() + 60*float(set_time)  # X minutes from now
    while True:
        if time.time() > timeout:
            break
        x*x

if __name__ == '__main__':
    processes = cpu_count()
    print ('utilizing %d cores\n' % processes)
    pool = Pool(processes)
    pool.map(f, range(processes))