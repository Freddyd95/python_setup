"""
arb_args - Takes in any number of arguments and prints them one at a time.

inner_func - Takes in two integers. Two nested functions should perform separate, distinct math operations using the integers. The result of both nested functions should then be added together and printed.

lunch_lady - Takes in two strings: a student's name and their lunch preference. The function should print both strings. If a lunch preference is not given, "Mystery Meat" should be printed instead.

sum_n_product - Accepts two integers and returns both the sum and the product.

alias_arb_args - Should be arb_args but assigned an alias. Remember, variables can hold functions in Python just like they can in JS. Alternatively, you can call a function from inside another function.

arb_mean - Accepts any number of integers and prints their average.

arb_longest_string - Accepts any number of strings and returns the longest one.

"""
def arb_args(*args):
    for arg in args:
        print (args)

# arb_args(1, "string", False, ["a", "b"])

def inner_func(x, y):
    def add_five(a):
        return a + 5
    
    def sub_two(b):
        return b -2 
    
    print(add_five(x) + sub_two(y))

# inner_func(10, 23)

def lunch_lady(name, preference="Mystery Meat"):
    print(f"{name} is eating {preference} for lunch.")

# lunch_lady('Billybob', "Pizza")

def sum_n_product(x, y):
    return x+y, x*y

#sum_result, product_result = sum_n_product(2, 3)
#print(sum_result)
#print(product_result)

alias_arb_args = arb_args

#alias_arb_args("string", 1, True)

def arb_mean(*args):
    total = 0
    for arg in args:
        total += arg
    print(total/len(args))

#arb_mean(0, 10, 0, 0, 0, 20)

def arb_longest_string(*args):
    longest = ""
    for arg in args:
        if len(arg) > len(longest):
            longest = arg
    return longest

#print(arb_longest_string("a", "ab", "superultralongstring", "a", "test"))