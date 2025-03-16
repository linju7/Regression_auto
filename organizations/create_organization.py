import sys
import os
from datetime import datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from login import open_url
from security import accounts


def fill_field(page):
    timestamp = datetime.now().strftime("%m%d%H%M")
    
    # 조직명    
    page.locator('input.lw_input[placeholder="조직명"]').fill(f'자동화조직_{timestamp}')
    
    # 설명
    page.locator('input.lw_input[placeholder="설명"]').fill(f'자동화로 생성된 조직입니다. (준일)')
    
    # 다국어 명
    if page.locator('input.lw_input[placeholder="Japanese"]').count() > 0:
        page.locator('input.lw_input[placeholder="Japanese"]').fill("일본어조직명(자동화)")
    if page.locator('input.lw_input[placeholder="English"]').count() > 0:
        page.locator('input.lw_input[placeholder="English"]').fill("영어조직명(자동화)")
    if page.locator('input.lw_input[placeholder="Chinese (CHN)"]').count() > 0:
        page.locator('input.lw_input[placeholder="Chinese (CHN)"]').fill("간체조직명(자동화)")
    if page.locator('input.lw_input[placeholder="Chinese (TWN)"]').count() > 0:
        page.locator('input.lw_input[placeholder="Chinese (TWN)"]').fill("번체조직명(자동화)")
    if page.locator('input.lw_input[placeholder="Korean"]').count() > 0:
        page.locator('input.lw_input[placeholder="Korean"]').fill("한국어조직명(자동화)")
    
    # 메일링 리스트
    page.locator('input.lw_input[placeholder="ID"]').fill(f"auto_{timestamp}")
    
    
    # TODO: 고급설정 추가 필요
    
    return page

def access_create_organization(page) :
    #조직 페이지 접근 버튼
    page.locator('a.shortcut_link:has(strong.shortcut_title:text-is("조직"))').click()

    #조직 추가 버튼
    page.locator('button.btn_save:text-is("조직 추가")').click()
    
    
    
    return page

def click_save(page) :
    page.locator('button.lw_btn_point:text-is("추가")').click()
    
    return page
    

def create_organization(page, instance, server) :
    page = open_url.open_url(page, instance, server, is_admin = True)
    
    page = access_create_organization(page)
    page = fill_field(page)
    page = click_save(page)

    return page