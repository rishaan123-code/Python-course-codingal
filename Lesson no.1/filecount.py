file=open("sample.txt","r")
count = 0
content= file.read()
colist= content.split("\n")
for i in colist: 
    if i :
        count = count+1
print("the number of the lines= are",count)