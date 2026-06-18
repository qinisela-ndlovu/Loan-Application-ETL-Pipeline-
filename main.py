from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data

print("STARTING ETL PIPELINE...")

DATA_PATH = "data/loan_data.csv"
DB_PATH = "output/loan_data.db" 

# read the data and store it in a DataFrame
df = extract_data(DATA_PATH)

# Trandform the data
clean_df = transform_data(df)

# load the clean data into a SQLite database
load_data(clean_df, DB_PATH)

print("ETL PIPELINE COMPLETED SUCCESSFULLY")