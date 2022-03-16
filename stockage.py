import shutil
total, used, free = shutil.disk_usage("/")
from math import ceil
import os
from pystyle import Colors, Colorate, Write

text = """
 ____ ___ ____  _  __  ____  ____   _    ____ _____ 
|  _ \_ _/ ___|| |/ / / ___||  _ \ / \  / ___| ____|
| | | | |\___ \| ' /  \___ \| |_) / _ \| |   |  _|  
| |_| | | ___) | . \   ___) |  __/ ___ \ |___| |___ 
|____/___|____/|_|\_\ |____/|_| /_/   \_\____|_____|
"""
os.system("clear")
print(Colorate.Horizontal(Colors.blue_to_green, text, 1))
print(" ")
d = used / total
eamount = ceil(100 * d)

Write.Print(f"Pourcentage -> {eamount}/100%\n", Colors.blue_to_green, interval=0.03)
Write.Print("Total -> %d Go \n" % (total // (2**30)), Colors.blue_to_green, interval=0.03)
Write.Print("Used -> %d Go \n" % (used // (2**30)), Colors.blue_to_green, interval=0.03)
Write.Print("Remaining -> %d Go \n" % (free // (2**30)), Colors.blue_to_green, interval=0.03)