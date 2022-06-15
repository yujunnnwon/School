# 피보나치 수열을 계산하는 함수
# 조건: n<=20, fibonacci(0) = 1, fibonacci(1) = 1

# 함수 선언
def fibonacci(num):
    if num == 0 or num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

# 함수 실행
try:
    print("20이하의 양의 정수를 입력하시오.")
    num = int(input())
    if num <= 20:
        print("fibonacci({:2d}) = {:2d}".format(num, fibonacci(num)))
    else:
        print("20이하의 양의 정수를 입력하시오.")
except RecursionError:
    print("음수를 입력하였습니다. 양의 정수를 입력하시오.")
except ValueError:
    print("실수를 입력하였습니다. 양의 정수를 입력하시오.")