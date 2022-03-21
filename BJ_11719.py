	
import sys
print(sys.stdin.read())


while True:
    try:
        print(input())
    except EOFError:
        break


#입력 이후 end of file일 경우에 컴파일 중단
#sys.stdin.read() eof 전까지 모두 입력 가능
#while 반복문 eof 시 break하여 종료