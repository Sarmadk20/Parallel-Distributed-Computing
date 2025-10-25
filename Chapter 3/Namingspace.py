import multiprocessing
import time
import os

def worker(shared_data, name):
    for _ in range(5):
        shared_data.number += 3
        print(f"{name} (PID {os.getpid()}) updated number to {shared_data.number}")
        time.sleep(0.3)

if __name__ == "__main__":
    manager = multiprocessing.Manager()
    shared_data = manager.Namespace()
    shared_data.number = 0

    p1 = multiprocessing.Process(target=worker, args=(shared_data, "Process A"))
    p2 = multiprocessing.Process(target=worker, args=(shared_data, "Process B"))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f"\nFinal value in namespace: {shared_data.number}")
