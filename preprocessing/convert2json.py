import csv
import json
 
def csv_to_json(csv_file_path, json_file_path):
    data_dict = {}
    final_arr=[]
    with open(csv_file_path, encoding = 'utf-8') as csv_file_handler:
        csv_reader = csv.DictReader(csv_file_handler)
        for rows in csv_reader:
            final_arr.append(rows)

    with open(json_file_path, 'w', encoding = 'utf-8') as json_file_handler:
        #Step 4
        json_file_handler.write(json.dumps(final_arr, indent = 4))

csv_file_path ='flipkart2.csv'
json_file_path ='flip.json'
 
csv_to_json(csv_file_path, json_file_path)