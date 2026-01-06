i = 0
while i < 5:
    print(i)
    i += 1


thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1 # Increment i to avoid infinite loop
            #output: apple, banana, cherry


# break in a while loop
fruits = ["apple", "banana", "cherry"]  
i = 0
while i < len(fruits):
    if fruits[i] == "banana":
        break
    print(fruits[i])
    i += 1 #output: apple

# continue in a while loop
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
i = 0
while i < len(fruits):
    if fruits[i] == "banana" or fruits[i] == "orange":
        i += 1
        continue
    print(fruits[i])
    i += 1
#output: apple, cherry, kiwi, melon, mango

#or
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
i = 0
while i < len(fruits):
    if fruits[i] == "orange":
        i += 1  # ← increment BEFORE continue
        continue
    print(fruits[i])
    i += 1      # ← increment at the END
#output: apple, banana, cherry, kiwi, melon, mango

