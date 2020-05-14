import requests
# import itertools
import datetime
import time
files_to_check = ('https://cdn-dlm.esd.sage.com/Sage50CanadianEdition/18611/SA_20201CP1.exe',
)
#czech_iterator= itertools.cycle(files_to_check)

def file_scan(file_list):
    for ural in file_list:
        dl = requests.get(ural)

        if dl.status_code not in (200,):
            print(f'the status code was{dl.status_code}')
        else:
            file_size = len(dl.content)/1000000000.0
            print(f'the file was {file_size} GB')



def main():
    while True:
        file_scan(files_to_check)

        dt = datetime.datetime.now() + datetime.timedelta(hours=1)
    
        while datetime.datetime.now() < dt:
            time.sleep(1)

main()