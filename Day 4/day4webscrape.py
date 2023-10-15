from bs4 import BeautifulSoup
import requests
responses=requests.get('https://news.ycombinator.com/')
contents=responses.text

soup=BeautifulSoup(contents,'html.parser')
heading_list=[]
headings=soup.find_all(class_='titleline')
for heading in headings:
    heading_list.append(heading.text)
for i in heading_list:
    print(i)
scores=soup.find_all(class_='score')
score_list=[]
for score in scores:
    score_list.append(score.text)
for i in score_list:
    print(i)
link_list=[]
alllinks=soup.find_all('span',class_='titleline')
for links in alllinks:
    link=links.find_all('a')
    for l in link:
        url=l.get('href')
        link_list.append(url)
for i in link_list:
    print(i)