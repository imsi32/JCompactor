"""JCompactor is JSON Compactor."""
import os
import json

def compactor(file):
    """The main part of the script. It compacts JSON file."""
    us={}
    try:
        with open(file, 'r', encoding="utf-8") as fr:
            us.update(json.load(fr))
        s1 = os.stat(file).st_size
    except FileNotFoundError:
        print(file, "Could not be found.")
        return print("Try Again")
    except json.decoder.JSONDecodeError:
        return print(file, "is empty.")

    with open(file, 'w', encoding="utf-8") as fw:
        json.dump(us, fw)
    s2 = os.stat(file).st_size
    print(20 * "*", "\n"+ os.path.basename(file), "\nBefore:", str(s1), "\nAfter:", str(s2), "\nDifference:", str(s1 - s2), "\n"+ 20 * "*")
    return s1 - s2


print("Welcome to the JCompactor.")
while True:
    print(80 * "*")
    q1 = int(input("What will you compact? File[1] or Directory(2): "))

    if q1 == 2:
        pass
    else:
        # File Composting
        f = input("What is file name: ")
        compactor(f)

    # Exit area
    q2 = int(input("Do you want to exit? Yes[1] or No(2): "))
    if q2 == 2:
        pass
    else:
        break
