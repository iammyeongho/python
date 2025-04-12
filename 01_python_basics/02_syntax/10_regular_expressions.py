# 파이썬 정규 표현식 예제
# 작성일: 2024-04-08
# 목적: 파이썬의 정규 표현식과 관련된 다양한 기능을 설명하는 예제 코드

# 1. 기본 정규 표현식
# 정규 표현식의 기본적인 사용 방법을 보여줍니다.
print("=== 1. 기본 정규 표현식 ===")

import re

# 문자열 검색
text = "안녕하세요, 파이썬 정규 표현식 예제입니다."
pattern = "파이썬"

# match: 문자열의 시작부터 패턴과 일치하는지 확인
match = re.match(pattern, text)
print(f"match 결과: {match}")  # None (문자열 시작이 '파이썬'이 아님)

# search: 문자열 어디든 패턴과 일치하는지 확인
search = re.search(pattern, text)
print(f"search 결과: {search}")  # <re.Match object; span=(6, 9), match='파이썬'>
if search:
    print(f"찾은 문자열: {search.group()}")
    print(f"시작 위치: {search.start()}")
    print(f"끝 위치: {search.end()}")

# 2. 정규 표현식 패턴
# 다양한 정규 표현식 패턴을 사용하는 방법을 보여줍니다.
print("\n=== 2. 정규 표현식 패턴 ===")

# 문자 클래스
text = "The cat and the hat sat on the mat."
pattern = "[hc]at"  # 'h' 또는 'c'로 시작하고 'at'으로 끝나는 문자열

matches = re.findall(pattern, text)
print(f"문자 클래스 패턴 '{pattern}'으로 찾은 결과: {matches}")

# 반복 패턴
text = "aaaabbbcccddd"
pattern = "a+"  # 'a'가 한 번 이상 반복

matches = re.findall(pattern, text)
print(f"반복 패턴 '{pattern}'으로 찾은 결과: {matches}")

# 선택 패턴
text = "The cat and the dog are pets."
pattern = "cat|dog"  # 'cat' 또는 'dog'

matches = re.findall(pattern, text)
print(f"선택 패턴 '{pattern}'으로 찾은 결과: {matches}")

# 그룹 패턴
text = "홍길동: 010-1234-5678, 김철수: 010-9876-5432"
pattern = r"(\w+): (\d{3}-\d{4}-\d{4})"  # 이름과 전화번호를 그룹으로 묶음

matches = re.findall(pattern, text)
print(f"그룹 패턴 '{pattern}'으로 찾은 결과: {matches}")

for name, phone in matches:
    print(f"이름: {name}, 전화번호: {phone}")

# 3. 정규 표현식 함수
# 정규 표현식 관련 다양한 함수를 사용하는 방법을 보여줍니다.
print("\n=== 3. 정규 표현식 함수 ===")

# findall: 모든 일치 항목 찾기
text = "파이썬, 자바, 파이썬, C++, 파이썬"
pattern = "파이썬"

matches = re.findall(pattern, text)
print(f"findall 결과: {matches}")

# finditer: 모든 일치 항목의 이터레이터 반환
matches = re.finditer(pattern, text)
print("finditer 결과:")
for match in matches:
    print(f"찾은 문자열: {match.group()}, 위치: {match.start()}-{match.end()}")

# split: 패턴으로 문자열 분할
text = "홍길동,김철수,이영희,박지성"
pattern = ","

parts = re.split(pattern, text)
print(f"split 결과: {parts}")

# sub: 패턴과 일치하는 부분을 다른 문자열로 대체
text = "파이썬은 재미있습니다. 파이썬은 강력합니다. 파이썬은 쉽습니다."
pattern = "파이썬"
replacement = "Python"

new_text = re.sub(pattern, replacement, text)
print(f"sub 결과: {new_text}")

# 4. 정규 표현식 플래그
# 정규 표현식 플래그를 사용하는 방법을 보여줍니다.
print("\n=== 4. 정규 표현식 플래그 ===")

# 대소문자 구분 없이 검색 (IGNORECASE)
text = "Python PYTHON python"
pattern = "python"

matches = re.findall(pattern, text)
print(f"대소문자 구분 검색 결과: {matches}")

matches = re.findall(pattern, text, re.IGNORECASE)
print(f"대소문자 구분 없이 검색 결과: {matches}")

# 여러 줄 검색 (MULTILINE)
text = "첫 번째 줄\n두 번째 줄\n세 번째 줄"
pattern = "^두"

matches = re.findall(pattern, text)
print(f"여러 줄 검색 결과 (기본): {matches}")

matches = re.findall(pattern, text, re.MULTILINE)
print(f"여러 줄 검색 결과 (MULTILINE): {matches}")

# 5. 정규 표현식 컴파일
# 정규 표현식을 컴파일하여 재사용하는 방법을 보여줍니다.
print("\n=== 5. 정규 표현식 컴파일 ===")

# 이메일 패턴 컴파일
email_pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

# 이메일 검증
emails = ["user@example.com", "invalid.email", "another.user@domain.co.kr"]

for email in emails:
    if email_pattern.match(email):
        print(f"{email}은(는) 유효한 이메일입니다.")
    else:
        print(f"{email}은(는) 유효하지 않은 이메일입니다.")

# 6. 정규 표현식 그룹
# 정규 표현식 그룹을 사용하는 방법을 보여줍니다.
print("\n=== 6. 정규 표현식 그룹 ===")

# 이름 있는 그룹
text = "홍길동: 010-1234-5678"
pattern = r"(?P<name>\w+): (?P<phone>\d{3}-\d{4}-\d{4})"

match = re.search(pattern, text)
if match:
    print(f"이름: {match.group('name')}")
    print(f"전화번호: {match.group('phone')}")
    print(f"전체 일치: {match.group(0)}")
    print(f"첫 번째 그룹: {match.group(1)}")
    print(f"두 번째 그룹: {match.group(2)}")

# 7. 정규 표현식 전방 탐색
# 정규 표현식 전방 탐색을 사용하는 방법을 보여줍니다.
print("\n=== 7. 정규 표현식 전방 탐색 ===")

# 긍정적 전방 탐색
text = "파이썬3, 파이썬2, 자바, 파이썬4"
pattern = r"파이썬(?=\d)"  # 숫자가 뒤에 오는 '파이썬'

matches = re.findall(pattern, text)
print(f"긍정적 전방 탐색 결과: {matches}")

# 부정적 전방 탐색
text = "파이썬3, 파이썬2, 자바, 파이썬"
pattern = r"파이썬(?!\d)"  # 숫자가 뒤에 오지 않는 '파이썬'

matches = re.findall(pattern, text)
print(f"부정적 전방 탐색 결과: {matches}")

# 8. 정규 표현식 후방 탐색
# 정규 표현식 후방 탐색을 사용하는 방법을 보여줍니다.
print("\n=== 8. 정규 표현식 후방 탐색 ===")

# 긍정적 후방 탐색
text = "가격: 1000원, 가격: 2000원, 가격: 3000원"
pattern = r"(?<=가격: )\d+"  # '가격: ' 뒤에 오는 숫자

matches = re.findall(pattern, text)
print(f"긍정적 후방 탐색 결과: {matches}")

# 부정적 후방 탐색
text = "가격: 1000원, 할인: 500원, 가격: 2000원"
pattern = r"(?<!할인: )\d+"  # '할인: ' 뒤에 오지 않는 숫자

matches = re.findall(pattern, text)
print(f"부정적 후방 탐색 결과: {matches}")

# 9. 정규 표현식 실용적인 예제
# 정규 표현식을 사용한 실용적인 예제를 보여줍니다.
print("\n=== 9. 정규 표현식 실용적인 예제 ===")

# HTML 태그 제거
html = "<p>이것은 <b>HTML</b> 텍스트입니다.</p>"
pattern = r"<[^>]+>"

clean_text = re.sub(pattern, "", html)
print(f"HTML 태그 제거 결과: {clean_text}")

# 전화번호 형식 변환
phone = "010-1234-5678"
pattern = r"(\d{3})-(\d{4})-(\d{4})"
replacement = r"(\1) \2-\3"

formatted_phone = re.sub(pattern, replacement, phone)
print(f"전화번호 형식 변환 결과: {formatted_phone}")

# 이메일 주소 추출
text = "연락처: user@example.com, 다른 이메일: another.user@domain.co.kr"
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

emails = re.findall(pattern, text)
print(f"이메일 주소 추출 결과: {emails}")

print("\n프로그램 종료") 