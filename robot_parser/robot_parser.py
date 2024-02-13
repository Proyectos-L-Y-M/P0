# -*- coding: utf-8 -*-
"""

"""


robot_commands: list = ['move', 'turn', 'face', 'put',
                        'pick', 'move-dir', 'run-dirs', 'move-face']

flow_commands: list = ['defvar', '=', 'skip',
                       'if', 'loop', 'repeat', 'defun']


class Variable:
    def __init__(self, name, value):
        self.name:  str = name
        self.value: str = value

    def modify_name(self, n: str):
        self.name = n

    def modify_value(self, v: str):
        self.value = v


def is_int(s: str) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        return False


def is_variable(value: str, program_variables: list) -> bool:
    for v in program_variables:
        if v.name == value:
            return True
    return False


def is_robot_command(value: str) -> bool:
    """ 
    Check if command is on robot commands group
    """
    return value in robot_commands

def get_blocks(chain:str, global_index:int)->list:
    
    
    chain.replace('(', '', 1)
    
    if len(chain) != 0:
        
        command = ''
        
        block = []
        
        for i in len(chain):
            
            c = chain[i]
            
            if c == '(':
                
                block.append(get_blocks(chain[i:]))
            
            if c == ')':
                return [command]
            
            else:
                command += c
        
    return None


def parse(program:str) -> bool:
    program = program.replace("\n", "").replace("\t", "")
    if program[0] != '(': # Todo programa debe comenzar con un "("
        return False
    else: 
        blocks = get_blocks(program, 1)
    
    pass
