
fruit={"apple":10,"banana":25, "mango":70,"orange":15,"grape":30,"kiwi":23}
a=input("enter fruit name ?").lower()

if a in fruit:
    print(f"fruit price of {a} is:{fruit[a]}")
else:
    print("sorry this fruit is not available")
