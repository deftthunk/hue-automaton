import ply.yacc as yacc
import ply.lex as lex
from event_lexer import *
from libhuematica import *
import sys, os
import os.path

def p_definition(p):
    '''
    definition  : definition head
                | head
    '''
    try: p[0] = (p[1], p[2])
    except: p[0] = p[1]


def p_head(p):
    '''
    head        : IF expression THEN head END
                | IF expression THEN expr_list END
                | IF expression THEN expr_list head END
    '''
    try: p[0] = (p[1], p[2], p[3], ("FLAG", p[4]), p[5], p[6])
    except: p[0] = (p[1], p[2], p[3], p[4], p[5])


def p_expr_list(p):
    '''
    expr_list   : expr_list expression
                | expression
    '''
    try: p[0] = (p[1], p[2])
    except: p[0] = ("FLAG", p[1])


def p_expression(p):
    '''
    expression  : OBJECT symbol rvalue
                | STATUS symbol rvalue
    '''
    if p[-1] == "IF":
        if p[2] == "=":
            p[2] = "=="
        p[0] = Test(p[1], p[2], p[3])
    else:
        p[0] = Assignment(p[1], p[2], p[3])
    

def p_symbol(p):
    '''
    symbol      : EQUAL
                | NOTEQUAL
    '''
    p[0] = p[1]


def p_rvalue(p):
    '''
    rvalue      : VALUE
                | LIST
    '''
    if isinstance(p[1], bool):
        p[0] = p[1]
    elif isinstance(p[1], int):
        p[0] = int(p[1])
    elif isinstance(p[1], float):
        p[0] = float(p[1])
    elif isinstance(p[1], list):
        p[0] = list(p[1])
    else:
        p[0] = p[1]


def p_error(token):
    if token is not None:
        print ("Line %s, illegal token %s" % (token.lineno, token.value))
    else:
        print('Unexpected end of input') 


def Parse(files=[]):
    lexer = lex.lex()
    parser = yacc.yacc()
    events = {}

    if files == []:
        for f in os.listdir("events"):
            path = os.path.join("events", f)
            if os.path.isfile(path):
                files.append(path)
            
    for event in files:
        with open(event, "r") as fh:
            output = fh.readlines()
            script = ''.join(output)
            events[event] = parser.parse(script)
            #events.append(parser.parse(script))
   
    return events



if __name__ == "__main__":
    lexer = lex.lex()
    parser = yacc.yacc()
    data = ""

    for line in sys.stdin:
        data += line
    
    ret = parser.parse(data)
    #print(dir(parser))
    #ret = parser.parse(data, debug=1)
    print(ret)

