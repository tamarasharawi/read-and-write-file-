import csv

def column (file_path):
    with open (file_path, mode='r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader :
            if any('column_num:' in cell for cell in row):
                for cell in row:
                    if 'column_num:' in cell:
                        row_data = cell.split()
                      #  print(row_data)
                        
                for item in row_data:
                    try:
                        num = int(item)
                        number =num
                    except ValueError:
                        pass
                return number

def read_csv(file_path, columns):
    with open(file_path, mode='r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            new_row = []
            count = 0  
            for cell in row:
                if count < columns:  
                    if cell == '':
                        new_row.append('missed word')
                    else:
                        new_row.append(cell)
                    count += 1  
            yield new_row


def drop_duplicates(data):
    new_data= []
    for row in data:
     if row not in new_data: 
            new_data.append(row)
    return new_data



num_of_col = column('file_example')

print("Number of columns ", num_of_col)

data_file = read_csv('fil_example', num_of_col)
data_file = drop_duplicates(data_file)

for row in data_file:
    print(row)

output_file = 'cleaned_data'
with open(output_file, mode='w') as csvfile:
    writer = csv.writer(csvfile)
    for row in data_file:
        writer.writerow(row)