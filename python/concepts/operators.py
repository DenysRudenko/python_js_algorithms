my_list = [1, 2, 3]

for num in range(3, 11, 3):
    print(num)

index_count = 0

for letter in "Example":
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count += 1


index_counter = 0
word = 'Example2'

for letter in word:
    print(word[index_counter])
    index_counter += 1

another_word = "Example3"

for item in enumerate(another_word):
    print(item)

for index, letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

my_list1 = [1, 2, 3, 4, 5]
my_list2 = ['a', 'b', 'c', 'd']

for item in zip(my_list1, my_list2):
    print(item)