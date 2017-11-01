#!/usr/bin/env python3

import subprocess

out = str(subprocess.check_output(["sensors", "-Au"]))

core0 = out.split("temp2_input:")
core1 = out.split("temp3_input:")

print(core0[1][1:3],core1[1][1:3],"")
