# Loan application ETL pipeline

This is a simple end-to-end ETL(Extract, Transform, load) pipeline built using Python. It processes a loan dataset, cleans and transforms the data and then loads it into SQLite database for further analyisis.

---
## The Project Objective

The goal of this project is to:
## 1. Extract
- Loaded loan dataset from CSV using pandas

## 2. Transform
- Handled missing values
- Cleaned categorical data
- Basic feature engineering(TotalIncome & IncomeToRatio)
- Encoded Loan_status

  ## 3. Load
  Stored cleaned data into SQLite database(loan.db)
---

## Project Structure

![project structure ](https://github.com/qinisela-ndlovu/Loan-Application-ETL-Pipeline-/blob/main/Project%20structure.png)

---

## Technologies used

- Python 3
- pandas
- SQLite (built-in library)

---

## Snap of pipeline runner:

![ETL Pipeline Output](https://github.com/qinisela-ndlovu/Loan-Application-ETL-Pipeline-/blob/main/Pipeline%20Runner.png)

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




