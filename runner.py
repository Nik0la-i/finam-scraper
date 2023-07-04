import os
from scrapy.cmdline import execute

os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    execute(
        [
            'scrapy',
            'crawl',
            'jobs',
            '-a',
            'start_date=2019/01/01',
            '-a',
            'end_date=2023/04/29',
            '-o',
            'world_ind_D_2019_202304.csv',
            '-t',
            'csv'
        ]
    )
except SystemExit:
    pass

# scrapy crawl jobs -a start_date="2019/01/01" -a end_date="2019/04/01" -o "2019_01-04.csv" -t csv
