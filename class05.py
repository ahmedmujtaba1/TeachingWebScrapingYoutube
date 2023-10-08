number = 9
print("[+] Welcome to the Game of Choosing Numbers")
print("[+] You have 5 tries to guess the number from 1-10........Let's start")
tries = 5
user_tries = 0
flag = True
while flag:
    if user_tries == tries:
        print("[+] You run out of tries. Better Luck Next Time")
        break
   
    var = int(input("[+] Choose any number from 1-10: "))
    if var == number:
        print("[+] Congratulations, You guessed the number!")
        break
    elif var > number:
        user_tries += 1
        print(f'[+] The number you guess is bigger. You have {tries - user_tries} tries remaining')
    elif var < number:
        user_tries += 1
        print(f'[+] The number you guess is lesser. You have {tries - user_tries} tries remaining')
