
import requests
import bs4

vidlink = input('enter links here: ')

vidid = vidlink.replace('https://www.pornhub.com/view_video.php?viewkey=ph5', '')

print(vidid)

tbofflink = 'https://www.tubeoffline.com/downloadFrom.php?host=PornHub&video=https%3A%2F%2Fwww.pornhub.com%2Fview_video.php%3Fviewkey%3Dph5' + vidid

print(tbofflink)

a = tbofflink

res = requests.get(a)

c = res.text

soup = bs4.BeautifulSoup(res.text, 'html.parser')

list = ''

for link in soup.findAll('a'):
    list += link.get('href') + '\n'

import re

#The string property returns the search string:

txt = list

x = re.split('\n', txt)


b = ['480']
c = [word for word in x if any(ignore in word for ignore in b)]

# for everylink in c:
#     print(everylink)

e = ['dm']
d = [word for word in c if any(ignore in word for ignore in e)]


f = d[0]

print(f)

import webbrowser
a_website = f

webbrowser.get('firefox').open_new_tab(a_website)

# def openurl(url):
#     import webbrowser
#     a_website = url
#     webbrowser.get('firefox').open_new_tab(a_website)

# for everylink in d:
#     openurl(everylink)