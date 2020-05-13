from multiprocessing import Event, Process, Queue
from opt import optParse
from pow import ProofOfWork
from sys import argv
from time import time

def main(argv):
    # Parse arguments
    arguments = optParse(argv)
    processes_count = arguments["processes_count"]
    difficulty = arguments["difficulty"]

    print("Running on %d processes with %d difficulty" % (processes_count, difficulty))

    completed = Event()             # Create a event for handle completion of work
    processes = list()              # Create a list of processes
    queue = Queue(processes_count)  # Create a queue to handle the state of processes

    # Create processes
    for _ in range(processes_count):
        process = ProofOfWork(queue, completed, difficulty)
        processes.append(process)
    
    # Start all created processes
    start_time = time()
    for process in processes:
        process.start()

    # Wait until proof of work is done
    completed.wait()

    # Wait for all processes to be done
    for process in processes:
        process.join()
    elapsed_time = time() - start_time

    # Create stats
    hashes_checked = 0
    hash = "not"
    nonce = -1
    # Check the state of all processes
    while not queue.empty():
        # Get state
        value = queue.get()
        # Process found hash
        if isinstance(value, dict):
            # Add hashes checked
            hashes_checked = hashes_checked + value["hashes_checked"]
            # Save found hash
            hash = value["hash"]
            # Save found nonce
            nonce = value["nonce"]
        # Process not found hash
        else:
            # Add hashes checked
            hashes_checked = hashes_checked + value

    # Print stats
    print(  "Hash %s found.\n"                          % hash +
            "Success with nonce %d.\n"                  % nonce +
            "%.0f minutes and %.0f seconds elapsed.\n"  % (elapsed_time / 60, elapsed_time % 60) +
            "Your hashing power is %.2f kH/s."          % float(hashes_checked / elapsed_time / 1000))

if __name__ == "__main__":
    main(argv)
