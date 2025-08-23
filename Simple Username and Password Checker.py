
print("hello")
name=input("please enter user name")
password=input("please enter password ")

name=name.lower()
name=name.replace(" ","_")
length=len(password)

print(f"username (fixed):{name}")
print(f"password length:{length}")


print(f"password length >=8?{length >=8}")
print(f"is username 'admin' ?{name=='admin'}")
print(f"is password '1234'{password=='1234'}")
print(f"is default account  ?{name=='admin'and (password=='1234')}")

message = f"welcom,{name}! yourpassword length is{length}"
print(message)