# -*- coding: utf-8 -*-
"""Data Science Project 1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lt5G6HtQHgql4tzZhrh6tDFaQviAfR4v
"""

import pandas as pd
import numpy as np

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Mobile_phone_price.csv')

df.head(10)

df['RAM '].unique()

df

df.shape

df.info()

#menghitung statistika dasar (hanya menghitung tipe data numerik --> int/float aja)
df.describe()

#mengecek apakah ada missing value
df.isna()

#berapa jumlah missing value perkolom
df.isna().sum()

#menampilkan jumlah value unik perkolom
df.nunique()

df['Price ($)'].unique()

df["Screen Size (inches)"].unique()

#cara agar tau apa yg menyebabkan data menjadi object
df[df['Screen Size (inches)'] == '7.6 (unfolded)']

df[df['Screen Size (inches)'] == '6.8 + 3.9']

df['Price ($)'].unique()

df[~df['Price ($)'].str.isnumeric()]

s = '$1,299'

s = s.replace('$', ' ')
s = s.replace(',', ' ')
s = s.replace(' ', '')

s

s.isnumeric()

df.describe()

df['Price ($)'].unique()

df.info()

df['RAM '].unique()

df['RAM '] = df['RAM '].str.replace('GB','')
df['RAM '] = df['RAM '].str.replace(' ','')
df['RAM '] = df['RAM '].astype(int)

df.describe()

df.info()

df

#mengurutkan nilai baterai dari yg paling kecil
df.sort_values(by = ['Battery Capacity (mAh)', 'Price ($)'], ascending = [True, False])

#5 data tertinggi pada kapasitas baterai
df.nlargest(5, 'Battery Capacity (mAh)')

import pandas as pd
import numpy as np

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Mobile_phone_price.csv')

df.info()

df['RAM '] = df['RAM '].str.replace('GB','')
df['RAM '] = df['RAM '].str.replace(' ','')
df['RAM '] = df['RAM '].astype(int)

df[~df['Price ($)'].str.isnumeric()]

df.info()

#cleaning
df['Price ($)'] = df['Price ($)'].str.replace('$','')
df['Price ($)'] = df['Price ($)'].str.replace(',','')
df['Price ($)'] = df['Price ($)'].astype(int)
df.describe()

df.info()

df.nlargest(5, 'Price ($)')

#filter utk melihat brand apple (khusus boolean)
df.loc[df['Brand'] == 'Apple']

#berapa banyak tiap brand
df['Brand'].value_counts()

df.loc[((df['Brand'] == 'Apple') & (df['Price ($)'] <= 600)), ['Brand', 'Model', 'Price ($)']]

df[((df['Brand'] == 'Apple') & (df['Price ($)'] <= 600))]

df.iloc[5:10, 0:3]

df['battery dollar'] = df['Battery Capacity (mAh)'] / df['Price ($)']

df
#semakin tinggi nilai battery dollar, berarti semakin besar kapasitasnya tetapi harganya murah

df.sort_values(by = 'battery dollar')

#menghitung rata-rata setiap brand dengan fungsi groupby dan aggregat
df.groupby(['Brand']).agg(avg_price = ('Price ($)', 'mean'), min_battery_dollar = ('battery dollar', 'min'))

pd.crosstab(df['Brand'], df['RAM '])

df.pivot_table(index = ['Brand'], values = 'Price ($)', aggfunc = 'mean')

df.info()

df_melt = df.melt(id_vars = ['Brand', 'Model', 'RAM ', 'Storage ', 'Screen Size (inches)', 'Camera (MP)'], \
       var_name = 'nama_kolom', value_name = 'nilai')

df_melt

df_melt['nama_kolom'].unique()

df_melt.sort_values(by = ['Brand']).head(20)

df.stack().head(30)

df_stacked = df.set_index(['Brand', 'Model', 'RAM ', 'Storage ', 'Screen Size (inches)', 'Camera (MP)']).stack().reset_index()
df_stacked

df_stacked.rename(columns = {'level_6': 'atribut', 0:'value'})

df

# mengkategorisasikan nilai Price menjadi 4 kategori dengan jumlah ukuran yang sama, misal Bronze, Silver, Gold, Platinum
bin_labels = ['Bronze', 'Silver', 'Gold', 'Platinum']
results, bin_edges = pd.qcut(df['Price ($)'], q = 4, labels = bin_labels, retbins = True)

results

bin_edges

results_table = pd.DataFrame(zip(bin_edges, bin_labels), columns =['Threshold', 'Tier'])
results_table

df['results'] = results
df

df['results'].value_counts()

bins = [0, 1000, 2000, 3000, 4000, 5000, 10000]
labels = [1, 2, 3, 4, 5, 6]
df['binned_battery'] = pd.cut(df['Battery Capacity (mAh)'], bins = bins, labels = labels)

df

df['binned_battery'].value_counts()

df['rank_price'] = df['Price ($)'].rank(ascending = True)
df

df.sort_values(by = ['rank_price'])

df[df['rank_price'] == 4.5]

body = ['Samsung', 'Xiaomi']
df[df['Brand'].isin(body)]

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Membaca dataset dari file CSV
file_path = "/content/drive/MyDrive/Colab Notebooks/Mobile_phone_price.csv"
df = pd.read_csv(file_path)

# Membersihkan data
df['Price ($)'] = df['Price ($)'].str.replace('$', '').str.replace(',', '').astype(int)
df['RAM '] = df['RAM '].str.replace('GB', '').str.strip().astype(int)

# Menambahkan kolom 'battery dollar'
df['battery dollar'] = df['Battery Capacity (mAh)'] / df['Price ($)']

# 1. Distribusi Harga
plt.figure(figsize=(10, 6))
sns.histplot(df['Price ($)'], bins=20, kde=True, color='blue')
plt.title('Distribusi Harga Perangkat Mobile', fontsize=16)
plt.xlabel('Harga ($)', fontsize=12)
plt.ylabel('Jumlah Perangkat', fontsize=12)
plt.grid(True)
plt.show()

# 2. Distribusi Kapasitas Baterai
plt.figure(figsize=(10, 6))
sns.histplot(df['Battery Capacity (mAh)'], bins=15, kde=True, color='green')
plt.title('Distribusi Kapasitas Baterai', fontsize=16)
plt.xlabel('Kapasitas Baterai (mAh)', fontsize=12)
plt.ylabel('Jumlah Perangkat', fontsize=12)
plt.grid(True)
plt.show()

# 3. Battery Dollar per Brand
plt.figure(figsize=(12, 8))
sns.boxplot(data=df, x='Brand', y='battery dollar', palette='viridis')
plt.title('Distribusi Battery Dollar per Brand', fontsize=16)
plt.xticks(rotation=45)
plt.xlabel('Brand', fontsize=12)
plt.ylabel('Battery Dollar', fontsize=12)
plt.grid(True)
plt.show()

# 4. Scatter Plot: Harga vs Kapasitas Baterai
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Battery Capacity (mAh)', y='Price ($)', hue='Brand', palette='Set2', s=100)
plt.title('Harga vs Kapasitas Baterai', fontsize=16)
plt.xlabel('Kapasitas Baterai (mAh)', fontsize=12)
plt.ylabel('Harga ($)', fontsize=12)
plt.legend(title='Brand', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()

# 5. Distribusi RAM per Brand
plt.figure(figsize=(12, 8))
sns.countplot(data=df, x='RAM ', hue='Brand', palette='coolwarm')
plt.title('Distribusi RAM per Brand', fontsize=16)
plt.xlabel('RAM (GB)', fontsize=12)
plt.ylabel('Jumlah Perangkat', fontsize=12)
plt.grid(True)
plt.legend(title='Brand', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()