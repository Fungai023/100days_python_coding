from traceback import print_tb

programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

for key in programming_dictionary:
    print(key)

for key in programming_dictionary:
    print(programming_dictionary[key])

my_dict = {}
my_dict["Apples"] =  5
print(my_dict)

# fastest way to create a dictionary and assigning data to it
my_farm =  dict(sheep = 7 , cows = 5 , dogs= 20 , lamb = 34)
print(len(my_farm))
print(my_farm)

