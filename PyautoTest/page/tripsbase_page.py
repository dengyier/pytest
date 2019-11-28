from poium import Page,PageElement,PageElements

class TripsbasePage(Page):
    search_input = PageElement(xpath='//input[@placeholder="Where do you want to go?"]',describe='输入框')
    search_buttom = PageElement(xpath='//*[@id="main-wrapper"]/section/section/div[1]/div[2]/div/div[1]/div/div/i',describe='搜索按钮')
    login_buttom = PageElement(css='div#header > div.right_part > div:nth-child(4) > div:nth-child(2) li',describe='login')


