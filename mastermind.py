n = int(input())
secret_code = int(input())
list_of_guess = []
list_of_pos = []
list_of_neg = []

def compare_two_numbers(num1, num2):
    posVal = negVal = 0
    used_list_num1 = []
    used_list_num2 = []
    for i in range (len(str(num1))):
        if(str(num1)[i] == str(num2)[i]):
            flag = 1
            for x in used_list_num1:
                if(x == i):
                    flag = 0
            for y in used_list_num2:
                if(y == i):
                    flag = 0
            if(flag == 0):
                continue
            else:                
                posVal += 1
                used_list_num1.append(i)
                used_list_num2.append(i)
                continue
        for j in range (len(str(num2))):
            if(str(num1)[i] == str(num2)[j]):
                flag = 1
                for x in used_list_num1:
                    if(x == i):
                        flag = 0
                for y in used_list_num2:
                    if(y == j):
                        flag = 0
                if(flag == 0):
                    continue
                else:
                    used_list_num1.append(i)
                    used_list_num2.append(j)
                    negVal += 1
                    break
    return posVal, negVal

list_of_guess.append(10**(n-1))
a, b = compare_two_numbers(secret_code, 10**(n-1))
list_of_pos.append(a)
list_of_neg.append(b)
for i in range(10**(n-1)+1, (10**n)-1):
    flag = 1   
    for j in range(len(list_of_guess)):
        a, b = compare_two_numbers(i, list_of_guess[j])
        if(list_of_pos[j] != a or list_of_neg[j] != b):
            flag = 0
            break
    if(flag == 0):
        continue
    else:
        list_of_guess.append(i)
        c, d = compare_two_numbers(secret_code, i)
        list_of_pos.append(c)
        list_of_neg.append(d)
        if(c == n):
            for num in list_of_guess:
                print(num)
            print("Found the secret code", secret_code)
            break
print("Guess list: ", list_of_guess)
print("# of digits in correct position:  ",list_of_pos)
print("# of digits in incorrect position: ",list_of_neg)

