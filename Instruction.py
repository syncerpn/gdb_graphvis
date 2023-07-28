# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 13:24:25 2023

@author: Nghia
"""

_JUMP_INST_PREFIX = "j"
_JUMP_NO_FORWARD = "jmp"

class Instruction:
    def __init__(self, addr, func_label, func_offset, opc, con, branch=None):
        self.addr = addr
        self.label = "<" + func_label + func_offset.strip("<>") + ">"
        self.opc = opc
        self.con = " ".join(con)
        self.branch = branch
        self.branching = False
        self.forward = True
        if self.branch and self.opc.startswith(_JUMP_INST_PREFIX):
            self.branching = True
        if self.opc == _JUMP_NO_FORWARD:
            self.forward = False
    
    def __str__(self):
        return f"{self.addr} {self.label} {self.opc:6s} {self.con} {self.branch if self.branch else ''}"
        