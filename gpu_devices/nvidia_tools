from pynvml import *
from pynvml.smi import *
import pynvml
import subprocess

class Nvidia():
    """Class containing methods that will run GPU diagnostics on NVIDIA hardware"""

    def __init__(self):
        """Contstructor"""
        try:
            # Initialize NVML
            pynvml.nvmlInit()
            self.nvidia_instance = nvidia_smi.getInstance()
        except pynvml.NVMLError as error:
            print(f'{error}')
        finally:
            pynvml.nvmlShutdown()


    def query_memory(self):
        """Method used to query nvidia device memory"""
        self.nvidia_instance.DeviceQuery('memory.free, memory.total')

    def get_driver_version():
        """Getter method used to get driver version"""
        driver_version = nvmlSystemGetDriverVersion()
        return f'Device Driver Firmware: {driver_version}'

    def get_device_count(self):
        """Getter method used to get GPU device count from system"""
        device_count = nvmlDeviceGetCount()

        return f'Rack contains {device_count} GPUs'
    
    def get_utilization_rates(self, handle):
        """Method used to get GPU utilization"""
        utilization = self.nvidia_instance.nvmlDeviceGetUtilizationRates(handle)

        return utilization

    def get_gpu_ecc_errors(self, handle):
        """Method used to get ECC errors from GPU"""
        ecc_mode = pynvml.nvmlDeviceGetEccMode(handle)
        if ecc_mode == pynvml.NVML_FEATURE_ENABLED:
            ecc_counts = pynvml.nvmlDeviceGetDetailedEccErrors(handle)
        else:
            print("ECC not supported on this device")
        return ecc_counts

    def get_handles(self):
        """Method used to return handle"""
        device_count = self.get_device_count()
        handles= list()
        for i in range(device_count):
                handles.append(self.nvidia_instance.nvmlUnitGetHandleByIndex(i))
        return handles
    
    def close_event(self):
        """Method used to shutdown NVML"""
        pynvml.nvmlShutdown()
            