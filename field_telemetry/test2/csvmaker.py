import csv

def makecsv(column_names, values_tup):
   
    newlist = []
    for row in values_tup:  # iterate through each tuple in the values list
        for col, val in zip(column_names, row):  # Zip the columns with the current row
            if val is not None:  # Check if the value is not None
                newlist.append((col, val))  # Print the column and its corresponding value
    # print(newlist)
    col_vals_dict = {}
    for tup in newlist:
        key, value = tup
        if key not in col_vals_dict:
            col_vals_dict[key] = []
        col_vals_dict[key].append(value)

    print(col_vals_dict)
    

    with open('names.csv', mode='w') as csvfile:
        writer = csv.writer(csvfile)

        # Write the header (keys of the dictionary)
        writer.writerow(col_vals_dict.keys())

        # * unpacks the list of values for each key
        # zip usually takes two lists but here each key value list are the lists
        for row in zip(*col_vals_dict.values()):
            writer.writerow(row)

    returntofunc = "I have returned"
    return returntofunc
        
    