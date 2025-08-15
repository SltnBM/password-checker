# Password Strength Checker
A simple Python script to check the strength of a given password. It evaluates the password based on several criteria, including length, uppercase letters, lowercase letters, numbers, and special symbols.

## Features
- **Checks password length**: Must be at least 8 characters.
- **Verifies uppercase letters**: At least one uppercase letter.
- **Checks for lowercase letters**: At least one lowercase letter.
- **Validates presence of numbers**: At least one digit.
- **Checks for special characters**: Supports common special characters like `!@#$%^&*()`.
- **Strength categorization**: Provides feedback based on the score.

## Requirements
1. Python 3.6+

## How to Use
1. Clone the repository
    ```bash
    git clone https://github.com/SltnBM/password-checker.git
    ```
2. Navigate to the project directory
    ```bash
    cd password-checker
    ```
3. Run the script
    ```bash
    python passwordChecker.py
    ```
>Enter a password when prompted, and the script will evaluate its strength.

## Example
```bash
Enter the password to check: MyPassword123!
Password Strength: Strong ✅ (Score: 5/5)
```

## Categories
- **Weak**: Score 2 or below
- **Fair**: Score 3 or 4
- **Strong**: Score 5