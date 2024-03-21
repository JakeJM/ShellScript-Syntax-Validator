import ply.lex as lex
import ply.yacc as yacc

#Define lexer tokens
tokens = (
    'FOR',
    'IN',
    'RANGE',
    'DO',
    'DONE',
    'LBRACE',
    'RBRACE',
    'ID',
    'NUMBER',
)

# Regular expression rules for simple tokens
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_RANGE = r'\.\.'
t_LBRACE = r'\{'
t_RBRACE = r'\}'

def t_FOR(t):
    r'for'
    return t

def t_IN(t):
    r'in'
    return t

def t_DONE(t):
    r'done'
    return t

def t_DO(t):
    r'do'
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
    '''statement : for_statement
                 | ID'''
    pass

def p_for_statement(p):
    '''for_statement : FOR ID IN range_or_list DO statement DONE '''
    print("Valid for loop declaration")

def p_range_or_list(p):
    '''range_or_list : values
                     | range
                     | list'''

def p_range(p):
    '''range : LBRACE NUMBER RANGE NUMBER RBRACE'''

def p_list(p):
    '''list : LBRACE values RBRACE'''

def p_values(p):
    '''values : value
              | values value'''

def p_value(p):
    '''value : ID
             | NUMBER'''

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

