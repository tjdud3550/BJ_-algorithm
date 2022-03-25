s = list(input())
for i in range(len(s)):
    if 90 >= ord(s[i]) >= 65:
        if (ord(s[i])+13) > 90:
            s[i] = chr(ord(s[i])-13)
        else:
            s[i] = chr(ord(s[i])+13)
    elif 122 >= ord(s[i]) >= 97:
        if (ord(s[i])+13) > 122:
            s[i] = chr(ord(s[i])-13)
        else:
            s[i] = chr(ord(s[i])+13)
print(*s,sep="")
      


#아스키 코드는 대문자랑 소문자가 아싀 번호가 다르다.
#대문자 65-90   
#소문자 97-122
