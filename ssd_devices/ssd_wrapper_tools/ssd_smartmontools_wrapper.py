import json
import os
import platform
import subprocess
import re

# Local Imports


class SmartMonTools:
    """Class used automate running SmartMonTools"""


    def __init__(self, path_to_json=None):
        """Constructor"""
        self.path_to_json = path_to_json
        self.config = None
        # Read JSON File
        # with open(self.path_to_json, mode="r", encoding="utf-8") as json_config:
        #      self.config = json.load(json_config)
        # self.storage_device = self.config[SSD][SSD_DEVICE]
        
    def get_overall_smart_test_status(self):
        """Method used to run SMART test of storage device"""
        smart_test_regex_pass= r"\bpassed\b"
        smart_test_regex_fail = r"\bfailed\b"
        cmd_output = subprocess.run(f"smartctl -H /dev/sda", capture_output=True)
        output = cmd_output.stdout.decode("utf-8")
        result_passed_match = re.search(pattern=smart_test_regex_pass, string=output, flags=re.IGNORECASE)
        result_failed_match = re.search(pattern=smart_test_regex_fail, string=output, flags=re.IGNORECASE)
        if result_passed_match:
            smart_test_result = result_passed_match.group()
        elif result_failed_match:
            smart_test_result = result_failed_match.group()
        else:
            smart_test_result = "Could not determine outcome of test!"

        return smart_test_result
        
    
    def get_ssd_serial_number(self):
        """Method used to get all wear leveling"""
        serial_number_regex = r"\d{2}\w{8}\d{2}" 
        cmd_output = subprocess.run(f"smartctl -a /dev/sda", capture_output=True)
        ssd_diagnostic_telemetry = cmd_output.stdout.decode("utf-8")
        match = re.search(pattern=serial_number_regex, string=ssd_diagnostic_telemetry)
        serial_number = match.group()

        return serial_number 

    def run_smart_test(self):
        """Method used to run SMART test of desired duration"""
        cmd_output = subprocess.run(f"smartctl -t long /dev/sda", capture_output=True)
        smart_test_telemetry = cmd_output.stdout.decode("utf-8")
        print()


if __name__ == """__main__""":

    smartctl = SmartMonTools()
    serial_number = smartctl.get_overall_smart_test_status()
    print(serial_number)
   