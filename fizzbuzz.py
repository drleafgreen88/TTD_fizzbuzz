def fizzbuzz(number):
    #figure out whether a number is divisible by three or five
    if number % 5 == 0 and number % 3 == 0:
        return "fizzbuzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return number
