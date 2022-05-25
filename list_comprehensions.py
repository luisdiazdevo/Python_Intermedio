from sqlite3 import SQLITE_UPDATE


def run():
    squares = [i**2 for i in range (1,1001) if i % 4 != 0 and i % 6 != 0 and i % 9 != 0] 
    
    #for i in range (1, 101):
        #if i % 3 != 0:
            #squares.append(i**2)
            
    
        
    print(squares)

if __name__ == "__main__":
    run()