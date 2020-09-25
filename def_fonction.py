
import csv

RAW_LOCAL_PATH = '../data/RAW/'
CURATED_LOCAL_PATH = '../data/CURATED/'
TITLE_FILE_NAME = 'title.basics.tsv'


def split_data(self):
        '''
        Break raw data into many files
        '''
        
        with open(RAW_LOCAL_PATH + TITLE_FILE_NAME, encoding='utf-8') as file_stream:    
            file_stream_reader = csv.DictReader(file_stream, delimiter='\t')
            
            open_files_references = {}

            for row in file_stream_reader:
                title_type = row['titleType']

                # Open a new file and write the header
                if title_type not in open_files_references:
                    output_file = open(CURATED_LOCAL_PATH + '{}.csv'.format(title_type), 'w', encoding='utf-8', newline='')
                    dictionary_writer = csv.DictWriter(output_file, fieldnames=file_stream_reader.fieldnames)
                    # dw.writeheader()
                    open_files_references[title_type] = output_file, dictionary_writer
                # Always write the row
                open_files_references[title_type][1].writerow(row)
            # Close all the files
            for output_file, _ in open_files_references.values():
                output_file.close()



