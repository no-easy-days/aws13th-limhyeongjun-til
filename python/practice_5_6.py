##실습 1 : 정렬하기

작성코드 :
cities = [
    {"name": "서울", "population": 9700000},
    {"name": "부산", "population": 3400000},
    {"name": "인천", "population": 2900000},
    {"name": "대구", "population": 2400000}
]

sorted_cities = sorted(cities, key=lambda x: x["population"])

for city in sorted_cities:
    print(f"{city['name']}: {city['population']:,}명")


##실습 2 : 데이터 변환

작성코드  :
str_numbers = ["10", "20", "30", "40", "50"]

result = []

for x in str_numbers:
    result.append(int(x) + 100)

print(result)

작성코드(수정) :  #람다를 쓰지않아서 다시...
result = list(map(lambda x: x + 100, map(int, str_numbers)))
print(result)

##실습 3 : 필터링

작성코드 :
products = [
    {"name": "노트북", "discount": 15},
    {"name": "마우스", "discount": 25},
    {"name": "키보드", "discount": 30},
    {"name": "모니터", "discount": 10}
]

discounted = list(filter(lambda x: x["discount"] >= 20, products))
print(discounted)
