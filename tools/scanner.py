import socket
import termcolor

def scan(targets,ports):
    print("\n" + "starting scan for" + str(target))
    for port in range(1,ports):
        scan_port(targets, port)

def scan_port(address,port):
    try:
        sock = socket.socket()
        sock.connect((address,port))
        print("port open" + str(port))
        sock.close()
    except:
        pass
         
targets= input("enter targets to scan(split them by , ==> )")
ports=int(input("enter how many port you want to scan ==> "))

if "," in targets:
    print(termcolor.colored("scanning multiple targets :<} "),"blue")
    for ipaddr in targets.split(","):
        scan(ipaddr.strip(" ",ports))
    else:
        scan(targets,ports)
                             