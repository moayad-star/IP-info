# Modules

import mechanicalsoup
import requests


# Color
green = "\033[;32;m"
red = "\033[;31;m"


# Test network
try:
    requests.get("https://www.iplocation.net/",timeout=5)
except (requests.exceptions.ConnectTimeout,requests.exceptions.ConnectionError,requests.exceptions.ReadTimeout,requests.exceptions.ChunkedEncodingError):
    exit(f"{red} You are offline!\n\n")


# Git IP info
browser = mechanicalsoup.StatefulBrowser(
    soup_config={'features': 'lxml'},
    raise_on_404=True,
    user_agent='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
)
browser.open("https://www.iplocation.net/")
Table = browser.page.find("table")


# Import [IP4,IP6,IPS,Location]
IP4 = str(Table.select("tr")[4].select("td"))[5:-6].strip()
IP6 = str(Table.select("tr")[1].select("td"))
IP6 = IP6[IP6.index('bold;">')+7:IP6.index("</span>")].strip()
ISP = str(Table.select("tr")[3].select("td"))[5:-6].strip()
Location = str(Table.select("tr")[2].select("td"))
Location = Location[5:Location.index(")")+1]


# Print IP
print(f"""

 {red}┌{'─'*40}┐
 {red}│{green}                IP-info                 {red}│
 {red}│{green}         Create by {red}Moayad Ahmed         │
 {red}│{green}   https://www.github.com/{red}moayad-star   │
 {red}└{'─'*40}┘


{red}IP4: {green}{IP4}
{red}IP6: {green}{IP6}
{red}ISP: {green}{ISP}
{red}Location: {green}{Location}


""")
