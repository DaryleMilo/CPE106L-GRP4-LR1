fileName = input('Input file name: ')
lines = []
with open(fileName, 'r') as f:
    for line in f:
        lines.append(line.strip())

while True:
    print ("The file has", len(lines), "lines.")
    if len(lines) == 0:
        break
    lineNumber = int(input("Enter a line number. Input 0 to quit"))
    if lineNumber ==0:
        break
    elif lineNumber > len(lines):
        print("Line number input should be less than or equal to", len(lines))
    else:
        print (lineNumber, ": ", lines[lineNumber -1])