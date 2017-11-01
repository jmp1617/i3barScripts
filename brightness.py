#!/usr/bin/env python3

import sys
import subprocess

brightness = subprocess.check_output("/usr/bin/brightnessctl").decode("utf-8").split()[7]
brightness = int((int(brightness)/1060)*100)

sys.stdout.write( str(brightness) )
sys.stdout.write( "%" )
sys.stdout.write( " " )
