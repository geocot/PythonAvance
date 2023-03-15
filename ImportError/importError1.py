from pip import main

def install(package):
    main(['install', package])

def install_all_packages(nomModule):
    for module in nomModule:
        try:
           __import__(module)
        except ImportError as e:
            install(e.name)

install_all_packages('bs4')

#Ou
import os
os.system("python -m pip install lxml")


