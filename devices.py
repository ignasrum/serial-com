#!/usr/bin/env python

import pyudev
import sys


class Device:
    def __init__(self, device):
        self.device_obj = device
        self.name = device.properties["ID_MODEL"]
        self.path = device.device_node

    def __str__(self):
        return "{}: {}".format(self.name, self.path)

def check_if_serial(device):
    if "ID_MODEL" not in device.properties:
        return False
    if "ID_SERIAL_SHORT" not in device.properties:
        return False
    return True

def list_devices():
    devices = []
    context = pyudev.Context()
    for device in context.list_devices(subsystem='tty'):
        if check_if_serial(device): devices.append(Device(device))
    return devices

def print_devices(devices):
    for device in devices:
        print("{}: {}".format(devices.index(device), device))
    if len(devices) == 0:
        print('No USB Serial devices detected.')

def main():
    devices = list_devices()
    print_devices(devices)

if __name__ == "__main__":
    main()
