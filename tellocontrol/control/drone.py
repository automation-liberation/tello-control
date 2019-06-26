import os
import logging
import socket
import time

log = logging.getLogger(__name__)


class Tello:
    def __init__(self):
        self.drone_ip = '192.168.10.1'
        self.drone_port = 8889
        self.drone = (self.drone_ip, self.drone_port)
        self.host_ip = ''
        self.host_port = 9000
        self.host = (self.host_ip, self.host_port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.connected = False

        self.connect_to_drone()

    def connect_to_drone(self):
        attempts = 30
        while attempts > 0:
            self.attempt_connection()
            if self.connected:
                break

            time.sleep(2)
            attempts -= 1
            log.warn(f'Connection to drone failed will attempt {attempts} more times')

    def attempt_connection(self):
        if os.system('ping -c 1 ' + self.drone_ip) == 0:
            self.establish_connection()

    def establish_connection(self):
        self.sock.bind(self.host)
        self.sock.setblocking(0)
        self.sock.sendto("command".encode(encoding="utf-8"), self.drone)
        self.connected = True

    def send_command(self, command: str):
        if self.connected:
            self.sock.sendto(command.encode(encoding="utf-8"), self.drone)

    def disconnect(self):
        self.sock.close()
        self.connected = False
