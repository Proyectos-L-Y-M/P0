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

def get_function_call(chain:str, global_index:int)->tuple:
    # global_index es donde empieza el paréntesis de los parámetros
    params = False

    pass

def get_commands(chain:str, global_index:int)->list:

    command = ''
    
    commands = []
    
    while global_index < len(chain):

        c = chain[global_index]
        if c == '(':
            func, global_index = get_function_call(chain[global_index:], global_index)
            if func is None:
                return None
        elif c == ')':
            if command != '':
                commands.append(command)
                command = ''
                global_index += 1
            else:
                return None
        else:
            command += c
            global_index += 1

    return commands


def check_basic_conditions(program:str):
    """
    Si alguna de las siguientes condiciones NO se cumple, 
    se retorna Flase
    """
    cond1 = len(program) >= 6   # La instrucción más corta es (null)
    cond2 = program[0] == '('   # Todo programa debe comenzar con un "("
    cond3 = program.count('(') == program.count(')') #El número de '(' debe ser igual al número de')'
    
    return cond1 and cond2 and cond3

# (((null)))

def parse(program:str) -> bool:
    
    

    program = program.replace("\n", "").replace("\t", "")
    
    if check_basic_conditions(program):     
        global_index = 1
        blocks = get_commands(program, global_index)
    
    else:
        return False


