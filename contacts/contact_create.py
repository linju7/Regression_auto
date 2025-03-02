import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from login import open_url 

def contact_create(page, instance, server) :
    page = open_url.open_url(page, instance, server, is_admin = True)
    
    return page