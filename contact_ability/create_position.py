import sys
import os
from datetime import datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from login_and_url import move_url
from security import accounts


def fill_field(page):
    timestamp = datetime.now().strftime("%m%d%H%M")
    
    #가장 마지막 요소를 선택하여 값을 입력함 
    
    # 직책명 입력 
    page.locator('input.lw_input[placeholder="직책"]').last.fill(f"준일_자동화_직책_{timestamp}")
    
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

def access_create_position(page) :
    
    # 수정 버튼 선택 
    page.locator('button.lw_btn:text-is("수정")').click()
    
    # 직책 추가
    page.locator('button.btn_add_row:text-is("직책 추가")').click()
    
    return page

def click_save(page) :
    # 저장 클릭 
    page.locator('button.lw_btn_point:text-is("저장")').click()
    return page
    

def create_position(page, instance, server) :
    url = "admin.worksmobile.com/member/job/positions"
    page = move_url.move_url(page, instance, server, url)
    page = access_create_position(page)
    page = fill_field(page)
    page = click_save(page)

    return page