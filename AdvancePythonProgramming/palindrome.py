def is_palindrome(number):
    return str(number) == str(number)[::-1]

def find_previous_palindrome(starting_number):
    number = starting_number - 1

    while not is_palindrome(number):
        number -= 1

    return number

specified_number = int(input("Enter a number: "))
previous_palindrome = find_previous_palindrome(specified_number)
print(f"The previous palindrome of {specified_number} is: {previous_palindrome}")
