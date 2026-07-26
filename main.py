import os
from uitls import read_fileTxt
from uitls import preProcess
from uitls import Chunk
from dotenv import load_dotenv
import os
load_dotenv()

# Getting the file
file_path =os.getenv('DPATH')

# Reading the whole file
data = read_fileTxt(file_path)
# Creating a single string NOT recommended for very big txt Python usually have the limit of  63 GB
txt = preProcess(data)
chuz = Chunk(txt)
print(chuz)



