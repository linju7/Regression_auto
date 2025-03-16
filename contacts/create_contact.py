import sys
import os
from datetime import datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from login import open_url
from security import accounts


def fill_field(page):
    timestamp = datetime.now().strftime("%m%d%H%M")
    
    # 모든 항목 표시 버튼 클릭
    page.wait_for_selector('button.opt_toggle.fold', state='visible')
    page.locator('button.opt_toggle.fold', has_text="모든 항목 표시").click()

    # 성
    page.wait_for_selector('input.lw_input[placeholder="성"][maxlength="80"]', timeout=5000)  # 5초 기다리기
    page.locator('input.lw_input[placeholder="성"][maxlength="80"]').fill("자동화_")

    # 이름
    page.locator('input.lw_input[placeholder="이름"][maxlength="80"]').fill(timestamp)
    
    # 다국어
    # 다국어 off 시 입력란이 없기 때문에, 조건문으로 존재하는지 체크를 하는 로직 추가함 
    if page.locator('input.lw_input[placeholder="姓(日本語)"]').count() > 0:
        page.locator('input.lw_input[placeholder="姓(日本語)"]').fill("일본어성")
    if page.locator('input.lw_input[placeholder="名(日本語)"]').count() > 0:
        page.locator('input.lw_input[placeholder="名(日本語)"]').fill("일본어이름")
    if page.locator('input.lw_input[placeholder="Last"]').count() > 0:
        page.locator('input.lw_input[placeholder="Last"]').fill("영어성")
    if page.locator('input.lw_input[placeholder="First"]').count() > 0:
        page.locator('input.lw_input[placeholder="First"]').fill("영어이름")
    if page.locator('input.lw_input[placeholder="성"][maxlength="100"]').count() > 0:
        page.locator('input.lw_input[placeholder="성"][maxlength="100"]').fill("한국어성")
    if page.locator('input.lw_input[placeholder="이름"][maxlength="100"]').count() > 0:
        page.locator('input.lw_input[placeholder="이름"][maxlength="100"]').fill("한국어이름")
    if page.locator('input.lw_input[placeholder="姓(简体中文)"]').count() > 0:
        page.locator('input.lw_input[placeholder="姓(简体中文)"]').fill("번체성")
    if page.locator('input.lw_input[placeholder="名(简体中文)"]').count() > 0:
        page.locator('input.lw_input[placeholder="名(简体中文)"]').fill("번체이름")
    if page.locator('input.lw_input[placeholder="姓(繁體中文)"]').count() > 0:
        page.locator('input.lw_input[placeholder="姓(繁體中文)"]').fill("간체성")
    if page.locator('input.lw_input[placeholder="名(繁體中文)"]').count() > 0:
        page.locator('input.lw_input[placeholder="名(繁體中文)"]').fill("간체이름")
        
    # 닉네임
    page.locator('input.lw_input[placeholder="닉네임"]').fill("자동화_닉네임")
    
    # ID
    page.locator('input.lw_input[placeholder="ID"]').fill(f"junil_{timestamp}")
    
    # 사용자 유형 1번째 선택 
    user_type_select = page.locator("//div[i[text()='사용자 유형']]//select[@id='member_type']")
    first_value = user_type_select.locator('option').nth(1).get_attribute('value')
    user_type_select.select_option(value=first_value)

    # 직급 1번째 선택 
    user_type_select = page.locator("//div[i[text()='직급']]//select[@id='member_type']")
    first_value = user_type_select.locator('option').nth(1).get_attribute('value')
    user_type_select.select_option(value=first_value)
    
    #조직/직책 선택 로직 필요
    #page.locator('button.generate', has_text="소속 조직 추가").click()
    
    
    # 사내번호
    page.locator('input.lw_input[placeholder="사내 번호"]').fill(f"P-{timestamp}")
    
    # 전화번호
    page.locator('input.lw_input[placeholder="전화번호"]').fill(f"T-{timestamp}")
    
    # 보조 이메일
    page.locator('button.generate', has_text="보조 이메일 추가").click()
    page.wait_for_selector('input.lw_input.email_id[placeholder="보조 이메일"]', timeout=5000)
    page.locator('input.lw_input.email_id[placeholder="보조 이메일"]').fill(f"sub_email_{timestamp}")

    
    # 개인 이메일 
    page.locator('input.lw_input[placeholder="개인 이메일"]').fill(f"private_email_{timestamp}")
    page.locator('input.lw_input[placeholder="직접 입력"]').fill(f"private.domain")
    
    # 사용 언어 한국어 선택 
    page.locator('select#language_type').select_option(label="Korean")
    
    # 근무처
    page.locator('input.lw_input[placeholder="근무처"]').fill(f"자동화_근무처")
    
    # 담당 업무
    page.locator('input.lw_input[placeholder="담당 업무"]').fill(f"자동화_담당업무")
    
    # 사용 SNS > X
    sns_dropdown = page.locator('div.box.fm_sns select#member_type')
    sns_dropdown.select_option(label="X")
    page.wait_for_selector('div.box.fm_sns input.lw_input[placeholder="ID"][maxlength="100"]', timeout=5000)
    page.locator('div.box.fm_sns input.lw_input[placeholder="ID"][maxlength="100"]').fill(f"auto-{timestamp}")

    # 생일
    page.locator('input.lw_input[name="birthday"]').fill("1999. 12. 31")
    
    # 입사일
    page.locator('input.lw_input[name="hiredDate"]').fill("2000. 01. 01")

    # 사원 번호
    page.locator('input.lw_input[placeholder="사원 번호"]').fill(f"자동화_{timestamp}")
    
    # 연결된 연락처
    page.locator('button.generate', has_text="연락처 연결").click()
    page.wait_for_selector('input.lwds_input[placeholder="관계"]', timeout=5000)
    page.locator('input.lwds_input[placeholder="관계"]').fill("자동화_관계")
    page.locator('input.lwds_input[placeholder="구성원"]').fill(f"준일")
    page.wait_for_selector('ul.member_list[style*="display: block"] li.has_txt', timeout=5000)
    page.locator('ul.member_list[style*="display: block"] li.has_txt').first.click()

    
    # 비밀번호
    page.locator('label[for="pw_admin"]').click()
    page.locator('input[placeholder="비밀번호"]').fill(accounts.nw_pw)
    page.locator('label[for="check01"]').click()
    
    
    # TODO: 비밀번호 옵션, 활성화 옵션, 라이선스 옵션 추가 필요
    
    return page

def access_create_contact(page) :
    #구성원 페이지 접근 버튼
    button = page.locator('a.shortcut_link:has(strong.shortcut_title:text-is("구성원"))')
    button.click() 

    #구성원 추가 버튼
    button = page.locator('button.lw_btn_point:text-is("구성원 추가")')
    button.click() 
    
    return page

def click_save(page) :
    page.locator('button.lw_btn_point:text-is("추가")').click()
    page.locator('button.lw_btn:text-is("확인")').click()
    
    return page
    

def create_contact(page, instance, server) :
    page = open_url.open_url(page, instance, server, is_admin = True)
    
    page = access_contact_create(page)
    page = fill_field(page)
    #page = click_save(page)

    return page