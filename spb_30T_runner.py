import os
from scrapy.cmdline import execute
from pathlib import Path
# import pd
import merger

os.chdir(os.path.dirname(os.path.realpath(__file__)))
print(os.path.dirname(os.path.realpath(__file__)))
tmp = 'spb_30T_temp.csv'
try:
    execute(
        [
            'scrapy',
            'crawl',
            'jobs',
            '-a',
            'start_date=2023/07/01',
            '-a',
            'end_date=2023/12/01',
            '-a',
            
            'config=spb_30T.json',
            '-o',
            tmp + ':csv'
        ]
    )
except SystemExit:
    pass


# src = Path(r'/home/nikolai/Yandex.Disk/data/finam/src_spb_30T.csv')
src = Path(r'C:\Users\nkoud\YandexDisk\data\finam\src_spb_30T.csv')

merger.merge(src=src, tmp=Path(tmp))



# scrapy crawl jobs -a start_date="2019/01/01" -a end_date="2019/04/01" -o "2019_01-04.csv" -t csv
