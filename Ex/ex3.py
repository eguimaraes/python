a=3
if a==2:
   b=3
elif a==3:
   b=5
else:
   b=7
for i in range (3,10):
    if i>5:
      print (i)
    else:
      print (i,'is not bigger than 5')
i=0
while i<20:
     i+=1
     print ('Still in the loop and i is',i)
a=3
try:
    b=a/0 
except:
    b=4
    print (b)
    
a = ['gnome','goblin','hobgoblin','troll']
for i in a:
   if 'b' in i:
     print (i)
print()
print()

for iy in range(5):
    for ix in range(5):
        print(iy,ix)

print()
print()
a='wombat'
print(a)
for i in a:
    print(i)
print()
print()
for i in a:
    if 'm' not in i:    
      print(i)

print()
print()
for i in a:
    if 'm' not in i:
        if 'a' in i:    
            break
        else:
            print(i)
print()
print()
soma=0
for i in range(51):
    soma=soma+i
print(soma)

print()
print()

n0=0
n1=0
n=1
soma=0
while n0+n < 1000:
    soma=n0+n;
    print (soma)
    n0=n;
    n=soma

  
   
   
  
   
  
