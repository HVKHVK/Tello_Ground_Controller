import socket
import time
import threading
import cv2
from threading import Thread


class Tello(object):
    UDP_IP = '192.168.10.1'
    SERVER_UDP_IP = '0.0.0.0'
    CONTROL_UDP_PORT = 8889
    RECEIVE_UDP_PORT = 8890
    STREAM_UDP_PORT = 11111

    def __init__(self):
        self.control_address = (self.UDP_IP, self.CONTROL_UDP_PORT)

        self.control_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.control_socket.bind(('', self.CONTROL_UDP_PORT))

        self.response = None

        self.camera_visual_on = False

        thread = threading.Thread(target=self.control_udp_receiver, args=())
        thread.daemon = True
        thread.start()

    def control_udp_receiver(self):
        while True:
            try:
                self.response, _ = self.control_socket.recv(1024)
            except Exception as error:
                print(error)
                break

    def get_udp_video_address(self):
        return 'udp://@' + self.SERVER_UDP_IP + ':' + str(self.STREAM_UDP_PORT)
