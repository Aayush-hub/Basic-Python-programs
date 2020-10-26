import subprocess

def ping(ip):
    try:
        if "time=" in str(subprocess.check_output(f'ping {ip}')):
            return 0
        else:
            return 1
    except KeyboardInterrupt:
        quit()
    except:
        return 1

def ip_maker(ip):
    ip_list = []
    while ip.endswith(".") is False:
        ip = ip[:-1]
    for i in range (1,255):
        address = ip + str(i)
        ip_list.append(address)
    return ip_list
    
def scanner(ip):
    up_list = []
    for address in ip_maker(ip):
        if ping(address) == 0:
            print(f"{address} is up!")
            up_list.append(address)
    #return up_list
    
    

def main():
    ip_addr = input("Please enter your router's local IP address (ex. 192.168.1.1): ")
    scanner(ip_addr)

if __name__ == '__main__':
    main()
