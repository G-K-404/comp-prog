lines = []
while True:
    try:
        line = input()
        line=line.strip()
        if not line:
            break
        lines.append(line)
    except EOFError:
        break
ans = {}
for x in lines:
    if('-' not in x):
        continue
    a, b = x.split("-")
    ans[a] = int(b)

ans = sorted(ans.items(), key=lambda item: item[1], reverse=True)

print(ans[0][0])