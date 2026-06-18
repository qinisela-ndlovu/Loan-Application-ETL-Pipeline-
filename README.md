# Loan application ETL pipeline

This is a simple end-to-end ETL(Extract, Transform, load) pipeline built using Python. It processes a loan dataset, cleans and transforms the data and then loads it into SQLite database for further analyisis.

---
## The Project Objective

The goal of this project is to:
- Extract raw loan data from a CSV file
- Clean and transform the dataset
- Perform basic feature engineering
- Load the processed data into a SQLite database

---

## Project Structure


---

## Technologies used

- Python 3
- pandas
- SQLite (built-in library)

---

## How to Run?

### 1. Install dependencies

```bash
pip install pandas
```

### 2. Navigate to the project folder

```bash
cd loan-etl-pipeline
```

### 3. Run the ETL pipeline

```bash
python main.py
```

### 4. Verify the output

After execution, a SQLite database file will be created in:

```text
output/loan.db
```

The database contains a table named:

```text
loan_data
```




