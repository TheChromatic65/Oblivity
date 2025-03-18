import time
time.sleep(3)

def display(char):
    print(char, end='', flush=True)
    time.sleep(0.05)
def wait():
    time.sleep(0.2)
def tim():
    time.sleep(0.5)
    
a = "This program will determine your identity."
b = "It will be described on the Oblivity Scale."
c = "Your scores and results will be explained once the test is finished."
d = "Please read the public disclosure file before taking the test."

for char in a:
    display(char)
print()
tim()
for char in b:
    display(char)
print()
tim()
for char in c:
    display(char)
print()
tim()
for char in d:
    display(char)
print()
print()
    
def menu():
    tim()
    print("#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#")
    tim()
    print("#                                          #")
    tim()
    print("#                OBLIVITY                  #")
    tim()
    print("#                                          #")
    tim()
    print("#   "'[1]'"Start                               #")
    tim()
    print("#   "'[2]'"About                               #")
    tim()
    print("#   "'[3]'"Changelog                           #")
    tim()
    print("#   "'[4]'"Credits                             #")
    tim()
    print("#   "'[5]'"Exit                                #")
    tim()
    print("#                                          #")
    tim()
    print("#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#")
    tim()
    print()
    tim()
    opt = input("[>-")
    if opt == ("1"):
        test()
    if opt == ("2"):
        about()
    if opt == ("3"):
        changelog()
    if opt == ("4"):
        credit()
    if opt == ("5"):
        exiT()

def test():
    print("")
def about():
    e = "The idea of the Oblivity Test emerged on 3/17/2025."
    f = "It was originally meant to determine the value of a human's life; how valuable it is to continue living it."
    g = "The test today is mostly meant to bring light to a person's persona, as well as the darkness within it."
    h = "A number of ratings were created here to try to reflect this persona into a concrete, definitive name."
    i = "Oblivity is derived from the word 'oblivion', meaning the state in which one is unaware of one's consciousness."
    j = "A wiki is being planned on Oblivion's github repository in the form of a organized folder with text files."
    k = "There, you can find an in-depth explanation on the algorithms and formulae that dictate the Oblivity rating."
    l = "The code is open-source, and all are free to submit a pull-request, however useless it may be."
    m = "The pull-request will likely be merged unless it harms the functionality of the code."
    n = "Oblivion is currently still being developed by it's main creator."
    o = "A changelog is available in the menu, showcasing the full history of the program."
    p = "View the github repo at https://github.com/TheChromatic65/Oblivity for more information."
    for char in e:
        display(char)
    print()
    wait()
    for char in f:
        display(char)
    print()
    wait()
    for char in g:
        display(char)
    print()
    wait()
    for char in h:
        display(char)
    print()
    for char in i:
        display(char)
    print()
    wait()
    for char in j:
        display(char)
    print()
    wait()
    for char in k:
        display(char)
    print()
    wait()
    for char in l:
        display(char)
    print()
    wait()
    for char in m:
        display(char)
    print()
    wait()
    for char in n:
        display(char)
    print()
    for char in o:
        display(char)
    print()
    wait()
    for char in p:
        display(char)
    print()
    print()
    menu()
menu()