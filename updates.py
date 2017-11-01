#!/usr/bin/env python3

import subprocess

updates = str(subprocess.check_output(["checkupdates"]).decode("utf-8")).count('\n')
if int(updates) != 0:
    print( updates,"" )
