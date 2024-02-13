# -*- coding: utf-8 -*-
"""
Universidad de los Andes
Lenguajes y Máquinas
P0 - Robot Parser
Febrero/2024

@author: YuneLotus
@author: JEAM1308
"""
import os
import robot_parser


def read_commands(root:str='./samples') -> list:
    """
    Lee todos los 
    Reads all the data of each file placed on the samples folder.
    """
    files_data = []
    
    samples_names = os.listdir(root)
    
    # Get data from each sample
    for path in samples_names:

        print(f'Reading {path} commands')
        
        with open((root + path), 'r') as f:
            
            files_data.append(f.read())

    return files_data


def main():
    files_data = read_commands()
    for i, program in enumerate(files_data):
        print('\n-------------------')
        print(f'Input {i + 1}')
        print('--\n', program, '\n--')

        validation = robot_parser.parse(program)

        print(f'\nIs Input {i + 1} using a correct syntax?')
        if validation:
            print(f"---> YES")
        else:
            print(f"---> NO")


if __name__ == "__main__":
    main()








