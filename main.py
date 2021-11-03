import routeros_api as ros

from random import randint
from time import sleep
import datetime

def main():
    conn = ros.RouterOsApiPool('10.10.10.122', username='admin', password='password', plaintext_login=True)
    api = conn.get_api()

    while True:
        beeper(api)

def beeper(api):
    delay = randint(300, 1500)
    frequency = str(randint(20, 20000))

    now = datetime.datetime.now()
    delay_delta = datetime.timedelta(seconds=delay)
    next_beep = now + delay_delta

    freq_message = "Beeped with a freq of: " + frequency
    delay_message = "Next beep is at: " + str(next_beep)

    api.get_binary_resource('/').call('log/info', {'message': delay_message.encode()})
    api.get_binary_resource('/').call('log/info', {'message': freq_message.encode()})
    api.get_binary_resource('/').call('beep', {'frequency': frequency.encode()})

    sleep(delay)

if __name__ == "__main__":
    main()