# Standard Imports
import sys


# Third Party Imports
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QWidget, \
    QTabWidget, QApplication
from PyQt5.QtCore import Qt, QRunnable, QThreadPool


class GPUDiagnosticsThread(QRunnable):
    """Thread class used to run GPU diagnostics"""


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
        self.gpu_diagnostics_tab = QHBoxLayout()
        self.gpu_load_utilization = QPushButton("GPU Load Utilization")
        self.gpu_frame_buffer_usage = QPushButton("Frame Buffer Usage")
        self.gpu_diagnostics_tab.addWidget(self.gpu_load_utilization)
        self.gpu_diagnostics_tab.addWidget(self.gpu_frame_buffer_usage)
        
        main_layout.addWidget(self.tabs)
        self.setLayout(main_layout)

        self.thread_pool = QThreadPool.globalInstance()

app = QApplication(sys.argv)
window = FrontPanel()
window.show()
app.exec()
sys.exit(app.exec_())

        
