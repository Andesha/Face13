import pandas as pd
import sys

df = pd.read_csv(sys.argv[1], sep='\t')
# df = df.drop(['sample', 'response_time', 'trial_type'],axis=1)
df = df.drop(['HED'],axis=1)
df.to_csv(sys.argv[1], sep='\t', index=None)
print('Done')
