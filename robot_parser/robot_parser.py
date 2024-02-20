# -*- coding: utf-8 -*-
"""

"""


robot_commands: list = ['move', 'turn', 'face', 'put',
                        'pick', 'move-dir', 'run-dirs', 'move-face']

flow_commands: list = ['defvar', '=', 'skip',
                       'if', 'loop', 'repeat', 'defun']

def parse_program(tokens):
    instructions = []
    while tokens:
        instruction, tokens = parse_instruction(tokens)
        instructions.append(instruction)
    return instructions

def parse_command(tokens):
    if not tokens:
        return False # raise SyntaxError("Se esperaba un comando, pero se encontró el final de la entrada.")
    token, token_type = tokens[0]
    if token_type == 'KEYWORD':
        command_parsers = {
            'defvar': parse_defvar,
            '=': parse_assignment,
            'move': parse_move,
            'skip': parse_skip,
            'turn': parse_turn,
            'face': parse_face,
            'put': parse_put,
            'pick': parse_pick,
            'move-dir': parse_move_dir,
            'run-dirs': parse_run_dirs,
            'move-face': parse_move_face,
            'null': parse_null,
        }
        if token in command_parsers:
            return command_parsers[token](tokens)
        else:
            return False #raise SyntaxError(f"Comando no reconocido: '{token}'.")
    else:
        return False #raise SyntaxError(f"Token inesperado '{token}' en lugar de un comando.")

def parse_instruction(tokens):
    # Verificar que haya al menos un token para analizar
    if not tokens:
        return False #raise SyntaxError("No se encontraron tokens para analizar la instrucción.")

    # Obtener el tipo de la instrucción a partir del primer token
    instruction_type = tokens[0][1]

    instruction_parsers = {
        'defvar': parse_defvar,
        '=': parse_assignment,
        'move': parse_move,
        'skip': parse_skip,
        'turn': parse_turn,
        'face': parse_face,
        'put': parse_put,
        'pick': parse_pick,
        'move-dir': parse_move_dir,
        'run-dirs': parse_run_dirs,
        'move-face': parse_move_face,
        'null': parse_null,
        'if': parse_if,
        'loop': parse_loop,
        'repeat': parse_repeat,
        'defun': parse_function_definition,
    }
    
    if instruction_type in instruction_parsers:
        return instruction_parsers[instruction_type](tokens[1:])
    else:
        return False #raise SyntaxError(f"Tipo de instrucción desconocido: {instruction_type}")

def parse_value(tokens):
    # Comprobar que hay tokens para analizar
    if not tokens:
        raise SyntaxError("Se esperaba un valor, pero se encontró el final de la entrada.")
    
    token, token_type = tokens[0]
    if token_type == 'NUMBER':
        # Si el primer token es un número, retornamos su valor
        return {
            'type': 'number',
            'value': int(token)
        }
    elif token_type == 'IDENTIFIER':
        # Si el primer token es un identificador, retornamos su valor
        return {
            'type': 'identifier',
            'name': token
        }
    elif token_type == 'CONSTANT':
        # Si el primer token es una constante, retornamos su valor
        return {
            'type': 'constant',
            'name': token
        }
    else:
        return False #raise SyntaxError(f"Token inesperado '{token}' al analizar un valor.")

def parse_defvar(tokens):
    if len(tokens) < 4:
        raise SyntaxError("Comando 'defvar' incompleto.")
    
    if tokens[1][1] != 'IDENTIFIER':
        raise SyntaxError("Se esperaba un identificador después de 'defvar'.")
    
    if tokens[2][0] != '=':
        raise SyntaxError("Se esperaba un signo '=' después del nombre de la variable en 'defvar'.")
    
    # Analizar el valor de la variable (puede ser un número, una variable o una constante)
    value = parse_value(tokens[3:])
    
    # Devolver una representación del comando 'defvar'
    return {'command': 'defvar', 'variable': tokens[1][0], 'value': value}

def parse_assignment(tokens):
    if len(tokens) < 3:
        raise SyntaxError("Comando de asignación incompleto.")
    
    if tokens[1][1] != 'IDENTIFIER':
        raise SyntaxError("Se esperaba un identificador después del signo '=' en la asignación.")
    
    # Analizar el valor asignado (puede ser un número, una variable o unax constante)
    value = parse_value(tokens[2:])
    
    # Devolver una representación del comando de asignación
    return {'command': 'assignment', 'variable': tokens[1][0], 'value': value}

def parse_move(tokens):
    if len(tokens) < 2:
        raise SyntaxError("Comando 'move' incompleto.")
    
    if tokens[1][1] != 'NUMBER':
        raise SyntaxError("Se esperaba un número después de 'move'.")
    
    # Obtener el número de pasos a mover
    steps = int(tokens[1][0])
    
    # Devolver una representación del comando 'move'
    return {'command': 'move', 'steps': steps}

def parse_skip(tokens):
    # Comprobar que hay suficientes tokens para analizar el comando skip
    if len(tokens) < 2:
        raise SyntaxError("Comando 'skip' incompleto.")

    # Verificar el formato del comando skip
    if tokens[0][0] != 'KEYWORD' or tokens[0][1] != 'skip':
        raise SyntaxError("Se esperaba el comando 'skip'.")
    if tokens[1][0] != 'NUMBER':
        raise SyntaxError("Se esperaba un número después de 'skip'.")

    # Devolver una estructura de datos que represente el comando skip
    return {
        'type': 'skip',
        'steps': int(tokens[1][0])  # El número de pasos a saltar
    }

def parse_skip(tokens):
    # Comprobar que hay suficientes tokens para analizar el comando skip
    if len(tokens) < 2:
        raise SyntaxError("Comando 'skip' incompleto.")

    # Verificar el formato del comando skip
    if tokens[0][0] != 'KEYWORD' or tokens[0][1] != 'skip':
        raise SyntaxError("Se esperaba el comando 'skip'.")
    if tokens[1][0] != 'NUMBER':
        raise SyntaxError("Se esperaba un número después de 'skip'.")

    # Devolver una estructura de datos que represente el comando skip
    return {
        'type': 'skip',
        'steps': int(tokens[1][0])  # El número de pasos a saltar
    }
 
def parse_turn(tokens):
    # Comprobar que hay suficientes tokens para analizar el comando turn
    if len(tokens) < 2:
        raise SyntaxError("Comando 'turn' incompleto.")

    # Verificar el formato del comando turn
    if tokens[0][0] != 'KEYWORD' or tokens[0][1] != 'turn':
        raise SyntaxError("Se esperaba el comando 'turn'.")
    if tokens[1][0] != 'SYMBOL':
        raise SyntaxError("Se esperaba una dirección después de 'turn'.")

    # Mapear las direcciones de giro a constantes definidas en el lenguaje
    directions = {
        ':left': 'left',
        ':right': 'right',
        ':around': 'around'
    }

    # Comprobar si la dirección es válida
    if tokens[1][1] not in directions:
        raise SyntaxError("Dirección de giro no válida.")

    # Devolver una estructura de datos que represente el comando turn
    return {
        'type': 'turn',
        'direction': directions[tokens[1][0]]  # La dirección hacia la que girar
    }

def parse_face(tokens):
    # Comprobar que hay suficientes tokens para analizar el comando face
    if len(tokens) < 2:
        raise SyntaxError("Comando 'face' incompleto.")

    # Verificar el formato del comando face
    if tokens[0][0] != 'KEYWORD' or tokens[0][1] != 'face':
        raise SyntaxError("Se esperaba el comando 'face'.")
    if tokens[1][0] != 'SYMBOL':
        raise SyntaxError("Se esperaba una dirección después de 'face'.")

    # Mapear las direcciones de orientación a constantes definidas en el lenguaje
    directions = {
        ':north': 'north',
        ':south': 'south',
        ':east': 'east',
        ':west': 'west'
    }

    # Comprobar si la dirección es válida
    if tokens[1][1] not in directions:
        raise SyntaxError("Dirección de orientación no válida.")

    # Devolver una estructura de datos que represente el comando face
    return {
        'type': 'face',
        'direction': directions[tokens[1][0]]  # La dirección hacia la que orientarse
    }

def parse_put(tokens):
    # Comprobar que hay suficientes tokens para analizar el comando put
    if len(tokens) < 3:
        raise SyntaxError("Comando 'put' incompleto.")

    # Verificar el formato del comando put
    if tokens[0][0] != 'KEYWORD' or tokens[0][1] != 'put':
        raise SyntaxError("Se esperaba el comando 'put'.")
    if tokens[1][0] != 'SYMBOL':
        raise SyntaxError("Se esperaba un tipo de objeto después de 'put'.")
    if tokens[2][0] != 'NUMBER':
        raise SyntaxError("Se esperaba un número después del tipo de objeto en 'put'.")

    # Mapear los tipos de objeto a constantes definidas en el lenguaje
    object_types = {
        ':balloons': 'balloons',
        ':chips': 'chips'
    }

    # Comprobar si el tipo de objeto es válido
    if tokens[1][1] not in object_types:
        raise SyntaxError("Tipo de objeto no válido en 'put'.")

    # Devolver una estructura de datos que represente el comando put
    return {
        'type': 'put',
        'object_type': object_types[tokens[1][0]],  # El tipo de objeto
        'amount': int(tokens[2][0])  # La cantidad de objetos a colocar
    }

def parse_pick(tokens):
    # Comprobar que hay suficientes tokens para analizar el comando pick
    if len(tokens) < 3:
        raise SyntaxError("Comando 'pick' incompleto.")

    # Verificar el formato del comando pick
    if tokens[0][0] != 'KEYWORD' or tokens[0][1] != 'pick':
        raise SyntaxError("Se esperaba el comando 'pick'.")
    if tokens[1][0] != 'SYMBOL':
        raise SyntaxError("Se esperaba un tipo de objeto después de 'pick'.")
    if tokens[2][0] != 'NUMBER':
        raise SyntaxError("Se esperaba un número después del tipo de objeto en 'pick'.")

    # Mapear los tipos de objeto a constantes definidas en el lenguaje
    object_types = {
        ':balloons': 'balloons',
        ':chips': 'chips'
    }

    # Comprobar si el tipo de objeto es válido
    if tokens[1][1] not in object_types:
        raise SyntaxError("Tipo de objeto no válido en 'pick'.")

    # Devolver una estructura de datos que represente el comando pick
    return {
        'type': 'pick',
        'object_type': object_types[tokens[1][0]],  # El tipo de objeto
        'amount': int(tokens[2][0])  # La cantidad de objetos a recoger
    }

def parse_move_dir(tokens):
    # Comprobar que hay suficientes tokens para analizar el comando move-dir
    if len(tokens) < 3:
        raise SyntaxError("Comando 'move-dir' incompleto.")

    # Verificar el formato del comando move-dir
    if tokens[0][0] != 'KEYWORD' or tokens[0][1] != 'move-dir':
        raise SyntaxError("Se esperaba el comando 'move-dir'.")
    if tokens[1][0] != 'NUMBER':
        raise SyntaxError("Se esperaba un número después de 'move-dir'.")
    if tokens[2][0] != 'SYMBOL':
        raise SyntaxError("Se esperaba una dirección después del número en 'move-dir'.")

    # Mapear las direcciones de movimiento a constantes definidas en el lenguaje
    directions = {
        ':front': 'front',
        ':right': 'right',
        ':left': 'left',
        ':back': 'back'
    }

    # Comprobar si la dirección es válida
    if tokens[2][1] not in directions:
        raise SyntaxError("Dirección de movimiento no válida en 'move-dir'.")

    # Devolver una estructura de datos que represente el comando move-dir
    return {
        'type': 'move-dir',
        'steps': int(tokens[1][0]),  # El número de pasos a mover
        'direction': directions[tokens[2][0]]  # La dirección hacia la que moverse
    }

def parse_move_face(tokens):
    # Comprobar que hay suficientes tokens para analizar el comando move-face
    if len(tokens) != 3:
        raise SyntaxError("Comando 'move-face' incompleto.")

    # Verificar el formato del comando move-face
    if tokens[0][0] != 'KEYWORD' or tokens[0][1] != 'move-face':
        raise SyntaxError("Se esperaba el comando 'move-face'.")
    if tokens[1][0] != 'NUMBER':
        raise SyntaxError("Se esperaba un número después de 'move-face'.")
    if tokens[2][0] != 'SYMBOL':
        raise SyntaxError("Se esperaba una dirección después del número en 'move-face'.")

    # Mapear las direcciones de orientación a constantes definidas en el lenguaje
    directions = {
        ':north': 'north',
        ':south': 'south',
        ':east': 'east',
        ':west': 'west'
    }

    # Comprobar si la dirección es válida
    if tokens[2][1] not in directions:
        raise SyntaxError("Dirección de orientación no válida en 'move-face'.")

    # Devolver una estructura de datos que represente el comando move-face
    return {
        'type': 'move-face',
        'steps': int(tokens[1][0]),  # El número de pasos a mover
        'direction': directions[tokens[2][0]]  # La dirección hacia la que orientarse
    }

def parse_run_dirs(tokens):
    # Comprobar que hay suficientes tokens para analizar el comando run-dirs
    if len(tokens) < 2:
        raise SyntaxError("Comando 'run-dirs' incompleto.")

    # Verificar el formato del comando run-dirs
    if tokens[0][0] != 'KEYWORD' or tokens[0][1] != 'run-dirs':
        raise SyntaxError("Se esperaba el comando 'run-dirs'.")
    if tokens[1][0] != 'LPAREN':
        raise SyntaxError("Se esperaba una lista de direcciones después de 'run-dirs'.")

    # Inicializar la lista de direcciones
    directions = []

    # Analizar la lista de direcciones
    index = 2
    while index < len(tokens):
        if tokens[index][0] == 'RPAREN':
            break
        elif tokens[index][0] != 'SYMBOL':
            raise SyntaxError("Se esperaba una dirección en la lista de direcciones.")
        else:
            directions.append(tokens[index][1])
        index += 1

    # Comprobar si la lista de direcciones está vacía
    if not directions:
        raise SyntaxError("Lista de direcciones vacía en 'run-dirs'.")

    # Mapear las direcciones de movimiento a constantes definidas en el lenguaje
    valid_directions = {
        ':front': 'front',
        ':right': 'right',
        ':left': 'left',
        ':back': 'back'
    }

    # Verificar si todas las direcciones en la lista son válidas
    for direction in directions:
        if direction not in valid_directions:
            raise SyntaxError("Dirección de movimiento no válida en 'run-dirs'.")

    # Devolver una estructura de datos que represente el comando run-dirs
    return {
        'type': 'run-dirs',
        'directions': [valid_directions[dir] for dir in directions]
    }

def parse_null(tokens):
    # Verificar que el comando null esté bien formado
    if len(tokens) != 1 or tokens[0][0] != 'KEYWORD' or tokens[0][1] != 'null':
        raise SyntaxError("Comando 'null' mal formado.")

    # Devolver una estructura de datos que represente el comando null
    return {
        'type': 'null'
    }

#----------------------------

def parse_block(tokens):
    # Verificar que los tokens estén delimitados correctamente por paréntesis
    if tokens[0][0] != 'LPAREN' or tokens[-1][0] != 'RPAREN':
        raise SyntaxError("El bloque de instrucciones debe estar delimitado por paréntesis.")

    # Remover los paréntesis que delimitan el bloque
    inner_tokens = tokens[1:-1]

    # Inicializar una lista para almacenar las instrucciones del bloque
    instructions = []

    # Analizar cada token dentro del bloque
    while inner_tokens:
        # Encontrar la posición del primer token que indica el inicio de una instrucción
        start_index = next((i for i, token in enumerate(inner_tokens) if token[0] != 'LPAREN'), None)

        # Si no se encuentra ningún token que indique el inicio de una instrucción, el bloque está vacío
        if start_index is None:
            break

        # Encontrar la posición del primer token que indica el final de una instrucción
        end_index = next((i for i, token in enumerate(inner_tokens[start_index:]) if token[0] == 'RPAREN'), None)

        # Si no se encuentra ningún token que indique el final de una instrucción, hay un error de sintaxis
        if end_index is None:
            raise SyntaxError("Símbolo de paréntesis de cierre faltante.")

        # Extraer los tokens que representan una instrucción y eliminarlos del bloque
        instruction_tokens = inner_tokens[start_index:start_index + end_index + 1]
        inner_tokens = inner_tokens[start_index + end_index + 1:]

        # Analizar la instrucción y agregarla a la lista de instrucciones
        instruction = parse_instruction(instruction_tokens)
        instructions.append(instruction)

    # Devolver la lista de instrucciones del bloque
    return instructions

def parse_blocked_condition(tokens):
    # Comprobar que hay suficientes tokens para analizar la condición blocked?
    if len(tokens) != 2:
        raise SyntaxError("Condición 'blocked?' incompleta.")

    # Verificar el formato de la condición blocked?
    if tokens[0][0] != 'LPAREN' or tokens[1][0] != 'KEYWORD' or tokens[1][1] != 'blocked?':
        raise SyntaxError("Formato incorrecto de la condición 'blocked?'.")

    # Devolver una estructura de datos que represente la condición blocked?
    return {
        'type': 'blocked?'
    }

def parse_can_put_condition(tokens):
    # Comprobar que hay suficientes tokens para analizar la condición can-put?
    if len(tokens) != 4:
        raise SyntaxError("Condición 'can-put?' incompleta.")

    # Verificar el formato de la condición can-put?
    if tokens[0][0] != 'LPAREN' or tokens[1][0] != 'KEYWORD' or tokens[1][1] != 'can-put?':
        raise SyntaxError("Formato incorrecto de la condición 'can-put?'.")

    # Verificar que el tipo de objeto a colocar sea válido
    if tokens[2][0] != 'SYMBOL' or tokens[2][1] not in (':chips', ':balloons'):
        raise SyntaxError("Tipo de objeto no válido en la condición 'can-put?'.")

    # Verificar que el número sea un valor numérico
    if tokens[3][0] != 'NUMBER':
        raise SyntaxError("Valor numérico esperado en la condición 'can-put?'.")

    # Devolver una estructura de datos que represente la condición can-put?
    return {
        'type': 'can-put?',
        'object_type': tokens[2][1],
        'number': int(tokens[3][1])
    }

def parse_can_pick_condition(tokens):
    # Comprobar que hay suficientes tokens para analizar la condición can-pick?
    if len(tokens) != 4:
        raise SyntaxError("Condición 'can-pick?' incompleta.")

    # Verificar el formato de la condición can-pick?
    if tokens[0][0] != 'LPAREN' or tokens[1][0] != 'KEYWORD' or tokens[1][1] != 'can-pick?':
        raise SyntaxError("Formato incorrecto de la condición 'can-pick?'.")

    # Verificar que el tipo de objeto a recoger sea válido
    if tokens[2][0] != 'SYMBOL' or tokens[2][1] not in (':chips', ':balloons'):
        raise SyntaxError("Tipo de objeto no válido en la condición 'can-pick?'.")

    # Verificar que el número sea un valor numérico
    if tokens[3][0] != 'NUMBER':
        raise SyntaxError("Valor numérico esperado en la condición 'can-pick?'.")

    # Devolver una estructura de datos que represente la condición can-pick?
    return {
        'type': 'can-pick?',
        'object_type': tokens[2][1],
        'number': int(tokens[3][1])
    }

def parse_can_move_condition(tokens):
    # Comprobar que hay suficientes tokens para analizar la condición can-move?
    if len(tokens) != 3:
        raise SyntaxError("Condición 'can-move?' incompleta.")

    # Verificar el formato de la condición can-move?
    if tokens[0][0] != 'LPAREN' or tokens[1][0] != 'KEYWORD' or tokens[1][1] != 'can-move?':
        raise SyntaxError("Formato incorrecto de la condición 'can-move?'.")

    # Verificar que la dirección sea válida
    if tokens[2][0] != 'SYMBOL' or tokens[2][1] not in (':north', ':south', ':east', ':west'):
        raise SyntaxError("Dirección no válida en la condición 'can-move?'.")

    # Devolver una estructura de datos que represente la condición can-move?
    return {
        'type': 'can-move?',
        'direction': tokens[2][1]
    }

def parse_is_zero_condition(tokens):
    # Comprobar que hay suficientes tokens para analizar la condición isZero?
    if len(tokens) != 3:
        raise SyntaxError("Condición 'isZero?' incompleta.")

    # Verificar el formato de la condición isZero?
    if tokens[0][0] != 'LPAREN' or tokens[1][0] != 'KEYWORD' or tokens[1][1] != 'isZero?':
        raise SyntaxError("Formato incorrecto de la condición 'isZero?'.")

    # Verificar que el valor sea un número
    if tokens[2][0] != 'NUMBER':
        raise SyntaxError("Valor numérico esperado en la condición 'isZero?'.")

    # Devolver una estructura de datos que represente la condición isZero?
    return {
        'type': 'isZero?',
        'value': int(tokens[2][1])
    }

def parse_not_condition(tokens):
    # Comprobar que hay suficientes tokens para analizar la condición not
    if len(tokens) != 3:
        raise SyntaxError("Condición 'not' incompleta.")

    # Verificar el formato de la condición not
    if tokens[0][0] != 'LPAREN' or tokens[1][0] != 'KEYWORD' or tokens[1][1] != 'not':
        raise SyntaxError("Formato incorrecto de la condición 'not'.")

    # Analizar la subcondición
    subcondition = parse_condition(tokens[2:])

    # Devolver una estructura de datos que represente la condición not
    return {
        'type': 'not',
        'condition': subcondition
    }

def parse_condition(tokens):
    # Comprobar que hay suficientes tokens para analizar la condición
    if len(tokens) < 2:
        raise SyntaxError("Condición incompleta.")

    # Verificar el formato de la condición
    if tokens[0][0] != 'LPAREN' or tokens[-1][0] != 'RPAREN':
        raise SyntaxError("Símbolos de paréntesis faltantes en la condición.")

    # Analizar la condición basada en el tipo de condición
    if tokens[1][0] == 'KEYWORD':
        if tokens[1][1] == 'facing?':
            return parse_facing_condition(tokens)
        elif tokens[1][1] == 'blocked?':
            return parse_blocked_condition(tokens)
        elif tokens[1][1] == 'can-put?':
            return parse_can_put_condition(tokens)
        elif tokens[1][1] == 'can-pick?':
            return parse_can_pick_condition(tokens)
        elif tokens[1][1] == 'can-move?':
            return parse_can_move_condition(tokens)
        elif tokens[1][1] == 'isZero?':
            return parse_is_zero_condition(tokens)
        elif tokens[1][1] == 'not':
            return parse_not_condition(tokens)
        else:
            raise SyntaxError("Condición no válida.")
    else:
        raise SyntaxError("Condición no válida.")

def parse_facing_condition(tokens):
    # Comprobar que hay suficientes tokens para analizar la condición
    if len(tokens) != 3:
        raise SyntaxError("Condición 'facing?' incompleta.")

    # Verificar el formato de la condición 'facing?'
    if tokens[0][0] != 'LPAREN' or tokens[1][0] != 'KEYWORD':
        raise SyntaxError("Formato incorrecto de la condición 'facing?'.")
    if tokens[2][0] != 'SYMBOL' or tokens[2][1] not in (':north', ':south', ':east', ':west'):
        raise SyntaxError("Dirección de orientación no válida en la condición 'facing?'.")

    # Devolver una estructura de datos que represente la condición 'facing?'
    return {
        'type': 'facing?',
        'direction': tokens[2][1]
    }

def parse_if(tokens):
    # Comprobar que hay suficientes tokens para analizar la estructura if
    if len(tokens) < 4:
        raise SyntaxError("Estructura 'if' incompleta.")

    # Verificar el formato de la estructura if
    if tokens[0][0] != 'KEYWORD' or tokens[0][1] != 'if':
        raise SyntaxError("Se esperaba la palabra clave 'if'.")
    condition = parse_condition(tokens[1])
    if tokens[2][0] != 'LPAREN' or tokens[-1][0] != 'RPAREN':
        raise SyntaxError("Símbolos de paréntesis faltantes.")
    
    # Obtener los bloques de instrucciones para el caso verdadero y el caso falso
    true_block_tokens = []
    false_block_tokens = []
    true_block_started = False
    false_block_started = False

    for token in tokens[3:-1]:
        if token[0] == 'LPAREN':
            if true_block_started:
                true_block_tokens.append(token)
            elif false_block_started:
                false_block_tokens.append(token)
            else:
                raise SyntaxError("Símbolo de paréntesis inesperado.")
        elif token[0] == 'RPAREN':
            if true_block_started:
                true_block_tokens.append(token)
            elif false_block_started:
                false_block_tokens.append(token)
            else:
                raise SyntaxError("Símbolo de paréntesis inesperado.")
        elif token[0] == 'KEYWORD' and token[1] == 'if':
            raise SyntaxError("Las estructuras de control no están permitidas dentro de un bloque if.")
        elif token[0] == 'KEYWORD' and token[1] == 'else':
            if true_block_started:
                true_block_started = False
                false_block_started = True
            else:
                raise SyntaxError("Palabra clave 'else' inesperada.")
        else:
            if true_block_started:
                true_block_tokens.append(token)
            elif false_block_started:
                false_block_tokens.append(token)

    # Analizar los bloques de instrucciones para el caso verdadero y el caso falso
    true_block = parse_block(true_block_tokens)
    false_block = parse_block(false_block_tokens)

    # Devolver una estructura de datos que represente la estructura if
    return {
        'type': 'if',
        'condition': condition,
        'true_block': true_block,
        'false_block': false_block
    }

def parse_loop(tokens):
    # Comprobar que hay suficientes tokens para analizar la estructura loop
    if len(tokens) < 3:
        raise SyntaxError("Estructura 'loop' incompleta.")

    # Verificar el formato de la estructura loop
    if tokens[0][0] != 'KEYWORD' or tokens[0][1] != 'loop':
        raise SyntaxError("Se esperaba el comando 'loop'.")
    if tokens[1][0] != 'LPAREN' or tokens[-1][0] != 'RPAREN':
        raise SyntaxError("Símbolos de paréntesis faltantes.")

    # Obtener los tokens dentro del bloque de instrucciones del loop
    inner_tokens = tokens[2:-1]

    # Analizar el bloque de instrucciones del loop
    loop_block = parse_block(inner_tokens)

    # Devolver una estructura de datos que represente la estructura loop
    return {
        'type': 'loop',
        'block': loop_block
    }

def parse_repeat(tokens):
    # Comprobar que hay suficientes tokens para analizar la estructura repeat
    if len(tokens) < 4:
        raise SyntaxError("Estructura 'repeat' incompleta.")

    # Verificar el formato de la estructura repeat
    if tokens[0][0] != 'KEYWORD' or tokens[0][1] != 'repeat':
        raise SyntaxError("Se esperaba el comando 'repeat'.")
    if tokens[1][0] != 'NUMBER':
        raise SyntaxError("Se esperaba un número después de 'repeat'.")
    if tokens[2][0] != 'LPAREN' or tokens[-1][0] != 'RPAREN':
        raise SyntaxError("Símbolos de paréntesis faltantes.")

    # Obtener el número de repeticiones
    repetitions = int(tokens[1][1])

    # Obtener los tokens dentro del bloque de instrucciones del repeat
    inner_tokens = tokens[3:-1]

    # Analizar el bloque de instrucciones del repeat
    repeat_block = parse_block(inner_tokens)

    # Devolver una estructura de datos que represente la estructura repeat
    return {
        'type': 'repeat',
        'repetitions': repetitions,
        'block': repeat_block
    }

def parse_function_definition(tokens):
    # Comprobar que hay suficientes tokens para analizar la definición de función
    if len(tokens) < 5:
        raise SyntaxError("Definición de función incompleta.")

    # Verificar el formato de la definición de función
    if tokens[0][0] != 'KEYWORD' or tokens[0][1] != 'defun':
        raise SyntaxError("Se esperaba el comando 'defun'.")
    if tokens[1][0] != 'SYMBOL':
        raise SyntaxError("Se esperaba el nombre de la función después de 'defun'.")
    if tokens[2][0] != 'LPAREN':
        raise SyntaxError("Símbolo de paréntesis de apertura faltante.")
    if tokens[-2][0] != 'RPAREN' or tokens[-1][0] != 'RPAREN':
        raise SyntaxError("Símbolos de paréntesis de cierre faltantes.")

    # Obtener el nombre de la función
    function_name = tokens[1][1]

    # Obtener los parámetros de la función
    parameters = [token[1] for token in tokens[3:-2] if token[0] == 'SYMBOL']

    # Obtener los tokens dentro del bloque de instrucciones de la función
    inner_tokens = tokens[tokens.index(('LPAREN', '(')) + 1: tokens.index(('RPAREN', ')'))]

    # Analizar el bloque de instrucciones de la función
    function_block = parse_block(inner_tokens)

    # Devolver una estructura de datos que represente la definición de función
    return {
        'type': 'function_definition',
        'name': function_name,
        'parameters': parameters,
        'block': function_block
    }

# Función para analizar estructuras de control
def parse_control_structure(tokens):
    # Comprobar que hay suficientes tokens para analizar la estructura de control
    if not tokens:
        raise SyntaxError("Se esperaba una estructura de control, pero se encontró el final de la entrada.")

    # Obtener el tipo de estructura de control
    control_type = tokens[0][1]

    # Verificar y llamar a la función de análisis correspondiente según el tipo de estructura de control
    if control_type == 'if':
        return parse_if(tokens[1:])
    elif control_type == 'loop':
        return parse_loop(tokens[1:])
    elif control_type == 'repeat':
        return parse_repeat(tokens[1:])
    elif control_type == 'defun':
        return parse_function_definition(tokens[1:])
    else:
        raise SyntaxError(f"Estructura de control no válida: {control_type}")


# Función para analizar llamados a funciones

def parse_argument(tokens):
    # Verificar que hay suficientes tokens para analizar un argumento
    if len(tokens) < 1:
        raise SyntaxError("Argumento incompleto.")

    # Verificar el tipo del token y devolver el argumento
    if tokens[0][0] == 'NUMBER':
        return int(tokens[0][1]), tokens[1:]
    elif tokens[0][0] == 'SYMBOL':
        return tokens[0][1], tokens[1:]
    else:
        raise SyntaxError("Tipo de argumento no válido.")

def parse_function_call(tokens):
    # Comprobar que hay suficientes tokens para analizar la llamada a una función
    if len(tokens) < 2 or tokens[0][0] != 'LPAREN':
        raise SyntaxError("Llamada a función incompleta o incorrecta.")

    # Verificar que el primer token sea un paréntesis de apertura y el segundo sea el nombre de la función
    if tokens[0][0] != 'LPAREN' or tokens[1][0] != 'SYMBOL':
        raise SyntaxError("Formato incorrecto de la llamada a función.")

    # Obtener el nombre de la función
    function_name = tokens[1][1]

    # Obtener los argumentos de la función
    args_tokens = tokens[2:-1]
    args = []

    # Parsear los argumentos
    while args_tokens:
        arg, args_tokens = parse_argument(args_tokens)
        args.append(arg)

    # Verificar el cierre del paréntesis
    if tokens[-1][0] != 'RPAREN':
        raise SyntaxError("Falta el paréntesis de cierre en la llamada a función.")

    # Devolver una estructura de datos que represente la llamada a la función
    return {
        'type': 'function_call',
        'name': function_name,
        'args': args
    }



