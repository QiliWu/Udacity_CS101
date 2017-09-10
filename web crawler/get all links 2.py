#4.提取所有链接
def get_next_page(page):
    start_link=page.find('<a href=')
    if start_link == -1:
        return None,0
    else:
        start_quote = page.find('"',start_link)
        end_quote = page.find('"',start_quote+1)
        url=page[start_quote+1:end_quote]
        return url, end_quote

    
def print_all_links(page):
    links=[]
    while True:
        url,endpos = get_next_page(page)
        if url:
            links.append(url)
            page=page[endpos:]
        else:
            break
    return links
