

# Local Imports
from gpu_devices.nvidia_gpu import Nvidia


class GPUDiagnostics:
    """Class used to run GPU diagnostic cases"""

    def __init__(self):
        """Constructor"""
        self.nvidia = Nvidia()
        self.handles = self.nvidia.get_handles()

    def high_gpu_temperature_alert(self):
        """Method used to handle GPU high temeprature alert"""
        for handle in self.handles:
            temperature = self.nvidia.get_temperature(handle)
            while temperature > target_temperature:
                temperature = self.nvidia.get_temperature(handle)
                utilization = self.nvidia.get_utilization_rates(handle)
                power_consumption = self.nvidia.get_power_info(handle)
                // function to reduce workloads

    