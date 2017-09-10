#2.提取下一个链接
def get_next_target(page):
    start_link=page.find('<a href=')
    start_quote=page.find('"',start_link)
    end_quote=page.find('"',stat_quote+1)
    url=page[start_quote+1:end_quote]
    print url
    page=page[end_quote:]
    start_link=page.find('<a href=')
    start_quote=page.find('"',start_link)
    end_quote=page.find('"',stat_quote+1)
    next_url=page[start_quote+1:end_quote]
    print next_url
