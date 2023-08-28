import random
fruits=["apple","orange","banana","mango","strawberry","watermelon"]
colours=["red","yellow","magenta","turquoise","crimson","teal"]
cities=["moscow","tokyo","nairobi","bangalore","stockholm","lisbon"]
vowels=["a","e","i","o","u"]
print("1.FRUITS")
print("2.COLOURS")
print("3.CITIES")
n=int(input("Choose a category(Enter option 1,2 or 3))"))
if n==1:
    x=random.randint(0,len(fruits)-1)
    word=fruits[x]
elif n==2:
    x=random.randint(0,len(colours)-1)
    word=colours[x]
else:
    x=random.randint(0,len(cities)-1)
    word=cities[x]

print("Start guessing, you have 5 lives.")
lives=5
l=[]
for i in range (len(word)):
    if word[i] in vowels:
        l.append(word[i])
    else:
        l.append("_")
for i in l:
    print(i,end=" ")
print()
while lives>0:
    count=0
    x=input("Enter your letter:")
    if x in word:
        for i in range(len(word)):
            if x==word[i]:
                l[i]=x
        for i in l:
            print(i,end=" ")
        print()
    else:
        
        for i in l:
            print(i,end=" ")
        print() 
        lives=lives-1
        print("Nah too bad, you have {} lives left".format(lives))
    
    l1=[]
    for i in word:
        l1.append(i)
    if l1==l:
        print("YOU WIN.")
        break
else:
    print("GAME OVER")
    
            




    