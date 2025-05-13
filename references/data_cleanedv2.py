import pandas as pd
df = pd.read_csv('03_Library Systembook.csv')
df.fillna('n/a')
df_clean = df.dropna()
#df_clean['Book checkout'] = df_clean['Book checkout'].str.replace('"','')
df_clean.loc[df_clean['Book checkout'].notna(), 'Book checkout']= df_clean['Book checkout'].str.replace('"','')
# Checking the ODBC Driver for SQL Server
import pyodbc

# List all ODBC drivers installed on the system
drivers = [driver for driver in pyodbc.drivers()]
print("ODBC Drivers available:")
for driver in drivers:
    print(driver)
    from sqlalchemy import create_engine

# Define the connection string to your MS SQL Server
server = 'localhost'  
database = 'DE5_Module5'
# Create the connection string with Windows Authentication
connection_string = f'mssql+pyodbc://@{server}/{database}?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'
# Create the SQLAlchemy engine
engine = create_engine(connection_string)
df = pd.DataFrame(df_clean)
df.to_sql('Books', engine, if_exists='replace',index=False)

# Calculate the number of days between two date columns

# Creating and using a function to enrich the data by adding in the time a book was on loan.

data_enriched = (df_clean, 'Book checked', 'Book Returned'='' 

def enrich_dateDuration(colA, colB, df_clean =data_enriched):
    """
    Takes the two input columns and the dataframe to create a new column date_delta which is the difference, in days, between colA and colB.
    
    Note: ColA should be the highest of the expected date columns.
    """
    df_clean['date_delta'] = (df_clean[colA]-df[colB]).dt.days
    return df_clean.head()

enrich_dateDuration(df_clean=data_enriched, colA='Book Returned', colB='Book checkout')