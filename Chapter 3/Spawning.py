import multiprocessing
import time
import random
import os

def download_file(file_id):
    print(f"[Process {file_id}] PID {os.getpid()} started downloading...")
    download_time = random.uniform(1.5, 4.0)
    time.sleep(download_time)
    print(f"[Process {file_id}] Completed in {download_time:.2f} seconds.\n")

if __name__ == "__main__":
    processes = []

    print("Starting multiple file downloads...\n")

    for file_id in range(1, 6):
        process = multiprocessing.Process(target=download_file, args=(file_id,))
        processes.append(process)
        process.start()

    time.sleep(1)
    print("Checking running downloads...\n")
    for file_id, process in enumerate(processes, start=1):
        print(f"Process {file_id} alive:", process.is_alive())

    for process in processes:
        process.join()

    print("\nAll downloads completed successfully!")
