def greet(name):
    if(name=="Khushi"):
        print("Special "+ name)
    else:
        print("Hello "+ name)

def cal(a,b):
    return a+b

a = ["Adarsh","Khushi","Prince","Rahul"]

for ele in a:
    greet(ele)


r =cal(5,6)
print(r)