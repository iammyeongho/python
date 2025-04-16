"""
Playwright 기능 테스트 예제
이 파일은 Playwright를 사용하여 웹 애플리케이션의 기능을 테스트하는 방법을 보여줍니다.
"""

import pytest
from playwright.sync_api import Page, expect
import time

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """브라우저 컨텍스트 설정"""
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
        "ignore_https_errors": True,
    }

@pytest.fixture(autouse=True)
def setup_teardown(page: Page):
    """각 테스트 전후 설정"""
    # 테스트 전 설정
    page.goto("http://localhost:5000")
    yield
    # 테스트 후 정리
    page.close()

def test_user_registration(page: Page):
    """사용자 등록 테스트"""
    # 등록 페이지로 이동
    page.click("text=회원가입")
    
    # 등록 폼 작성
    page.fill("input[name='username']", "testuser")
    page.fill("input[name='email']", "test@example.com")
    page.fill("input[name='password']", "password123")
    page.click("button[type='submit']")
    
    # 성공 메시지 확인
    success_message = page.locator(".alert-success")
    expect(success_message).to_contain_text("회원가입이 완료되었습니다")

def test_user_login(page: Page):
    """사용자 로그인 테스트"""
    # 로그인 페이지로 이동
    page.click("text=로그인")
    
    # 로그인 폼 작성
    page.fill("input[name='email']", "test@example.com")
    page.fill("input[name='password']", "password123")
    page.click("button[type='submit']")
    
    # 로그인 성공 확인
    welcome_message = page.locator(".welcome-message")
    expect(welcome_message).to_contain_text("환영합니다")

def test_post_creation(page: Page):
    """게시글 작성 테스트"""
    # 로그인 먼저 수행
    test_user_login(page)
    
    # 게시글 작성 페이지로 이동
    page.click("text=새 글 작성")
    
    # 게시글 작성 폼 작성
    page.fill("input[name='title']", "테스트 게시글")
    page.fill("textarea[name='content']", "이것은 테스트 게시글입니다.")
    page.click("button[type='submit']")
    
    # 게시글 작성 성공 확인
    success_message = page.locator(".alert-success")
    expect(success_message).to_contain_text("게시글이 작성되었습니다")

def test_post_comment(page: Page):
    """댓글 작성 테스트"""
    # 로그인 먼저 수행
    test_user_login(page)
    
    # 게시글 목록에서 첫 번째 게시글 클릭
    page.click(".post-list .post:first-child")
    
    # 댓글 작성 폼 작성
    page.fill("textarea[name='comment']", "테스트 댓글입니다.")
    page.click("button[type='submit']")
    
    # 댓글 작성 성공 확인
    new_comment = page.locator(".comment-list .comment:last-child")
    expect(new_comment).to_contain_text("테스트 댓글입니다")

def test_error_handling(page: Page):
    """오류 처리 테스트"""
    # 잘못된 이메일로 로그인 시도
    page.click("text=로그인")
    page.fill("input[name='email']", "wrong@example.com")
    page.fill("input[name='password']", "wrongpassword")
    page.click("button[type='submit']")
    
    # 오류 메시지 확인
    error_message = page.locator(".alert-danger")
    expect(error_message).to_contain_text("이메일 또는 비밀번호가 올바르지 않습니다")

def test_navigation(page: Page):
    """네비게이션 테스트"""
    # 메인 페이지로 이동
    page.goto("http://localhost:5000")
    
    # 모든 네비게이션 링크 확인
    nav_links = page.locator("nav a")
    expected_links = ["홈", "게시판", "로그인", "회원가입"]
    
    for link in nav_links.all():
        link_text = link.text_content()
        assert link_text in expected_links
        # 각 링크 클릭 후 페이지 로드 확인
        link.click()
        assert page.url.startswith("http://localhost:5000")

def test_responsive_design(page: Page):
    """반응형 디자인 테스트"""
    # 다양한 화면 크기로 테스트
    screen_sizes = [
        {"width": 1920, "height": 1080},  # 데스크톱
        {"width": 1366, "height": 768},   # 노트북
        {"width": 768, "height": 1024},   # 태블릿
        {"width": 375, "height": 667}     # 모바일
    ]
    
    for size in screen_sizes:
        page.set_viewport_size(size)
        time.sleep(1)  # 레이아웃 변경 대기
        
        # 메뉴 버튼 표시 여부 확인 (모바일)
        if size["width"] <= 768:
            menu_button = page.locator(".menu-button")
            expect(menu_button).to_be_visible()
        else:
            nav_links = page.locator("nav a")
            for link in nav_links.all():
                expect(link).to_be_visible()

def test_keyboard_navigation(page: Page):
    """키보드 네비게이션 테스트"""
    # Tab 키로 포커스 이동
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")
    
    # 현재 포커스된 요소 확인
    focused_element = page.evaluate("document.activeElement.tagName")
    assert focused_element in ["INPUT", "BUTTON", "A"]

def test_accessibility(page: Page):
    """접근성 테스트"""
    # 이미지에 alt 속성 확인
    images = page.locator("img")
    for img in images.all():
        alt_text = img.get_attribute("alt")
        assert alt_text is not None and alt_text != ""
    
    # 폼 요소에 label 연결 확인
    form_inputs = page.locator("input, textarea")
    for input in form_inputs.all():
        input_id = input.get_attribute("id")
        if input_id:
            label = page.locator(f"label[for='{input_id}']")
            expect(label).to_be_visible()

def test_performance(page: Page):
    """성능 테스트"""
    # 페이지 로드 시간 측정
    start_time = time.time()
    page.goto("http://localhost:5000")
    load_time = time.time() - start_time
    assert load_time < 3.0  # 3초 이내 로드
    
    # 네트워크 요청 모니터링
    with page.expect_response("**/*") as response:
        page.click("text=게시판")
        response = response.value
        assert response.status == 200
        assert response.request.resource_type in ["document", "xhr", "fetch"] 