from playwright.sync_api import sync_playwright

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

#로그인, 페이지 이동
from login_and_url import login, open_url

#구성원 생성 
from contacts import create_contact        

#외부 연락처 생성 
from contacts import create_external_contact

# 내부 그룹 + 서비스 생성
from groups import create_group_service

# 외부 그룹 + 서비스 생성
from groups import create_external_group_service

# 조직 생성
from organizations import create_organization

# 직책/직급/사용자유형/상태 생성
from contact_ability import create_position, create_level, create_usertype, create_status

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
        #page = create_contact.create_contact(page,instance,server)
        
        #외부 연락처 추가
        #page = create_external_contact.create_external_contact(page,instance,server)

        # 그룹 추가
        #page = create_group_service.create_group_service(page,instance,server)
        
        # 외부 그룹 추가
        #page = create_external_group_service.create_external_group_service(page,instance,server)

        # 조직 추가
        #page = create_organization.create_organization(page,instance,server)
        
        # 직책 추가
        #page = create_position.create_position(page,instance,server)

        # 직급 추가
        #page = create_level.create_level(page,instance,server)

        # 사용자 유형 추가
        # page = create_usertype.create_usertype(page,instance,server)
        
        # 상태 추가
        page = create_status.create_status(page,instance,server)

        #-----------------브라우저 유지-----------------
        # 브라우저 유지 
        page.pause()
        
if __name__ == "__main__":
    main()

