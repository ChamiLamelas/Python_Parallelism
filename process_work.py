import multiprocessing
import sys


def work():
    s = 0
    for i in range(100_000_000):
        s += i


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 work_demo.py NPROCESSES")
        sys.exit(1)

    nprocesses = int(sys.argv[1])
    processes = list()
    for _ in range(nprocesses):
        newprocess = multiprocessing.Process(target=work)
        newprocess.start()
        processes.append(newprocess)
    print(
        f"spawned {nprocesses} child processes -- waiting for them to finish")
    for p in processes:
        p.join()
    print("main process done")


if __name__ == '__main__':
    main()
