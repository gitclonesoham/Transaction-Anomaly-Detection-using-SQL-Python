# Transaction Anomaly Detection using SQL & Python

This project focuses on identifying unusual or potentially risky transactions in retail sales data using **rule-based anomaly detection**.  
The goal is to simulate how data analysts detect abnormal patterns in transactions using SQL logic and exploratory data analysis, without relying on machine learning models.

---

## Dataset

The dataset used in this project is a retail sales dataset sourced from Kaggle:

🔗 **Sales Forecasting Dataset (Kaggle)**  
https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting

The dataset contains transactional information such as:
- Order details  
- Customer identifiers  
- Sales values  
- Discount rates  
- Order dates  

This dataset is suitable for identifying unusual transaction behavior using analytical rules.

---

## Tools & Technologies

- **PostgreSQL** – storing and querying transaction data  
- **SQL** – aggregations, statistical baselines, and rule-based anomaly detection  
- **Python** – exploratory analysis and visualization  
  - Pandas  
  - Matplotlib  

---

## Project Workflow

1. Established baseline transaction metrics using SQL (average sales, standard deviation, average discount)  
2. Defined rule-based conditions to flag anomalous transactions  
3. Identified high-value orders and transactions with unusually high discounts  
4. Analyzed anomaly distribution using Python  
5. Visualized transaction behavior to support analytical findings  

---

## Anomaly Detection Rules

Transactions were flagged based on the following conditions:
- **High Value Orders** – sales significantly higher than the normal range  
- **High Discount Transactions** – unusually large discounts compared to average values  

These rules help identify transactions that may require further investigation.

---

## Visualizations

The following visualizations were created as part of the analysis:
- Distribution of detected transaction anomalies  
- Sales distribution with statistical anomaly threshold  
- Discount vs Sales scatter plot to study pricing behavior  

These plots help explain why certain transactions are flagged as anomalies.

---

## Key Insights

- A small number of transactions account for unusually high sales values  
- Higher discounts are associated with wide variability in sales behavior  
- Rule-based detection is effective for highlighting potentially risky transactions  
- Simple statistical thresholds can provide meaningful insights without complex models  

---

## Conclusion

This project demonstrates how SQL and Python can be used together to detect and explain anomalous transaction behavior.  
It highlights a practical, interpretable approach to risk analysis that is commonly used in real-world data analytics scenarios.

 
