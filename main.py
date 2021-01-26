import sys
import time
import subprocess
from halo import Halo

input("Press enter to change you ip address")
spinner = Halo(text='Changing IP.. ', spinner='dots')
spinner.start()
subprocess.call('start /wait python release.py', shell=True)
time.sleep(2)
subprocess.call('start /wait python renew.py', shell=True)
time.sleep(5)
spinner.stop()
print("IP Successfully Renewed & Released.")
time.sleep(1)
input("Press enter to exit.")
