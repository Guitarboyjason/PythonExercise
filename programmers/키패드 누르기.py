numbers = [1,3,4,5,8,2,1,4,5,9,5]

hand = "right"
result = ""
left = 10
right = 12
left_to_middle = 100
right_to_middle = 100
left_count = 0
right_count = 0

for i in numbers:
    if i in [1,4,7]:
        result += "L"
        left = i
    elif i in [3,6,9]:
        result += "R"
        right = i
    else:
        if i == 0:
            i = 11
        if i > left:
            if left in [1,4,7,10] :
                left_to_middle = left + 1
                left_count = 1
            else:
                left_to_middle = left
                left_count = 0
            while left_to_middle != i :
                left_to_middle += 3
                left_count += 1
        else:            
            if left in [1,4,7,10] :
                left_to_middle = left + 1
                left_count = 1
            else:
                left_to_middle = left
                left_count = 0
            while left_to_middle != i :
                left_to_middle -= 3
                left_count += 1
        if i > right:
            if right in [3,6,9,12] :
                right_to_middle = right - 1
                right_count = 1
            else:
                right_to_middle = right
                right_count = 0
            while right_to_middle != i :
                right_to_middle += 3
                right_count += 1
        else:            
            if right in [3,6,9,12] :
                right_to_middle = right - 1
                right_count = 1
            else:
                right_to_middle = right
                right_count = 0
            while right_to_middle != i :
                right_to_middle -= 3
                right_count += 1
        if left_count > right_count or (left_count == right_count and hand == "right"):
            right = i
            result += "R"
        elif left_count < right_count or (left_count == right_count and hand == "left"):
            left = i
            result += "L"
print(result)