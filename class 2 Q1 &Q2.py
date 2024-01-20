#Que 1
first_name = input("Enter first name \n")
last_name = input("Enter last name \n")

def string_alternative (name):
    return (name[::2])
def full_name (first_name,  last_name):
    name = first_name + " " + last_name
    print("full name : ", name)
    sa = string_alternative(name)
    print("alternative letters : ", sa)

full_name(first_name, last_name)




#Que 2

from collections import Counter
# to read file
with open('/content/drive/My Drive/input.txt', 'r') as ipFile:
    lines = ipFile.readlines()

opLines = []
#file1.close()
listOfWords = []

for line in lines:
    opLines.append(line)
    line = line.strip()
    listOfWords.extend(line.split(" "))

opLines.append("Word_Count:")
elementsCount = Counter(listOfWords)

# to count occurance of each word
for ele, count in elementsCount.items():
  opLines.append(f"{ele} - Count: {count}")

# to add content in file
with open('/content/drive/My Drive/outputFile.txt', 'w') as opFile:
    for line in opLines:
        opFile.write(line + '\n')

ipFile.close()
opFile.close()






