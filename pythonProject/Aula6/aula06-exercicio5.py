for num in range(2,2001):
    primo = True

    for divisor in range(2,num):
        if num % divisor == 0:
            primo = False
            break
    if primo:
        print(num)