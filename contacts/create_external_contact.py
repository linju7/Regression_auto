import sys
import os
from datetime import datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from login_and_url import open_url
from security import accounts

def fill_field(page):
    timestamp = datetime.now().strftime("%m%d%H%M")
    
    # "자세히 입력하기" 버튼 클릭
    page.locator('a:has-text("자세히 입력하기")').click()
    
    # 성
    page.wait_for_selector('input[placeholder="성"][maxlength="100"]', timeout=5000)
    page.locator('input[placeholder="성"][maxlength="100"]').fill("자동화_성")
    
    # 이름
    page.locator('input[placeholder="이름"][maxlength="100"]').fill(f"자동화_{timestamp}")
    
    # 닉네임
    page.locator('input[placeholder="닉네임"][maxlength="100"]').fill("자동화_닉네임")
    
    # 소속
    page.locator('input[placeholder="소속"][maxlength="100"]').fill("자동화_소속")
    
    # 부서
    page.locator('input[placeholder="부서"][maxlength="100"]').fill("자동화_부서")
    
    # 직책
    page.locator('input[placeholder="직책"][maxlength="100"]').fill("자동화_직책")
    
    # 전화번호
    page.locator('input[placeholder="전화번호"][maxlength="100"]').fill(f"010-{timestamp}")
    
    # 이메일
    page.locator('input[placeholder="이메일"][maxlength="256"]').fill(f"test_{timestamp}@example.com")
    
    # 홈페이지
    page.locator('input[placeholder="URL"][maxlength="100"]').fill("https://example.com")
    
    # 생일·기념일
    if page.locator('input[placeholder="yyyymmdd"][maxlength="100"]').count() > 0:
        page.locator('input[placeholder="yyyymmdd"][maxlength="100"]').fill("19991231")
    elif page.locator('input[placeholder="연도. 월. 일."][maxlength="100"]').count() > 0:
        page.locator('input[placeholder="연도. 월. 일."][maxlength="100"]').fill("1999. 12. 31")
    elif page.locator('input[type="date"][maxlength="100"]').count() > 0:
        page.locator('input[type="date"][maxlength="100"]').fill("1999-12-31")
        
    # 메신저·SNS
    page.locator('input[placeholder="ID"][maxlength="100"]').fill("messenger_id")
    
    # 메모
    page.locator('textarea[placeholder="메모(최대 4,000자)"][maxlength="4000"]').fill("자동화 테스트 메모")
    
    
    # TODO : 주소, 공개범위, 편집 허용, 태그 추가 필요
    # 주소
    # page.locator('div.selectbox').nth(1).click()  # 두 번째 selectbox 요소 클릭
    # page.locator('ul > li:has-text("직접입력")').click()  
    # page.locator('input[placeholder="우편번호"][maxlength="20"]').fill("12345")
    # page.locator('input[placeholder="주소"][maxlength="100"]').fill("서울특별시 강남구 테헤란로 123")
    
    return page

def access_create_external_contact(page) :
    # "새로 만들기" 버튼 클릭
    page.locator('a.skin_corp_bg.skin_corp_txt.has_dropdown:has-text("새로 만들기")').click()
    
    # "외부 연락처 직접 입력" 항목 선택
    page.locator('a:has-text("외부 연락처 직접 입력")').first.click()
    
    return page

def click_save(page) :
    page.locator('button.btn_point:has-text("저장")').first.click()
    
    return page
    

def create_external_contact(page, instance, server) :
    page = open_url.open_url(page, instance, server, is_admin = False)
    
    page = access_external_contact_create(page)
    page = fill_field(page)
    page = click_save(page)

    return page