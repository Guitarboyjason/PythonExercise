N = int(input())
name = input()

for _ in range(N):
    old_name = input()
    new_name = ""
    for i in range(int(len(old_name)/len(name))):
        # if i == name[0]:
        #     if new_name == "":
        #         tmp_len = 0
        #         new_name = new_name + i
        #     elif 

        #     else:
        #         tmp_len += 1
        tmp_name = name
        for j in old_name:
            if j == tmp_name[0]:
                while tmp_name != "":
                    if tmp_name