#!/bin/sh

COAP_DIR=coap
sudo mkdir /$COAP_DIR


sudo cp $COAP_DIR/thermostat.jar /$COAP_DIR
sudo cp $COAP_DIR/station.jar /$COAP_DIR
sudo cp $COAP_DIR/thermostat-dtls.jar /$COAP_DIR
sudo cp $COAP_DIR/station-dtls.jar /$COAP_DIR
sudo cp $COAP_DIR/discovery.sh /$COAP_DIR
sudo cp $COAP_DIR/startup.sh /$COAP_DIR
sudo cp $COAP_DIR/response_spoofer.py /$COAP_DIR
sudo cp $COAP_DIR/set_temperature.py /$COAP_DIR
sudo cp $COAP_DIR/CoAP.imn /home/ilab/.core/configs/
sudo cp $COAP_DIR/attack.sh /$COAP_DIR
sudo cp $COAP_DIR/loop_discovery.sh /$COAP_DIR

sudo apt-get update
sudo apt --assume-yes install default-jre
sudo apt-get --assume-yes install python-pip
sudo pip install CoAPthon
sudo pip install scapy
sudo pip install bitstring
