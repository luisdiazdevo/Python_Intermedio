from functools import reduce


def run ():
    from functools import reduce
    my_list = [2, 2, 2, 2, 2]
    resultado = reduce(lambda a, b : a*b, my_list)
    print(resultado) 
        

if __name__ == "__main__":
    run()