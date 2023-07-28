# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 14:09:54 2023

@author: Nghia
"""
import re

from CodeBlock import CodeBlock
from Instruction import Instruction

ADDR_PREFIX = "0x"
LABEL_PREFIX = "<"
LABEL_SUFFIX = ">"

class CodeStructure:
    def __init__(self, gdb_disas_file, func_name):
        self.func_name = func_name
        self.blocks = {}
        self.block_id = None
        
        insts = []
        
        with open(gdb_disas_file, "r") as f:
            data = f.readlines()
            
        for line in data:
            line = line.strip()
            elements = re.split(": | ", line)
            elements = [e for e in elements if e]
            
            e_addr = None
            e_label = None
            e_branch = None
            e_opc = None
            e_con = []
            
            for e in elements:
                if e.startswith(ADDR_PREFIX):
                    if e_addr is None:
                        e_addr = e
                    else:
                        e_con.append(e)
                elif e.startswith(LABEL_PREFIX) and e.endswith(LABEL_SUFFIX):
                    if e_label is None:
                        e_label = e
                    else:
                        e_branch = e
                else:
                    if e_opc is None:
                        e_opc = e
                    else:
                        e_con.append(e)
            
            inst = Instruction(e_addr, func_name, e_label, e_opc, e_con, e_branch)
            if inst.branching:
                if inst.branch not in self.blocks:
                    self.blocks[inst.branch] = CodeBlock()
            
            insts.append(inst)
        
        insts = sorted(insts, key=lambda x: int(x.addr, 16))
        for inst in insts:
            self._add_inst(inst)
    
    def _add_inst(self, inst):
        if inst.label in self.blocks:
            self.block_id = inst.label
            
        elif not self.blocks or self.block_id is None:
            self.blocks[inst.label] = CodeBlock()
            self.block_id = inst.label
           
        self.blocks[self.block_id].add_inst(inst)
        
        if self.blocks[self.block_id].lock:
            self.block_id = None
        
        if inst.branching:
            if inst.branch not in self.blocks:
                self.blocks[inst.branch] = CodeBlock()
    
    def __str__(self):
        sorted_blocks_head = sorted(self.blocks.keys(), key=lambda x: int(self.blocks[x].head, 16))
        repr_str = ""
        for head in sorted_blocks_head:
            repr_str += f"{head}\n{str(self.blocks[head])}\n"
            
        return repr_str