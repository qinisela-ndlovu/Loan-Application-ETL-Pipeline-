# Save Clean Data to SQLite Database
import sqlite3

def load_data(df, db_path, table_name="loan_data"):
    print(f"[LOAD] Saving data to database: {db_path}, table: {table_name}...")

    # connect(or create) the SQLite database
    conn = sqlite3.connect(db_path)

    # load datagrame into SQL table
    df.to_sql(table_name, conn, if_exists="replace", index=False)

    conn.commit()
    conn.close()

    print(f"[LOAD] Data saved to database: {db_path}, table: {table_name}")
 
