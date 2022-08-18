#다음 코드의 결과값은?
from cgi import print_arguments
from ctypes.wintypes import PINT
from queue import PriorityQueue


a = "Life is too short, you need python"

if "wife" in a: #거짓
    print("wife")
elif "pyhton" in a and "you" not in a: #거짓
    print("python")
elif "shirt" not in a: #참
    print("shirt")
elif "need" in a: #참
    print("need")
else:
    print("none")