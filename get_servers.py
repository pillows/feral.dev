# Converting the servers in the feral_server list
# to it's respective ip
import socket

with open("feral_servers", "r") as server:

    for slot in server:

        slot = slot.strip('\n')
        ip = socket.gethostbyname(slot).strip('\n')
        print(slot, ip)
