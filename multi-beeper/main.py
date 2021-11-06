from time import sleep
from random import randint

from router import Router

def main():
    ip_list = []
    routers = []

    for ip in ip_list:
        routers.append(Router(ip, 'admin', 'password'))
    
    while True:
        frequency = str(randint(350, 6000))
        delay = randint(300, 1500)

        for router in routers:
            router.run(frequency, delay)

        sleep(delay)

if __name__ == '__main__':
    main()
