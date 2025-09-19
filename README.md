
# Simple Algorithm for Password Brute-Force

## Bruteforce Password Cracker
This program implements a brute-force attack to find short passwords. It generates all possible combinations of a defined alphabet and measures the number of attempts needed to find the password, as well as the time taken by the attack.

## How to run the script
Clone the repository and enter the folder:

Bash

git clone https://github.com/tuusuario/simple-algorithm-for-breaking-passwords-controlled-brute-force.git
cd simple-algorithm-for-breaking-passwords-controlled-brute-force


## Run the Python script:

Bash

python bruteforce.py
You will see the following information in the terminal:

- Password found

- Number of attempts

- Execution time

At the end, a graph will be displayed illustrating how the execution time increases with the length of the password.

## Example output

- Testing passwords of length 1:
Found: a | Attempts: 1 | Time: 0.0001 seconds

- Testing passwords of length 2:
Found: ab | Attempts: 27 | Time: 0.0023 seconds

- Testing passwords of length 3:
Found: abc | Attempts: 703 | Time: 0.05 seconds

## Reflection
If the password has 8 or more characters and uses uppercase letters, numbers, and symbols, the number of possible combinations grows exponentially. A brute force attack could take years or even centuries, depending on the alphabet and its length. That's why long, complex passwords are much more secure.