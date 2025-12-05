import os
# TCP Test 
 
# os.system('sudo iperf3 -c 195.20.1.20 -n 800000M -i 30')

os.system('sudo iperf3 -c 195.20.1.20 -n 1020M -i 30') 

# As a client
# os.system('sudo iperf3 -s') # As client


# UDP Test
# os.system('sudo iperf3 -c 195.20.1.20 -u -b 8000000M -l 8k -n 1000M')
# os.system('sudo iperf3 -c 195.20.1.20 -u -b 8000000M')
# iperf3 -c 195.20.1.20 -u
# iperf3 -c 195.20.1.20 -u -b 1000M
# iperf3 -c 195.20.1.20 -u -b 1000M
# iperf3 -c 195.20.1.20 -u -b 1024M
# iperf3 -c 195.20.1.20 -u -b 1000M -l 2k
# iperf3 -c 195.20.1.20 -u -b 1000M -l 8k
# iperf3 -c 195.20.1.20 -u -b 1000M -l 8k  -n 8000000M
# iperf3 -c 195.20.1.20 -u -b 1000M -l 8k  -n 8000000M  -i 30
# iperf3 -c 195.20.1.20 -u -b 1000M -l 8k  -n 1000M 
