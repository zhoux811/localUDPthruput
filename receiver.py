import socket
from time import sleep, time
import select
from threading import Timer
import sys

re_try_n = 0


def main(base_wait_time, Y, drop_rate):
    time_used = time()

    base_wait_time = float(base_wait_time)
    Y = int(Y)

    if Y:
        print('RECEIVER: Y value is ' + str(Y))
    else:
        Y = input('RECEIVER: Y value? (from [150, 250, 450, 650, 850, 1000]) \n')
        print('RECEIVER: Y value is ' + str(Y))

    print('RECEIVER: base_wait_time is : ' + str(base_wait_time))
    print('RECEIVER: running receiver')

    address = "127.0.0.1"
    MESSAGE = b"this is receiver!"

    RECEIVER_ROUTER = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ROUTER_RECEIVER = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    RECEIVER_ROUTER.bind((address, 33333))

    def listening(start_from, end_at):
        global re_try_n
        counter = start_from
        NACK_sent = False
        while counter < end_at - 1:
            data, addr = RECEIVER_ROUTER.recvfrom(65565)

            L = len(data)

            # print('\nRECEIVER: expecting( counter):' + str(counter))
            # print('RECEIVER:  got data : ' + str(L))

            if L == counter:
                print('RECEIVER: so far so good. just received : ' + str(L))
                counter += 1
                NACK_sent = False

            elif L != counter and not NACK_sent:
                RECEIVER_ROUTER.sendto(bytes(counter), (address, 22222))

                re_try_n += 1
                NACK_sent = True

            elif L != counter and NACK_sent:
                listening(counter, end_at)
                break

            else:
                counter += 1

    start_index = 0
    listening(start_index, Y)

    print(
        '|#######################################|\n' * 2 +
        '|   RECEIVER: sent  %s  NACK packets\t|\n' % re_try_n +
        '|#######################################|\n' * 2
    )

    time_used = time() - time_used

    f = open('result.txt', 'a+')
    f.write('\nRECEIVER received %s ordered packets. '
            'total %s bytes. '
            'base wait time: %s sec. '
            'used %s NACK packets. took %s seconds. '
            'drop_rate was %s. '
            'thruput is %s bytes/sec. '
            % (Y, (1+Y)*Y/2, base_wait_time, re_try_n, time_used, drop_rate, (1+Y)*Y/2/time_used))
    #f.close()

    exit()


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
