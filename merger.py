import pandas as pd
from pathlib import Path


def merge(src: Path, tmp: Path):
    df_new = pd.read_csv(tmp)
    if src.exists():
        df_old = pd.read_csv(src)
        (pd.concat([df_old, df_new], ignore_index=True, axis=0)
         .drop_duplicates()
         .sort_values(by=['datetime'], ascending=False)
         .to_csv(src, index=False)
         )
    else:
        df_new.sort_values(by='datetime', ascending=False).to_csv(src, index=False)

    tmp.unlink()