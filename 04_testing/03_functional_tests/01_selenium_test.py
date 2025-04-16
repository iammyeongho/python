"""
Selenium 기능 테스트 예제
이 파일은 Selenium을 사용하여 웹 애플리케이션의 기능을 테스트하는 방법을 보여줍니다.
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

class TestWebApp(unittest.TestCase):
    """웹 애플리케이션 기능 테스트"""

    @classmethod
    def setUpClass(cls):
        """테스트 클래스 시작 시 호출됩니다."""
        # Chrome 드라이버 초기화
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)  # 암시적 대기 설정
        cls.wait = WebDriverWait(cls.driver, 10)  # 명시적 대기 설정

    @classmethod
    def tearDownClass(cls):
        """테스트 클래스 종료 시 호출됩니다."""
        cls.driver.quit()

    def setUp(self):
        """각 테스트 메서드 실행 전에 호출됩니다."""
        # 테스트용 웹 애플리케이션 URL
        self.base_url = "http://localhost:5000"
        self.driver.get(self.base_url)

    def test_user_registration(self):
        """사용자 등록 테스트"""
        # 등록 페이지로 이동
        register_link = self.driver.find_element(By.LINK_TEXT, "회원가입")
        register_link.click()

        # 등록 폼 작성
        username_input = self.driver.find_element(By.NAME, "username")
        email_input = self.driver.find_element(By.NAME, "email")
        password_input = self.driver.find_element(By.NAME, "password")
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        username_input.send_keys("testuser")
        email_input.send_keys("test@example.com")
        password_input.send_keys("password123")
        submit_button.click()

        # 성공 메시지 확인
        success_message = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "alert-success"))
        )
        self.assertIn("회원가입이 완료되었습니다", success_message.text)

    def test_user_login(self):
        """사용자 로그인 테스트"""
        # 로그인 페이지로 이동
        login_link = self.driver.find_element(By.LINK_TEXT, "로그인")
        login_link.click()

        # 로그인 폼 작성
        email_input = self.driver.find_element(By.NAME, "email")
        password_input = self.driver.find_element(By.NAME, "password")
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        email_input.send_keys("test@example.com")
        password_input.send_keys("password123")
        submit_button.click()

        # 로그인 성공 확인
        welcome_message = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "welcome-message"))
        )
        self.assertIn("환영합니다", welcome_message.text)

    def test_post_creation(self):
        """게시글 작성 테스트"""
        # 로그인 먼저 수행
        self.test_user_login()

        # 게시글 작성 페이지로 이동
        new_post_link = self.driver.find_element(By.LINK_TEXT, "새 글 작성")
        new_post_link.click()

        # 게시글 작성 폼 작성
        title_input = self.driver.find_element(By.NAME, "title")
        content_input = self.driver.find_element(By.NAME, "content")
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        title_input.send_keys("테스트 게시글")
        content_input.send_keys("이것은 테스트 게시글입니다.")
        submit_button.click()

        # 게시글 작성 성공 확인
        success_message = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "alert-success"))
        )
        self.assertIn("게시글이 작성되었습니다", success_message.text)

    def test_post_comment(self):
        """댓글 작성 테스트"""
        # 로그인 먼저 수행
        self.test_user_login()

        # 게시글 목록에서 첫 번째 게시글 클릭
        first_post = self.driver.find_element(By.CSS_SELECTOR, ".post-list .post:first-child")
        first_post.click()

        # 댓글 작성 폼 작성
        comment_input = self.driver.find_element(By.NAME, "comment")
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        comment_input.send_keys("테스트 댓글입니다.")
        submit_button.click()

        # 댓글 작성 성공 확인
        new_comment = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".comment-list .comment:last-child"))
        )
        self.assertIn("테스트 댓글입니다", new_comment.text)

    def test_error_handling(self):
        """오류 처리 테스트"""
        # 잘못된 이메일로 로그인 시도
        login_link = self.driver.find_element(By.LINK_TEXT, "로그인")
        login_link.click()

        email_input = self.driver.find_element(By.NAME, "email")
        password_input = self.driver.find_element(By.NAME, "password")
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        email_input.send_keys("wrong@example.com")
        password_input.send_keys("wrongpassword")
        submit_button.click()

        # 오류 메시지 확인
        error_message = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "alert-danger"))
        )
        self.assertIn("이메일 또는 비밀번호가 올바르지 않습니다", error_message.text)

    def test_navigation(self):
        """네비게이션 테스트"""
        # 메인 페이지로 이동
        self.driver.get(self.base_url)

        # 모든 네비게이션 링크 확인
        nav_links = self.driver.find_elements(By.CSS_SELECTOR, "nav a")
        expected_links = ["홈", "게시판", "로그인", "회원가입"]

        for link in nav_links:
            self.assertIn(link.text, expected_links)
            # 각 링크 클릭 후 페이지 로드 확인
            link.click()
            self.assertTrue(self.driver.current_url.startswith(self.base_url))

    def test_responsive_design(self):
        """반응형 디자인 테스트"""
        # 다양한 화면 크기로 테스트
        screen_sizes = [
            (1920, 1080),  # 데스크톱
            (1366, 768),   # 노트북
            (768, 1024),   # 태블릿
            (375, 667)     # 모바일
        ]

        for width, height in screen_sizes:
            self.driver.set_window_size(width, height)
            time.sleep(1)  # 레이아웃 변경 대기

            # 메뉴 버튼 표시 여부 확인 (모바일)
            if width <= 768:
                menu_button = self.driver.find_element(By.CLASS_NAME, "menu-button")
                self.assertTrue(menu_button.is_displayed())
            else:
                nav_links = self.driver.find_elements(By.CSS_SELECTOR, "nav a")
                for link in nav_links:
                    self.assertTrue(link.is_displayed())

if __name__ == '__main__':
    unittest.main() 