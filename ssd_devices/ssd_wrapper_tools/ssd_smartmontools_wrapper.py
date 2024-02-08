import json
import os
import platform
import subprocess

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
        cmd_output = subprocess.run(f"smartctl -H /dev/sda")
        output = cmd_output.stdout
       
        #storage_device_overall_health = data[5]


        #return storage_device_overall_health
    
    def get_all_wear_leveling(self):
        """Method used to get all wear leveling"""
        cmd_output = subprocess.run(f"smartctl -a /dev/sda", capture_output=True)
        ssd_smart_data = cmd_output.stdout.decode("utf-8")
        output = ssd_smart_data.split("\r\n")
        
        print(output)
        return ssd_smart_data

    
    def get_all_reallocation_events(self):
        """Method used to gather all reallocation events on SSD"""


if __name__ == """__main__""":

    smartctl = SmartMonTools()
    smartctl.get_all_wear_leveling()
   