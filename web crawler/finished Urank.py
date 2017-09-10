#统计点击数

# One way search engines rank pages
# is to count the number of times a
# searcher clicks on a returned link.
# This indicates that the person doing
# the query thought this was a useful
# link for the query, so it should be
# higher in the rankings next time.

# (In Unit 6, we will look at a different
# way of ranking pages that does not depend
# on user clicks.)

# Modify the index such that for each url in a
# list for a keyword, there is also a number
# that counts the number of times a user
# clicks on that link for this keyword.

# The result of lookup(index,keyword) should
# now be a list of url entries, where each url
# entry is a list of a url and a number
# indicating the number of times that url
# was clicked for this query keyword.

# You should define a new procedure to simulate
# user clicks for a given link:

# record_user_click(index,word,url)

# that modifies the entry in the index for
# the input word by increasing the count associated
# with the url by 1.

# You also will have to modify add_to_index
# in order to correctly create the new data
# structure, and to prevent the repetition of
# entries as in homework 4-5.


cache = {
   'http://udacity.com/cs101x/urank/index.html': """<html>
<body>
<h1>Dave's Cooking Algorithms</h1>
<p>
Here are my favorite recipes:
<ul>
<li> <a href="http://udacity.com/cs101x/urank/hummus.html">Hummus Recipe</a>
<li> <a href="http://udacity.com/cs101x/urank/arsenic.html">World's Best Hummus</a>
<li> <a href="http://udacity.com/cs101x/urank/kathleen.html">Kathleen's Hummus Recipe</a>
</ul>

For more expert opinions, check out the 
<a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a> 
and <a href="http://udacity.com/cs101x/urank/zinc.html">Zinc Chef</a>.
</body>
</html>






""", 
   'http://udacity.com/cs101x/urank/zinc.html': """<html>
<body>
<h1>The Zinc Chef</h1>
<p>
I learned everything I know from 
<a href="http://udacity.com/cs101x/urank/nickel.html">the Nickel Chef</a>.
</p>
<p>
For great hummus, try 
<a href="http://udacity.com/cs101x/urank/arsenic.html">this recipe</a>.

</body>
</html>






""", 
   'http://udacity.com/cs101x/urank/nickel.html': """<html>
<body>
<h1>The Nickel Chef</h1>
<p>
This is the
<a href="http://udacity.com/cs101x/urank/kathleen.html">
best Hummus recipe!
</a>

</body>
</html>






""", 
   'http://udacity.com/cs101x/urank/kathleen.html': """<html>
<body>
<h1>
Kathleen's Hummus Recipe
</h1>
<p>

<ol>
<li> Open a can of garbanzo beans.
<li> Crush them in a blender.
<li> Add 3 tablespoons of tahini sauce.
<li> Squeeze in one lemon.
<li> Add salt, pepper, and buttercream frosting to taste.
</ol>

</body>
</html>

""", 
   'http://udacity.com/cs101x/urank/arsenic.html': """<html>
<body>
<h1>
The Arsenic Chef's World Famous Hummus Recipe
</h1>
<p>

<ol>
<li> Kidnap the <a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a>.
<li> Force her to make hummus for you.
</ol>

</body>
</html>

""", 
   'http://udacity.com/cs101x/urank/hummus.html': """<html>
<body>
<h1>
Hummus Recipe
</h1>
<p>

<ol>
<li> Go to the store and buy a container of hummus.
<li> Open it.
</ol>

</body>
</html>




""", 
}

def get_page(url):
    if url in cache:
        return cache[url]
    else:
        return None


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def get_all_links(page):
    links=[]
    while True:
        url,endpos=get_next_page(page)
        if url:
            links.append(url)
            page=page[endpos:]
        else:
            break
    return links

def add_to_index(index,keyword,url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword]=[url]

def add_page_to_index(index,url,content):
    keywords=content.split()
    for keyword in kewwords:
        add_to_index(index,keyword,url)
    


def crawl_web(seed):
    tocrawl=[seed]
    crawled=[]
    index={}
    graph={}
    while tocrawl:
        page=tocrawl.pop()
        if page not in crawled:
            content=get_page(page)
            add_page_to_index(index,page,content)
            outlinks = get_all_links(contents)
            graph[page]=outlinks # <url>:[list of pages it links to] 
            union(tocrawl,outlinks)
            crawled.append(page)
    return index.graph

def lookup(index,keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None

def compute_ranks(graph):
    d=0.8 # damping factor
    numloops=10
    ranks={}
    npages=len(graph)
    for page in graph:
        ranks[page]=1.0/npages
    for i in range(0,numloops):
        newranks={}
        for page in graph:
            newrank=(1-d)/npages
            for node in graph:
                if page in graph[node]:
                    newrank=newrank+d*(ranks[node]/len(graph))
            newranks[page]=newrank
        ranks=newranks
    return ranks
            
