# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 02:47:20 2023

@author: NghiaServer
"""

import matplotlib.pyplot as plt

from CodeStructure import CodeStructure

import turtle as T

gdb_disas_file = "bomblabz_phase_6.gasm"


cs = CodeStructure(gdb_disas_file, "phase_6")
print(cs)

# T.Screen()
# T.TurtleScreen._RUNNING=True
# # T.up()
# T.setposition(0,-13)
# # T.down()

# T.hideturtle()

# # T.write(str(cs), font=("Consolas", 8, "normal"))
# T.write("dg", font=("Consolas", 8, "normal"))

# T.done()
