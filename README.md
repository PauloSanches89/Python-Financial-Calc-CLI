# 💰 Financial Calculator: Investment & Bond Repayment

This is a command-line Python program that allows users to calculate either:

- 📈 Investment returns based on simple or compound interest
- 🏠 Bond (home loan) repayments over a set period

## 🧩 Problem Statement

Understanding how money grows through investment or estimating monthly home loan repayments can be complex. This program simplifies these calculations through a guided, interactive interface — helping users make more informed financial decisions.

---

## 🚀 Features

* 🧮 Calculate Simple or Compound Interest
* 🏦 Estimate Monthly Loan Repayments using real financial formulas
* 🔁 Robust Input Validation to ensure smooth user experience
* 📊 Clear, well-formatted financial outputs
* 📌 User decision loop for choosing between investment and bond tools

---

## 📌 How It Works

### 1. **Menu Selection**

The user is prompted to choose between two options:

```
investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan
```

Invalid inputs are caught and re-prompted until a correct option is provided.

---

### 2. **Investment Option**

User inputs:

* Initial deposit (`principal`)
* Interest rate (entered as % but converted internally)
* Investment duration in years
* Interest type: `simple` or `compound`

#### 💡 Calculations:

* **Simple Interest:**
  `A = P(1 + rt)`
* **Compound Interest:**
  `A = P(1 + r)^t`

The result is displayed with a financial breakdown of the inputs used.

---

### 3. **Bond Option**

User inputs:

* Present value of the house
* Annual interest rate
* Number of months for repayment

#### 💡 Calculation:

$$
\text{Monthly Repayment} = \frac{i \cdot P}{1 - (1 + i)^{-n}}
$$

Where:

* P = house value (loan amount)
* i = monthly interest rate (`annual / 12`)
* n = number of months

---

## 🛠 Technologies Used

* Python 3
* `math` module for exponentiation
* `try/except` and `while` loops for input validation
* String formatting for currency output

---

## 📚 What I Learned

* Building CLI applications with Python
* Implementing real-world financial formulas in code
* Handling user input gracefully using `try/except`
* Designing interactive programs that improve user understanding

---

## ✅ Example Output

```plaintext
Using the current parameters:
Interest rate: 8.0%
Years of investment: 5
Initial deposit: R10000
Type of interest: Compound
You will receive R14693.28
```

---

## 📁 Project Status

This project was completed as part of a **Data Science Bootcamp**, forming a foundational toolset in Python programming, user interaction, and applied logic.

Future versions may include:

* CSV export of results
* Json export

---

## 🔗 How to Run

1. Clone the repository
2. Run the script using:

```bash
python financial_calculator.py
```

Ensure you're using **Python 3.6+** for best compatibility.

---
