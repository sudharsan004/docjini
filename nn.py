from googlesearch import search 
import urllib
import requests,random
from bs4 import BeautifulSoup
# a=input("Enter search term: ")
# # to search 
# b=input("enter extension to search")
import time

def ss():
    a='chemistry twelfth model question paper'
    b='pdf'
    query = a+"ext:"+b
    tld=['co.in','com']
    result= search(query, tld="co.in", num=10, stop=10, pause=2)
    print(result)
    count=0
    for i in result:
        print(i)
        count+=1
    print(count)
    for j in result : 
        if '.'+b in j:
            print(j.title())
            print(j.discription())
import time

user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"

def search2(term,user_agent):
    print(user_agent)
    user_agent=str(user_agent)
    query = term+" ext:"+'pdf'
    URL = f"https://google.com/search?q={query}"
    headers = {"user-agent" : user_agent}
    resp = requests.get(URL, headers=headers)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
    results = []
    for g in soup.find_all('div', class_='r'):
        anchors = g.find_all('a')
        if anchors:
            link = anchors[0]['href']
            title = g.find('h3').text
            item = {
                "title": title,
                "link": link
            }
            if '.pdf' in str(item['link']):
                results.append(item)
    for i in results:
        print(i)
    return results

start = time.time()
# search2(term='chemistry twelfth model question paper',user_agent=user_agent)
ss()
print(f'Time: {time.time() - start}')

# import requests,time
# from urllib.parse import quote
# from bs4 import BeautifulSoup
# start = time.time()
# api='AIzaSyCRnZPkS3zDBbzFL8Bn5vb2In8oFijBIs4'
# 'key=AIzaSyCRnZPkS3zDBbzFL8Bn5vb2In8oFijBIs4&cx=010825230688325870404:28ddwsmp3uq&q=lectures+ext:pdf'
# def search3():
#     q='digital system'
#     BASE_URL='https://www.googleapis.com/customsearch/v1?'
#     PARAMS={'fileType':'pdf',
#         'safe':"active",
#         'key':'AIzaSyCRnZPkS3zDBbzFL8Bn5vb2In8oFijBIs4',
#         'cx':'010825230688325870404:28ddwsmp3uq',
#         'q':q
#     }
#     r = requests.get(BASE_URL,PARAMS)
#     results=[]
#     data = r.json()
#     for i in range(10):
#         item = {
#                 "title": data['items'][i]['title'],
#                 "link": data['items'][i]['link'],
#                 "description":data['items'][i]['snippet']
#             }
#         results.append(item)
#     return results
# r=search3()
# for i in r:
#     print(i['title'])

# def search1(term):
#     start = time.time()
#     #print(1)
#     query = term+" ext:"+'pdf'
#     result= search(query, tld="com", num=10, stop=10, pause=2.0)
#     url_list=[]
#     for i in result:
#         if '.pdf' in i:
#             print(i)
#             url_list.append(i)
#     print(f'Time: {time.time() - start}')
#     return url_list


# user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"

# def search2(term,user_agent):
#     start = time.time()
#     print(user_agent)
#     user_agent=str(user_agent)
#     query = term+" ext:"+'pdf'
#     URL = f"https://google.com/search?q={query}"
#     headers = {"user-agent" : user_agent}
#     resp = requests.get(URL, headers=headers)
#     if resp.status_code == 200:
#         soup = BeautifulSoup(resp.content, "html.parser")
#     results = []
#     for g in soup.find_all('div', class_='r'):
#         anchors = g.find_all('a')
#         if anchors:
#             link = anchors[0]['href']
#             title = g.find('h3').text
#             item = {
#                 "title": title,
#                 "link": link
#             }
#             if '.pdf' in str(item['link']):
#                 results.append(item)
#     for i in results:
#         print(i)
#     print(f'Time: {time.time() - start}')
#     return results

# search3(term):
#     BASE_URL='https://www.googleapis.com/customsearch/v1?key=AIzaSyCRnZPkS3zDBbzFL8Bn5vb2In8oFijBIs4&cx=010825230688325870404:28ddwsmp3uq&q='
#     search_url=urljoin(BASE_URL+term+' filetype:pdf')
#     print(search_url)

# print(f'Time: {time.time() - start}')

