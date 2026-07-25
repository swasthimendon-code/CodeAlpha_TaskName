import pandas as pd
import matplotlib.pyplot as plt

data={
    "Product":["laptop","mobile","tablet","headphones","smartwatch"],
    "Sales":[120,200,80,150,100]

}
df=pd.DataFrame(data)
fig,ax=plt.subplots(1,3,figsize=(18,6))


ax[0].bar(df["Product"],df["Sales"])
ax[0].set_title("Product Sales")
ax[0].set_xlabel("Product")
ax[0].set_ylabel("Sales")
ax[0].tick_params(axis="x",rotation=45)

ax[1].plot(df["Product"],df["Sales"],marker="o")
ax[1].set_title("Sales Trend")
ax[1].set_xlabel("Product")
ax[1].set_ylabel("Sales")
ax[1].tick_params(axis="x",rotation=45)

ax[2].pie(
    df["Sales"],
    labels=df["Product"],
    autopct="%1.1f%%")
ax[2].set_title("Sales Distribution")
fig.suptitle("SALES DASHBOARD",fontsize=18)

plt.tight_layout()
plt.show()

import seaborn as sns
plt.figure(figsize=(8,5))
sns.barplot(x="Product",y="Sales", data=df)
plt.title("sales by product using seaborn")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,5))
sns.barplot(
    x="Product",
    y="Sales",
    data=df)
plt.title("sales comparison identify best and worst selling products")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=45)
for i,value in enumerate(df["Sales"]):plt.text(i,value+5,str(value),ha="center")
plt.tight_layout()
plt.show()

best_product=df.loc[df["Sales"].idxmax(),"Product"]
best_sales=df["Sales"].max()
worst_product=df.loc[df["Sales"].idxmin(),"Product"]
worst_sales=df["Sales"].min()
print("\nDATA STORY")
print("--------------------")
print(best_product, "is the best-selling product with", best_sales, "sales.")
print(worst_product, "is the lowest-selling product with",worst_sales, "sales.")
print("The company should focus on promoting the best-selling products")
print("and improve the sales of low-performing products")


print("\nPORTFOLIO PROJECT")
print("-------------------------")
print("Project: Sales Data Visualization Dashboard")
print("Tools:python,pandas,matplotlib,seaborn")
print("visualizations:Bar Chart,Line Chart,Pie chart")
print("Insights:mobile is the best selling product")
print("Insight:Tablet has the lowest sales")
print("Decision:focus on promoting high-selling products and improving low-selling products")