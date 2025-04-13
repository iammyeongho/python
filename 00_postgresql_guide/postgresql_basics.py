import psycopg2
from psycopg2 import Error
from datetime import datetime

def connect_to_database():
    """
    PostgreSQL 데이터베이스에 연결하는 함수
    
    Returns:
        connection: 데이터베이스 연결 객체
        None: 연결 실패 시
    """
    try:
        # 연결 정보 설정
        # host: 데이터베이스 서버 주소 (localhost는 같은 컴퓨터)
        # database: 연결할 데이터베이스 이름
        # user: 데이터베이스 사용자 이름
        # password: 사용자 비밀번호
        connection = psycopg2.connect(
            host="localhost",
            database="postgres",  # 기본 데이터베이스
            user="postgres",      # 기본 사용자
            password="password"   # 설정한 비밀번호
        )
        print("PostgreSQL 데이터베이스에 성공적으로 연결되었습니다.")
        return connection
    except Error as e:
        print(f"PostgreSQL 연결 중 오류가 발생했습니다: {e}")
        return None

def create_database(connection, dbname):
    """
    새로운 데이터베이스를 생성하는 함수
    
    Args:
        connection: 데이터베이스 연결 객체
        dbname: 생성할 데이터베이스 이름
    """
    try:
        # autocommit 모드 설정 (데이터베이스 생성 시 필요)
        connection.autocommit = True
        cursor = connection.cursor()
        
        # 데이터베이스 생성 쿼리 실행
        cursor.execute(f"CREATE DATABASE {dbname}")
        print(f"데이터베이스 '{dbname}'가 생성되었습니다.")
    except Error as e:
        print(f"데이터베이스 생성 중 오류가 발생했습니다: {e}")

def create_table(connection):
    """
    학생 정보를 저장하는 테이블을 생성하는 함수
    
    Args:
        connection: 데이터베이스 연결 객체
    """
    try:
        cursor = connection.cursor()
        
        # 테이블 생성 쿼리
        # SERIAL: 자동 증가 정수 (MySQL의 AUTO_INCREMENT와 유사)
        # PRIMARY KEY: 기본 키 제약 조건
        # UNIQUE: 유니크 제약 조건
        # NOT NULL: NULL 값 허용하지 않음
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS students (
            id SERIAL PRIMARY KEY,           -- 자동 증가 기본 키
            name VARCHAR(100) NOT NULL,      -- 학생 이름
            student_id VARCHAR(20) UNIQUE NOT NULL,  -- 학번 (유니크)
            grade INTEGER NOT NULL,          -- 학년
            major VARCHAR(100) NOT NULL,     -- 전공
            birth_date DATE NOT NULL,        -- 생년월일
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- 레코드 생성 시간
        )
        '''
        cursor.execute(create_table_query)
        connection.commit()
        print("테이블이 성공적으로 생성되었습니다.")
    except Error as e:
        print(f"테이블 생성 중 오류가 발생했습니다: {e}")

def insert_data(connection):
    """
    샘플 학생 데이터를 삽입하는 함수
    
    Args:
        connection: 데이터베이스 연결 객체
    """
    try:
        cursor = connection.cursor()
        
        # 데이터 삽입 쿼리
        # %s: 파라미터화된 쿼리 (SQL 인젝션 방지)
        insert_query = '''
        INSERT INTO students (name, student_id, grade, major, birth_date)
        VALUES (%s, %s, %s, %s, %s)
        '''
        
        # 샘플 데이터
        sample_data = [
            ('홍길동', '20230001', 1, '컴퓨터공학', '2000-01-01'),
            ('김철수', '20230002', 2, '전자공학', '1999-05-15'),
            ('이영희', '20230003', 3, '기계공학', '1998-11-30')
        ]
        
        # 여러 레코드를 한 번에 삽입
        cursor.executemany(insert_query, sample_data)
        connection.commit()
        print("데이터가 성공적으로 삽입되었습니다.")
    except Error as e:
        print(f"데이터 삽입 중 오류가 발생했습니다: {e}")

def select_data(connection):
    """
    학생 데이터를 조회하는 함수
    
    Args:
        connection: 데이터베이스 연결 객체
    """
    try:
        cursor = connection.cursor()
        
        # 모든 학생 데이터 조회
        select_query = "SELECT * FROM students"
        cursor.execute(select_query)
        
        # 모든 결과 레코드 가져오기
        records = cursor.fetchall()
        
        print("\n학생 목록:")
        for row in records:
            print(f"ID: {row[0]}, 이름: {row[1]}, 학번: {row[2]}, 학년: {row[3]}, 전공: {row[4]}, 생년월일: {row[5]}")
    except Error as e:
        print(f"데이터 조회 중 오류가 발생했습니다: {e}")

def update_data(connection):
    """
    학생 데이터를 수정하는 함수
    
    Args:
        connection: 데이터베이스 연결 객체
    """
    try:
        cursor = connection.cursor()
        
        # 데이터 수정 쿼리
        # WHERE 절로 수정할 레코드 지정
        update_query = '''
        UPDATE students
        SET grade = %s
        WHERE name = %s
        '''
        
        # 홍길동 학생의 학년을 4학년으로 수정
        cursor.execute(update_query, (4, '홍길동'))
        connection.commit()
        print("데이터가 성공적으로 수정되었습니다.")
    except Error as e:
        print(f"데이터 수정 중 오류가 발생했습니다: {e}")

def delete_data(connection):
    """
    학생 데이터를 삭제하는 함수
    
    Args:
        connection: 데이터베이스 연결 객체
    """
    try:
        cursor = connection.cursor()
        
        # 데이터 삭제 쿼리
        # WHERE 절로 삭제할 레코드 지정
        delete_query = "DELETE FROM students WHERE name = %s"
        
        # 이영희 학생 데이터 삭제
        cursor.execute(delete_query, ('이영희',))
        connection.commit()
        print("데이터가 성공적으로 삭제되었습니다.")
    except Error as e:
        print(f"데이터 삭제 중 오류가 발생했습니다: {e}")

def main():
    """
    메인 함수: 모든 데이터베이스 작업을 순차적으로 실행
    """
    # 데이터베이스 연결
    connection = connect_to_database()
    if not connection:
        return

    try:
        # 테이블 생성
        create_table(connection)
        
        # 데이터 삽입
        insert_data(connection)
        
        # 데이터 조회
        select_data(connection)
        
        # 데이터 수정
        update_data(connection)
        print("\n수정 후 데이터:")
        select_data(connection)
        
        # 데이터 삭제
        delete_data(connection)
        print("\n삭제 후 데이터:")
        select_data(connection)
        
    finally:
        # 연결 종료 (리소스 정리)
        if connection:
            connection.close()
            print("\nPostgreSQL 연결이 종료되었습니다.")

if __name__ == "__main__":
    main() 