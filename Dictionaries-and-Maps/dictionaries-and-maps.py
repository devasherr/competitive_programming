# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

phoneMap = {}
for _ in range(n):
    person = (input().split())
    phoneMap[person[0]] = person[1]
    
try:
    while True:
        curPerson = input()
        if curPerson in phoneMap:
            print(curPerson + "=" + phoneMap[curPerson])
        else:
            print("Not found")
except EOFError:
    pass
