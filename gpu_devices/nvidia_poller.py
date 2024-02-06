from gpu_devices.nvidia_gpu import Nvidia
import threading
import concurrent.futures
import logging
import time
import pandas as pd

format = "%(asctime)s: %(message)s"
logger = logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

class NvidiaPoller:
    """Class usedd to run NVIDIA metrics"""

    def __init__(self, polling_interval: int, collection_time: int, gpu_count: int):
        """Constructor"""
        self.nvidia = Nvidia()
        self.polling_interval = polling_interval
        self.collection_time = collection_time
        self.gpu_count = gpu_count


    def create_gpu_polling_thread(self):
        """Method used to consumer thread"""
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            executor.map(self.countdown_timer, range(self.gpu_count))



    def collect_gpu_diagnostic_data(self):
        """Method used to collect diagnostic data"""
        for handle_n in self.handles:
            clock_info = self.nvidia.get_clock_info(handle_n)
            temperature = self.nvidia.get_temperature(handle_n)
            ecc_counts = self.nvidia.get_gpu_ecc_errors(handle_n)
            total_memory, free_memory, used_memory = self.nvidia.get_memory_info(handle_n)
            time.sleep(self.polling_interval)
    
    def countdown_timer(self):
        """Method used to count down time for how long GPU diagnostics are supposed to be collected"""
        while self.collection_time > 0:
            self.collection_time -= 1
            self.collect_gpu_diagnostic_data()



        




if __name__  == """__main__""":
    try:
        while True:
            gpu_diagnostics = NvidiaPoller()
            gpu_diagnostics.collect_diagnostic_data()
    except KeyboardInterrupt:
        print("Monitoring GPU!")