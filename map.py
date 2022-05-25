def run ():
    my_list = [1, 2, 3, 4, 5]
    new_list = list(map(lambda x : x**2, my_list))

    print(new_list)


if __name__ == "__main__":
    run()