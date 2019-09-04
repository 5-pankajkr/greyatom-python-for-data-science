# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
bank=pd.read_csv(path)


# code starts here
categorical_var=bank.select_dtypes(include='object')
print(categorical_var)

numerical_var=bank.select_dtypes(include='number')
print(numerical_var)

# code ends here


# --------------
# code starts here
# bank.drop('Loan_ID', inplace=True, axis=1)
banks=bank.drop('Loan_ID', axis=1)

# banks.columns
null=banks.isnull().sum()
print(null)

bank_mode=banks.mode().iloc[0]
# bank_mode=banks.mode()
print(bank_mode)

banks.fillna(bank_mode, inplace=True)
# banks.apply(lambda x: x.fillna(x.mode()), axis=0)

null2=banks.isnull().sum()
print(null2)
#code ends here


# --------------
# Code starts here

avg_loan_amount=pd.pivot_table(banks, index=['Gender', 'Married', 'Self_Employed'], values='LoanAmount', aggfunc=np.mean)

print(avg_loan_amount)

# code ends here



# --------------
# code starts here




loan_approved_se=len(banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')])
print(loan_approved_se)

loan_approved_nse=len(banks[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')])
print(loan_approved_nse)

Loan_Status=614

percentage_se=100*loan_approved_se/Loan_Status
percentage_nse=100*loan_approved_nse/Loan_Status

print(percentage_se, percentage_nse)
# code ends here


# --------------
# code starts here

loan_term=banks['Loan_Amount_Term'].apply(lambda x : x/12)
# banks.head()
print(len(loan_term))
big_loan_term=len(loan_term[loan_term>=25])
print(big_loan_term)

# code ends here


# --------------
# code starts here

loan_groupby=banks.groupby('Loan_Status')

loan_groupby=loan_groupby['ApplicantIncome', 'Credit_History']
# loan_groupby.first()

mean_values=loan_groupby.mean()
print(mean_values)
# code ends here


