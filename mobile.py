import pandas as pd
import matplotlib.pyplot as plt


# Reading the Excel file (sheet "Tech") into a pandas DataFrame
df = pd.read_excel(r"D:\Mobile_Price_Analysis_Project\project\mobile_price_comparison.xlsx",
             engine="openpyxl")

# Load dataset
print("File loaded:", df.shape)   # Prints the shape (rows, columns)

df.columns = df.columns.str.strip().str.lower()
print(df.columns)


# # Handle missing values
df["ram/storage"] = df["ram/storage"].fillna("No comment") 
#  Fill empty values in 'comments' column with "No comment"

# Convert datatypes
for c in ["brand", "model"]:
     df[c] = df[c].astype(str).str.strip()

     df["rating"] = df["rating"].astype(float)
# Convert rating to float for numeric operations
    # df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Remove duplicates
df.drop_duplicates(inplace=True)

#Max and Min rating
print("Minimun rating per brand:\n",df["rating"].min())
print("Maximun rating per brand:\n",df["rating"].max())


print("Average Rating Per Brand:\n", df.groupby("brand")["rating"].mean())
# Average rating per product
print("\nTop 6 reviews:\n", df.sort_values(by="rating", ascending=False).head(6))
# Top 10 reviews (sorted by rating, descending)

# Visualization
# Histogram-ratings
df["rating"].plot(kind="hist", bins=10, title="Histogram of Ratings")
plt.xlabel("Rating")
plt.show()

# Average rating per brand as a bar chart
df.groupby("brand")["rating"].mean().plot(kind="bar", title="Average Rating by brand")
plt.ylabel("Average Rating")
plt.show()

# Pie chart of average rating per brand
df.groupby("brand")["rating"].mean().plot(kind="pie",autopct='%1.1f%%', title="Rating by Brand")
plt.ylabel(" ")  
plt.show()

# comparing brand vs rating -scatter plot
df.reset_index().plot(kind="scatter", x="index", y="rating", title="Scatter: Product Index vs Rating")
plt.show()

# Cleaned excel file created 
df.to_excel("Cleaned_data.xlsx",index=False)



