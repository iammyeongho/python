# 파이썬 데이터 타입 예제
# 작성일: 2024-04-08
# 목적: 파이썬의 다양한 데이터 타입과 그 사용법을 설명하는 예제 코드

# 1. 숫자형 (Number)
# 파이썬은 정수(int), 실수(float), 복소수(complex) 타입을 지원합니다.
print("=== 1. 숫자형 (Number) ===")

# 정수형 (int)
# 파이썬의 정수는 크기 제한이 없으며, 메모리가 허용하는 한 무한히 큰 수를 다룰 수 있습니다.
integer = 42
print(f"정수: {integer}, 타입: {type(integer)}")
print(f"큰 정수: {2**100}, 타입: {type(2**100)}")

# 실수형 (float)
# 실수는 부동 소수점 숫자로, 소수점이 있는 숫자를 나타냅니다.
float_num = 3.14
print(f"실수: {float_num}, 타입: {type(float_num)}")
print(f"과학적 표기법: {1.23e-4}, 타입: {type(1.23e-4)}")

# 복소수형 (complex)
# 복소수는 실수부와 허수부로 구성된 숫자입니다.
complex_num = 1 + 2j
print(f"복소수: {complex_num}, 타입: {type(complex_num)}")
print(f"실수부: {complex_num.real}, 허수부: {complex_num.imag}")

# 2. 문자열 (String)
# 문자열은 문자들의 시퀀스로, 작은따옴표(') 또는 큰따옴표(")로 둘러싸여 있습니다.
print("\n=== 2. 문자열 (String) ===")

# 기본 문자열
string1 = "안녕하세요"
string2 = '파이썬'
print(f"기본 문자열: {string1}, 타입: {type(string1)}")
print(f"작은따옴표 문자열: {string2}, 타입: {type(string2)}")

# 여러 줄 문자열
# 삼중 따옴표를 사용하여 여러 줄의 문자열을 만들 수 있습니다.
multi_line = """이것은
여러 줄의
문자열입니다."""
print(f"여러 줄 문자열:\n{multi_line}")

# 문자열 연산
print("\n문자열 연산:")
print(f"문자열 연결: {string1 + ' ' + string2}")
print(f"문자열 반복: {'*' * 5}")
print(f"문자열 길이: {len(string1)}")
print(f"문자열 인덱싱: {string1[0]}")
print(f"문자열 슬라이싱: {string1[0:2]}")

# 3. 불리언 (Boolean)
# 불리언은 True와 False 두 가지 값만 가질 수 있는 논리형 데이터 타입입니다.
print("\n=== 3. 불리언 (Boolean) ===")

# 기본 불리언 값
boolean_true = True
boolean_false = False
print(f"True: {boolean_true}, 타입: {type(boolean_true)}")
print(f"False: {boolean_false}, 타입: {type(boolean_false)}")

# 불리언 연산
print("\n불리언 연산:")
print(f"True and True: {True and True}")
print(f"True or False: {True or False}")
print(f"not True: {not True}")

# 4. None 타입
# None은 값이 없음을 나타내는 특별한 타입입니다.
print("\n=== 4. None 타입 ===")

none_value = None
print(f"None: {none_value}, 타입: {type(none_value)}")

# 5. 시퀀스 타입
# 시퀀스는 순서가 있는 데이터의 집합입니다.
print("\n=== 5. 시퀀스 타입 ===")

# 리스트 (List)
# 리스트는 변경 가능한(mutable) 시퀀스입니다.
my_list = [1, "두", 3.0, True]
print(f"리스트: {my_list}, 타입: {type(my_list)}")
print(f"리스트 길이: {len(my_list)}")
print(f"리스트 인덱싱: {my_list[0]}")
print(f"리스트 슬라이싱: {my_list[1:3]}")

# 튜플 (Tuple)
# 튜플은 변경 불가능한(immutable) 시퀀스입니다.
my_tuple = (1, "두", 3.0, True)
print(f"\n튜플: {my_tuple}, 타입: {type(my_tuple)}")
print(f"튜플 길이: {len(my_tuple)}")
print(f"튜플 인덱싱: {my_tuple[0]}")
print(f"튜플 슬라이싱: {my_tuple[1:3]}")

# 6. 매핑 타입
# 매핑은 키-값 쌍으로 데이터를 저장합니다.
print("\n=== 6. 매핑 타입 ===")

# 딕셔너리 (Dictionary)
# 딕셔너리는 키-값 쌍의 집합입니다.
my_dict = {
    "이름": "홍길동",
    "나이": 25,
    "직업": "학생"
}
print(f"딕셔너리: {my_dict}, 타입: {type(my_dict)}")
print(f"딕셔너리 키: {list(my_dict.keys())}")
print(f"딕셔너리 값: {list(my_dict.values())}")
print(f"딕셔너리 항목: {list(my_dict.items())}")

# 7. 집합 타입
# 집합은 중복되지 않은 요소들의 집합입니다.
print("\n=== 7. 집합 타입 ===")

# 집합 (Set)
my_set = {1, 2, 3, 3, 4, 4, 5}  # 중복된 값은 자동으로 제거됩니다
print(f"집합: {my_set}, 타입: {type(my_set)}")
print(f"집합 길이: {len(my_set)}")

# 집합 연산
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(f"\n집합 연산:")
print(f"합집합: {set1 | set2}")
print(f"교집합: {set1 & set2}")
print(f"차집합: {set1 - set2}")
print(f"대칭차집합: {set1 ^ set2}")

print("\n프로그램 종료") 