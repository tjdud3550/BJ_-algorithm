

from array import array


n= int(input())
array = []
array = list(map(int,str(n)))
array.sort(reverse=True)
for n in  array:
    print(n, end ="")

#str() 함수 이용하여 정수를문자열로 변환
#f-포맷을 이용하여 python에서 정수를 문자열로 변환 
