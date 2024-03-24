# Credit-Card-Number-Verifier
 Luhn algorithm

This Python script (`verify_card_number.py`) provides functionality to verify the validity of credit card numbers using the Luhn algorithm. The Luhn algorithm, also known as the modulus 10 or mod 10 algorithm, is a simple checksum formula used to validate a variety of identification numbers, including credit card numbers.

## How to Use

1. **Install Python:** Ensure you have Python installed on your system. If not, you can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository:** Clone this repository to your local machine using Git:

   ```
   git clone https://github.com/your_username/your_repository.git
   ```

3. **Navigate to the Directory:** Move into the directory containing the script.

   ```
   cd your_repository
   ```

4. **Run the Script:** Execute the script by running the following command:

   ```
   python verify_card_number.py
   ```

5. **Input Card Number:** Input the credit card number when prompted.

6. **Output:** The script will output whether the provided credit card number is valid or invalid.

## Algorithm Explanation

The script employs the Luhn algorithm to verify the validity of a credit card number. Here's a brief explanation of the algorithm used:

1. Reverse the credit card number.
2. Separate the digits of the reversed number into two groups: odd-positioned digits and even-positioned digits.
3. Sum up the digits in the odd-positioned group.
4. Double the digits in the even-positioned group. If any resulting number is greater than or equal to 10, sum the digits of that number.
5. Add the sums obtained from steps 3 and 4.
6. If the total sum modulo 10 equals 0, the credit card number is valid; otherwise, it is invalid.

## Example

Suppose you have a credit card number `4111-1111-4555-1111`. The script removes any hyphens or spaces from the input, resulting in `4111111145551111`. Upon running the script, it verifies the validity of this credit card number using the Luhn algorithm and outputs either "VALID!" or "INVALID!" based on the result.

## Note

- Ensure that the provided credit card number is valid and has the correct format. The script does not perform checks for invalid formats or alphabetic characters.
- This script serves for educational purposes and may require further customization or validation for production use.
