### Simple Types and built in fuctions

print("bacon")

rock = 12
stone = 7

sky=rock%stone

tree = range

rock = float(rock)
print(type(str(rock)))

# type()
# print()
# range()
# int()
# str()
# float()
# len()

### Dicts and Lists

## Simple list example

mylist = ['hello', 1, 17]
print(mylist[1])

# 1. Define a list with 1 string, 1 int and 1 float
canoe = ['bear', 123, 6.34]
# 2. print the 3rd element of your list
print(canoe[2])
# 3. Define a dict with 2 key pairs.
boat = {"pencil": "strawberry","pen": 89,"Dallas": "Cowboys"}
print(boat)
# 4. Define a emply list
cow = []
print(cow)
# 5. Define a emply Dict
dog = {}
print(dog)
# 6. Reverse the order of the list (use google after 5 mins of trying)
canoe = ['bear', 123, 6.34]
canoe.reverse()
print(canoe)
print(canoe[:-1])

canoe.sort(reverse=True)

# 6.1 Use list comprehension for the following
numlist = list(range(10))
##6.1a output only the first 3 elements of numlist
numlist[0:3]
##6.1b output only the last 3 elements of numlist
numlist[7:10]
##6.1c output every other element of numlist
numlist[::2]
##6.1d output numlist backwards
numlist[::-1]
##6.2 Loop through numlist and print every element
for element in numlist:
    print(element)
# 7. Combine two dicts into one.
spaceman = {"comet": "fast", "star": 7.90, "peanutbutter": "chocolate"}
print(spaceman)
shuttle = {"fuel": "liquid_oxygen", "sheild": "ceramics", "loading_bay": "doors"}
print(shuttle)
rocket = {**shuttle, **spaceman}
print(rocket)

tron = {"dict": {"fuel": "liquid_oxygen", "sheild": "ceramics", "loading_bay": "doors"}}

# 7.1 print the value for key 'fuel' of the shuttle dict
shuttle["fuel"]
# 7.2 Loop through all element of the shuttle dict and print the keys and values
for key, value in shuttle.items():
    print(key, value)

for key in shuttle:
    print(key, shuttle[key])
# 7.3 Use help to find a built in fuction for dicts that prints all the keys. hint help(shuttle)
rocket.keys()

# 8. Create a tuple, 10 min research why they are different then lists
tup = (3,5,1)
popcorn = [3,5,1]
popcorn.append(4)  ## works
tup.append(4)    ## doens't work tuples are immutable