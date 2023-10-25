import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation 
    return ''.join(random.choice(characters) for _ in range(length))

target_password = input("Enter a password to crack: ")
target_length = len(target_password)
count = 0

while True:
    count += 1
    guessed_password = generate_random_password(target_length)
    print(f"Attempt {count}: {guessed_password}", end='\r')
    
    if guessed_password == target_password:
        break

print(f"\nPassword successfully cracked: {target_password}")
print(f"Number of attempts: {count}")


