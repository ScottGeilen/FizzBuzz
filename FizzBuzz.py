#! /usr/bin/python3

# Local variable fizzbuzz cycles through until 100 is met
for fizzbuzz in range(101):

    # Number divisible by 15? Print 'FizzBuzz'
    if fizzbuzz % 15 == 0:
        print('FizzBuzz')
        continue

    # Number divisible by 3? Print 'Fizz'
    if fizzbuzz % 3 == 0:
        print('Fizz')
        continue
    
    # Number divisible by 5? Print 'Buzz'
    elif fizzbuzz % 5 == 0:
        print('Buzz')
        continue
    
    # Print the numbers within range(100)
    print(fizzbuzz)