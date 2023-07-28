# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 03:19:38 2023

@author: NghiaServer
"""

class CodeBlock:
    def __init__(self):
        self.insts = {}
        self.head = None
        self.tail = None
        self.lock = False
        self.connect_to = None
    
    def add_inst(self, inst):
        assert not self.lock, f"[ERRO] try adding instruction to locked code block:\n{self.__str__}"
        self.insts[inst.addr] = inst
        
        if inst.branching or not inst.forward:
            self.lock = True
        # if inst.
        #     self.connect_to = 
        
        if self.head is None:
            self.head = inst.addr    
        elif self.head > inst.addr:
            self.head = inst.addr
            
        if self.tail is None:
            self.tail = inst.addr
        elif self.tail < inst.addr:
            self.tail = inst.addr
    
    def __str__(self):
        return '\n'.join([str(self.insts[k]) for k in sorted(self.insts.keys(), key=lambda x: int(x, 16))])
        