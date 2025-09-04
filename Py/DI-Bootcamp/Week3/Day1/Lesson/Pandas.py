import pandas as pd

data = {
    'Book Title': ['The Great Gatsby', 'To Kill a Mockingbird', '1984', 'Pride and Prejudice', 'The Catcher in the Rye'],
    'Author': ['F. Scott Fitzgerald', 'Harper Lee', 'George Orwell', 'Jane Austen', 'J.D. Salinger'],
    'Genre': ['Classic', 'Classic', 'Dystopian', 'Classic', 'Classic'],
    'Price': [10.99, 8.99, 7.99, 11.99, 9.99],
    'Copies Sold': [500, 600, 800, 300, 450]
}

df = pd.DataFrame(data)
#Use head() to view the first few rows of the DataFrame.
#Use describe() to get a statistical summary of the numerical columns.
#Use info() to get a concise summary of the DataFrame, including the number of non-null entries in each column.
#Sort the DataFrame based on the Price or Copies Sold.
#Filter the books by a specific Genre or books with Price above a certain threshold.
#Group the books by Author and sum up the Copies Sold.

print(df.head())
print('----------------------------------------------------------------\n')
print(df.describe())
print('----------------------------------------------------------------\n')
print(df.info())
print('----------------------------------------------------------------\n')
print(df.sort_values(by='Price'))
print('----------------------------------------------------------------\n')
print(df.sort_values(by='Copies Sold', ascending=False))
print('----------------------------------------------------------------\n')
print(df[df['Genre'] == 'Classic'])
print('----------------------------------------------------------------\n')
print(df[df['Price']>10])
print('----------------------------------------------------------------\n')
print(df.groupby('Author')['Copies Sold'].sum())
