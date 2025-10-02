# Password Generator Console App

## Overview
This project provides two Python scripts for password management:

### 1. passgen.py
- Generates a random password with customizable length and optional special characters.
- By default, creates a base64-encoded password file using the filename you specify.
- Optionally, can also create a plain text password file with the `-plain` parameter.
- Special characters (if enabled) will be between 10% and 20% of the password length.

#### Usage
```bash
python passgen.py -filename <filename> [-add-special] [-length <length>] [-plain]
```
- `-filename` (required): Output file for base64 password.
- `-add-special`: Include special characters (10%-20% of password).
- `-length`: Password length (default: 10).
- `-plain`: Also create a plain text password file.

#### Examples
- Generate a 16-character base64 password:
  ```bash
  python passgen.py -filename mypass.txt -length 16
  ```
- Generate a 20-character password with special characters, both base64 and plain files:
  ```bash
  python passgen.py -filename mypass.txt -length 20 -add-special -plain
  ```

### 2. decode_pass.py
- Decodes a base64 password file and prints the plain password to the console.

#### Usage
```bash
python decode_pass.py -b64file <base64_file>
```
- `-b64file` (required): Base64 password file to decode.

#### Example
```bash
python decode_pass.py -b64file mypass.txt
```

## Environment Requirements
- Python 3.11 or newer (recommended)
- No external dependencies required (uses only standard library)

## Setup
1. Create a Python virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate  # On Windows
   ```
2. Run the scripts as shown above.

## Notes
- Base64 files will not overwrite existing files; an iteration number will be appended if needed.
- All output files are created in the current working directory.
