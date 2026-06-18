# transform.py
def transform_data(df):
    print("[TRANSFORM] Starting data cleaning...")

    #  Drop duplicates
    df = df.drop_duplicates()

    #  Fill missing values
    df["Gender"] = df["Gender"].fillna("Unknown")
    df["Married"] = df["Married"].fillna("No")
    df["Dependents"] = df["Dependents"].fillna("0")
    df["Self_Employed"] = df["Self_Employed"].fillna("No")
    df["Credit_History"] = df["Credit_History"].fillna(0)

    #  Fix Dependents column ("3+" → 3)
    df["Dependents"] = df["Dependents"].replace("3+", 3)

    #  Convert numeric columns
    df["Dependents"] = df["Dependents"].astype(float)

    #  My Feature Engineering
    df["TotalIncome"] = df["ApplicantIncome"] + df["CoapplicantIncome"]

    df["IncomeToLoanRatio"] = df["TotalIncome"] / df["LoanAmount"]

    #  Encode target variable
    df["Loan_Status"] = df["Loan_Status"].map({"Y": 1, "N": 0})

    print("[TRANSFORM] Done. Shape:", df.shape)

    return df