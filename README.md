# Python Parallelism

**March 2023**

## Description 

This repository demonstrates the difference between Python threads and processes in terms of how they parallelize over CPU cores. I monitor the CPU usage of multiple independent Python threads and processes running on separate cores. By Python threads, I mean objects of the type `threading.Thread` and by processes I mean objects of the type `multiprocessing.Process`. The work done in these threads and processes is just summing the numbers `0` to `99,999,999`. CPU utilization monitored with `psutil`.

## Platform

* CPU Two 32-core AMD 7542 at 2.9GHz (128 logical CPUs)
* RAM: 512GB ECC Memory (16x 32 GB 3200MHz DDR4)
* Ubuntu 18.04 
* Python 3.10.9

## Prerequisites 

* [psutil](https://pypi.org/project/psutil/) installable via `pip`.

## Running

1. Open a shell and run `python3 monitor.py NSECS` `NSECS` being the amount of time it will monitor CPU and RAM usage, querying these metrics every 1 second. 
2. Open a shell and run `python3 thread_work.py NTHREADS`. 

Repeat with `process_work.py NPROCESSES` in step 2. 

## Results 

| Amount of Parallelism | Observation |
|---|---|
| `NTHREADS = 1` | We observe 1 logical CPU being at about 100% utilization. |
| `NTHREADS = 2` | We observe 2 logical CPUs in use being at about 50% utilization. |
| `NTHREADS = 4` | We observe 4 logical CPUs in use being at about 16-36% utilization. |
| `NPROCESSES = 1` | We observe 1 logical CPU being at about 100% utilization. |
| `NPROCESSES = 2` | We observe 2 logical CPUs being at about 100% utilization. |
| `NPROCESSES = 4` | We observe 4 logical CPUs being at about 100% utilization. |

## Analysis

It seems that Python (`threading`) threads don't actually utilize 100% of the logical CPUs they are parallelized over, while Python (`multiprocessing`) processes do.

## Contributors 

* [Chami Lamelas](https://sites.google.com/brandeis.edu/chamilamelas) - Author

