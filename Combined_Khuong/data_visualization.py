#plot_histogram, plot_scatter
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#loan_dataset = pd.read_csv("train_u6lujuX_CVtuZ9i.csv")

#Plot_Histogram
def plot_histogram(loan_dataset, check):
    #Education vs Loan Status
    if check == 1:
        sns.countplot(x = "Education", hue = "Loan_Status", data = loan_dataset)
        plt.title("Loan Status vs Education")
        plt.show()

    # Married & loan Status 
    elif check == 2:
        sns.countplot(x = "Married", hue = "Loan_Status", data = loan_dataset);
        plt.title("Loan status vs Married")
        plt.show()

    #Gender & Loan Status
    elif check == 3:
        sns.countplot(x = "Gender", hue = "Loan_Status", data = loan_dataset);
        plt.title("Loan status vs Gender")
        plt.show()

    #Property_Area & Loan Status
    elif check == 4:
        sns.countplot(x = "Property_Area", hue = "Loan_Status", data = loan_dataset);
        plt.title("Loan status vs Property_Area")
        plt.show()

    #Self_Employed & loan Status
    else:
        sns.countplot(x = "Self_Employed", hue = "Loan_Status", data = loan_dataset);
        plt.title("Loan Status vs Self_Employed")
        plt.show()

def plot_scatter(loan_dataset, check):
    #CoapplicantIncome vs LoanAmount
    if check == 1:
        plt.scatter(loan_dataset["CoapplicantIncome"], loan_dataset["LoanAmount"]);
        plt.xlabel("Coapplicant income")
        plt.ylabel("Loan Amount")
        plt.title("Coapplicant income vs Loan Amount")
        plt.show()

    #ApplicantIncome vs LoanAmount
    elif check ==2:
        plt.scatter(loan_dataset["ApplicantIncome"], loan_dataset["LoanAmount"]);
        plt.xlabel("Applicant income ")
        plt.ylabel("Loan Amount")
        plt.title("Applicant income vs Loan Amount")
        plt.show()

    #ApplicantIncome vs Loan Amount Term
    else: 
        plt.scatter(loan_dataset["ApplicantIncome"], loan_dataset["Loan_Amount_Term"]);
        plt.xlabel("Applicant income ")
        plt.ylabel("Loan Amount Term")
        plt.title("Applicant income vs Loan Amount Term")
        plt.show()
