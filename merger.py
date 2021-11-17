import pandas as pd
import numpy as np

# load dataframes
redwine = pd.read_csv('winequality-red.csv', sep=';')
whitewine = pd.read_csv('winequality-white.csv', sep=';')

# type name
winetype = 'Red_wine'

# added the column to set the red wines as Red_whines
redwine[winetype] = np.ones(redwine.shape[0])

# added the column to set the white wines as not Red_whines
whitewine[winetype] = np.zeros(whitewine.shape[0])

# merged dataframes
merged = redwine.append(whitewine)

# verifying if both are in the merged
print()
print(merged[(merged[winetype] == 0.0)].head(5).to_markdown())
print(merged[(merged[winetype] == 1.0)].head(5).to_markdown())

# changed the names to capitalized and replaced spaces with underscores
for column in merged.columns:
    print(column)
    merged.rename(columns={column: column.capitalize().replace(' ', '_')}, inplace=True)

# showcasing again
print(merged.head(5).to_markdown())
# saving merged to merged.csv
merged.to_csv(index=False, path_or_buf='merged.csv')
