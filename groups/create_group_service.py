import sys
import os
from datetime import datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from login import open_url
from security import accounts

def access_create_group_service(page):
    # "새로 만들기" 버튼 클릭
    page.locator('a.skin_corp_bg.skin_corp_txt.has_dropdown:has-text("새로 만들기")').click()

    # "그룹 추가" 항목 선택
    page.locator('a:has-text("그룹 추가")').first.click()
    page.wait_for_selector('div.layer_content', state='attached')  # 요소가 DOM에 붙어있는지 확인

    # 새로운 페이지로 포커싱 이동 (팝업창)
    new_page = None
    def handle_new_page(new):
        nonlocal new_page
        new_page = new

    page.context.on('page', handle_new_page)

    # "그룹 만들기" 버튼 클릭
    page.locator('a.link:has-text("그룹 만들기")').first.click()

    # Wait for the new page to be created
    while new_page is None:
        page.wait_for_timeout(100)  # Wait for a short time to allow the new page to be created

    # 새 페이지가 로딩될 때까지 대기
    new_page.wait_for_load_state('domcontentloaded')

    return new_page


def fill_field(page):
    
    timestamp = datetime.now().strftime("%m%d%H%M")
    
    # 그룹명
    page.wait_for_selector('input[placeholder="그룹명을 입력해주세요."]', timeout=5000)
    page.locator('input[placeholder="그룹명을 입력해주세요."]').fill(f"자동화_{timestamp}")
    
    # 설명
    page.locator('textarea[placeholder="설명을 입력해주세요."]').fill(f"자동화로 생성된 그룹입니다. (준일)")
    
    # TODO : 마스터/멤버, 메시지방 기능, 고급설정, 외부메일, 공개설정, 알림보내기 구현 필요

    return page

def click_save(page):
    # "추가" 버튼 클릭
    page.locator('button.btn_point:has-text("추가")').first.click()

    # 중간에 숫자가 달라질 수 있는 URL 패턴을 기다림
    page.wait_for_url('https://contact.worksmobile.com/v2/p/popup/groups/*/view')

    # "닫기" 버튼 클릭
    page.locator('button.btn:has-text("닫기")').first.click()

    return page

def create_group_service(page, instance, server) :
    page = open_url.open_url(page, instance, server, is_admin = False)
    
    new_page = access_create_group_service(page)
    new_page = fill_field(new_page)
    new_page = click_save(new_page)

    return page