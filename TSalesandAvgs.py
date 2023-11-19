import pandas as pd
import matplotlib.pyplot as plt

#Read CSV
car_df = pd.read_csv('car_df.csv')
car_df.head()

##Total Sales over Time

#Graph One

#Make Line Chart
car_df.plot(x='observation_date', y='Number of Cars Sold', kind='line')

#Labels & Titles
plt.xlabel('Date')
plt.ylabel('Total Sales (in thousands)')
plt.title('Total Sales over Time')

#Rotate labels
plt.xticks(rotation=45)

#Show
plt.show()

#Graph Two

#Date type
car_df['observation_date'] = pd.to_datetime(car_df['observation_date'])

#Figure size
plt.figure(figsize=(10, 6))

#Make Line Chart
plt.plot(car_df['observation_date'], car_df['Number of Cars Sold'])

#Labels & Titles
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.title('Total Sales over Time')

#Rotate labels
plt.xticks(rotation=45)

#Custom labels
custom_labels = ['2008', '2010', '2013', '2015', '2018', '2020', '2023']

#Set custom labels
plt.xticks(car_df['observation_date'][::10], custom_labels)

#Formatting
plt.gca().get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

#Gridlines
plt.grid(True)

#Show
plt.show()

##Amount Financed over Time

#Graph One

#Make Line Chart
car_df.plot(x='observation_date', y=['Average Amount Financed (New)', 'Average Amount Financed (Used)'], kind='line')

#Labels & Titles
plt.xlabel('Date')
plt.ylabel('Amount Financed (in thousands)')
plt.title('Amount Financed over Time')

#Rotate labels
plt.xticks(rotation=45)

#Show
plt.show()

#Graph Two

#Figure size
plt.figure(figsize=(10, 6))

#Make Line Chart
plt.plot(car_df['observation_date'], car_df['Average Amount Financed (New)'], label='New')
plt.plot(car_df['observation_date'], car_df['Average Amount Financed (Used)'], label='Used')

#Labels & Titles
plt.xlabel('Date')
plt.ylabel('Amount Financed ( in thousands)')
plt.title('Amount Financed over Time')

#Rotate labels
plt.xticks(rotation=45)

#Custom labels
custom_labels = ['2008', '2010', '2013', '2015', '2018', '2020', '2023']

#Set custom labels
plt.xticks(car_df['observation_date'][::10], custom_labels)

#Show
plt.legend()

#Gridlines
plt.grid(True)

#Show
plt.show()

#Graph Three

#Figure size
plt.figure(figsize=(10, 6))

#Make Line Chart
plt.plot(car_df['observation_date'], car_df['Average Amount Financed (New)'], label='New')

#Make Line Chart
plt.plot(car_df['observation_date'], car_df['Average Amount Financed (Used)'], label='Used')

#Total amount financed
total_amount_financed = car_df['Average Amount Financed (New)'] + car_df['Average Amount Financed (Used)']

#Make Line Chart
plt.plot(car_df['observation_date'], total_amount_financed, label='Total')

#Labels & Titles
plt.xlabel('Date')
plt.ylabel('Amount Financed (in thousands)')
plt.title('Amount Financed over Time')

#Rotate labels
plt.xticks(rotation=45)

#Custom labels
custom_labels = ['2008', '2010', '2013', '2015', '2018', '2020', '2023']

#Set custom labels
plt.xticks(car_df['observation_date'][::10], custom_labels)

#Show
plt.legend()

#Gridlines
plt.grid(True)

#Show
plt.show()