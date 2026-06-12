#abs()
print(abs(-18))
#pow
print(pow(3,8))
print(round(3.49988563,3))
print(divmod(6,2))
#iterables
#enemurate
fruits=["apple","banana","guava"]
for i,fruits  in enumerate(fruits, start=2):
    print(i,fruits)
#zip()
names=["ravi","roj","abc"]
rollno=[1,3,4]
print(list(zip(names,rollno)))
#map()
nums = [1,2,3,4]
sums=list(map(lambda x:x+3,nums))
print(sums)
words=["hello","pavi","python"]
uppercase= list(map(str.upper,words))
print(uppercase)
#sorted
nums=[4,7,8,2,4,7]
print(sorted(nums))
print(sorted(nums,reverse=True))
print(int(input("enter a number:")))
print(float(input("enter a number:")))
list=[1,3,56,7]
print(max(list))
udh=("pav","id","IBG")
print(max(udh))
print(tuple(udh))







           