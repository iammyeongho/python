# 학생 관리 시스템

학생, 학급, 성적, 출석 정보를 관리하는 웹 애플리케이션입니다.

## 기능

### 학급 관리
- 학급 목록 조회
- 학급 추가/수정
- 학급 상세 정보 조회

### 학생 관리
- 학생 추가/수정
- 학생 상세 정보 조회
- 학급별 학생 목록 조회

### 성적 관리
- 성적 추가/수정
- 학생별 성적 조회
- 학급별 성적 조회
- 성적 통계 (평균, 최고점, 최저점, 표준편차)

### 출석 관리
- 출석 정보 추가/수정
- 학생별 출석 조회
- 학급별 출석 조회
- 출석 통계 (출석, 지각, 조퇴, 결석)

## 기술 스택

- **Backend**: Flask 3.0.2
- **Database**: SQLite
- **Frontend**: HTML, CSS (Bootstrap), JavaScript

## 설치 및 실행

1. 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. 필요한 패키지 설치
```bash
pip install -r requirements.txt
```

3. 애플리케이션 실행
```bash
python app.py
```

4. 웹 브라우저에서 접속
```
http://localhost:5000
```

## 프로젝트 구조

```
student_management/
├── app.py              # Flask 애플리케이션
├── models.py           # 데이터 모델
├── database.py         # 데이터베이스 관련 기능
├── requirements.txt    # 필요한 패키지 목록
├── static/             # 정적 파일 (CSS, JS, 이미지)
│   └── css/
│       └── style.css
└── templates/          # HTML 템플릿
    ├── base.html
    ├── class_list.html
    ├── class_detail.html
    ├── class_form.html
    ├── class_grades.html
    ├── class_attendance.html
    ├── student_detail.html
    ├── student_form.html
    ├── grade_form.html
    └── attendance_form.html
```

## 사용 방법

1. 학급 관리
   - 메인 페이지에서 학급 목록 확인
   - "학급 추가" 버튼으로 새 학급 생성
   - 학급 상세 페이지에서 정보 수정

2. 학생 관리
   - 학급 상세 페이지에서 학생 목록 확인
   - "학생 추가" 버튼으로 새 학생 등록
   - 학생 상세 페이지에서 정보 수정

3. 성적 관리
   - 학생 상세 페이지에서 성적 목록 확인
   - "성적 추가" 버튼으로 새 성적 입력
   - 학급 상세 페이지에서 "성적 관리"로 전체 성적 확인

4. 출석 관리
   - 학생 상세 페이지에서 출석 목록 확인
   - "출석 정보 추가" 버튼으로 새 출석 정보 입력
   - 학급 상세 페이지에서 "출석 관리"로 전체 출석 확인

## 라이센스

MIT License 