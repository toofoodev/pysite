# PySite  |  Wes Parker
# PS (v1.1)
# PySite Load
print("PySite Engine 1")
print("(Made by Wes/TooFooDev)\n")
# Web Brouser
def web():
    print("Welcome to PySite!")
    print("Type a site to go to it.")
    inputweb = input("")

    # PySite:
    if inputweb == "pysite.py":
        print("\n")
        print("PySite: pysite.py")
        pysite_indexpy()
    
    if inputweb == "pysite.py/poop":
        print("\n")
        print("PySite: pysite.py/poop")
        pysite_poop_indexpy()
        
    # Wes:
    if inputweb == "wes.py":
        print("\n")
        print("PySite: wes.py")
        wes_indexpy()
        
    if inputweb == "wes.py/wesisgoofy":
        print("\n")
        print("PySite: wes.py/wesisgoofy")
        wes_wesisgoofy_indexpy()
    
    print("\n" + inputweb + " is not valid!" + "\n")
    web()
# Python Websites
# PySite:
def pysite_indexpy():
    print("Skibidi PySite")
    print("\n")
    web()
def pysite_poop_indexpy():
    print("POOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOP")
    print("\n")
    web()
# Wes:
def wes_indexpy():
    print("WES WES WES WES WES WES WES WES WES WES WES WES WES WES WES WES WES WES WES WES WES WES WES WES WES WES WES WES WES WES WES WES WES WES")
    print("\n")
    web()
def wes_wesisgoofy_wrongpy():
    # PySite:Hidden
    print("WRONG")
    print("WRONG")
    print("WRONG")
    print("WRONG")
    print("WRONG")
    print("WRONG")
    print("WRONG")
    print("WRONG")
    print("WRONG")
    print("WRONG")
    print("WRONG")
    print("WRONG")
    print("WRONG")
    print("WRONG")
    print("WRONG\n")
    web()
def wes_wesisgoofy_indexpy(): 
    print("Wes is very goofy.")
    print("Is Wes goofy?")
    inputuser = input("Yes or no?\n")
    if inputuser == "yes":
        print("Good!\n")
        web()
    else:
        wes_wesisgoofy_wrongpy()

# Run Site
web()
