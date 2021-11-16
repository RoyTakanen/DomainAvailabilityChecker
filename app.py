import itertools
import socket
import whois

def check_domain_availability(combinations, tld):
    for combination in combinations:
        domain = ''.join(combination) + "." + tld

        #print("DNS checking...", domain)

        try:
            ip = socket.gethostbyname(domain)
            #print(domain + "," + ip + ",false")
        except:
            #print("Whois checking...",domain)
            try:
                whois_data = whois.query(domain)
                if whois_data == None:
                    #print(domain + ",0.0.0.0,true")
                    print("[+]", domain)
                    break
            except:
                pass
                #print("Darn utf-8!")
        print("[-]", domain)
def main():
    # TODO: csv and/or json outputs

    print("""
______  ___  _____ 
|  _  \/ _ \/  __ \\
| | | / /_\ \ /  \/
| | | |  _  | |    
| |/ /| | | | \__/\\
|___/ \_| |_/\____/

Domain Availability Checker

Features:

[+] Brute forces every possible domain
[+] Check DNS first and then Whois
[+] Custom tld's
[+] Custom domain length
    """)

    while True:
        while True:
            tld = input("Enter domain tld (no dot): ")

            if not "." in tld:
                break    
            print("I SAID NO F*CKING DOT!")
        
        all_characters = 'abcdefghijklmnopqrstuvwxyz'
        all_numbs = '1234567890'

        print("Select character lists to the combination generator.")
        print("These should be separated by comma and/or space. Example: 1, 2")

        print()
        print("Character lists:")
        print()

        print("1.", all_characters)
        print("2.", all_numbs)

        print()

        selection = input("Character lists: ").replace(",", " ").split()

        print()

        character_list = ""

        for selected in selection:
            if selected == "1":
                character_list += all_characters
            if selected == "2":
                character_list += all_numbs

        domain_length = int(input("Enter domain length: "))

        combinations = itertools.product(*([character_list] * domain_length))

        print()
        print("Starting checking...")
        print()

        check_domain_availability(combinations, tld)
        print()
        print("Done!")
        break

if __name__ == "__main__":
    main()