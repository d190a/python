
name= input("enter name")
note=input("enter note")

with open("file.txt","w")as file:
  file.write("name:"+name+"\n")
  file.write("note:"+note+"\n")

print("\nsaved content:")
with open("file.txt","r")as file:
   print(file.read())