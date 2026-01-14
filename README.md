# E-Commerce Sales Analysis 2025

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Pandas](https://img.shields.io/badge/Pandas-Latest-green.svg)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A comprehensive data analytics project analyzing e-commerce sales patterns throughout 2025. This project demonstrates data manipulation, statistical analysis, and insight generation using Python and Pandas.

## 📊 Project Overview

This project analyzes 1,500 e-commerce transactions across multiple product categories, regions, and payment methods. The analysis provides actionable insights into sales performance, customer behavior, and business trends.

### Key Features

- **Comprehensive Sales Analysis**: Revenue tracking, product performance, and temporal trends
- **Regional Insights**: Geographic sales distribution and regional performance metrics
- **Discount Impact**: Analysis of pricing strategies and discount effectiveness
- **Customer Behavior**: Payment preferences and purchasing patterns
- **Clean, Documented Code**: Well-structured Python code with detailed documentation

## 📁 Dataset

**File**: `ecommerce_sales_2025.csv`

### Dataset Specifications

- **Records**: 1,500 transactions
- **Time Period**: January 1, 2025 - December 31, 2025
- **Products**: 7 categories (Laptop, Smartphone, Tablet, Headphones, Smartwatch, Camera, Gaming Console)
- **Regions**: 5 markets (North America, Europe, Asia, South America, Africa)
- **Payment Methods**: 4 options (Credit Card, PayPal, Debit Card, Bank Transfer)

### Columns

| Column | Type | Description |
|--------|------|-------------|
| `date` | datetime | Transaction date |
| `product` | string | Product name |
| `category` | string | Product category |
| `quantity` | integer | Units purchased |
| `base_price` | integer | Original product price |
| `discount_percent` | integer | Applied discount (0-20%) |
| `final_price` | float | Final transaction amount |
| `region` | string | Customer region |
| `payment_method` | string | Payment type |
| `customer_id` | string | Unique customer identifier |

## 🔍 Analysis Components

The `analysis.py` script provides:

1. **Basic Statistics**
   - Total revenue and average transaction values
   - Customer count and transaction volume
   - Overall discount metrics

2. **Product Performance**
   - Revenue by product
   - Best-selling items
   - Average pricing analysis

3. **Regional Analysis**
   - Sales distribution across regions
   - Regional performance comparison
   - Market penetration insights

4. **Temporal Patterns**
   - Monthly and quarterly revenue trends
   - Seasonal patterns identification
   - Peak period analysis

5. **Category Insights**
   - Performance by product category
   - Category-level metrics

6. **Discount Effectiveness**
   - Impact of discounts on revenue
   - Discount strategy evaluation

7. **Payment Method Trends**
   - Payment preference analysis
   - Transaction value by payment type

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/kevin-vasilescu/ecommerce-sales-analysis.git
cd ecommerce-sales-analysis
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

### Usage

Run the analysis script:

```bash
python analysis.py
```

The script will output comprehensive analysis results to the console, including:
- Statistical summaries
- Performance metrics
- Key insights and recommendations

## 📈 Key Findings

Based on the 2025 sales data:

- **Total Revenue**: $1,750,475.20
- **Average Transaction**: $1,166.98
- **Total Units Sold**: 3,767
- **Unique Customers**: 1,373

### Top Performers

1. **Best Product**: Laptop ($437,723 revenue)
2. **Leading Region**: Asia ($375,564)
3. **Dominant Category**: Electronics (75% of revenue)
4. **Best Month**: March ($171,347)

### Insights

- Electronics category drives 75% of total revenue
- Asia and Africa are the strongest markets
- 60% of transactions use Credit Card or Bank Transfer
- Discounts are applied conservatively (avg 6%)
- Consistent sales throughout the year with Q1 peak

## 🛠️ Technical Stack

- **Language**: Python 3.8+
- **Libraries**:
  - Pandas: Data manipulation and analysis
  - NumPy: Numerical computing
  - Datetime: Temporal data handling

## 📝 Code Structure

```
ecommerce-sales-analysis/
│
├── analysis.py                 # Main analysis script
├── ecommerce_sales_2025.csv   # Dataset
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── .gitignore                # Git ignore file
```

## 🎯 Future Enhancements

Potential improvements for this project:

- [ ] Add data visualizations (matplotlib/seaborn)
- [ ] Implement customer segmentation analysis
- [ ] Create interactive dashboard (Plotly/Streamlit)
- [ ] Add predictive modeling for sales forecasting
- [ ] Incorporate customer lifetime value analysis
- [ ] Develop automated reporting system

## 📊 Sample Output

```
============================================================
BASIC STATISTICS
============================================================
Total Revenue: $1,750,475.20
Average Transaction Value: $1166.98
Total Units Sold: 3,767
Unique Customers: 1,373
Average Discount: 5.99%

============================================================
PRODUCT PERFORMANCE ANALYSIS
============================================================
                Total Revenue  Avg Price  Transactions  Units Sold
Laptop            437723.10    848.30        516          516
Smartphone        374489.25    653.57        573          573
Camera            285178.05    518.51        550          550
...
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📧 Contact

**Kevin Vasilescu**
- GitHub: [@kevin-vasilescu](https://github.com/kevin-vasilescu)
- LinkedIn: [Kevin Vasilescu](https://www.linkedin.com/in/kevin-vasilescu/)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Dataset generated synthetically for educational purposes
- Project developed as part of data analytics portfolio
- Built with Python data science ecosystem

---

⭐ **Star this repository if you find it helpful!**
