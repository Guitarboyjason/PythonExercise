phone_book = [ "97674223", "1195524421","119"]

def solution(phone_book):
    hash_arr = hash(phone_book)
    for i in hash_arr:
        if i is not [] and len(i) != 1:
            for j in range(len(i)-1):
                for k in range(j+1,len(i)):
                    if j != i :
                        for l in range(1,len(i[j])):
                            if i[j][l] != i[k][l]:
                                break
                            elif l == len(i[j])-1:
                                return False
    return True
def hash(phone_book):
    hash_arr = [[] for _ in range(10)]
    for i in phone_book:
        hash_arr[int(i[0])].append(i)
    print(hash_arr)
    return hash_arr
def sort(hash_arr):
    for i in hash_arr:
        if i != []:
            for j in i:
                break
print(solution(phone_book))