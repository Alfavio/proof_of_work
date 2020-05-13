from hashlib import sha256
from multiprocessing import Process
from opt import DEFAULT_DIFFICULT
from random import randint
from sys import maxsize


# Class of process to handle proof of work.
class ProofOfWork(Process):
    encoding = 'utf-8'

    # Constructor
    def __init__(self, queue, completed, difficulty = DEFAULT_DIFFICULT):
        super(ProofOfWork, self).__init__()
        self.__queue = queue                # queue to handle the state of the process
        self.__completed = completed        # event for handle completion of work
        self.__target = '0' * difficulty    # count of zeroes at the start of the wanted hash
        self.__hashes_checked = 1           # count of checked hashes

    # Start of process
    def run(self):
        # Get hash
        hash_result = self.__getHash(self.__getNonce())
        
        # Repeatedly find a hash that matches our rules. In this case, the count of zeroes at the start of the hash.
        while not hash_result[0].startswith(self.__target):
            # Check if some process found hash
            if self.__completed.is_set():
                # Save count of checked hashes to state
                self.__queue.put(self.__hashes_checked)
                return
            # Get hash
            hash_result = self.__getHash(self.__getNonce())
            # Add counter
            self.__hashes_checked = self.__hashes_checked + 1

        # Notify processes that hash was found.
        self.__completed.set()
        # Save found hash, nonce, and count of checked hashes to state
        self.__queue.put(dict(hash=hash_result[0], nonce=hash_result[1], hashes_checked=self.__hashes_checked))
        return

    # Function to get hash
    def __getHash(self, nonce):
        return sha256(('%d' % (nonce)).encode(self.encoding)).hexdigest(), nonce

    # Get nonce. Random integer in this case.
    def __getNonce(self):
        return randint(0, maxsize)