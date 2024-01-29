#fruit list
fruits=["rasberry","blueberry","pineapple"]
fruits.append("apple")
del fruits[2]
print(fruits)

#number list
num1=[1,2,3]
num2=[4,5,6]
num1.extend(num2)
result=[x * 2 for x in num1] 
print(result)

#week list
week=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print(week[2])

#groups name and age
group=[("Jawwad",20), ("Imran",19),("Moiz",23)]
for i in group:
  print(i)
