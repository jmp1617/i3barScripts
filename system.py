#!/usr/bin/env python3

import sys
import subprocess

idle = str((100-(float(subprocess.check_output("mpstat").split()[-1].decode("utf-8"))))).split('.')
memory = str(((16000000-float(subprocess.check_output("vmstat").split()[26].decode("utf-8")))/1000000)).split('.')

sys.stdout.write(idle[0])
sys.stdout.write('.')
sys.stdout.write(idle[1][:2])
sys.stdout.write('%  ')
sys.stdout.write(memory[0])
sys.stdout.write('.')
sys.stdout.write(memory[1][:2])
sys.stdout.write("/16G \n")
