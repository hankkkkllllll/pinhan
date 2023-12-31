# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 12:57:50 2023

@author: God
"""

#print("test")

import sys
from bluepy import btle

if len(sys.argv) != 2:
    print("Usage: python3 testPY.py <device_address>")
    sys.exit(1)

device_address = sys.argv[1]

try:
    print(f"Connecting to {device_address}")
    peripheralObject = btle.Peripheral("D3:36:38:E3:DE:6B")
    print("Connected successfully.")
except Exception as e:
    print(f"Failed to connect to {device_address}: {e}")
    sys.exit(1)
