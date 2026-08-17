# #It will look like [start, last)
# for i in range(1,7):
#     print(i)

# # [0,last-1]
# for i in range(5):
#     print(i)


#Loop throught list

a = ["Adarsh","Khushi","Roshan",1]

for name in a:
    print(type(name))


for name in a:
    print(name)



# Loop through list +  dictionary

b=[
    {1:"Adarsh",2:"Khushi"},
    {2:"Khushi"},
    {"Prince":3}
]

for ele in b:
    print(ele)

for ele in b:
    for key,value in ele.items():
        print(key,value)