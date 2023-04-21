import secrets

chrs = 'A-Za-z0-9&,._;=8,'

length = input("Hvor mange karakterer skal der være i dit password?: ")

passwordchrs = ''.join(secrets.choice(chrs) for i in range(int(length))) # inde i vores forloop skriver vi "(8)" for at sætte en længde på vores password - int = integer

print("***PASSWORD***")

print("Her er dit password:",passwordchrs)

# python "password.py"