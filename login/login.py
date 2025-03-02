'''
    login(page, instance, server, is_admin)
    
    page : 현재 열려있는 브라우저 객체
    인스턴스 : 국가 코드 값, string (ex. kr1, jp1, jp2)
    서버 : alpha, stage, real
    is_admin : 불리언 값
    
    인지할 내용
    - 로그인 함수에서 url을 재연산하고 있음 > 로드 되는 동안 기다려야 하기 때문, 추후 최적화 로직 생각하기

'''


import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from security import accounts
from open_url import get_url


# 로그인을 수행하는 함수
def login_web(page, userid, userpw):
    page.fill("#user_id", userid)
    page.click("#loginStart")
    
    page.fill("#user_pwd", userpw)
    page.click("#loginBtn")

    return page


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
    
    
    
#로그인 함수 호출부
def login(page,instance, server, is_admin):
    userid = get_userid(instance, server)
    userpw = get_userpw(instance)
    url = get_url(instance,server,is_admin)
    
    page = login_web(page, userid, userpw)
    try:
        page.wait_for_url(url, timeout=60000)  # 최대 60초 대기
        print(f"✅ 로그인 후 최종 URL 로딩 완료: {page.url}")
    except Exception as e:
        print(f"❌ 로그인 후 URL 대기 실패: {e}")
    
    return page