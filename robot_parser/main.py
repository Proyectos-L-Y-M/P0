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

def read_programs(root:str='./programs') -> list:
    """
    De la carpeta 'programs', se lee cada archivo (programa) que será analizado.
    """
    programs = [] # Aquí se guardará cada programa en forma de string      
    programs_paths = os.listdir(root) # Se listan los nombres (paths) de cada archivo que contiene un programa
    
    for path in programs_paths: # Para cada dirección de archivo:
        print("\n\t" + f"Leyendo el programa del archivo {path} ...")
        file = open((root + path), 'r') # Se abre el archivo
        program = file.read()           # Se lee el programa
        programs.append(program)        # Se agrega a la lista
        file.close()                    # Se cierra el archivo
    return programs # Al final, se retorna la lista de todos los programas

def main():
    programs = read_programs()
    print("="*20 +" RESULTADOS "+ "="*20)
    for i, program in enumerate(programs, start=1):
        print("\n" + f'Program # {i} :')
        print('\n' + program + '\n' + '-'*20)
        ans = robot_parser.parse(program)
        msj = 'VÁLIDA' if ans else 'INVÁLIDA'  
        print("\n\t" + f"La sintaxis de este programa (# {i}) es {msj}")
        print('\n' + "="*20)

if __name__ == "__main__":
    main()



