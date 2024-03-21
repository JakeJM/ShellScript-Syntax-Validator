import ply.lex as lex
import ply.yacc as yacc

# Define lexer tokens
tokens = (
    'DECLARE',
    'ASSOC',
    'LPAREN',
    'RPAREN',
    'EQUALS',
    'ID',
    'NUMBER',
    'COMMA',
    'LBRACKET',
    'RBRACKET',
)

# Regular expression rules for simple tokens
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'='
t_COMMA = r','
t_LBRACKET = r'\['
t_RBRACKET = r'\]'

def t_DECLARE(t):
    r'declare'
    return t

def t_ASSOC(t):
    r'\-A'
    return t

# A regular expression rule for numbers
def t_NUMBER(t):
    r'\d+'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Building the lexer
lexer = lex.lex()

# Parsing rules
def p_array_initialize(p):
    '''array_initialize : DECLARE ASSOC ID EQUALS LPAREN array_elements RPAREN'''
    print("Valid 2D Array Initialization")

def p_array_elements(p):
    '''array_elements : array_assignment
                      | array_elements array_assignment'''

def p_array_assignment(p):
    '''array_assignment : LBRACKET array_index RBRACKET EQUALS value'''

def p_array_index(p):
    '''array_index : NUMBER COMMA NUMBER'''

def p_value(p):
    '''value : ID
             | NUMBER'''

# Error rule for syntax errors
def p_error(p):
    if p:
        # Get the line number from the lexer
        line_number = lexer.lineno
        print(f"Syntax error at line {line_number}; Unexpected token '{p.value}'")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

if __name__ == "__main__":
    print("Enter your code (type 'quit' to stop):")
    data = ""
    while True:
        l = input()
        if l.strip() == 'quit':
            break
        data += l + '\n'

    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok.type, tok.value, tok.lineno, tok.lexpos)

    try:
        parser.parse(data)
    except EOFError:
        pass

