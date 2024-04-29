



capitals = {"USA" : "Washington D.C.",
            "India": "New Dehli",
            "China" : "Bejing",
            "Russia": "Moscow"}

#print(dir(capitals))

print(capitals.get("USA"))

if capitals.get("Japan"):
    print("That capitol exists")
else:
    print("That capitol doesn't exist")

capitals.update({"Germany": "Berlin"})

print(capitals)