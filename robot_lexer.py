
import tokenize
from io import BytesIO

# Definición de tokens
keywords = {'defvar', '=', 'move', 'skip', 'turn', 'face', 'put', 'pick', 
            'move-dir', 'run-dirs', 'move-face', 'null', 'if', 'loop', 
            'repeat', 'defun', 'north', 'south', 'east', 'west', 'chips', 
            'balloons', 'front', 'right', 'left', 'back', 'isZero', 'not'}

constants = {'Dim', 'myXpos', 'myYpos', 'myChips', 'myBalloons', 
             'balloonsHere', 'ChipsHere', 'Spaces'}

# Función para tokenizar la entrada
def tokenize_input(input_str):
    tokens = []
    for tok in tokenize.tokenize(BytesIO(input_str.encode('utf-8')).readline):
        token_type, token_value, _, _, _ = tok
        if token_type == tokenize.NAME:
            if token_value in keywords:
                tokens.append((token_value, 'KEYWORD'))
            elif token_value in constants:
                tokens.append((token_value, 'CONSTANT'))
            else:
                tokens.append((token_value, 'IDENTIFIER'))
        elif token_type == tokenize.NUMBER:
            tokens.append((token_value, 'NUMBER'))
        elif token_type == tokenize.OP and token_value in ['(', ')', '?']:
            tokens.append((token_value, 'SYMBOL'))
    return tokens

# Ejemplo de uso
input_str = """
(defun funcName (p1 p2 p3)
  (if (= 1 2)
    (move 10)
    (turn :left)))
"""

tokens = tokenize_input(input_str)
for token, token_type in tokens:
    print(f"{token}: {token_type}")