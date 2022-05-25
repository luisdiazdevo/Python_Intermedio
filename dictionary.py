def run():
    import math
    squares = { i : i**3 for i in range (1 , 101) if i % 3 != 0}
    raiz = { i: math.sqrt(i) for i in range (1 ,1001 ) }
    
    print(raiz)


if __name__ == "__main__":
    run()