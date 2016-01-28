# apstudynotes-Hacker
All the apstudynotes.org/essays essays for free!

Disclaimer: The legality of using this program is a grey area. I've only provided the code and program.

To use the program...
 - Click "Download ZIP"
 - Extract the files from "apstudynotes-Hacker.zip"
 - Run "AP Study Notes Hacker.py" #NOTE: You must have Python installed to be able to run a .py
 - Wait for the program to create all the files for you to enjoy!

# The Buildup
When I was a high school senior applying to colleges, I found the website www.apstudynotes.org/essays/ extremely helpful.
I took immense inspiration from reading the essays, and it significantly helped me shape my essays when application season started.

However, most of the essays are barred behind a pay wall. At the time, I was able to bypass this by going into inspect element
and just deleting the paywall and changing the 'blur' effect. They've since changed the site and it's become a little more difficult
to actually get through to the essays.

I've been learning Python and I finally reached the web scraping chapter. A few pages in, I decided to stop where I
was at and start writing a program to dowload all 141 essays on the apstudynotes site. Let the hacking begin!

# The Code
First, let's go over the imports.
```python
import os, requests, bs4
```
We import os, requests, and bs4. We use os (Operating System) to check for and create directories - where the files will be located, requests to get the website html, and bs4 (Beautiful Soup) to parse it.

The next part of the code is self explanatory.
```
# Create a txt, html, and doc folder if they don't already exist
if not os.path.exists("./txt"):
    os.makedirs("./txt")
if not os.path.exists("./html"):
    os.makedirs("./html")
if not os.path.exists("./doc"):
    os.makedirs("./doc")
```

Now the next step we *could* take is to open up every single url and copy it into a .txt document. Then we'd read every single url from the .txt document... But why do that when we have Python?
```
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
```
Instead, we requests.get('https://www.apstudynotes.org/essays/') and parse the html for all links in header 3. Each link is added to urlList and edited a little to get the full url to each different essay on the website.

To create a name for each file, we edit urlList.
```
# Get the titles of each essay, so we can name the files accurately
titleList = []
for i in range(len(elems)):
    tempString = urlList[i]
    tempString = tempString[len(str(r"https://www.apstudynotes.org/")):(len(tempString)-1)]
    for j in range(len(tempString)):
        if tempString[j] == '/':
            tempString = tempString[:j] + '-' + tempString[j+1:]
    titleList.append(tempString)
```

