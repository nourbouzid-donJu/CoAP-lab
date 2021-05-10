# Python imports
import re
import sys

# Scapy imports
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import IP, TCP, conf, Raw
from scapy.contrib.coap import *


def inject(src, dst):
    sock = conf.L3socket()
    
    PAYLOAD = CoAP(ver = 1, type = 0, code = 0x42, msg_id = 0xface, options=[("Content-Format", b"\x00")], paymark = b"\xff")
    PAYLOAD.add_payload(Raw(""))
    packet = IP(src=src, dst=dst) / UDP(sport=5683, dport=5683) / PAYLOAD

    sock.send(packet)


def main():
    src = str(sys.argv[1])
    dst = str(sys.argv[2])
    inject(src, dst)


if __name__ == "__main__":
    sys.exit(main())
