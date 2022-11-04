from os.path import exists
from Sem7_8_PB_CSV import creating
from Sem7_8_PB_File import writing_scv
from Sem7_8_PB_File import writing_txt


path = 'Sem7_8_PB.csv'
valid = exists(path)
if not valid:
    creating()

writing_scv()
writing_txt()