# Standard Imports
import sys

# Local Imports
from gpu_devices.nvidia_gpu_diagnostics import NvidiaDiagnostics

# Third Party Imports
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QWidget, \
    QTabWidget, QApplication, QGridLayout
from PyQt5.QtCore import Qt, QRunnable, QThreadPool


class GPUDiagnosticsThread(QRunnable):
    """Thread class used to run GPU diagnostics"""
    
    def __init__(self):
        """Constructor"""
        super().__init__()
       
    
    def run(self):
        gpu_diag_routine = NvidiaDiagnostics()
        gpu_diag_routine.gpu_diagnostics()

class FrontPanel(QWidget):
    """Class used for front panel"""

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.setWindowTitle("Gray AI Diagnostics Tool")
        self.setGeometry(500, 500, 500, 500)

        # Main Layout
        main_layout = QVBoxLayout()

        # Tab Layout
        self.gpu_diagnostics_tab = QWidget()
        self.ssd_diagnostics_tab = QWidget()
        self.cpu_diagnostics_tab = QWidget()
        self.dimm_diagnostics_tab = QWidget()
        self.diagnostics_config_tab = QWidget()
        self.tabs = QTabWidget()
        self.tabs.addTab(self.gpu_diagnostics_tab, "GPU Diagnostics Tab")
        self.tabs.addTab(self.ssd_diagnostics_tab, "SSD Diagnostics Tab")
        self.tabs.addTab(self.cpu_diagnostics_tab,  "CPU Diagnostics Tab")
        self.tabs.addTab(self.dimm_diagnostics_tab, "DIMM Diagnostics Tab")

        # GPU Diagnostics Tab Layout
        gpu_diagnostics_tab_layout = QGridLayout()
        self.gpu_diagnostics = QPushButton("GPU Diagnostics")
        self.gpu_load_utilization = QPushButton("GPU Load Utilization")
        self.gpu_frame_buffer_usage = QPushButton("Frame Buffer Usage")
        gpu_diagnostics_tab_layout.addWidget(self.gpu_diagnostics, 0, 0)
        gpu_diagnostics_tab_layout.addWidget(self.gpu_load_utilization, 0 , 1)
        gpu_diagnostics_tab_layout.addWidget(self.gpu_frame_buffer_usage, 1, 0)
        self.gpu_diagnostics.clicked.connect(self.on_run_gpu_diagnostics)

        self.gpu_diagnostics_tab.setLayout(gpu_diagnostics_tab_layout)

        
        main_layout.addWidget(self.tabs)
        self.setLayout(main_layout)

        self.thread_pool = QThreadPool.globalInstance()

    def on_run_gpu_diagnostics(self):
        """Event handler for running GPU Diagnostics"""
        gpu_diagnostics_thread = GPUDiagnosticsThread()
        self.thread_pool.start(gpu_diagnostics_thread)

app = QApplication(sys.argv)
window = FrontPanel()
window.show()
app.exec()
sys.exit(app.exec_())

        
