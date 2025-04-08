from database import Database

def print_menu():
    print("\n=== 학생 관리 시스템 ===")
    print("1. 학생 추가")
    print("2. 학생 조회")
    print("3. 전체 학생 목록")
    print("4. 학생 정보 수정")
    print("5. 학생 삭제")
    print("0. 종료")
    print("===================")

def get_student_info():
    name = input("이름: ")
    while True:
        try:
            age = int(input("나이: "))
            break
        except ValueError:
            print("나이는 숫자로 입력해주세요.")
    while True:
        try:
            grade = int(input("학년: "))
            break
        except ValueError:
            print("학년은 숫자로 입력해주세요.")
    return name, age, grade

def main():
    db = Database()
    
    while True:
        print_menu()
        choice = input("선택하세요: ")
        
        if choice == "1":
            print("\n=== 학생 추가 ===")
            name, age, grade = get_student_info()
            student = db.create_student(name, age, grade)
            print(f"\n학생이 추가되었습니다: {student}")
            
        elif choice == "2":
            print("\n=== 학생 조회 ===")
            try:
                student_id = int(input("학생 ID: "))
                student = db.get_student(student_id)
                if student:
                    print(f"\n{student}")
                else:
                    print("\n해당 ID의 학생을 찾을 수 없습니다.")
            except ValueError:
                print("\n올바른 ID를 입력해주세요.")
                
        elif choice == "3":
            print("\n=== 전체 학생 목록 ===")
            students = db.get_all_students()
            if students:
                for student in students:
                    print(student)
            else:
                print("\n등록된 학생이 없습니다.")
                
        elif choice == "4":
            print("\n=== 학생 정보 수정 ===")
            try:
                student_id = int(input("학생 ID: "))
                student = db.get_student(student_id)
                if student:
                    print(f"\n현재 정보: {student}")
                    print("\n수정할 정보를 입력하세요. (변경하지 않을 항목은 엔터를 누르세요)")
                    name = input("이름: ").strip()
                    age_str = input("나이: ").strip()
                    grade_str = input("학년: ").strip()
                    
                    age = int(age_str) if age_str else None
                    grade = int(grade_str) if grade_str else None
                    
                    updated_student = db.update_student(
                        student_id,
                        name if name else None,
                        age,
                        grade
                    )
                    print(f"\n수정된 정보: {updated_student}")
                else:
                    print("\n해당 ID의 학생을 찾을 수 없습니다.")
            except ValueError:
                print("\n올바른 ID를 입력해주세요.")
                
        elif choice == "5":
            print("\n=== 학생 삭제 ===")
            try:
                student_id = int(input("삭제할 학생 ID: "))
                if db.delete_student(student_id):
                    print("\n학생이 삭제되었습니다.")
                else:
                    print("\n해당 ID의 학생을 찾을 수 없습니다.")
            except ValueError:
                print("\n올바른 ID를 입력해주세요.")
                
        elif choice == "0":
            print("\n프로그램을 종료합니다.")
            break
            
        else:
            print("\n잘못된 선택입니다. 다시 선택해주세요.")

if __name__ == "__main__":
    main() 