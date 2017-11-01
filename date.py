#!/usr/bin/env python3

import sys
import subprocess

date = (subprocess.check_output("date")).decode("utf-8").split()

print(date[0], date[1], date[2], "<b>", date[3], "</b>")
