def verify_card_number(card_number):
    # Initialize sum of odd digits to 0
    sum_of_odd_digits = 0
    
    # Reverse the card number
    card_number_reversed = card_number[::-1]
    
    # Extract odd-positioned digits
    odd_digits = card_number_reversed[::2]

    # Calculate sum of odd digits
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    # Initialize sum of even digits to 0
    sum_of_even_digits = 0
    
    # Extract even-positioned digits
    even_digits = card_number_reversed[1::2]
    
    # Calculate sum of even digits
    for digit in even_digits:
        # Double the digit
        number = int(digit) * 2
        
        # If the result is greater than or equal to 10, adjust the sum
        if number >= 10:
            number = (number // 10) + (number % 10)
        
        # Add the adjusted number to the sum of even digits
        sum_of_even_digits += number
    
    # Calculate the total sum
    total = sum_of_odd_digits + sum_of_even_digits
    
    # Print the total sum (for debugging purposes)
    print(total)
    
    # Check if the total sum is divisible by 10
    return total % 10 == 0

def main():
    # Example credit card number
    card_number = '4111-1111-4555-1111'
    
    # Remove hyphens and spaces from the card number
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    # Verify the validity of the card number
    if verify_card_number(translated_card_number):
        # If valid, print "VALID!"
        print('VALID!')
    else:
        # If invalid, print "INVALID!"
        print('INVALID!')

# Entry point of the script
main()
