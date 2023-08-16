import pandas as pd
from pathlib import Path

#compression_opts = dict(method='zip', archive_name='out.csv') 

def merge(src: Path, tmp: Path):
    df_new = pd.read_csv(tmp)
    print(df_new.shape)
    print(src)
    if src.exists():
        print('merge data...',)
        df_old = pd.read_csv(src)
        df = pd.concat([df_old, df_new], ignore_index=True, axis=0)
        df = df.drop_duplicates().sort_values(by=['datetime'], ascending=False)
        df.to_csv(src, index=False)
        print('done')
    else:
        df_new.sort_values(by='datetime', ascending=False).to_csv(src, index=False)
        

    tmp.unlink()
