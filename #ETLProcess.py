#Extract
#Identify data sources (e.g., databases, CSV files, APIs).
#Use libraries like pandas, csv, or requests to read data. For databases, use libraries like sqlite3, psycopg2 (for PostgreSQL), or pymysql (for MySQL).

import pandas as pd
    # Extract from CSV
    data = pd.read_csv('data.csv')
    # Extract from SQL database
    import sqlite3
    conn = sqlite3.connect('mydatabase.db')
    data = pd.read_sql_query("SELECT * FROM mytable", conn)
    conn.close()

#Transform
#Clean data: Handle missing values, duplicates, and errors.
#Transform data: Convert data types, filter, aggregate, and enrich data.
#Use pandas for data manipulation.

# Clean data
    data.dropna(inplace=True)
    data.drop_duplicates(inplace=True)
    # Transform data
    data['column_new'] = data['column_old'] * 2

#Load
#Load the transformed data into the destination (e.g., database, CSV file, data warehouse).
#Use pandas to write to CSV or libraries like sqlite3 or sqlalchemy to write to databases.
# Load to CSV
    data.to_csv('data_transformed.csv', index=False)
    # Load to SQL database
    import sqlite3
    conn = sqlite3.connect('mydatabase.db')
    data.to_sql('mytable_transformed', conn, if_exists='replace', index=False)
    conn.close()

#Use cron to schedule it