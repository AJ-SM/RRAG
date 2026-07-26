import os
from dotenv import load_dotenv
import os
load_dotenv()
filePath = os.getenv('DPATH')

# Read and get Functions DATA..
def read_fileTxt(filepath:str):
    with open(filepath,'r') as f:
        return f.readlines()

def preProcess(data:list):
    final_txt=""
    for line in data:
        ls =  line[:-1]
        ls = ls.strip()

        if not ls:
            continue
        if not ls.endswith('.'):
            ls+="."

        final_txt+=ls
    return final_txt


# Do Chunking
def Chunk(data:list, chunkSize:int = 500):
    chunks=[]
    target = ""
    ctr= 0
    for word in data:

        if ctr==chunkSize :
            chunks.append(target)
            target = ""
            ctr=0
        else:
            target+=word
            ctr+=1

    chunks.append(target)





    return chunks

if __name__=='__main__':
    content = read_fileTxt(filePath)
    txt = preProcess(content)
    # print(txt)
    ckz =Chunk(txt)
