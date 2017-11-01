#!/usr/bin/env python3

import subprocess

print((str(subprocess.check_output(["sensors", "-Au"])).split("fan1_input: "))[1].split('.')[0],"rpm ")
