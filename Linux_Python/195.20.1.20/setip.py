import os
os.system('sudo ifconfig eth0 down')
os.system('sudo ifconfig eth0 195.20.1.31')
os.system('sudo ifconfig eth0 up')
# os.system('sudo ping 195.20.1.20')
