from pathlib import Path
import json
import pandas as pd
from pprint import pprint

path = Path('./sekolahmu')

dataframes = []
for js in path.iterdir():
    t1 = json.loads(open(js).read())
    test_df = pd.DataFrame(t1['data'])
    dataframes.append(test_df)
df = pd.concat(dataframes)
df.to_csv('./sekolahmu/sekolahmu.csv', index=False)
