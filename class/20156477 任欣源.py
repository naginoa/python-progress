import re


with open('sohu.html', encoding='utf-8') as f:
    html = f.read()
    allfinds = re.findall(r"<a.*?href=.*?<\/a>",html, re.I)
    
    for i in allfinds:
        #print(i)
        href = re.findall(r"htt.*?\"", i, re.I)
        for j in href:
            link = j[:-1]
            print(link)
            with open('result.txt', 'a') as f:
                f.writelines(link)
                f.writelines('\n')
        texts = re.findall(r">.*?\<", i, re.I)
        for k in texts:
            text = k[1:-1]
            print(text)
            with open('result.txt', 'a') as f:
                f.writelines(text)
                f.writelines('\n')
        