#this is the list of data for the user prompts
ulist = ["Thomas", "Milena", "Matthew","Doug","Donovan","Nate","Rachel","Chris","Marie","Nikitia","Gary", "Richard",
          "Frank", "Elsa", "John", "Erik", "Trevor", "Peter","Luke","John","Jacob"]
#user prompt
print("what would you like to do?")
print("1.sort\n2.reverse\n3.print list")

#creating an integer from use input
number = int(input("Enter 1, 2, or 3:"))
#if statements and error catch
if number == 1:
    ulist.sort()
    print(ulist)
if number == 2:
    ulist.reverse()
    print(ulist)
if number == 3:
    print(ulist)
else:
    print("invalid parameter")

