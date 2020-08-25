def fizzbuzz(n):

    if n % 15 == 0:
        return("FizzBuzz")
    
    else:
        if n % 3 == 0:
            return("Buzz")
        
        elif n % 5 == 0:
            return("Fizz")

        else:
            return n

        
        