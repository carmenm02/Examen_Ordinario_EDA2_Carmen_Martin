from datatime import datetime
from ejer3 import *

def sortByDate(elem):
    return datetime.strptime(elem.fecha, '%d/%m/%Y')
