def triangle(a):
    try:
        a = int(a)
        for num_of_stars in range(a + 1):
            num_of_spaces = abs(a - num_of_stars)
            print(" " * num_of_spaces + "*" * (num_of_stars * 2 + 1))
    except:
        print("error, wrong input value type")
