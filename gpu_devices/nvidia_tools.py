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
            self.pynvml = pynvml()
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
        utilization = self.nvidia_instance.nvmDeviceGetUtilizationRates(handle)
        gpu_utilization = utilization.gpu
        memory_utilization = utilization.memory

        return gpu_utilization, memory_utilization

    def get_power_info(self, handle):
        """Method used to get power info from GPU"""
        power_info = pynvml.nvmlDeviceGetPowerUsage(handle)
        
        return power_info / 1000.0

    def get_clock_info(self, handle):
        """Method used to get clock info"""
        clock_info = pynvml.nvmlDeviceGetClockInfo(handle, pynvml.NVML_CLOCK_GRAPHICS)

        return clock_info / 1000.0

    
    def get_fan_speed(self, handle):
        """Method used to get fan speed of GPU"""
        try:
            fan_speed = pynvml.nvmlDeviceGetFanSpeed(handle)
        except pynvml.NVMLError as error:
            print(f"Error getting fan speed: {error}")
            raise error
        

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

    def get_temperature(self, handle):
        """Method used to get temeprature from GPU"""
        temperature = pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)

        return temperature 

    def get_memory_info(self, handle):
        """Method used to get memory info of GPU"""
        memory_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
        total_memory = memory_info.total / (1024 ** 2)
        free_memory = memory_info.free / (1024 ** 2)
        used_memory = memory_info.used / (1024 ** 2)

        return total_memory, free_memory, used_memory
    
    def get_pci_information(self, handle):
        """Method used to return PCI information """
        pci_info = pynvml.nvmlDeviceGetPciInfo_v3(handle)
        bus  = pci_info.bus
        device_id = pci_info.device
        domain = pci_info.domain
        bus_type = pci_info.bustType
        bus_id = pci_info.busId

        return pci_info, bus, device_id, domain, bus_type, bus_id


    def get_clock_faults(self, handle):
        """Method used to get clock faults NVIDIA GPU """
        
        clock_faults = pynvml.nvmlDeviceGetCurrentClocksThrottleReasons(handle)
        
        return clock_faults
    
    def close_event(self):
        """Method used to shutdown NVML"""
        pynvml.nvmlShutdown()
            
