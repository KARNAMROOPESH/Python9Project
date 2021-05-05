import pandas as pd
import plotly_express as pe
import statistics
import math

d = pd.read_csv('./data.csv')
l = d['1'].tolist()
sl = []

mean = statistics.mean(l)

for i in l:
    diff = mean - i
    mult = diff * diff
    sl.append(mult)

sum1 = sum(sl)
length = len(sl) - 1
ans = sum1/length
std = math.sqrt(ans)

print(std)

