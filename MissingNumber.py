# def finding_missing_number(data,range):
#     total_sum=range*(range+1)//2
#
#     actual_sum=sum(data)
#
#     missing_number=total_sum-actual_sum
#     return missing_number
#
# data=[1,2,4,5,6]
# range=6
# missing=finding_missing_number(data,range)
# print("a missing number is",missing)
#
#
# # //primeNumber
# for i in range(2,20):
#     prime=True
#     for j in range(2,i):
#         if i%j==0:
#             prime=False
#             break
#     if prime:
#         print(i)
#
# # // countList
#
# myList=["apple","orange","apple","mango","mango"]
# count={}
# for i in myList:
#     # //print(i)
#     if i in count:
#         count[i] +=1
#     else:
#         count[i]=1
# print(count)
#

#second heighest rank



# l={"apple":"fruit","orange":"fruit","hero":"bike","pepsi":"drink"}
# for k in l.keys():
#     print("value of k is",k)
# for v in l.values():
#     print("value of v is", v)
# l.items()

# for k,v in l.items():
#     print("keys",k,"values",v)

# data=["andromeda-shrub","beflower-flower","daffodil-flower","lilac-shrub"]
# flowers=[]
# shrubs=[]
# for i in data:
#     if "flower" in i:
#         flowers.append(i)
#     elif "shrub" in i:
#         shrubs.append(i)
# print(flowers)
# print(shrubs)

# tuple unpacking
# mylist=[(1,2),(3,4),(5,6)]
# for i,j in mylist:
#     print(i)
#
# p='i am the best'
# print(p[0])
# print(p[-1])

# import pandas as pd
# import requests
#
# # raw_data=requests.get("https://storage.googleapis.com/generall-shared-data/startups_demo.json")
# # # print(raw_data.text)
# #
# # with open("raw_files/raw_data.json","w") as f:
# #     f.write(raw_data.text)
#
# raw_df=pd.read_json("raw_files/raw_data.json",lines=True)
# # print(raw_df.sample((10)))
# # print(raw_df['link'])
#
# secure_startup_df=raw_df.loc[raw_df['link'].str.contains("https")].sort_values("name").reset_index(drop=True)
# print(secure_startup_df)
# print(secure_startup_df.count())

# addition of two number

# def add(num1,num2):
#     sum_of_no=num1+num2
#     return sum_of_no
# sum=add(10,20)
# print(sum)



# for i in range(2,20):
#     prime=True
#     for j in range(2,i):
#         if i%j==0:
#             prime=False
#             break
#     if prime:
#         print(i)


# for i in range(2, 20):
#     prime = True
#     for j in range(2, i):
#         if i % j == 0:
#             prime = False
#             break
#     if prime:
#         print(i)
#
# for m in range(2, 20):
#     prime = True
#     for j in range(2, m):
#         if m % j == 0:
#             prime = False
#
#     if prime:
#         print(m)


# def find_missing_numbers(numbers, start, end):
#     # Use a list comprehension to find missing numbers
#     return [i for i in range(start, end + 1) if i not in numbers]
#
# # Example usage
# numbers = [1, 2, 4, 6, 7, 9,11]
# start_range = 1
# end_range = 11
#
# missing = find_missing_numbers(numbers, start_range, end_range)
# print("Missing numbers:", missing)


# primeNumber

# for i in range(2,20):
#     prime=True
#     for j in range(2,i):
#         if i%j==0:
#             prime=False
#             break
#     if prime:
#         print(i)

    # missing Number

def missing_number(inputNumber,start,end):


    return[i for i in range(start,end+1) if i not in inputNumber]



inputNumber=1,3,4,5,7,10,11
start=1
end=11

miss_number=missing_number(inputNumber,start,end)
print(miss_number)








