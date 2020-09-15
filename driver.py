from threading import Thread
from time import sleep
import os
import sys

# Y = ''
# base_wait_time = ''
# router_drop_rate = ''
Y, base_wait_time, router_drop_rate = sys.argv[1], sys.argv[2], sys.argv[3]


def main(Y, base_wait_time, router_drop_rate):

    def router():
        global base_wait_time, Y, router_drop_rate
        cmd = ('python  router.py  %s ' % router_drop_rate)
        os.system(cmd)

    def receiver():
        global base_wait_time, Y, router_drop_rate
        cmd = ('python receiver.py %s %s %s' % (base_wait_time, Y, router_drop_rate))
        os.system(cmd)

    def sender():
        global base_wait_time, Y, router_drop_rate
        cmd = ('python  sender.py  %s  %s ' % (base_wait_time, Y))
        os.system(cmd)

    t_router = Thread(target=router, args=())
    t_receiver = Thread(target=receiver, args=())
    t_sender = Thread(target=sender, args=())

    t_router.start()
    sleep(0.5)
    t_receiver.start()
    sleep(0.5)
    t_sender.start()


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])