#!/usr/bin/env python

import serial
import time
import sys

def send_command(path, baud_rate, command):
    serialPort = serial.Serial(path, baud_rate, exclusive = True)
    cmd = command + "\n"
    serialPort.write(cmd.encode())
    time.sleep(1)
    lines = serialPort.read(serialPort.in_waiting).decode().splitlines(True)
    serialPort.close()
    output = ""
    for line in lines: output += line
    return output

def main():
    if len(sys.argv) < 3:
        print("Wrong arguments")
        exit(-1)
    path = sys.argv[1]
    baud_rate = sys.argv[2]
    commands = sys.argv[3:]
    try:
        baud_rate = int(baud_rate)
    except ValueError:
        print("Invalid baud rate input")
        exit(-1)
    for command in commands:
        print("-" * 20)
        print(command + ": \n")
        output = send_command(path, baud_rate, command + "\n")
        if output == "": output = "No output"
        print(output)

if __name__ == "__main__":
    main()
