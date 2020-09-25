import csv


def file_spliter(data_path, file_name, column_to_split_on):

    with open(data_path + "/RAW/" + file_name, encoding = 'utf-8') as file :
        file_dict = csv.DictReader(file, delimiter = '\t')

        already_opened_files = {}

        for row in file_dict:
            file_column = row[column_to_split_on]

            if file_column not in already_opened_files:
                out_file = open(data_path + f"/CURATED/{file_column}.csv", 'w', encoding='utf-8')
                dict_writer = csv.DictWriter(out_file, fieldnames=file_dict.fieldnames)
                dict_writer.writeheader()
                already_opened_files[file_column] = out_file, dict_writer

            already_opened_files[file_column][1].writerow(row)

        for output, _ in already_opened_files.values():
            output.close()
