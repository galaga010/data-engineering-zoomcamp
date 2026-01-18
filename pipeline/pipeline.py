'''
import sys
print("arguments", sys.argv)

day = int(sys.argv[1])
if len(sys.argv) < 2:
    print("Usage: python pipeline/pipeline.py <month>")
    sys.exit(1)
month = int(sys.argv[1])

print(f"Running pipeline for day {day}")


import pandas as pd

df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
print(df.head())

df.to_parquet(f"output_day_{sys.argv[1]}.parquet")
'''

import sys
import pandas as pd

# 1. Check if arguments exist BEFORE accessing them
if len(sys.argv) < 2:
    print("Usage: python pipeline.py <day>")
    sys.exit(1)

# 2. Now it is safe to access sys.argv[1]
day = int(sys.argv[1])
print(f"Running pipeline for day {day}")

# Rest of your script...
df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
print(df.head())

df.to_parquet(f"output_day_{day}.parquet")

