# Password Strength Checker

A simple Python script to check the strength of a given password. It evaluates the password based on several criteria, including length, uppercase letters, lowercase letters, numbers, and special symbols.

## Features
- **Checks password length**: Must be at least 8 characters.
- **Verifies uppercase letters**: At least one uppercase letter.
- **Checks for lowercase letters**: At least one lowercase letter.
- **Validates presence of numbers**: At least one digit.
- **Checks for special characters**: Supports common special characters like `!@#$%^&*()`.
- **Strength categorization**: Provides feedback based on the score.

## Categories
- **Weak**: Score 2 or below 🚫
- **Fair**: Score 3 or 4 💡
- **Strong**: Score 5 ✅

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/SltnBM/password-checker.git
    cd password-checker
    ```

## Usage

1. Run the script using Python:
    ```bash
    python passwordChecker.py
    ```

2. Enter a password when prompted, and the script will evaluate its strength.

## Example

```bash
Enter the password to check: Example123!
Password Strength: Strong ✅ (Score: 5/5)
