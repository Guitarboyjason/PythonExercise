# def number_adder(N,count,page_list):
#     if count == 0:
#         tmp = N % 10
#         N = int(N/10)
#         for i in range(1,tmp):
#             page_list[i] += 1
#         if N != 0:
#             number_adder(N,count+1,page_list)

#     else:
#         tmp = N % 10
#         N = int(N/10)
#         for i in range(10):
#             page_list[i] += tmp*(10**(count-1))
#         if N != 0:
#             number_adder(N,count+1,page_list)


#         # page_list

N = int(input())

page_list = [0 for _ in range(10)]

# number_adder(N,0,page_list)

for i in range(1,N+1):
    tmp_list = list(str(i))
    for j in tmp_list:
        page_list[int(j)]+=1

for i in page_list:
    print(i,end=" ")