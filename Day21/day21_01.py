# Variable positional arguments

def pos_args(*args):
    
    # 'args' is of tuple data type
    for arg in args:
        print(arg)

pos_args(1,2,3)
