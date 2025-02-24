import socket
import threading

def scanport(ip,port):
    try:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(5)
        result=sock.connect((ip,port))
        if result == 0:
            print(f"port {port} is open")
        sock.close
    except Exception as e:
        print(f'Error scanning port {port} : {e}')

def scanports(ip,start_port,end_port):
    threads=[]
    for port in range(start_port,end_port+1):
        thread=threading.Thread(target=scanport,args=(ip,port))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    target_ip= input("enter the target ip address :")
    start_port=int(input("Enter the starting port :"))
    end_port=int(input("Enter the ending port :"))

    print(f"Scannning ports {start_port}-{end_port} on {target_ip}..\n")
    scanports(target_ip,start_port,end_port)
    print("scan complete")