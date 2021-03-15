from functions.utils import fileToLineList
import re

pathOne = "..\\files\\temp\\Yq5hMp11.txt"
lineList = fileToLineList(pathOne)
regex = '^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+[.]\w{2,3}$'
combex = '^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+[.]\w{2,3}:[A-Za-z0-9\._!#$%&()*+,-./:;<=>?@^_`{|}~]+$'
combex2 = '[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+[.]\w{2,3}:[A-Za-z0-9\._!#$%&()*+,-./:;<=>?@^_`{|}~]+'
passex = '^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$'

for i in lineList:
    emails = re.findall(combex2, i)
    if emails: print(emails)
