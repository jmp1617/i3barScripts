#!/usr/bin/env python3

import sys
import subprocess

ip = subprocess.check_output("/home/jacob/.config/i3/scripts/ip_get").decode("utf-8").strip('\n')
sys.stdout.write( ip )
sys.stdout.write( " " )
