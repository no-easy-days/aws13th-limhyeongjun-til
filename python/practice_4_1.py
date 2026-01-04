## 실습 4-1 : 등급 판정
작성코드 :
score = int(input("점수를 입력하세요: "))



if 100>= score >= 90:
    print("A")
elif 90 > score >= 80:
    print("B")
elif 80 > score >= 70:
    print("C")
elif 70 > score >= 60:
    print("D")
elif 60 > score >=0:
    print("F")
else:
    print("잘못된 입력입니다")

## 실습 4-2 : 구구단 출력
작성코드 :
dan = int(input("원하는 단을 입력해주세요 : "))

print(f"\n=== {dan}단 === ")
for num in range(1, 10):
    result = dan * num
    print(f"{dan} x {num} = {result}")

## 실습 4-3 : 소수판별(도전!)
작성코드 : 
for number1 in range(2, 101):
    for number2 in range(2, number1):
        if number1 % number2 == 0:
            break
    else:
        print(number1)

## 실습 4-4 : 숫자 맞추기 게임 (도전!)
작성코드 :
import random
answer = random.randint(1, 100)
attempts = 0

while True:
    user_answer = int(input("정답을 입력해주세요 : "))
    attempts += 1
    if user_answer < answer:
        print("더 큰 수를 입력하세요")
    elif user_answer > answer:
        print("더 작은 수를 입력하세요")
    else:
        print(f"정답입니다! {attempts}번만에 맞추셨습니다!")

        break
