# str1="salom olam"
# for harf in range(len(str1+'2')):
#     for harf1 in range(harf):
#         print(str1[harf1])
# print("\n")   
    
# def count(num: int):
#     dct={}
#     for son in num:
#         if son.isalpha():
#             continue
#         if not dct.get(son):
#             dct[son]=1
#         else:
#             dct[son]+=1
#     return dct
# n=int(input("n: "))
# n1=str(n)
# print(count(n1)) 
            
# num=int(input("num: "))
# if num%2:

#     for i in range(1,num+2):
#         sum=0
#         for k in range(1,i):
#             print(k,end="+")
#             sum+=k
#         print("\b=",sum)
#     print("\n")
# elif not num%2:
#     for i in range(1,num):
#         sum=0
#         for k in range(i,num-1):
#             print(k,end="+")
#             sum+=k
#         print("\b=",sum)
#     print("\n")

# srt=input("string kiriting: ")
# text=srt.split()
# srt1=[]
# for i in range(len(text)):
#     if i==0 or i==len(text)-1:
#         srt1.append(text[i][::-1])
#     else: 
#         srt1.append(text[i])
# print(*srt1)

# num='00008300'
# count=0
# for i in range(len(num)):
#     if num[i]=='0':
#         count+=1
#     else:
#         break
# print(count)

def bigger_price(num: int, lst: list):
   for i in range(len(lst)):
      if i>num-1:
        break
      else:
        print(lst[i])

  
num=int(input("num: "))
lst=[{'name':'samsung','prise':'2000'},{'name':'iphone','prise':'3000'},{'name':'redmi','prise':'1000'}]
lst.sort(key=lambda x:x['prise'],reverse=True)
bigger_price(num,lst)
