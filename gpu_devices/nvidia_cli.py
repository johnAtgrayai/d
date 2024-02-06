import argparse




class NvidiaCLI:
    """Class used to interface with NVIDIA tools via command line interface"""


    def __init__(self, ecc, temp, memory):
        """Constructor"""
        self.ecc = ecc 
        self.temp = temp
        self.memory = memory

    


if __name__ == """__main__""":
    args = argparse.ArgumentParser()
    args.add_argument("-e", "--ecc", type=str, help="Get ECC diagnostics from GPU")
    args.add_argument("-t", "--temp", type=str, help="Get temperature from GPU")
    args.add_argument("-w", "--power", type=str, help="Get power consumption from GPU")
    args.add_argument("-p", "--pci", type=str, help="Get pci information from GPU")
    parsed_args = args.parse_args()
    ecc_info = parsed_args.ecc
    