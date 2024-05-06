# Variable Keyword arguments

def keyword_args(**kwargs):
    
    # kwargs is of `dict` datatype
    for k, v in kwargs.items():
        print(k, v)

keyword_args(a=10, b='asd')
