#string concepts 
#declaring strings
str="i am tanushree"
str2='i am in banglore' 
#concatanation
str1="tanu"
str2="shree"
print(str1+str2)
#length
name="banana"
name=len(name)
print(name)
#indexing
a="TANUSHREE"
print(a[4])
print(a[6])
#slicing
q="123456"
print(q[1:4])
print(q[0:6])
#string functions
L="i am studying in global adedamy of technology"
print(L.endswith("ogy"))
print(L.endswith("asd"))
print(L.capitalize())
print(L.replace("adedamy","academy"))
print(L.count("i"))
#WAP to input user's first name and print its length
# NAME =input("enter your name :")
# print(len(NAME))
#WAP to finf the occurances of $ in string
occ="tanu$r$hubo$du$yu$"
print(occ.count("$"))
#acess the first and last char of string
w="global college"
# print(len(w))
# print(w[0])
# print(w[-1])
fir_char =w[0]
last_char=w[-1]
print("first char is:",fir_char)
print("last char is :",last_char)

