def permute(start, answer):
    if (len(start) == 0):
        print(answer)
        return
     
    for i in range(len(start)):
        ch = start[i]
        left = start[0:i]
        right = start[i + 1:]
        combined = left + right
        permute(combined, answer + ch)

answer = ""
file = open('file.txt', 'r')
read = file.readlines()

for i in range(len(read)): 
    start = sorted(read[i].strip())
    permute(start, answer)