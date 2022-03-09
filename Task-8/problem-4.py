import pandas as pd
import numpy as np

series = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai', 'campus'])
newSeries = series.map(lambda x: x[0].upper() + x[1:-1] + x[-1])

print(series)
print(newSeries)

a = np.array(newSeries)
print(*a, sep=' ')