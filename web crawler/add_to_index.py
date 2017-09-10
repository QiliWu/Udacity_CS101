#添加页面至索引（add_page_to_index)
# Define a procedure, add_page_to_index,
# that takes three inputs:

#   - index
#   - url (String)
#   - content (String)

# It should update the index to include
# all of the word occurences found in the
# page content by adding the url to the
# word's associated url list.

index=[]

def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0]==keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])

def add_page_to_index(index,url,content):
    keywords=content.split()
    for keyword in kewwords:
        add_to_index(index,keyword,url)
    return index
        
