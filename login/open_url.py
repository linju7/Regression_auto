'''
    open_url(instance, server, is_admin)
    
    인스턴스 : 국가 코드 값, string (ex. kr1, jp1, jp2)
    서버 : alpha, stage, real
    is_admin : 불리언 값

'''

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from security import accounts, urls

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

def open_url(page, instance, server, is_admin):
    url = get_url(instance, server, is_admin)
    try:
        page.goto(url, wait_until="domcontentloaded", timeout=6000)
        print(f"✅ 페이지 이동 성공: {page.url}")
    except Exception as e:
        print(f"❌ 페이지 이동 실패: {e}")
    
    
    return page