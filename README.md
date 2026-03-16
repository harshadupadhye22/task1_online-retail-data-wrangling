# Online Retail Data Wrangling Project

## Overview
This project is part of the Data Immersion & Wrangling task.  
The goal is to explore, clean, and transform a retail dataset to make it suitable for analysis.

The dataset contains retail order information including product details, pricing, quantity, and shipping data.

---

## Dataset Information
The dataset contains 9994 rows and 16 columns.

### Columns in the Dataset
- Order Id
- Order Date
- Ship Mode
- Segment
- Country
- City
- State
- Postal Code
- Region
- Category
- Sub Category
- Product Id
- Cost Price
- List Price
- Quantity
- Discount Percent

---

## Objectives
The main objectives of this project are:

- Understand the dataset structure
- Identify data quality issues
- Clean and transform the data
- Generate a processed dataset ready for analysis

---

## Data Cleaning Steps
The following steps were performed using Python:

1. Loaded the dataset using pandas
2. Checked dataset shape and column names
3. Removed duplicate rows
4. Removed rows with missing values
5. Converted Order Date to datetime format
6. Removed invalid values (negative price or quantity)
7. Created new columns:
   - Total Sales
   - Year
   - Month
8. Exported the cleaned dataset

---

## Technologies Used
- Python
- Pandas
- Command Prompt
- GitHub

---

## Project Structure
