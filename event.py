from libhuematica import *


class Event:
    def __init__(self, name, code):
        self.name = name
        self.realcode = None
        self.pseudocode = None


    def Run(self):
        return exec(self.code)
        





def Convert_Pseudo_Code(e, d):
    def object_lookup(table, name):
        '''
        find the correct HUE device by doing a lookup in
        a hashmap of type -> {name : object}
        '''
        return d.obj_lookup[table][name]


    def decode_objects(token):
        decode = []
        obj = token.left
        parts = obj.split('.')
        ## ie. 'room', 'light', 'time'
        table = parts[0]
        print("table: ", parts[0])

        ## room, sensor, or light
        if len(parts) == 3:
            name = parts[1]
            feature = parts[2]
            
            hue_obj = object_lookup(table, name)
            print("real name: ", hue_obj.name)
            method = d.api_lookup[table][feature]
            print("method: ", method)
            new_token = '.'.join([hue_obj, method])
            print("new token: ", new_token)
            
             
        ## time or date
        elif len(parts) == 2:
            pass
        else:
            pass




    def format_code(e):
        '''
        turn the user-generated event files into real code by: 
        - removing non-Python syntax
        - correcting spacing issues
        - resolving user-generated global variables
        '''
        nonlocal indent_size
        nonlocal indent
        indent = " " * indent_size

        for token in e:
            if type(token) == tuple:
                format_code(token)
            elif isinstance(token, Expression):
                token = decode_objects(token)
                blurb_array.append(" ".join([token.left, token.op, token.right]))
                if isinstance(token, Assignment):
                    ## since this is a standalone expression, we need indenting and newline
                    blurb_array.insert(-1, indent)
                    blurb_array.append("\n")
                else:
                    blurb_array.append(":\n")
            elif token == "IF":
                blurb_array.append(indent)
                blurb_array.append("if ")
                #breakpoint()
            elif token == "THEN":
                indent_size += 4
                continue
            elif token == "END":
                indent_size -= 4
            elif token == "FLAG":
                '''artifically created a tuple in cases where user writes an single 
                assignemnt, as this results in no tuple being generated. this flag 
                gets dropped here and the tuple processed so that spacing lines up
                #lazyshortcut
                '''
                continue
            else:
                raise Exception("Found unexpected token")


    blurb = """"""
    blurb_array = []
    indent_size = 4
    indent = " "
    format_code(e)
    blurb = ''.join(blurb_array)
    
    return blurb




