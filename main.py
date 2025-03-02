import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from login import login



# 테스트 환경 설정
server = "real"
instance = "jp2"
is_admin = True



#수행
login.login(instance, server, is_admin)