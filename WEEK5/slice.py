1)SYNTAX
my_list = [num for num in range (1,6)]
print(my_list)
print([True,False,"1"])

2)CONSTUCTOR
my_list = list(["Lists", "are", "useful!"])
print(my_list)

3)COMPREHENSIVE
my_list = [num for num in range (1,6)]
print(my_list)
print([True,False,"1"])

4)INDEXING SINGLE ELEMENTS
my_list = [num for num in range (1,6)]
print(my_list)

element = my_list[2]space_movies = ['Interstellar', 'Gravity', 'The Martian', 'Apollo 13', 'Star Wars']
print(space_movies)

space_movies.remove('Gravity')
print(space_movies)
print(element)

5)INDEXING PORTIONS OF THE LIST
my_list = [num for num in range (1,6)]
print(my_list)

element = my_list[2]
my_list = [num for num in range (1,6)]
my_list[start:end]

my_list = [1, 5, 10, 15, 20, 25, 30, 35, 40]
my_new_list = [2:5]

print(my_new_list)


6)NEGATIVE INDEXING
my_list = [num for num in range (1,6)]

last_element = my_list[-1]
print(last_element)


7)OUT OF RANGE INDEX VALUES
my_list = [num for num in range (1,6)]

try:
    element = my_list[10]
except IndexError:
    print("Index is out of range!")


8)THE APPEND() METHOD
my_list = [12, 19, 26, 23]
my_list.append(30)
print(my_list)


9)THE EXTEND(() OF METHOD
python_datatypes = ["lists"]
python_datatypes.extend(["tuples", "sets"])
print(python_datatypes)


10)MODIFYING A SINGLE ELEMENTS
blue_shades = ['navy', 'sky blue', 'saphire', 'powder blue', 'teal', 'turquoise']
blue_shades[2] = 'sapphire'

print(blue_shades)


11)MODIFYING MULTIPLE ELEMENTS
blue_shades = ['navy', 'sky blue', 'sapphire', 'powder blue', 'teal', 'turquoise']
blue_shades[0:2] = ['denim', 'aqua']

print(blue_shades)


12)DIFFERENT NUMBER OF ELEMENTS THAT THE SPECIFIED RANGE
blue_shades = ['navy', 'sky blue', 'sapphire', 'powder blue', 'teal', 'turquoise']
blue_shades[0:1] = ['denim', 'aqua']
print(blue_shades)

blue_shades = ['navy', 'sky blue', 'sapphire', 'powder blue', 'teal', 'turquoise']
blue_shades[0:4] = ['denim', 'aqua']
print(blue_shades)


13)REASSINING THE LISTblue_shades 
['navy', 'sky blue', 'sapphire', 'powder blue', 'teal', 'turquoise']

blue_shades = ['cobalt', 'azure', 'ice blue']
print(blue_shades)


14)DELETING A SINGLE ELEMENT
space_movies = ['Interstellar', 'Gravity', 'The Martian', 'Apollo 13', 'Star Wars']
print(space_movies)

del space_movies[2]
print(space_movies)


15)DELETING MULTIPLE ELEMENTS
space_movies = ['Interstellar', 'Gravity', 'The Martian', 'Apollo 13', 'Star Wars']

del space_movies[1:3]
print(space_movies)


16)REMOVING BY VALUES
space_movies = ['Interstellar', 'Gravity', 'The Martian', 'Apollo 13', 'Star Wars']
print(space_movies)


17)CLEARING THE ENTIRE LIST
space_movies = ['Interstellar', 'Gravity', 'The Martian', 'Apollo 13', 'Star Wars']
space_movies.clear()
print(space_movies)


18)THE POP() METHOD
space_movies = ['Interstellar', 'Gravity', 'The Martian', 'Apollo 13', 'Star Wars']

removed_movie = space_movies.pop(2)
print("The removed movie is = " + removed_movie)
print(space_movies)


19)SYNTAX
my_list = [1, 5, 10, 15, 20, 25, 30]
print(my_list[0:2])

my_list = [1, 5, 10, 15, 20, 25, 30]

my_list[0:2] = 50, 55
print(my_list)


20)THE STEP PARAMETER
my_list = [1, 5, 10, 15, 20, 25, 30]

print(my_list[1:5:2])

space_movies.remove('Gravity')
print(space_movies) 


21)SLICING FROM THE BEGINNING
my_list = [1, 5, 10, 15, 20, 25, 30]

slice_list_from_start = my_list[:4]
print(slice_list_from_start)


22)SLICING FROM A  SPECIFIC INDEX TILL THE ENDmy_list = [1, 5, 10, 15, 20, 25, 30]

slice_list_till_end = my_list[4:]
print(slice_list_till_end)


23)NEGATIVE SLICING
my_list = [1, 5, 10, 15, 20, 25, 30]

last_three_elements = my_list[-3:]
print("Last three elements:", last_three_elements)

my_list = [1, 5, 10, 15, 20, 25, 30]

skip_every_second_from_end = my_list[-1:-6:-2]
print(skip_every_second_from_end)

My_list = [1, 5, 10, 15, 20, 25, 30]

reversed_list = my_list[::-1]
print(reversed_list)


24)EXPRESSION
numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]

print(squares)


25)CONDITION
numbers = [1, 2, 3, 4, 5]
odd_numbers = [num for num in numbers if num % 2 != 0]

print(odd_numbers)

words = ["hoodie", "rivers", "cat", "monitor", "bag", "cup"]
short_words = [word for word in words if len(word) <= 5]

print(short_words)

26)ASSIGNMENT TO MULTIPLE VARIABLES
numbers = [1, 2, 3, 4, 5]
pairs = [(num, num * 2) for num in numbers]

27)TRANSFORMING ELEMENTS
songs = ['Neon Lights', 'Pieces', 'Everything']
uppercase_songs = [song.upper() for song in songs]

print(uppercase_songs)
