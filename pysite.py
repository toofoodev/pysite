# PySite  |  Wes Parker
# PySite Load
print("PySite Engine 0.1\n")
# Web Brouser
def web():
    print("Welcome to PySite!")
    print("Type a site to go to it.\n")
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
    if inputweb == "wes.py":
        print("\n")
        print("PySite: wes.py")
        wes_indexpy()
    
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

# Run Site
web()
