from fuzzywuzzy import fuzz
import re
import requests
inputurl = 'http://localhost:3000/source'
targeturl = 'http://localhost:3000/target'
inp_data = requests.get(inputurl).json().get('formatFields')
tar_data = requests.get(targeturl).json().get('formatFields')
for ke,val in inp_data.items():
    print (ke)
    for i in val:
        res = []
        i = re.sub(r'[,-./]|\s',r'',i)
        for j in tar_data:
            c = (fuzz.token_set_ratio(j,i))
            a = (fuzz.ratio(j,i))
            if not res:
                res = [i,j,a+c]
            else:
                if res[2] < a+c:
                    res = [i,j,a+c]
        print(res)