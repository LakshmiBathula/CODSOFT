import random
import string

def generatePSWD(l, complexity):
    if complexity == "low":
        c = string.ascii_lowercase + string.ascii_uppercase
    elif complexity == "medium":
        c = string.ascii_letters + string.digits
    elif complexity== "high":
        c= string.ascii_letters + string.digits + string.punctuation
    else:
        print(" Please choose 'low', 'medium', or 'high'.")
        return None

    p= ''.join(random.choice(c) for _ in range(l))
    return p

def pswdGenerator():
    print("Password Generator")

    l = int(input("Enter the length of the password: "))
    print("Please enter a valid number for the password length.")
    

    if l<= 0:
        print("Please enter a positive number for password length.")
        return

    complexity = input("Enter the complexity level ('low', 'medium', or 'high'): ").lower()

    password = generatePSWD(l, complexity)
    
    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    pswdGenerator()
