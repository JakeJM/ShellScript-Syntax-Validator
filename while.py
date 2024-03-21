import ply.lex as lex
import ply.yacc as yacc

#Define lexer tokens
tokens = (
    'WHILE',
    'DO',
    'DONE',
    'LBRACKET',
    'RBRACKET',
    'ID',
    'DOLLAR',
    'NUMBER',
    'EQUALS',
    'NOTEQUALS',
    'LESSER',
    'GREATER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
)

# Regular expression rules for simple tokens
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_DOLLAR = r'\$'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

def t_WHILE(t):
    r'while'
    return t

def t_DONE(t):
    r'done'
    return t

def t_DO(t):
    r'do'
    return t

def t_EQUALS(t):
    r'-eq'
    return t

def t_NOTEQUALS(t):
    r'-ne'
    return t

def t_LESSER(t):
    r'-lt'
    return t

def t_GREATER(t):
    r'-gt'
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
def p_statement(p):
    '''statement : while_statement
                 | ID'''
    pass

def p_expression(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression EQUALS expression
                  | expression NOTEQUALS expression
                  | expression GREATER expression
                  | expression LESSER expression
                  | DOLLAR ID
                  | NUMBER'''

def p_while_statement(p):
    '''while_statement : WHILE LBRACKET expression RBRACKET DO statement DONE '''
    print("Valid while loop declaration")

def p_error(p):# Error rule for syntax errors
    if p:
        # Get the line number from the lexer
        line_number = lexer.lineno
        print(f"Syntax error at line {line_number}; Unexpected token '{p.value}'")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

if __name__=="__main__":
    print("Enter your code(type 'quit' to stop):")
    data=""
    while True:
        l=input()
        if(l.strip()=='quit'):
            break
        data+=l+'\n'
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok.type, tok.value, tok.lineno, tok.lexpos)
    
    try:
        parser.parse(data)
    except EOFError:
        pass

