#!/usr/bin/env python3

import subprocess
import sys

sys.stdout.write(subprocess.check_output(["du","-sh","/home/jacob"]).decode("utf-8").split()[0])
sys.stdout.write('/180G \n')
