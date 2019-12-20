# Sarvesh Gupta
# 10/8/2019
# Telephone Database

import shelve

def main():
    try:
        phoneDB = shelve.open("Data.txt")
    except IOError:
        print("Error: unable to open file")
    else:
        print("Commands are 'whois phone-number' 'add phone-number' ' search keyword' 'quit'")

    cmd = input("Command: ")

    while cmd != 'quit':
        words = cmd.split()
        if words[0] == 'whois':
            try:
                print(words[1], phoneDB[words[1]])
            except:
                print("Error")
        elif words[0] == 'add':
            tempData = phoneDB.get(words[1], "->")
            for w in words[2:]:
                tempData = tempData + " " + w
                phoneDB[words[1]] = tempData
        elif words[0] == 'search':
            for w in phoneDB.keys():
                if phoneDB[w].find(words[1]) >= 0:
                    print(w, phoneDB[w])
                else:
                    print("There is no command by that name")
        cmd = input("Command:")

    phoneDB.close()
    return

main()

