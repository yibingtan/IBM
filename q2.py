record = = input()
for i in range(record):
    value = input().split(' ')

allValid = True
errorCodes = []
for rec in range(record):
    value = input().split(' ')
    if value[1] == False:
        errorCodes.append(value[2])
        allValid = False

if allValid == True:
    print("Yes")
else:
    print("No")
    print(*errorCodes)
