import shutil
total, used, free = shutil.disk_usage("/")
from math import ceil
import os
from progress.bar import Bar

text = """
 ____ ___ ____  _  __  ____  ____   _    ____ _____ 
|  _ \_ _/ ___|| |/ / / ___||  _ \ / \  / ___| ____|
| | | | |\___ \| ' /  \___ \| |_) / _ \| |   |  _|  
| |_| | | ___) | . \   ___) |  __/ ___ \ |___| |___ 
|____/___|____/|_|\_\ |____/|_| /_/   \_\____|_____|
"""
os.system("clear")
print(text)
print(" ")
d = used / total
eamount = ceil(100 * d)
bar = Bar('\033[1mDisk Space :\033[m', max=100)
for i in range(eamount):
    bar.next()
bar.finish()

print("\033[1mTotal ->\033[m %d Go" % (total // (2**30)))
print("\033[1mUsed ->\033[m %d Go" % (used // (2**30)))
print("\033[1mRemaining ->\033[m %d Go" % (free // (2**30)))