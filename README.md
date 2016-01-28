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
```python
import os, requests, bs4
```
