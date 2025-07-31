# Import libraries
import pandas as pd

# Load the dataset
df = pd.read_csv("Raw dataset\Flight_Dataset.csv")
print(df.head())

print("\nNo. of Rows and Columns in the dataset:-", df.shape,"\n")

df.info()

# Remove Unncessary Columns
df.drop(['Unnamed: 0'], axis=1, inplace=True)
df.drop(['flight'], axis=1, inplace=True)

print("\n",df.head(3))


print("\n",df['class'].unique())
df['class'] = df['class'].map({"Economy":0, "Business":1})

print("\n",df['stops'].unique())
df['stops'] = df['stops'].map({"zero":0, "one":1, "two_or_more":2})

df = pd.get_dummies(
    df, columns=[
        'airline', 'source_city', 'departure_time', 
        'arrival_time', 'destination_city'
    ], drop_first=True
)

# Convert Boolean columns to int
df[df.select_dtypes('bool').columns] = df.select_dtypes('bool').astype(int)

# Save the dataset
df.to_csv("Fully Cleaned data.csv")


