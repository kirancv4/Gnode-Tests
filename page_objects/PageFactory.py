"""
PageFactory uses the factory design pattern. 
get_page_object() returns the appropriate page object.
Add elif clauses as and when you implement new pages.
Pages implemented so far:
1. Product chart smartphone page
"""

from page_objects.Product_Smartphone_Page import Product_Smartphone_Page
from page_objects.Gnod_Home_Page import Gnod_Home_Page
import conf.base_url_conf
from page_objects.zero_page import Zero_Page

class PageFactory():
    "PageFactory uses the factory design pattern."
    def get_page_object(page_name,base_url=conf.base_url_conf.base_url):
        "Return the appropriate page object based on page_name"
        test_obj = None
        page_name = page_name.lower()
        
        if page_name in ["zero","zero page","agent zero"]:
            test_obj = Zero_Page(base_url=base_url)

        if page_name in ["gnod","main page","homepage"]:
            test_obj = Gnod_Home_Page(base_url=base_url)

        return test_obj

    get_page_object = staticmethod(get_page_object)