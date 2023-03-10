from functools import wraps
import time 

class Repeater():
    
    def __call__(self,func):
        @wraps(func)
        def wrapper(*args):
            #print(args)
            iter = 0
            index = 0
            
            for arg in args:
                if type(arg) == int:
                    iter = arg
                    index = args.index(arg)
                    break
            args = list(args)
            for i in range(iter,1,-1):
                args[index] = i
                func(*args,)
                time.sleep(2)

        return wrapper


