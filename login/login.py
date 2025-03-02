from playwright.sync_api import sync_playwright

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from security import accounts, urls



def login_web(url, userid, userpw):
    with sync_playwright() as p:

        # Chromium 브라우저 실행
        browser = p.chromium.launch(headless=False) 
        page = browser.new_page()  
        
        # url 이동 
        page.goto(url)
        
        # id 입력 후 로그인 버튼 선택
        page.fill("#user_id", userid)
        page.click("#loginStart")

        # pw 입력 후 최종 로그인 버튼 선택 
        page.fill("#user_pwd", userpw)
        page.click("#loginBtn")
        
        # 브라우저 유지
        page.pause()
        
        # 브라우저 종료 (ENTER 입력 시 종료)
        browser.close()

#인스턴스 + 서버로 url 조정 
def get_url(instance, server, is_admin) :
    ret = "https://"
    
    if server == "alpha" :
        ret += urls.alpha
    elif server == "stage" :
        ret += urls.stage
        
    if is_admin :
        ret += urls.admin
    else :
        ret += urls.service
        
    if instance in ["kr1", "jp1", "jp2"] :
        ret += urls.naverworks
    
    return ret

#인스턴스 + 서버로 id 분류
def get_userid(instance, server):
    ret = ""
    
    if instance == "kr1" :
        if server == "alpha" :
            ret = accounts.alpha_kr1_id
        else :
            ret = accounts.stage_kr1_id
    
    elif instance == "jp1" :
        if server == "alpha" :
            ret = accounts.alpha_jp1_id
        else :
            ret = accounts.stage_jp1_id
            
    elif instance == "jp2" :
        if server == "alpha" :
            ret = accounts.alpha_jp2_id
        else :
            ret = accounts.stage_jp2_id

    return ret 

#인스턴스로 비밀번호 분류
def get_userpw(instance) :
    ret = ""
    
    if instance in ["kr1", "jp1", "jp2"] :
        ret = accounts.nw_pw
    
    return ret 
    
##인스턴스 + 서버 입력으로 파라미터 값 조정 
def login(instance, server, is_admin):
    url = get_url(instance, server, is_admin)
    userid = get_userid(instance, server)
    userpw = get_userpw(instance)
    
    login_web(url,userid, userpw)