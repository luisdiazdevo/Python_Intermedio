def run():
    palindromo = lambda string: string == string == string[::-1]

    print(palindromo("Luis"))
if __name__ == "__main__":
    run()