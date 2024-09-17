def add_number (num1, num2):
    return num1 + num2
#use of integer to convert a string "input" into an integer so that the result wont concatinate, this will prevent you from getting concatinated values intead of the sum. We can use float instead of int to handle decimal places 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#add_number function
results = add_number(num1, num2)
print("The sum is: ", results)    


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


check_the_number = int(input("Enter the number: " ))
print( "Is the number even? ", is_even(check_the_number))    


def reverse_string (text):

# reversing the text using slicing notation. Take the string from start to end in reverse order.
    return text [:: -1]

input_text = input("Enter the string to reverse: ")
print ("Reversed string: ", reverse_string(input_text))



def count_vowels (text):

    vowels = "aeiouAEIOU"

    count = 0

    # Go through each character in the input text.
    for nature in text:

        # Checking if the chacter is a vowel.
        if nature in vowels:
            count += 1

            # Return the total count of vowels.
    return count 

input_text = input("Enter a name to count vowels: ")
print("No of vowels: ", count_vowels(input_text))        



def calculate_factorial(n):
    if n < 0:
        raise ValueError("Input should be a non-negative no.")
    factorial = 1

    for i in range(2, n+1):

        factorial *= i
    return factorial

print(calculate_factorial(0))


def apply_decorator(func):
    def wrapper():
        print("Decorate applied")
        return func()
    return wrapper
def decorator_func (func):
    return apply_decorator(func)

def output_function() :
    print("Original function has been called")


apply_decorator = decorator_func (output_function)
apply_decorator()


def sort_by_age(persons):
    return sorted(persons, key=lambda person: person[1])

def get_persons():
    persons =[]
    while True :
        name = input("Enter your name(or type 'done' to finish): ")
        if name.lower() == "done":
            break
        try:
            age = int(input("Enter your age: "))

        except ValueError:
            print('Invalid age please enter a number')
            continue

        # Add name and age as a tuple to the list.
        persons.append((name,age))
    return persons

person_list = get_persons()
sorted_people = sort_by_age(person_list)
print(sorted_people)


def merge_dicts (dict1, dict2):
    merged_dict = dict1.copy ()

    for key, value in dict2.items():
        if key in merged_dict:
            # Sum the values if the key already exists.
            merged_dict[key] += value
            # Add the key-value pair if the key does not exist.
        else:
            merged_dict[key] = value 

    return merged_dict

def input_dict(prompt):
    result = {}
    print(prompt)

    while True:
        key = input ("Enter the key(or type 'done' when you finished): ")
        if key.lower() == "done":
            break
        try:
            value = int(input("Enter the value: "))
        except ValueError:
            print("Invalid value please enter a number")
            continue
        result [key] = value
    return(result)

dict1 = input_dict("Enter the key-value pair for the first dictionary")
dict2 = input_dict("Enter the key-value pair for the second dictionary")


merged = merge_dicts(dict1, dict2)
print("Merged dictionary: ", merged)


def car(make, model, year):
    # Function to display the car info.
    def display_info():
        # Print the car in this format.
        print(f"Car Information: {year} {make} {model}")

        # Calling the display_info to show the car details.

    display_info()

make = input("Enter the make of the car: ")
model = input("Enter the model of the car: ")
year = input("Enter the year of the car: ")

car(make, model, year)


