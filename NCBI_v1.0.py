
# coding: utf-8

import sys
import urllib.request
from bs4 import BeautifulSoup
"""载入相应模块"""

def open_url(term):

    #打开网页
 
    url = 'https://www.ncbi.nlm.nih.gov/gene/?term=' + term
    req = urllib.request.Request(url)
    req.add_header("User-Agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36")
    page  = urllib.request.urlopen(req)
    html = page.read()
    soup = BeautifulSoup(html, "lxml")
    return soup

def open_urlensembl(term):

    # 打开ENSEMBL网页

    url = 'http://www.ensembl.org/Ailuropoda_melanoleuca/Gene/Summary?db=core;g=' + term
    req = urllib.request.Request(url)
    req.add_header("User-Agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36")
    page  = urllib.request.urlopen(req)
    html = page.read()
    soup = BeautifulSoup(html, "lxml")
    return soup

def open_url2(term):
    """
    打开某个基因的具体介绍界面
    """
    url = 'https://www.ncbi.nlm.nih.gov/gene/' + term
    req = urllib.request.Request(url)
    req.add_header("User-Agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36")
    page  = urllib.request.urlopen(req)
    html = page.read()
    soup = BeautifulSoup(html, "lxml")
    return soup

def get_GeneSymbol(term):
    
    # 获得每个ENSEMBL对应对应GeneSymbol号

    soup = open_url(term)
    try:
        GeneSymbol = soup.find("dd", class_= "noline").get_text()
    except AttributeError:
        soup = open_urlensembl(term)
        pre = soup.find_all("div", class_="lhs")[0]
        result = soup.find_all("div", class_= "rhs")[0]
        if pre.get_text() == 'Description':
            GeneSymbol = ''.join(result.get_text().split("[")[0].strip())
        else:
            GeneSymbol = "No Description"
        #print('*****', GeneSymbol)
        
    """
    # 如果ENSEMBL没有对应的结果， 则会抛出错误， 如果不存在， 则使用expect检索ENSEMBL号在EMSEMBL对应的Description，使用Description进行查询
    """
    return GeneSymbol 
    # 因为find_all返回的是包含所有符合条件的值的列表， 所以无法对列表使用get_text()， 如果是find则返回符合条件的第一个值

def get_item(GeneSymbol):
    """
    获得每个Gene ID对应的Description， 如果是人类的则进行查询，否则直到找到人类的为止
    """
    term = '+'.join(GeneSymbol.split(' '))
    #print(term)
    soup = open_url(term)
    IDs, Description = [], []
    #dic = {}
    # 构建字典，按照ID和Description对应的关系

    for i in soup.find_all("span", class_= "gene-id"):
        IDs.append(i.get_text().split(":")[1].strip())
    # 找出每个Symbol对应的ID
    
    array = soup.find_all("td")
    for i in range(1, len(array), 5):
        Description.append(array[i].get_text())
    # 找出每个ID对应的描述， 然后看描述中是否有human或者Homo Spanines等表示人类的词汇

    #for i in range(len(IDs)):
    #    dic[IDs[i]] = [Description[i]]
    # 构建字典，按照ID和Description对应的关系

    for i in range(len(Description)):
        if ''.join(Description[i]).find("human") != -1 or ''.join(Description[i]).find("Homo sapiens") != -1:
            ids = ''.join(IDs[i])
            break
    
    return ids
    #  如果Description中包含人类的内容，则把对应的ID号输出， 只输出第一个符合内容的结果

def get_summary(IDs):
    """
    对get_item的输出结果进行查询，输入summary和Organism的内容
    """
    result = []
    # 储存符合筛选条件的所有节点的内容，然后对这些内容进行重新分割，筛选
    soup = open_url2(IDs)
    for i in soup.find_all("div", class_= "section"):
        # 如果按照列表来处的话， 会发现所有的内容都属于列表中的一个元素， 而且包含换行符
        result.append(i.get_text())
    content = ''.join(result).split("\n")
    # 所以先把所有的元素转换位字符串后在自行进行切割
    if "Summary" in content:
        Summary = ''.join(content[content.index("Summary")+1].split('[')[0])
    else:
        Summary = "There is no summary"
    Organism = ''.join(content[content.index("Organism")+2])
    # 正在考虑要不要输出Organism， 毕竟get_item已经筛选过所有的Organism为human

    return Summary, Organism

def main():
    with open ('/home/insilicon/Desktop/第二次人工免疫下调.txt', 'r') as file:
        for line in file:
            line = line.strip()
            print(line)
            GeneSymbol = get_GeneSymbol(line)
            if GeneSymbol == "No Description":
                print(GeneSymbol, '\n')
                continue
                # 如果GeneSymbol==Can't find this ENSEMBL ID， 则进行下一个条目的查询
            else:
                IDs = get_item(GeneSymbol)
                print(IDs)
                Summary, Organism = get_summary(IDs)
                print(Organism)
                print(Summary)
                print('\n')
                
if __name__ == "__main__":
    main()



