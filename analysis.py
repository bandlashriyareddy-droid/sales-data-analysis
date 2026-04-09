import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sales_data.csv")

print(data)

region_sales = data.groupby("Region")["Sales"].sum()

region_sales.plot(kind="bar")
plt.show()