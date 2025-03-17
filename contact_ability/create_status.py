import sys
import os
from datetime import datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from login_and_url import move_url
from security import accounts


def fill_field(page):
    timestamp = datetime.now().strftime("%m%d%H%M")
    
    #가장 마지막 요소를 선택하여 값을 입력함 
    
    # 상태 입력 
    page.locator('input.lw_input[placeholder="상태"]').last.fill(f"준일_자동화_상태_{timestamp}")
    
    # 일본어 입력 
    page.locator('div.lang_field:has-text("Japanese") input.lw_input').last.fill(f"자동화_JP_{timestamp}")

    # 영어 입력 
    page.locator('div.lang_field:has-text("English") input.lw_input').last.fill(f"자동화_EN_{timestamp}")

    # 한국어 입력 
    page.locator('div.lang_field:has-text("Korean") input.lw_input').last.fill(f"자동화_KR_{timestamp}")

    # 중국어 (중국) 입력 
    page.locator('div.lang_field:has-text("Chinese (CHN)") input.lw_input').last.fill(f"자동화_CN_{timestamp}")

    # 중국어 (대만) 입력 
    page.locator('div.lang_field:has-text("Chinese (TWN)") input.lw_input').last.fill(f"자동화_TW_{timestamp}")
    
    return page

def access_create_status(page) :
    
    # 수정 버튼 선택 
    page.locator('button.lw_btn:text-is("수정")').click()
    
    # 상태 추가 선택 
    page.locator('button.btn_add_row:text-is("상태 추가")').click()
    
    return page

def click_save(page) :
    # 저장 클릭 
    page.locator('button.lw_btn_point:text-is("저장")').click()
    
    # 확인 레이어 기다리고 저장
    page.wait_for_selector('button.lw_btn_point:text-is("확인")')
    page.locator('button.lw_btn_point:text-is("확인")').click()
    
    return page
    

def create_status(page, instance, server) :
    url = "admin.worksmobile.com/member/status"
    page = move_url.move_url(page, instance, server, url)
    page = access_create_status(page)
    page = fill_field(page)
    page = click_save(page)

    return page