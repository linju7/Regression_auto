from playwright.sync_api import sync_playwright

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from security import account, url



def login(id, pw):
    with sync_playwright() as p:

        # 1. Chromium 브라우저 실행
        browser = p.chromium.launch(headless=False)  # headless=True이면 UI 없이 실행됨
        page = browser.new_page()  
        

#인스턴스 + 서버로 url 조정 
def get_url(instance, server) :
    ret = "https://"
    
    if server == "alpha" :
        ret += url.alpha
    elif server == "stage" :
        ret += url.stage
        
    if instance in ["kr1", "jp1", "jp2"] :
        ret += url.naverworks
    
    return ret

#인스턴스 + 서버로 id 분류
def get_userid(instance, server):
    ret = ""
    
    if instance == "kr1" :
        if server == "alpha" :
            ret = account.alpha_kr1_id
        else :
            ret = account.stage_kr1_id
    
    elif instance == "jp1" :
        if server == "alpha" :
            ret = account.alpha_jp1_id
        else :
            ret = account.stage_jp1_id
            
    elif instance == "jp2" :
        if server == "alpha" :
            ret = account.alpha_jp2_id
        else :
            ret = account.stage_jp2_id

    return ret 

#인스턴스 + 서버로 비밀번호 분류
def get_userpw(instance, server) :
    ret = ""
    
    if instance in ["kr1", "jp1", "jp2"] :
        ret = account.nw_pw
    
    return ret 
    
##인스턴스 + 서버 입력으로 파라미터 값 조정 
def login_selector(instance, server):
    modified_url = get_url(instance, server)
    userid = get_userid(instance, server)
    userpw = get_userpw(instance, server)
    
    print(modified_url, userid, userpw)
    
login_selector("jp1", "real")