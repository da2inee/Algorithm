X = int(input())
line = 0
end = 0
while X > end:
    line += 1
    end += line 
diff = end - X
if line % 2 == 0:
    top = line - diff
    bottom = 1 + diff
if line % 2 == 1:
    top = 1 + diff
    bottom = line - diff
print("%d/%d"%(top,bottom))
