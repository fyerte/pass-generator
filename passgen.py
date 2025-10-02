import argparse
import base64
import random
import string
import os

DEFAULT_LENGTH = 10

# Character sets
ALPHANUMERIC = string.ascii_letters + string.digits
SPECIAL_CHARS = '!@#$%^&*()-_=+[]{}|;:,.<>?/'

def generate_password(length, add_special):
    if not add_special:
        chars = ALPHANUMERIC
        return ''.join(random.choice(chars) for _ in range(length))
    else:
        min_special = max(1, int(length * 0.10))
        max_special = max(min_special, int(length * 0.20))
        num_special = random.randint(min_special, max_special)
        num_alphanum = length - num_special
        specials = [random.choice(SPECIAL_CHARS) for _ in range(num_special)]
        alphanums = [random.choice(ALPHANUMERIC) for _ in range(num_alphanum)]
        password_chars = specials + alphanums
        random.shuffle(password_chars)
        return ''.join(password_chars)

def save_password(filename, password):
    # Save plain text
    with open(filename, 'w') as f:
        f.write(password)

def save_base64_password(filename, password):
    b64_password = base64.b64encode(password.encode()).decode()
    base_name = os.path.splitext(filename)[0]
    b64_filename = f"{base_name}.txt"
    iteration = 1
    while os.path.exists(b64_filename):
        b64_filename = f"{base_name}_{iteration}.txt"
        iteration += 1
    with open(b64_filename, 'w') as f:
        f.write(b64_password)

def main():
        parser = argparse.ArgumentParser(description='Generate a password and store it in plain text and base64 encoded files.')
        parser.add_argument('-help', action='store_true', help='Show usage and context help')
        parser.add_argument('-add-special', action='store_true', help='Include special characters in the password (10%-20% of password will be special chars)')
        parser.add_argument('-length', type=int, default=DEFAULT_LENGTH, help='Length of the password (default: 10)')
        parser.add_argument('-filename', required=True, help='Filename for the base64 password file')
        parser.add_argument('-plain', action='store_true', help='Also create plain text password file')
        args = parser.parse_args()

        if args.help:
                print("""
Usage: python passgen.py -filename <filename> [-add-special] [-length <length>] [-plain]

Mandatory:
    -filename      Output file for base64 password
Optional:
    -add-special   Include special characters (10%-20% of password will be special chars)
    -length        Password length (default: 10)
    -plain         Also create plain text password file

If -add-special is specified, the password will contain at least 10% and at most 20% special characters.
By default, only a base64 encoded password file is created. Use -plain to also create a plain text file.
                """)
                return

        password = generate_password(args.length, args.add_special)
        save_base64_password(args.filename, password)
        print(f"Base64 password file generated: {os.path.splitext(args.filename)[0]}.txt (or with iteration if exists)")
        if args.plain:
            save_password(args.filename, password)
            print(f"Plain password file also generated: {args.filename}")

if __name__ == '__main__':
    main()
