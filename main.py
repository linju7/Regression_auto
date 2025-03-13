from playwright.sync_api import sync_playwright

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from login import login, open_url
from contacts import contact_create
from contacts import external_contact_create


# 테스트 환경 설정
server = "real"
instance = "jp2"
is_admin = False



#---------수행-------

#첫 페이지 객체 생성 
def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) 
        page = browser.new_page()  
        #-----------------초기 설정-----------------
        
        
        
        
        # 페이지 이동
        page = open_url.open_url(page, instance, server, is_admin)
        
        #로그인
        page = login.login(page, instance, server, is_admin)
    
        #구성원 추가
        #page = contact_create.contact_create(page,instance,server)
        
        #외부 연락처 추가
        page = external_contact_create.external_contact_create(page,instance,server)




        #-----------------브라우저 유지-----------------
        # 브라우저 유지 
        page.pause()
        
if __name__ == "__main__":
    main()

