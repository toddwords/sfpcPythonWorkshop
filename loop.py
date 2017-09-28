myText = "hello everyone how are you doing today?"
myList = myText.split()

for word in myList:
    if (myList.index(word) > len(myList)/2):
        break
    if 'h' in word:
        print word
myNum = 2
for num in range(0,4):
	myNum = myNum * 2
	print myNum

myValue = 2

while (myValue < 500):
    myValue = myValue * 2
    print myValue

