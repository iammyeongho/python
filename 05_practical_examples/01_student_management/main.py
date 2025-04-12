# 학생 관리 시스템 - 메인 프로그램
# 작성일: 2024-04-09
# 목적: 학생 정보 관리 시스템의 사용자 인터페이스 제공

from typing import Optional
from models import Student
from database import Database

class StudentManagementSystem:
    """
    학생 관리 시스템의 메인 클래스
    
    속성:
        db (Database): 데이터베이스 연결 객체
    """
    
    def __init__(self):
        """시스템 초기화"""
        self.db = Database()
    
    def input_student_info(self) -> Student:
        """
        사용자로부터 학생 정보를 입력받음
        
        반환:
            Student: 입력된 학생 정보를 담은 객체
        """
        print("\n=== 학생 정보 입력 ===")
        name = input("이름: ").strip()
        while True:
            try:
                age = int(input("나이: ").strip())
                if age > 0:
                    break
                print("나이는 양수여야 합니다.")
            except ValueError:
                print("올바른 나이를 입력하세요.")
        
        grade = input("학년: ").strip()
        major = input("전공: ").strip()
        
        return Student(name=name, age=age, grade=grade, major=major)
    
    def add_student(self) -> None:
        """새로운 학생을 추가"""
        student = self.input_student_info()
        student_id = self.db.add_student(student)
        print(f"\n학생이 추가되었습니다. (ID: {student_id})")
    
    def view_student(self) -> None:
        """학생 정보를 조회"""
        try:
            student_id = int(input("\n조회할 학생 ID: ").strip())
            student = self.db.get_student(student_id)
            
            if student:
                print("\n=== 학생 정보 ===")
                print(student)
            else:
                print(f"\nID {student_id}인 학생을 찾을 수 없습니다.")
        except ValueError:
            print("\n올바른 ID를 입력하세요.")
    
    def list_students(self) -> None:
        """모든 학생 목록을 조회"""
        students = self.db.get_all_students()
        
        if students:
            print("\n=== 학생 목록 ===")
            for student in students:
                print(student)
        else:
            print("\n등록된 학생이 없습니다.")
    
    def update_student(self) -> None:
        """학생 정보를 수정"""
        try:
            student_id = int(input("\n수정할 학생 ID: ").strip())
            student = self.db.get_student(student_id)
            
            if student:
                print("\n=== 현재 정보 ===")
                print(student)
                print("\n새로운 정보를 입력하세요.")
                
                updated_student = self.input_student_info()
                updated_student.id = student_id
                
                if self.db.update_student(updated_student):
                    print("\n학생 정보가 수정되었습니다.")
                else:
                    print("\n학생 정보 수정에 실패했습니다.")
            else:
                print(f"\nID {student_id}인 학생을 찾을 수 없습니다.")
        except ValueError:
            print("\n올바른 ID를 입력하세요.")
    
    def delete_student(self) -> None:
        """학생을 삭제"""
        try:
            student_id = int(input("\n삭제할 학생 ID: ").strip())
            student = self.db.get_student(student_id)
            
            if student:
                print("\n=== 삭제할 학생 정보 ===")
                print(student)
                confirm = input("\n정말 삭제하시겠습니까? (y/n): ").strip().lower()
                
                if confirm == 'y':
                    if self.db.delete_student(student_id):
                        print("\n학생이 삭제되었습니다.")
                    else:
                        print("\n학생 삭제에 실패했습니다.")
                else:
                    print("\n삭제가 취소되었습니다.")
            else:
                print(f"\nID {student_id}인 학생을 찾을 수 없습니다.")
        except ValueError:
            print("\n올바른 ID를 입력하세요.")
    
    def search_students(self) -> None:
        """학생을 검색"""
        keyword = input("\n검색할 키워드: ").strip()
        students = self.db.search_students(keyword)
        
        if students:
            print(f"\n=== '{keyword}' 검색 결과 ===")
            for student in students:
                print(student)
        else:
            print(f"\n'{keyword}'와 일치하는 학생이 없습니다.")
    
    def show_menu(self) -> None:
        """메인 메뉴를 표시"""
        print("\n=== 학생 관리 시스템 ===")
        print("1. 학생 추가")
        print("2. 학생 조회")
        print("3. 학생 목록")
        print("4. 학생 수정")
        print("5. 학생 삭제")
        print("6. 학생 검색")
        print("0. 종료")
    
    def run(self) -> None:
        """프로그램 실행"""
        while True:
            self.show_menu()
            choice = input("\n선택: ").strip()
            
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.view_student()
            elif choice == '3':
                self.list_students()
            elif choice == '4':
                self.update_student()
            elif choice == '5':
                self.delete_student()
            elif choice == '6':
                self.search_students()
            elif choice == '0':
                print("\n프로그램을 종료합니다.")
                break
            else:
                print("\n잘못된 선택입니다. 다시 선택하세요.")

if __name__ == "__main__":
    system = StudentManagementSystem()
    system.run() 