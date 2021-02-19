from ply import lex
import sys

tokens = (
    "EQUAL",
    "NOTEQUAL",
    "VALUE",
    "LIST",
    "OBJECT",
    "COMMAND",
)

reserved = {
    'IF'        : 'IF',
    'THEN'      : 'THEN',
    'ELSE'      : 'ELSE',
    'END'       : 'END',
    'STATUS'    : 'STATUS'
}

t_ignore = " \t"

t_EQUAL = r"="
t_NOTEQUAL = r"!="
t_LIST = r"\[[^]]+\]"

tokens = list(tokens) + list(reserved.values())

def t_COMMAND(t):
    r'[A-Z]+'
    t.type = reserved.get(t.value,'COMMAND')    # Check for reserved words
    return t

def t_OBJECT(t):
    r"([0-9A-Za-z_\-]+\.)+[0-9A-Za-z_-]+"
    return t

def t_VALUE(t):
    r"[0-9a-z:_\-\.]+"
    return t

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)




if __name__ == "__main__":
    lexer = lex.lex()
    data = ""
    
    for line in sys.stdin:
        data += line

    lexer.input(data)
      
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
