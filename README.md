# DAC - Domain Availability Checker

## Features

[+] Brute forces every possible domain
[+] Check DNS first and then Whois
[+] Custom tld's
[+] Custom domain length

## Installation

Requirements

```python
pip3 install -r requirements.txt
```

## Example usage

```bash
❯ python3 app.py

______  ___  _____ 
|  _  \/ _ \/  __ \
| | | / /_\ \ /  \/
| | | |  _  | |    
| |/ /| | | | \__/\
|___/ \_| |_/\____/

Domain Availability Checker

Features:

[+] Brute forces every possible domain
[+] Check DNS first and then Whois
[+] Custom tld's
[+] Custom domain length
    
Enter domain tld (no dot): fi
Select character lists to the combination generator.
These should be separated by comma and/or space. Example: 1, 2

Character lists:

1. abcdefghijklmnopqrstuvwxyz
2. 1234567890

Character lists: 1

Enter domain length: 2

Starting checking...

[-] aa.fi
[-] ab.fi
[-] ac.fi
[-] ad.fi
[-] ae.fi
[-] af.fi
[-] ag.fi
[-] ah.fi
[-] ai.fi
[-] aj.fi

```