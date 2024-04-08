import subprocess
import time

# Execute sniff.py
subprocess.run(['python', 'C:\Users\HP\Documents\FINAL YEAR PROJECT\programs\project prototype 1\module one\sniff.py'], capture_output=True)

# Wait for 25 seconds
time.sleep(25)

# Execute blockchain.py
subprocess.run(['python', 'C:\Users\HP\Documents\FINAL YEAR PROJECT\programs\project prototype 1\module one\blockchain.py'], capture_output=True)

# Wait for 25 seconds
time.sleep(25)

# Execute dnsmodule.py
subprocess.run(['python', 'C:\Users\HP\Documents\FINAL YEAR PROJECT\programs\project prototype 1\module one\DnsModule.py'], capture_output=True)
