numbers = []
for i in range(5):
    num = input(f'Enter number {i + 1}:')
    numbers.append(int(num))
num_string = ' '.join(map(str, numbers))
print('Numbers entered:', num_string)
smallest = min(numbers)
largest = max(numbers)
print(f'The smallest number given was {smallest}')
print(f'The largest number given was {largest}')
product = smallest * largest
print(f'The product of the two numbers extraccted was {product}')
