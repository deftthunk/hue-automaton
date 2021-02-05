import ply.yacc as yacc
import ply.lex as lex
from config_lexer import *
import sys


def p_head(p):
    '''
    head        : IF expression THEN head END
                | IF expression THEN expr_list END
    '''
    p[0] = (p[2], p[4])


def p_expr_list(p):
    '''
    expr_list   : expr_list expression
                | expression
    '''
    try: p[0] = (p[1], p[2])
    except: p[0] = p[1]


def p_expression(p):
    '''
    expression  : OBJECT symbol rvalue
                | STATUS symbol rvalue
    '''
    p[0] = (p[1], p[2], p[3])


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


if __name__ == "__main__":
    lexer = lex.lex()
    parser = yacc.yacc()
    data = ""

    for line in sys.stdin:
        data += line
    
    ret = parser.parse(data)
    #ret = parser.parse(data, debug=1)
    print(ret)
