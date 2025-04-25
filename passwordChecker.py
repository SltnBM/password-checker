import re

def check_strength(password):
    score = 0
    remarks = ""

    # Minimum length of 8 characters
    if len(password) >= 8:
        score += 1

    # Contains uppercase letter
    if re.search(r"[A-Z]", password):
        score += 1

    # Contains lowercase letter
    if re.search(r"[a-z]", password):
        score += 1

    # Contains number
    if re.search(r"[0-9]", password):
        score += 1

    # Contains symbol
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Category based on score
    if score <= 2:
        remarks = "Weak 🚫"
    elif score == 3 or score == 4:
        remarks = "Fair 💡"
    else:
        remarks = "Strong ✅"

    return score, remarks

# Main
if __name__ == "__main__":
    password = input("Enter the password to check: ")
    score, remarks = check_strength(password)
    print(f"Password Strength: {remarks} (Score: {score}/5)")
