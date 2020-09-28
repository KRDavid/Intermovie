import requests
import sys
import os
from zipfile import ZipFile

class downloader():
    def __init__(self, data_path):
        self.data_path = data_path
        if not os.path.exists(self.data_path + f"/CURATED"):
            os.makedirs(self.data_path + f"/CURATED")
        if not os.path.exists(self.data_path + f"/RAW"):
            os.makedirs(self.data_path + f"/RAW")
        if not os.path.exists(self.data_path + f"/OUTPUT"):
            os.makedirs(self.data_path + f"/OUTPUT")

    def data_download(self, file_name, download_url):
        print('Data downloading...')
        with open(self.data_path + "/RAW/" + file_name, "wb") as file:
            response = requests.get(download_url, stream=True)
            total_length = response.headers.get('content-length')

            if total_length is None: # no content length header
                file.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    file.write(data)
                    done = int(50 * dl / total_length)
                    sys.stdout.write("\r[%s%s]" % ('■' * done, ' ' * (50-done)) )    
                    sys.stdout.flush()

        print('Download finished')

    def data_extract(self, file_name):
        print("Data extracting...")
        with ZipFile(self.data_path + "/RAW/" + file_name, 'r') as zipObj:
            zipObj.extractall(self.data_path + "/RAW")
        print("Extraction complete")
