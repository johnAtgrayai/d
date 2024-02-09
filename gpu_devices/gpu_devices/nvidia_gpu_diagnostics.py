# Local Imports
from gpu_wrappers.nvidia_gpu import Nvidia


class NvidiaDiagnostics:
    """Class used for running NVIDIA Diagnostic parameters"""

    def __init__(self):
        """Constructor"""
        self.nvidia_wrapper = Nvidia()
        self.handles = Nvidia.get_handles()

    def gpu_diagnostics(self):
        """Method used to run diagnostics on GPU"""
        for handle_n in self.handles:
            clock_info = self.nvidia.get_clock_info(handle_n)
            temperature = self.nvidia.get_temperature(handle_n)
            ecc_counts = self.nvidia.get_gpu_ecc_errors(handle_n)
            total_memory, free_memory, used_memory = self.nvidia.get_gpu_video_memory_info(handle_n)
            
        return handle_n, clock_info, temperature, ecc_counts, total_memory, free_memory, used_memory