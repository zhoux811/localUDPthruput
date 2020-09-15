import socket
from random import randint
import select
import sys


def main(drop_rate):
    address = "127.0.0.1"
    MESSAGE = b"this is router!"

    drop_rate = float(drop_rate)

    if drop_rate:
        print('ROUTER: drop rate is ' + str(drop_rate) + '%, namely 1 out of ' + str(100 / drop_rate))
    else:
        drop_rate = float(input('ROUTER: drop rate? (key in 100 for 100 percent) 0.1 suggested\n'))
        print('ROUTER: drop rate is ' + str(drop_rate) + '%, namely 1 out of ' + str(100 / drop_rate))

    SENDER_ROUTER = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    RECEIVER_ROUTER = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ROUTER_SENDER = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ROUTER_RECEIVER = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sockets = [SENDER_ROUTER, RECEIVER_ROUTER, ROUTER_SENDER, ROUTER_RECEIVER]

    ROUTER_RECEIVER.bind((address, 22222))
    ROUTER_SENDER.bind((address, 44444))

    print('ROUTER: router always work')

    while True:
        ready_socks, _, _ = select.select(sockets, [], [])
        # this will block until at least one socket is ready
        # if nothing transfered in 10, timeout
        if ready_socks[0]:
            for sock in ready_socks:
                data, addr = sock.recvfrom(65565)

                if '33333' in str(addr):  # !!!! RECEIVER !!!!
                    # print("ROUTER received message from RECEIVER: %s %s" % (data, addr))
                    print("\n#################\nROUTER: NACK from RECEIVER!!! need : " + str(len(data)) + "\nforwarding to SENDER\n#################\n")
                    ROUTER_SENDER.sendto(data, (address, 11111))
                    # exit()

                elif '11111' in str(addr):  # !!! from SENDER !!!

                    # DROP!!!
                    if randint(0, int(100 / drop_rate)) == 0:
                        print('\n#################\nROUTER: dropped a packet!!!\n#################\n')
                    # DROP!!!

                    else:
                        # print("ROUTER received message from SENDER: %s %s" % (data, addr))
                        # print(" SENDER transmitting (detail omitted) forwarded")
                        # print(len(data))

                        ROUTER_RECEIVER.sendto(data, (address, 33333))
                else:
                    print('who is trying on port 22222 or 44444!!!!????')


if __name__ == '__main__':
    main(sys.argv[1])
