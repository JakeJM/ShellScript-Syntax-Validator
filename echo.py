import ply.lex as lex
import ply.yacc as yacc

#Define lexer tokens
tokens = (
    'ECHO',
    'ID',
    'DOLLAR',
    'NUMBER',
    'PAR', 
)

# Regular expression rules for simple tokens
#t_ECHO = r'echo'
#t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_PAR = r'\''
t_DOLLAR = r'\$'

def t_ECHO(t):
    r'echo'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
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


def p_echo_statement(p):
    '''echo_statement : ECHO statement '''
    printf("Valid echo statement")


def p_statement(p):
    '''statement : PAR expression PAR
                 | expression '''
    pass

def p_expression(p):
    '''expression : ID
                  | DOLLAR ID
                  | NUMBER
                  | expression ID
                  | expression DOLLAR ID 
                  | expression NUMBER'''


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

