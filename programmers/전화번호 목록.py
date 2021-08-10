phone_book = ["12","123","1235","567","88"]

def solution(phone_book):
    sort(phone_book)
    for i in range(len(phone_book)-1):
        for j in range(i+1,len(phone_book)):
            if phone_book[i] in phone_book[j]:
                return True
    return False

def sort(phone_book):
    for i in range(len(phone_book)-1,1,-1):
        for j in range(i):
            if len(phone_book[j]) > len(phone_book[i]):
                tmp = phone_book[j]
                phone_book[j] = phone_book[i]
                phone_book[i] = tmp
    
print(solution(phone_book))