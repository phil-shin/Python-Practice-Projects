#takes integer input and run through collatz algorithm to reduce to 1
def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2  == 1:
        return 3*number+1
print('Please enter a number:')
try:
    number = int(input())
except ValueError:
    print('Entered value must be an integer')
    print('Please enter an integer number')
    number = int(input())
while number != 1:
    number=collatz(number)
    print(number)
