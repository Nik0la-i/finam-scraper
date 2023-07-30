import os
from scrapy.cmdline import execute
from pathlib import Path
# import pd
import merger

os.chdir(os.path.dirname(os.path.realpath(__file__)))
tmp = 'spb_daily_temp.csv'
try:
    execute(
        [
            'scrapy',
            'crawl',
            'jobs',
            '-a',
            'start_date=2023/07/24',
            '-a',
            'end_date=2023/07/26',
            '-a',
            'config=spb_daily.json',
            '-o',
            tmp + ':csv'
        ]
    )
except SystemExit:
    pass

src = Path(r'C:\data\finam\src_spb_daily.csv')
merger.merge(src=src, tmp=Path(tmp))



# scrapy crawl jobs -a start_date="2019/01/01" -a end_date="2019/04/01" -o "2019_01-04.csv" -t csv