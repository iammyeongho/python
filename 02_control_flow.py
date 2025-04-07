# 조건문과 반복문

# 1. if-elif-else 조건문
age = 20

if age < 20:
    print("미성년자입니다.")
elif age == 20:
    print("성인이 되었습니다.")
else:
    print("성인입니다.")

# 2. for 반복문
print("\nfor 반복문 예제:")
# 리스트를 이용한 반복
fruits = ["사과", "바나나", "오렌지"]
for fruit in fruits:
    print(fruit)

# range를 이용한 반복
print("\n1부터 5까지 출력:")
for i in range(1, 6):
    print(i)

# 3. while 반복문
print("\nwhile 반복문 예제:")
count = 0
while count < 3:
    print(f"카운트: {count}")
    count += 1

# 4. break와 continue
print("\nbreak 예제:")
for i in range(5):
    if i == 3:
        break
    print(i)

print("\ncontinue 예제:")
for i in range(5):
    if i == 2:
        continue
    print(i)

# 5. 중첩 반복문
print("\n중첩 반복문 예제:")
for i in range(2):
    for j in range(2):
        print(f"i={i}, j={j}")

# 6. 리스트 컴프리헨션
print("\n리스트 컴프리헨션 예제:")
squares = [x**2 for x in range(5)]
print(squares) 