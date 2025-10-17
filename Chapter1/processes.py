from code import do_something
import time
import multiprocessing
import threading

if __name__ == "__main__":
    size = 10000000  # workload size
    counts = [5, 10, 15]  # process/thread counts to test

    print("\n=== Multiprocessing Test ===")
    for procs in counts:
        jobs = []
        start_time = time.time()

        # Create and start processes
        for i in range(procs):
            out_list = []
            process = multiprocessing.Process(target=do_something, args=(size, out_list))
            jobs.append(process)

        for p in jobs:
            p.start()

        for p in jobs:
            p.join()

        end_time = time.time()
        print(f"Processes: {procs}, Time taken = {end_time - start_time:.4f} seconds")

    print("\n=== Multithreading Test ===")
    for threads in counts:
        jobs = []
        start_time = time.time()

        # Create and start threads
        for i in range(threads):
            out_list = []
            thread = threading.Thread(target=do_something, args=(size, out_list))
            jobs.append(thread)

        for t in jobs:
            t.start()

        for t in jobs:
            t.join()

        end_time = time.time()
        print(f"Threads: {threads}, Time taken = {end_time - start_time:.4f} seconds")

    print("\nAll processing complete.")
