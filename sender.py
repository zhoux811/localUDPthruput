from pathlib import Path
import socket
from time import sleep
import sys
import select
from math import pow, log10


def main(base_wait_time, Y):
    base_wait_time = 2 * float(base_wait_time)
    Y = int(Y)

    if Y:
        print('SENDER: Y value is ' + str(Y))
    else:
        Y = input('SENDER: Y value? (from [150, 250, 450, 650, 850, 1000]) \n')
        print('SENDER: Y value is ' + str(Y))
    print('SENDER: base_wait_time is : ' + str(base_wait_time))
    print('SENDER: running SENDER')

    address = "127.0.0.1"
    MESSAGE = b"this is SENDER!"

    SENDER_ROUTER = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ROUTER_SENDER = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    SENDER_ROUTER.bind((address, 11111))

    sleep(2)

    def there_is_NACK(end_at_passed_down):
        # print('SENDER: waiting for NACK')
        SENDER_ROUTER.setblocking(0)
        # sleep(wait_time + 1)
        ready = select.select([SENDER_ROUTER], [], [], base_wait_time * 2)
        # to be safe. ned larger BASE wait time . tell receiver respectively
        if ready[0]:
            data, addr = SENDER_ROUTER.recvfrom(65565)
            if '44444' in str(addr):
                print('\nSENDER: got NACK from ROUTER!!!!!!!')
                new_start_from = len(data)

                print('SENDER: RECEIVER says he wants : ' + str(new_start_from))

                sequence(new_start_from, end_at_passed_down)

    def sequence(start_from, end_at):
        t_value = 1

        retry_counter = 0
        y = start_from

        while y < end_at - 1:
            '''
            if y == end_at:
                print('SENDER: all sends complete')
                return retry_counter
                break
            '''
            for i in range(t_value):
                SENDER_ROUTER.sendto(bytes(y), (address, 44444))
                y += 1

            print('SENDER: packets sent :\t%d\tto\t%d ' % (y - t_value, y))

            # should start waiting
            if there_is_NACK(end_at):
                retry_counter += 1  # use later
                break

            else:
                # print('SENDER: no NACK')
                t_value *= 2

    start_index = 0
    sequence(start_index, Y)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
