s= input().strip()
if not s:
    print('')
else:
    groups = []
    current = s[0]
    count = 1
    for char in s[1:]:
        if char == current:
            count+=1
        else:
            groups.append((count, int(current)))
            current = char
            count = 1
    groups.append((count, int(current)))
    print(' '.join(f"({a} , {b})" for a, b in groups))