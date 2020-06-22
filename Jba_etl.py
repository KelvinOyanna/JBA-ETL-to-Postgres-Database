import pandas as pd
import re

month_data = []
ref = []
with open('cru-ts-2-10.1991-2000-cutdown.pre', 'r') as raw_file:
    for line in raw_file:
        line_data = raw_file.readline()
        if re.search(r'^(Grid-ref=) +[0-9], +[0-9]+', line_data):
            ref_data = re.search(r'^(Grid-ref=) +[0-9], +[0-9]+', line_data).group()
            ref_data =  ref_data.split(' ')
            xref = ref_data[3].strip(',')
            yref = ref_data[4]
            ref.append([xref, yref])
        elif re.search(r'([0-9]+ +)+[0-9]+' , line_data):
            row_data = re.search(r'([0-9]+ +)+[0-9]+' , line_data).group()
            #month_data.append(row_data)
            print(row_data)

            #print(ref_data) [0-9]+ [0-9] [0-9] [0-9] [0-9] [0-9] [0-9] [0-9] [0-9] [0-9] [0-9]  +[0-9]
      
    #print(month_data[0])
    #print(ref)



"""
for item in line:
                main_data.append(item)
                for month_item in main_data:
                    month_data.append(month_item)
"""