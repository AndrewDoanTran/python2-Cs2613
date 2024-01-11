
# def clean_token(x):
#     empty = ""
#     for i in range(len(x)):
#         if x[i] == x[i].upper():
#             x[i] = x[i].lower()
#             empty += x[i]
#         elif x[i].isalpha() != True:
#             x[i]= ""
#             empty += x[i]
#     print(empty) 

# clean_token(String)

# for element in list:
#     if end_start_char(element, element+1) == True:
#         count1 += 1
#     if(element + 1 == list[len(list)-1]):
#         break   

# for x in range(len(list)):
#     print(list[x])

def clean_token(x):
    empty = ""
    for char in x:
        if char.isalpha() == False:
            x = ""
        elif char.isupper() == True:
            x = char.lower()
        else:
            x = char
        empty += x
    return len(empty)



def repeat_letter(x):
    list = []
    i = 0
    check = False
    
    for char in x:
        if char.isalpha() == True:
            list.append(char)
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i].lower() == list[j].lower():
                check = True
                break
    return check          
                


def end_start_char(x,y):
    check = False
    if x[len(x)-1].lower() == y[0].lower():
        check = True
    return check

count = 0
count1 = 0
index = 0

input_sen = input("Input a sentence for statistics:\n")

list = input_sen.split()

while index < len(list):
    if repeat_letter(list[index].lower()) == True:
        count += 1
    index += 1

index = 0

while index < len(list)-1:
    if end_start_char(list[index].lower(), list[index+1].lower()) == True:
        count1 += 1
    if(list[index+1].lower() == list[len(list)-1].lower()):
        break
    index += 1

print()
print("Total number of alphabetic characters:", clean_token(input_sen))
print()
print("Total number of words with repeated alphabetic characters:", count)
print()
print("Total number of end-start letter matches:", count1)
print()

count = 0
count1 = 0
index = 0

input_sen = input("Input a sentence for statistics:\n")

list = input_sen.split()

while index < len(list):
    if repeat_letter(list[index].lower()) == True:
        count += 1
    index += 1

index = 0

while index < len(list)-1:
    if end_start_char(list[index].lower(), list[index+1].lower()) == True:
        count1 += 1
    if(list[index+1].lower() == list[len(list)-1].lower()):
        break
    index += 1

print()
print("Total number of alphabetic characters:", clean_token(input_sen))
print()
print("Total number of words with repeated alphabetic characters:", count)
print()
print("Total number of end-start letter matches:", count1)
