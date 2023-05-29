#coding:utf-8
import pandas as pd
import requests
from threading import Thread
import csv
urls=[]

with open('chatgptnetwork.csv', newline='',encoding='utf-8') as f:
    
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        a=row[0]
        urls.append(a)



def check_text(url, keyword):
    try:
        r = requests.get(url, timeout=10)
        # 判断响应文本是否包含关键字 
        if keyword in r.text:
            print (r.text)
            if keywords in r.text:
                print('1')

            else:
                print(2)
                with open('a.txt', 'a') as f:
                    f.write(url + '\n')
    except requests.exceptions.RequestException as e:
        pass

# 定义 URL 列表和关键字 

keyword = 'ChatGPT'
keywords='apikey'
keywo='未经授权，请先进行验证。'

# 创建多线程，执行 check_text 函数
threads = [Thread(target=check_text, args=(url, keyword)) for url in urls]

# 开始执行多线程
for thread in threads:
    thread.start()

# 等待所有线程执行完毕
for thread in threads:
    thread.join()

print('完成！')