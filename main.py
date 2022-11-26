# write your code here
my_name = "badriya"
my_age = 21
print(f"My name is {my_name} and I am {my_age} years old.")
first_number = 17
second_number = 9
operation = input("enter the operation")
if operation == "+": 
    print(first_number + second_number )
elif operation == "-":
    print(first_number - second_number)
elif operation == "*":
    print(first_number*second_number)
elif operation == "/":
    print(first_number/second_number)
else:
    print("not valid")
ask_numb = input("Enter a number from 1 to 12: ")
ask_noun = input("Enter a noun (plural): ")
ask_name = input("Enter a name: ")
choose_sentence = input("Enter a sentence: ")
ask_verb = input("Enter a verb: ")
print(f"It was {ask_numb} o'clock when I heard a knock at the door. I opened the door and there was a box full of {ask_noun} with a note saying From Mr. {ask_name}. Just as I closed the door I heard a scream {choose_sentence}. I froze in place and all I could do was {ask_verb}.")
