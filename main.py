import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from login import login



# 테스트 환경 설정
server = "stage"
instance = "jp2"




#수행
login.login_selector(instance, server)
