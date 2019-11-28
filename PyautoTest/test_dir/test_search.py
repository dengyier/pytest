import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.tripsbase_page import TripsbasePage
import pytest

class TestSearch:
    def test_search_case(self,browser,base_url):
        page=TripsbasePage(browser)
        page.get(base_url)
        page.search_input="Los"
        page.search_buttom.click()
if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_search.py"])




