print('\nArray of numbers separated by spaces')
array = str(input('> '))
array = array.split(' ')
array = [int(n) for n in array]

largest = 0
secondLargest = 0

for i in array:
    if i > largest:
        secondLargest = largest
        largest = i
    elif i > secondLargest:
        secondLargest = i

print('Largest', str(largest))
print('Second Largest', str(secondLargest))
