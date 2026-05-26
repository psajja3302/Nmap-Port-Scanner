'''Used Kali Linux for this Code!!!'''

import nmap
import re
import threading

NUM_THREADS = 400

def scanner(ip, port, lock):
    try:
        nm = nmap.PortScanner()
        with lock:
            result = nm.scan(ip, str(port))
            port_status = (result['scan'][ip]['tcp'][port]['state'])
            print(f"Port {port} is {port_status}")
    except:
        with lock:
            print(f"Cannot scan port {port}")


def main():
    #Validity Check of IP address using regex
    validip = re.compile('^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$')
    while True:
        ipinput = input('\nEnter the ip address you would like to scan (Ex: 192.168.23.23): ').strip()
        if validip.search(ipinput):
            break
        else:
            print('\nEnter a valid ip address.')

    #Validity Check of port ranges (0-65535)
    while True:
        portinput = input('\nEnter the range of ports you would like to scan (Ex: 23-53): ').strip()
        parts = portinput.split('-')
        min, max = parts[0], parts[1]
        if (len(parts) == 2
            and ((min.isdigit() and (0 <= int(min) <= 65535)))
            and (max.isdigit() and (0 <= int(max) <= 65535))
            and int(min) <= int(max)):
            min, max = int(parts[0]), int(parts[1])
            break
        print('Invalid range. Use format 0-65535, min must be <= max.')

    print(f'\nScanning ports {min} – {max} on {ipinput}...\n')

    #Threading Process using Scanner 
    lock = threading.Lock()
    t_list = []
    ports = []

    for port in range(min, max + 1):
        t = threading.Thread(target=scanner, args=(ipinput, port, lock))
        t_list.append(t)
        t.start()
        if len(t_list) >= NUM_THREADS:
            for t in t_list:
                t.join()
            t_list.clear()
    for t in t_list:
        t.join()


if __name__ == "__main__":
    main()
