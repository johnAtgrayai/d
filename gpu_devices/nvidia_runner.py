from gpu_devices.nvidia_tools import Nvidia
import pandas as pd


class NvidiaRunner:
    """Class usedd to run NVIDIA metrics"""

    def __init__(self, ecc, temp, memory, ):
        """Constructor"""
        self.nvidia = Nvidia()
        self.handles = self.nvidia.get_handles()
        self.ecc = ecc 
        self.temp = temp
        self.memory = memory




    def collect_diagnostic_data(self):
        """Method used to collect diagnostic data"""
        for handle_n in self.handles:
            clock_info = self.nvidia.get_clock_info(handle_n)
            temperature = self.nvidia.get_temperature(handle_n)
            ecc_counts = self.nvidia.get_gpu_ecc_errors(handle_n)
            total_memory, free_memory, used_memory = self.nvidia.get_memory_info(handle_n)

        




if __name__  == """__main__""":
    try:
        while True:
            gpu_diagnostics = NvidiaRunner()
            gpu_diagnostics.collect_diagnostic_data()
    except KeyboardInterrupt:
        print("Monitoring GPU!")