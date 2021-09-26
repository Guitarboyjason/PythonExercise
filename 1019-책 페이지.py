# N = int(input())

# page_list = [0 for _ in range(10)]


# # for i in range(1,N+1):
# #     tmp_list = list(str(i))
# #     for j in tmp_list:
# #         page_list[int(j)]+=1

# # for i in page_list:
# #     print(i,end=" ")

# #패턴이라는게 있을텐데... 숫자만 보고 바로 판단할 수 있나

# #423 과 400 + 23 은 같다
# #나눠서 생각을 해보자




# # 1의자리 수 : 1~그 수까지 1씩 더함
# # 10의 자리 수 : 0 ~ 9까지 그 수만큼을 더함. 또한 1부터 그 수 전까지 10씩 더함
# # 100의 자리 수 : 0 ~ 9까지 10 * 그 수만큼을 더함. 또한 1부터 그 수까지 100을 더함


# #321까지라고 생각을 해보자. 그럼 300까지 는 같은 패턴을 가짐.
# # 자리수가 내려갈 때 마다 앞의 숫자들이 호출 된다.

# N = list(str(N))
# done_N_list = []
# # for i in range(tmp_range):
# #     for j in range(N[i]):
# #         page_list[]+10**(tmp_range-1)
#     #0번째 원소는 4자리 일 경우 4번째    
#     #어떻게 해야할까 231 이라 가정하면 200 에서 2는 한번, 100은 1이 100번 등장한다.
#     #32에서 백의자리 2 가 32+1번 나온다.
#     #2 에서 십의자리 3이 2+1번 나온다.

#     #4132 라고 할 때 1,2,3,이 1000번씩, 4가 133번 등장
#     #100의 자리에서 0이 100번, 1이 33번
#     #10의 자리에서 0,1,2 가 10번 3이 3번
#     #1의 자리에서 0,1,2가 한번씩

# for i in range(len(N)):
#     if i == 0 :
#         for j in range(1,int(N[i])):
#             page_list[j] += 10**(len(N)-1)
#         done_N_list.append(int(N[i]))
#     else:
#         for j in range(int(N[i])):
#             page_list[j] += 10**(len(N)-i-1)
#         for k in done_N_list:
#             page_list[k] += int(N[i])*10**(len(N)-i-1)
#         done_N_list.append(int(N[i]))
# print(page_list)


#-------------------------------------------------------
#09.26

def count_pages(N,cnt):
    if cnt == 0:
        if  len(N) == 1:            #N이 1의자리 일 때
            for i in range(1,int(N[0])):
                cnt_arr[i] += 1
        else:                       #N이 1의자리가 아닐 때
            for i in range(1,int(N[0])):
                cnt_arr[i] += 10**(len(N)-1)        # 첫번째 자리에 0을 제외하고 + 한다
            cnt_arr[int(N[0])] += (int("".join(N[1:]))+1)
            count_pages(N[1:],1)

    else:                   # 이 함수가 처음 실행이 된 것이 아닐 때
        if len(N) == 1:
            for i in range(0,int(N[0])+1):
                cnt_arr[i] += 1
        else:
            for i in range(int(N[0])):
                cnt_arr[i] += 10 **(len(N)-1)
            cnt_arr[int(N[0])] += (int("".join(N[1:])+1))
            count_pages(N[1:],1)

N = input()                         #str 로 값을 받음
cnt_arr = [0 for _ in range(10)]
for i in range(10):
    cnt_arr[i] += int(N)//10
cnt_arr[0] -= 1
N = list(N)

count_pages(N,0)

if cnt_arr[0] == -1:
    cnt_arr[0] += 1

for i in range(10):
    print(cnt_arr[i],end=" ")







