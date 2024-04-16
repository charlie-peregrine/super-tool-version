# change_version.py, Charlie Jordan, 4/16/2024

import re
from os import replace as osreplace

with open("SUPERTOOLVERSION", 'r') as f:
    lines = f.read().split('\n')

version_line = lines[0]

print("Old Version:", version_line)
new_version = input("New Version: ")

m = re.match(r'^v(\d+)\.(\d+)\.(\d+)$', new_version)
if m:
    with open("SUPERTOOLVERSION2", 'w') as f:
        f.write("\n".join([new_version] + lines[1:]))
    osreplace("SUPERTOOLVERSION2", "SUPERTOOLVERSION")
else:
    print("Version Change Failed")

