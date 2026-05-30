'''Used Kali Linux for this Code!!!'''

import nmap
import re
import threading

NUM_THREADS = 400

def scanner(ip, port, ports, display):
    try:
        nm = nmap.PortScanner()
        result = nm.scan(ip, str(port), arguments='-sV') # -sV detection. Arguments can be changed if a larger breadth of commands is preferred.
        tcp_data = result['scan'][ip]['tcp'][port]
        state = tcp_data.get('state', 'unknown')

        if display == '1' and state != 'open':
            return

        port_info = {
            'port': port,
            'state': state,
            'service': tcp_data.get('name', '') or 'unassigned',
            'product': tcp_data.get('product', ''),
            'version': tcp_data.get('version', ''),
            'protocol': tcp_data.get('protocol', 'tcp') if 'protocol' in tcp_data else 'tcp',
        }
        ports[port] = port_info
    except:
        pass


def main():
    #Validity Check of IP address using regex
    validip = re.compile(r'^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$')
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

    #User picks if they would like all ports displayed or open ports only.
    while True:
        print('\nWhat ports would you like to display?')
        print('1 - Open ports only')
        print('2 - All ports')
        display = input('Enter choice (1/2): ').strip()
        if display in ('1', '2'):
            break
        print('Invalid choice. Enter 1 or 2.')

    print(f'\nScanning ports {min} – {max} on {ipinput}...\n')

    #Threading Process using Scanner method
    t_list = []
    ports = {}

    for port in range(min, max + 1):
        t = threading.Thread(target=scanner, args=(ipinput, port, ports, display))
        t_list.append(t)
        t.start()
        if len(t_list) >= NUM_THREADS:
            for t in t_list:
                t.join()
            t_list.clear()
    for t in t_list:
        t.join()

    #Formatted Output, very similar to running the nmap command
    print(f"\n{'PORT':<10} {'STATE':<12} {'PROTOCOL':<10} {'SERVICE':<15} {'PRODUCT & VERSION'}")
    print("-" * 70)
    for port in sorted(ports.keys()):
        info = ports[port]
        product_version = f"{info['product']} {info['version']}".strip()
        print(f"{info['port']:<10} {info['state']:<12} {info['protocol']:<10} {info['service']:<15} {product_version or 'N/A'}")

    open_count = sum(1 for info in ports.values() if info['state'] == 'open')
    closed_count = sum(1 for info in ports.values() if info['state'] != 'open')

    if display == '1':
        print(f"\nScan complete. {open_count} open port(s) found.")
    else:
        print(f"\nScan complete. {open_count} open port(s) found. {closed_count} closed/filtered port(s) found.")


if __name__ == "__main__":
    main()