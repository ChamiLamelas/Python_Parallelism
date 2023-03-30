import threading
import sys


def work():
    s = 0
    for i in range(100_000_000):
        s += i


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 work_demo.py NTHREADS")
        sys.exit(1)

    nthreads = int(sys.argv[1])
    threads = list()
    for _ in range(nthreads):
        newthread = threading.Thread(target=work)
        newthread.start()
        threads.append(newthread)
    print(f"spawned {nthreads} threads -- waiting for them to finish")
    for t in threads:
        t.join()
    print("main thread done")


if __name__ == '__main__':
    main()
