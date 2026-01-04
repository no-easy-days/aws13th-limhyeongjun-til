##실습 3-1 : 이메일 주소 분리하기
작성코드 : 
email = "lhj990118@gmail.com"

parts = email.split("@")

print(parts[0])
print(parts[1])

## 실습 3-2 : 비밀번호 길이 검사
작성코드 :
password1 = input("비밀번호를 입력하세요 : ")

if len(password1) >= 8:
    print("유효한 비밀번호입니다")
else:
    print("비밀번호가 8자 미만입니다")

##실습3-3 : 3의 배수 찾기
작성코드 :
result = []

for x in range(1,21):
    if x % 3 == 0:
        result.append(x)

print(result)

##실습코드 3-4 : 공통 관심사 찾기
작성코드 :
chulsoo = ["축구", "영화", "음악", "게임", "독서"]
younghee = ["영화", "음악", "요리", "여행", "독서"]

set_chulsoo = set(chulsoo)
set_younghee = set(younghee)

common = set_younghee & set_chulsoo

print(f"공통관심사 : {common}")

##실습코드 3-5 : 최고 점수 학생 찾기
작성코드 :
scores = {
    "철수": 85,
    "영희": 92,
    "민수": 78,
    "지수": 95,
    "현우": 88
}

max_score = 0
max_name = ""

for name, score in scores.items():
    if score > max_score:
        max_score = score
        max_name = name


print(f"최고점수학생 : {max_name}, 점수 : {max_score}")
