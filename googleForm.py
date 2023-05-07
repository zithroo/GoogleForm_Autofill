import requests
from bs4 import BeautifulSoup

url = "https://docs.google.com/forms/d/e/1FAIpQLScTpJwpQsorXr5j-af5AxVVyOUizFjn4XJNnubEMgV-sdiUAQ/formResponse"

def fill_form():
    value_0 = {
        # Name
        "entry.1174952989": "DerickSun", 
        # Email Address , Note that @ = %04 in URL
        "entry.108090783": "b101109025%40tmu.edu.tw",
        # Phone num
        "entry.286276851": "0912345678",
        # Fill answer accoording to options in form
        "entry.1638716274": "臺北醫學大學 Taipei Medical University",
        "entry.1449184513": "大學生 College Students",
        # Colleage
        "entry.785522089": "Med"
    }
    value_1 = {
        # Answer: Don't touch
        "entry.1628933266": "B.核能/Nuclear energy",
        "entry.1572816013": "B. 第五級最省電/The fifth level is the most power-efficient",
        "entry.1924288890": "A. 風力/ Wind energy",
        "entry.486085256": "D.天然氣/Natural gas",
        "entry.1728449788": "5"
    }

    newUrl = url +\
        "?{}".format("&".join("{}={}".format(k,v) for k,v in value_0.items()))+\
        "&pageHistory=0,1&{}&submit=Submit".format("&".join("{}={}".format(k,v) for k,v in value_1.items())) 
    print("newUrl= "+newUrl)
    return newUrl


def submit(url):
    try:
        response = requests.post(url, data = {})
        if response.status_code == 200:
            print("Submitted successfully")
            
            soup = BeautifulSoup(response.content, 'html.parser')
            title_tag = soup.find('title')
            if title_tag and title_tag.text.strip() == \
                'SDGs 書展系列活動~SDG7線上有獎徵答抽好禮！ Event Series-SDGs Book Exhibition: SDG 6 online quiz contest to win awards!':        
                print('表單提交成功')
            else:
                print('表單提交失敗')
            return True
        else:
            print("Error! Status code:", response.status_code)
            return False
    except Exception as e:
        print("Error:", e)
        return False
    
submit(fill_form())

# Test form
"""
    url_t = "https://docs.google.com/forms/d/e/1FAIpQLSdtSKHDkAKsGw-Mfb5xWSvNgWaTRZDycMYIV-H4A42v2NvBKg/formResponse"
    value_t0 = {
        "entry.1117810575": "jason%40zz",
        "entry.652095033": "123",
        "entry.853223333": "College"
    }
    value_t1 = {
        "entry.2072610791": "A",
        "entry.33220194": "2"
    }
    Response title: AutofillTest
"""

"""
<div jsname="o6bZLc">
    <input type="hidden" name="entry.108090783" value="dijochkbv">
    <input type="hidden" name="entry.273842807" value="oijhkvb">
    <input type="hidden" name="entry.286276851" value="hjvcjsbknl">
    <input type="hidden" name="entry.785522089" value="kljhg">
    <input type="hidden" name="entry.1174952989" value="sadljfkb">
    <input type="hidden" name="entry.1449184513" value="大學生 College Students">
    <input type="hidden" name="entry.1638716274" value="臺北醫學大學 Taipei Medical University">
    <input type="hidden" name="dlut" value="1683433836230">
</div>
<div jsname="o6bZLc">
    <input type="hidden" name="entry.1628933266" value="A. 太陽能 /Solar energy">
    <input type="hidden" name="entry.1572816013" value="B. 第五級最省電/The fifth level is the most power-efficient">
    <input type="hidden" name="entry.1924288890" value="C.太陽能/Solar energy">
    <input type="hidden" name="entry.486085256" value="D.天然氣/Natural gas">
    <input type="hidden" name="entry.1728449788" value="5">
    <input type="hidden" name="dlut" value="1683434362675">
</div>
response title = "SDGs 書展系列活動~SDG7線上有獎徵答抽好禮！ Event Series-SDGs Book Exhibition: SDG 6 online quiz contest to win awards!"
"""

# https://docs.google.com/forms/d/e/1FAIpQLSdtSKHDkAKsGw-Mfb5xWSvNgWaTRZDycMYIV-H4A42v2NvBKg/formResponse?entry.1117810575=jason&entry.652095033=123&entry.853223333=College&entry.2072610791=A&entry.33220194=2&pageHistory=0,1&submit=Submit