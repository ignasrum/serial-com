#!/usr/bin/env python

import os
import argparse

import devices


def get_devices():
    return devices.list_devices()

def get_input(devs):
    devices.print_devices(devs)
    if len(devs) == 0: exit(-1)

    selected_device = input("Select device: ")
    try:
        selected_device = int(selected_device)
        if selected_device not in range(len(devs)): raise Exception("Invalid selection")
    except Exception as e:
        print(e)
        exit(-1)
    baud_rate = input("Enter baud rate: ")
    try:
        baud_rate = int(baud_rate)
    except ValueError:
        print("Invalid input: must be an int")
        exit(-1)
    command = input("Enter command: ")
    command += "\n"
    return selected_device, baud_rate, command

def main():
    devs = get_devices()
    selected_device, baud_rate, command = get_input(devs)
    os.system("sudo python command.py {} {} {}".format(devs[selected_device].path, baud_rate, command))

if __name__ == "__main__":
    main()
