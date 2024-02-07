# Standard Imports
import os

# Third Party Imports
import pandas as pd

# Local Imports
from gpu_devices.gpu_wrappers.nvidia_gpu import Nvidia


class GPUDiagnostics:
    """Class used to run GPU diagnostic cases"""

    def __init__(self, target_temperature = 25.0):
        """Constructor"""
        self.nvidia = Nvidia()
        self.handles = self.nvidia.get_handles()
        self.target_temperature = target_temperature
        
    
   

    def high_gpu_temperature_alert(self, handle):
        """Method used to handle GPU high temeprature alert"""
        temperature = list()
        utilization = list()
        power_consumption = list()
        i = 0 
        temperature.append(self.nvidia.get_temperature(handle))
        while temperature[i] > self.target_temperature:
                temperature.append(self.nvidia.get_temperature(handle))
                utilization.append(self.nvidia.get_utilization_rates(handle))
                power_consumption.append(self.nvidia.get_power_info(handle))
                i += 0

        return temperature, utilization, power_consumption
    
   

                

    

    def collect_metrics_for_video_memory(self):
        """Method used to handle GPU high video memory alert"""
        for handle in self.handles 

