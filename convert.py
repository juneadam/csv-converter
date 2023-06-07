import json
import csv

# csv file name https://www.geeksforgeeks.org/working-csv-files-python/
# filename = "birddex.csv"
 
def convertCSVtoDict(filename, output_name):
    # initializing the titles and rows list
    fields = []
    rows = []

    output_name = {'data': []}
    
    # reading csv file
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
        
        # extracting field names through first row
        fields = next(csvreader)
    
        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)
    # for row in rows[:5]:
    #     # parsing each column of a row
    #     for col in row:
    #         print("%10s"%col,end=" "),
    #     print('\n')

    for row in rows:
        temp_obj = {}
        for i, col in enumerate(row):
            temp_obj[fields[i]] = col
        output_name['data'].append(temp_obj)

    print(f'this is the json:\n{output_name}')

    return output_name

def writeDICTtoJSON(dict_input, output):
    json_input = json.dumps(dict_input)

    with open(output + ".json", 'w') as file:
        file.write(json_input)

# writeDICTtoJSON(convertCSVtoDict(filename, 'birddex_json'), 'BIRDDEX')
