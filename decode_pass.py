import argparse
import base64
import os

def decode_password(b64_file):
    if not os.path.exists(b64_file):
        print(f"File not found: {b64_file}")
        return
    with open(b64_file, 'r') as f:
        b64_content = f.read().strip()
    try:
        decoded = base64.b64decode(b64_content).decode()
        print(f"Decoded password: {decoded}")
    except Exception as e:
        print(f"Error decoding password: {e}")

def main():
        parser = argparse.ArgumentParser(description='Decode a base64 password file and show the password.')
        parser.add_argument('-b64file', required=False, help='Base64 password file to decode')
        parser.add_argument('-help', action='store_true', help='Show usage and context help')
        args = parser.parse_args()
        if args.help or not args.b64file:
                print("""
Usage: python decode_pass.py -b64file <base64_file>

Mandatory:
    -b64file   Base64 password file to decode
Optional:
    -help      Show usage and context help

Decodes the password stored in base64 format and prints it to the console.
                """)
                return
        decode_password(args.b64file)

if __name__ == '__main__':
    main()
