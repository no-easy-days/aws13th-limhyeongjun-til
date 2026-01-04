## 실습 5-1 : 계산기 함수
작성코드 :
def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            return "0으로 나눌 수 없습니다"
        return a / b
    else:
        return "지원하지 않는 연산자입니다"

    pass

print(calculator(10, 5, '+'))
print(calculator(10, 5, '-'))
print(calculator(10, 5, '*'))
print(calculator(10, 5, '/'))
print(calculator(10, 0, '/'))
print(calculator(10, 5, '%'))

##실습 5-2 : 학생 성적 처리
작성 코드 : 
def print_report(name, scores):

    average = sum(scores) / len(scores)
    high_score = max(scores)
    low_score = min(scores)

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"==={name} 성적표 ===")
    print(f"점수: {scores}")
    print(f"평균: {average:.1f}점")
    print(f"최고점: {high_score}점" )
    print(f"최저점: {low_score}점")
    print(f"등급: {grade}")

    pass

print_report("김철수", [85, 92, 78, 96, 88])

##실습 5-3 : 비밀번호 검증
작성코드 :

def validate_password(password):

    if len(password) < 8:
        return (False, "8자 이상이어야 합니다") #괄호 없어도됨(파이썬에서는 False, "메세지" 이거 자체가 튜플이라 ()없어도됨/ 초보자는 가독성을 높이기위해 써도 상관없음)

    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break

    if not has_digit:
        return (False, "숫자를 포합해야 합니다")

    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break

    if not has_upper:
        return (False, "대문자를 포함해야 합니다")

    return (True, "유효한 비밀번호입니다")


    pass

print(validate_password("abc"))
print(validate_password("abcdefgh"))
print(validate_password("abcdefg1"))
print(validate_password("Abcdefg1"))
