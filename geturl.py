import requests

# encoding = 'utf-8' parameter is for windows
with open('htmlfile','w',encoding='utf-8') as f:
    baseUrl = "https://cspiration.com/leetcodeClassification"
    f.write(str(requests.get(baseUrl).text))