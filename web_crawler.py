#!/usr/bin/python
import sys
def get_page(url):
    if url[0:3] == "www":
        url = "http://" + url
    try:
        import urllib.request
        resource = urllib.request.urlopen(url)
        content = resource.read().decode(resource.headers.get_content_charset())
        return content
    except:  # in case something fails, returns an empty string
        return ""


def get_next_target(page):
    start_link = page.find("<a href=")
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote


# the union of two lists
def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)


# it gathers all the urls in a list
def get_all_links(page, links, word):
    while True:
        url, endpos = get_next_target(page)
        if url:
            if not url.find("/"):
                if len(url) > 1 and word in url and " " not in url:
                    check = "www.mbtelecom.ro" + url
                    if not check in links:
                        print(check)
                        #print(check.encode(sys.stdout.encoding, errors='replace'))
                        links.append(check)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed, word):
    tocrawl = [seed]  # pages that we need to crawl
    crawled = []  # list of the pages we've already crawled
    links = []
    while tocrawl:
        #if tocrawl[-1][0:16] == "www.mbtelecom.ro":
        page = tocrawl.pop()  # depth-first search: we extract the last element from the list
        if page not in crawled:
            content = get_page(page)
            links = get_all_links(content, links, word)
            union(tocrawl, links)
            crawled.append(page)
    return crawled


def main():
    links = crawl_web('www.mbtelecom.ro', sys.argv[1])
    #print(links)
    return links

if __name__ == "__main__":
    main()
