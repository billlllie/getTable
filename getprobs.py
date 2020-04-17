from bs4 import BeautifulSoup


class ProbGetter:
    @staticmethod
    def getCorTab(keywrods,htmlstr):
        soup = BeautifulSoup(htmlstr,'html.parser')
        res = []
        for word in keywords:
            res.append(soup.find(id=word))
        return res

    @staticmethod
    def generateTable(body):
        name = body.find(class_="col-header").contents[0]
        mds = "\n## "+name+"\n\n|题号\t|题目链接\t|讲解链接\t|说明\t|\n|-------|------|------|------|\n"
        tableEntries = body.find('table').find_all('tr')
        for no,entry in enumerate(tableEntries):
            if no<2:
                continue
            else:
                tds = entry.find_all('td')
                line = ""
                if len(tds[1]) == 0:
                    line += "|"+tds[0].contents[0]+"\t||||\n"
                else:
                    line += "|"+tds[0].contents[0]+"\t|["
                    line += str(tds[1].a.contents[0]).strip('\n').strip('\t')+"]("+tds[1].a['href']+")\t|["
                    line += tds[2].a.contents[0]+"]("+tds[2].a['href']+")\t|"
                    # print(line.replace('\n',''))
                    line = line.replace('\n','')
                    if len(tds[3].contents) == 0:
                        line += "|\n"
                    else:
                        line += tds[3].contents[0]+"|\n"
                    
                    mds += line
        return mds

    @staticmethod
    def generateTodo(body):
        name = body.find(class_="col-header").contents[0]
        mds = "\n## "+name+"\n\n"
        tableEntries = body.find('table').find_all('tr')
        for no,entry in enumerate(tableEntries):
            if no<2:
                continue
            else:
                tds = entry.find_all('td')
                line = ""
                if len(tds[1])==0:
                    line += tds[0].contents[0]+'\n'
                else:
                    line += '- [ ] '+tds[0].contents[0]+'\t|'
                    line += '['+str(tds[1].a.contents[0]).strip('\n').strip('\t')+']('+tds[1].a['href']+')\t|'
                    line += '['+tds[2].a.contents[0]+"]("+tds[2].a['href']+")\t|"
                    line = line.replace('\n','')
                    if len(tds[3].contents) == 0:
                        line += "\n"
                    else:
                        line += tds[3].contents[0]+"\n"
                
                mds += line
        return mds

keywords = ["Array","String","Math","Tree","Backtracking",
"DynamicProgramming","LinkedList","BinarySearch","Matrix",
"DFSBFS","StackPriorityQueue","BitManipulation","TopologicalSort",
"Random","Graph","UnionFind","Trie","Design"]
htmlstr = ""
with open('htmlfile','r',encoding='utf-8') as f:
    htmlstr = f.read()

for i,word in enumerate(keywords):
    keywords[i] = "nav-"+word

body = ProbGetter.getCorTab(keywords,htmlstr)

# encoding = 'utf-8' parameter is for windows
with open('table.md','w',encoding='utf-8')as f:
    f.write("")

with open('table.md','a',encoding='utf-8')as f:
    markdownStr = map(ProbGetter.generateTable,body)
    for md in list(markdownStr):
        f.write(md)

with open('todo.md','w',encoding='utf-8')as f:
    f.write("")

with open('todo.md','a',encoding='utf-8')as f:
    markdownStr = map(ProbGetter.generateTodo,body)
    for md in list(markdownStr):
        f.write(md)