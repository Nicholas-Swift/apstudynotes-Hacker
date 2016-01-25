#! python3
# AP Study Notes Hacker! www.apstudynotes.org has some amazing essays,
# however, they're stuck behind a "Pay $14 to read this" wall. I'm cheap,
# so I'm looking to save $14. Let's get the hacking started!

import os, requests, bs4

# Create a txt, html, and doc folder if they don't already exist
if not os.path.exists("./txt"):
    os.makedirs("./txt")
if not os.path.exists("./html"):
    os.makedirs("./html")
if not os.path.exists("./doc"):
    os.makedirs("./doc")

# Get the URLs to apstudynotes.org's 141 essays.
res = requests.get('https://www.apstudynotes.org/essays/')
soup = bs4.BeautifulSoup(res.text, 'html.parser')
elems = soup.select('h3 > a')
urlList = []
for link in elems:
    urlList.append(str(link.attrs))
for i in range(len(urlList)):
    urlList[i] = urlList[i].replace("{'href': '", "")
    urlList[i] = urlList[i].replace("'}", "")
    urlList[i] = 'https://www.apstudynotes.org' + urlList[i]
    print(urlList[i])

# Get the titles of each essay, so we can name the files accurately
titleList = []
for i in range(len(elems)):
    tempString = urlList[i]
    tempString = tempString[len(str(r"https://www.apstudynotes.org/")):(len(tempString)-1)]
    for j in range(len(tempString)):
        if tempString[j] == '/':
            tempString = tempString[:j] + '-' + tempString[j+1:]
    titleList.append(tempString)


# Now we have all the pages - perfect!
# Time to get all the text from each page and put it into a .txt file
for i in range(len(urlList)):
    print('Getting contents: ' + urlList[i] + '...')
    res = requests.get(urlList[i])
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    elems = soup.select('p')
    
    print('\tCreating .txt, .html, and .doc files')
    filetxt = open(str('txt/' + str(i+1) + ' ' + titleList[i] + '.txt'), 'w', encoding='utf-8')
    filehtml = open(str('html/' + str(i+1) + ' ' + titleList[i] + '.html'), 'w', encoding='utf-8')
    filedoc = open(str('doc/' + str(i+1) + ' ' + titleList[i] + '.doc'), 'w', encoding='utf-8')
    
    for i in range(len(elems)):
        filetxt.write(str('\n' + elems[i].getText() + '\n\n')) #txt file
        filehtml.write(str(elems[i])) #html file
        filedoc.write('\n' + elems[i].getText() + '\n\n') #doc file
        
    filetxt.close()
    filehtml.close()
    filedoc.close()
