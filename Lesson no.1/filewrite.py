with open('sample.txt', 'r', encoding='utf-8') as file:
  print(file.read())
  file.close()

filewrite= open("sample.txt",'w')
filewrite.write("stories of Mahabharata")
filewrite.close()
fr= open("sample.txt",'r')
print("the file after modification is")
print(fr.read())
fr.close()

    