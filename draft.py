# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 02:47:20 2023

@author: NghiaServer
"""

import matplotlib.pyplot as plt
import re

gdb_disas_file = "bomblab_phase_5.gasm"

with open(gdb_disas_file, "r") as f:
    data = f.readlines()
    
for line in data:
    line = line.strip()
    elements = re.split(": | ", line)
    elements = [e for e in elements if e]
    print(elements)
