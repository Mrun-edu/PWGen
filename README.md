# Pi Password Generator

A Python CLI tool that generates passwords by converting characters to digits from Pi based on their position in the alphabet.

## How It Works

The password generator uses a simple but clever algorithm:
- Each letter in the alphabet (a-z) corresponds to a position (0-25)
- Each position maps to a digit from Pi's decimal expansion
- For example: `a` (position 0) → `3`, `e` (position 4) → `5`

**Pi digits used:** `3.14159265358979323846264338327...`

## Features

- ✅ **CLI and Interactive modes** - Use with arguments or run interactively
- ✅ **Input validation** - Only accepts letters, numbers, spaces, and special characters: `@`, `.`, `,`
- ✅ **Quiet mode** - Perfect for scripting and piping
- ✅ **Character mapping display** - See how each character converts to a digit
- ✅ **Cross-platform** - Works on Linux, macOS, and Windows

# Make the script executable (Linux/macOS)
chmod +x sifre.py

### Interactive Mode

Run without arguments to enter interactive mode:

```bash
python3 sifre.py
```

Enter a name or quote exp.(Go0dp@ssw0rd.): emirhan
Original name: emirhan
Generated password: 5953637

Character mapping:
  'e' (index 4) -> '5'
  'm' (index 12) -> '9'
  'i' (index 8) -> '5'
  'r' (index 17) -> '3'
  'h' (index 7) -> '6'
  'a' (index 0) -> '3'
  'n' (index 13) -> '7'
```

### CLI Mode

Pass the name as an argument:

```bash
python3 sifre.py alice
or
alias pwgen='/File/Path/sifre.py'
```

Output:
```
Original name: alice
Generated password: 38545
```

### Quiet Mode

Get only the password (useful for scripting):

```bash
python3 sifre.py alice --quiet
```

Output:
```
38545
```

### Show Character Mapping

Display the character-to-digit mapping in CLI mode:

```bash
python3 sifre.py alice --show-mapping
```

Output:
```
Original name: alice
Generated password: 38545

Character mapping:
  'a' (index 0) -> '3'
  'l' (index 11) -> '8'
  'i' (index 8) -> '5'
  'c' (index 2) -> '4'
  'e' (index 4) -> '5'
```

### Help

View all available options:

```bash
python3 sifre.py --help
```

## Examples

### Valid Inputs

```bash
# Simple name
python3 sifre.py alice

# Email address
python3 sifre.py alice@example.com

# Multiple names with comma
python3 sifre.py "alice, bob"

# Quote or phrase
python3 sifre.py "Go0dp@ssw0rd."

# Numbers and letters
python3 sifre.py user123
```

### Invalid Inputs

The following characters are **not allowed**: `! # $ % ^ & * ( ) - _ = + [ ] { } | \ / ? < > ~ ` and others.

```bash
# Will fail - contains #
python3 sifre.py "alice#123"
# Error: Invalid character '#' found. Only letters, numbers, spaces, and @ . , are allowed.

# Will fail - contains !
python3 sifre.py "hello!"
# Error: Invalid character '!' found. Only letters, numbers, spaces, and @ . , are allowed.
```

## Command-Line Options

| Option | Short | Description |
|--------|-------|-------------|
| `--help` | `-h` | Show help message and exit |
| `--quiet` | `-q` | Only output the password without additional information |
| `--show-mapping` | `-m` | Show character-to-digit mapping |

## Use Cases

### Scripting

Generate passwords in shell scripts:

```bash
#!/bin/bash
PASSWORD=$(python3 sifre.py "myname" --quiet)
echo "Your password is: $PASSWORD"
```

### Batch Processing

Process multiple names:

```bash
for name in alice bob charlie; do
    echo "$name: $(python3 sifre.py "$name" --quiet)"
done
```

Output:
```
alice: 38545
bob: 191
charlie: 4738545
```

## Character Mapping Reference

| Letter | Index | Pi Digit | Letter | Index | Pi Digit |
|--------|-------|----------|--------|-------|----------|
| a | 0 | 3 | n | 13 | 7 |
| b | 1 | 1 | o | 14 | 9 |
| c | 2 | 4 | p | 15 | 3 |
| d | 3 | 1 | q | 16 | 2 |
| e | 4 | 5 | r | 17 | 3 |
| f | 5 | 9 | s | 18 | 8 |
| g | 6 | 2 | t | 19 | 4 |
| h | 7 | 6 | u | 20 | 6 |
| i | 8 | 5 | v | 21 | 2 |
| j | 9 | 3 | w | 22 | 6 |
| k | 10 | 5 | x | 23 | 4 |
| l | 11 | 8 | y | 24 | 3 |
| m | 12 | 9 | z | 25 | 3 |

## Technical Details

- **Language:** Python 3
- **Dependencies:** None (uses only standard library)
- **Modules used:** `argparse`, `sys`
- **Input validation:** Checks for empty strings and invalid characters
- **Exit codes:** 
  - `0` - Success
  - `1` - Invalid input or error

## License

Free to use and modify.

## Author

Created as a simple password generation tool using mathematical constants.
