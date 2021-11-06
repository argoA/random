import routeros_api as ros

from random import randint
from time import sleep
import datetime

class Router():
    def __init__(self, ip, user, passw):
        self.ip = ip
        self.user = user
        self.passw = passw

        # Make connection
        self.conn = ros.RouterOsApiPool(ip, username=user, password=passw, plaintext_login=True)
        self.api = self.conn.get_api()

        # Beep variables
        self.double_beep = False


    def run(self, frequency, delay):
        # Log messages
        self.beep_freq_message = "Beeped with a freq of: " + frequency
        self.next_beep_message = "Next beep is at: " + self.get_next_beep_time(delay) # Unsure if this works
        self.double_beep_message = "Just sent a double beep!"

        # Chance at a double beep
        chance = randint(1,100)
        if chance >= 90:
            self.double_beep = True

            self.beep(frequency)
            sleep(0.25)
            self.beep(frequency)
        else:
            self.beep(frequency)

        self.send_log()
        self.double_beep = False

    def beep(self, frequency):
        self.api.get_binary_resource('/').call('beep', {'frequency': frequency.encode()})  

    def send_log(self):
        if self.double_beep == True:
            self.api.get_binary_resouce('/').call('log/info', { 'message': self.double_beep_message.encode() })

        self.api.get_binary_resource('/').call('log/info', { 'message': self.beep_freq_message.encode() })
        self.api.get_binary_resource('/').call('log/info', { 'message': self.next_beep_message.encode() })

    def get_next_beep_time(self, delay):
        now = datetime.datetime.now()
        delay_delta = datetime.timedelta(seconds=delay)
        
        return str(now + delay_delta)
