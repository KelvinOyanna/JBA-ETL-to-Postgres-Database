import pandas
with open("cru-ts-2-10.1991-2000-cutdown.pre", "r") as raw_file:
    month = []
    year = []
    main_data = []
    index = 0

    raw_file.seek(249)
    raw_data =  raw_file.readlines()
    
    print(raw_data)

""""
    line_data = []
    for line in raw_data:
        if not line.startswith("Grid-ref="):
            line_data.append(line)
    
    print(line_data[9])



            month.append(line_data)
            #for row in main_data:
    print(month[5])
                main_data.append(row)
    for item in main_data:
        month.append(item)
    for item2 in main_data:
        year.append(item2[0])
    month_year_data = pandas.DataFrame([month, year], columns = ['Months','Years'])
    print(month_year_data.head())
    """







##        while index < len(reading):
##            ncontent = reading[index]
##
##            index +=1
##            print(index, ncontent)
            
        #lstapnd = lst_a.append(reading[1])
        #print(lstapnd)
    
