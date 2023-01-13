from itertools import count


s = input()
s = list(s)
ans = ""
for i in range(len(s)):
    if ('0' <= s[i] and s[i] <= '9'):
        ans = ans + s[i]
    elif ('A' <= s[i] and s[i] <= 'Z'):
        ans = ans + s[i]
    elif ('a' <= s[i] and s[i] <= 'z'):
        ans = ans + s[i]

ans = ans.lower()
if (ans[::-1] == ans):
    print("True")
else:
    print("False")
