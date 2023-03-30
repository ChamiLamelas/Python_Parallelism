import psutil
import time
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 psutil_demo.py NSECS")
        sys.exit(1)
    
    logical_cpus = psutil.cpu_count()
    physical_cpus = psutil.cpu_count(logical=False)
    threads_per_cpus = logical_cpus // physical_cpus
    print(
        f"CPU HW Stats\n\t# Logical = {logical_cpus}\n\t# Physical = {physical_cpus}\n\t# Threads/CPU = {threads_per_cpus}")

    nsecs = int(sys.argv[1])
    for i in range(nsecs):
        if i > 0:
            time.sleep(1)
        cpu = list(enumerate(psutil.cpu_percent(percpu=True)))
        nonzero_cpu = sorted([e for e in cpu if e[1] > 0],
                            key=lambda e: e[1], reverse=True)
        print("CPU Utilization (core: utilization): " +
            " ".join(f"{core}: {util}%" for (core, util) in nonzero_cpu))
        ram = psutil.virtual_memory().percent
        print(f"RAM: {ram}%")

if __name__ == '__main__':
    main()