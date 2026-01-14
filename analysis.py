#!/usr/bin/env python3
"""
E-Commerce Sales Analysis 2025

This script performs comprehensive data analysis on e-commerce sales data,
including revenue analysis, product performance, regional insights, and customer behavior.

Author: Kevin Vasilescu
Date: January 2026
"""

import pandas as pd
import numpy as np
from datetime import datetime

def load_data(filepath='ecommerce_sales_2025.csv'):
    """
    Load the e-commerce sales dataset.
    
    Args:
        filepath (str): Path to the CSV file
    
    Returns:
        pd.DataFrame: Loaded dataset
    """
    df = pd.read_csv(filepath)
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.month
    df['quarter'] = df['date'].dt.quarter
    df['day_of_week'] = df['date'].dt.day_name()
    return df

def basic_statistics(df):
    """
    Calculate and display basic statistics.
    
    Args:
        df (pd.DataFrame): Sales dataset
    """
    print("="*60)
    print("BASIC STATISTICS")
    print("="*60)
    print(f"Total Revenue: ${df['final_price'].sum():,.2f}")
    print(f"Average Transaction Value: ${df['final_price'].mean():.2f}")
    print(f"Median Transaction Value: ${df['final_price'].median():.2f}")
    print(f"Total Units Sold: {df['quantity'].sum():,}")
    print(f"Total Transactions: {len(df):,}")
    print(f"Unique Customers: {df['customer_id'].nunique():,}")
    print(f"Average Discount: {df['discount_percent'].mean():.2f}%")
    print(f"Date Range: {df['date'].min().date()} to {df['date'].max().date()}")
    print()

def product_analysis(df):
    """
    Analyze product performance.
    
    Args:
        df (pd.DataFrame): Sales dataset
    """
    print("="*60)
    print("PRODUCT PERFORMANCE ANALYSIS")
    print("="*60)
    
    product_stats = df.groupby('product').agg({
        'final_price': ['sum', 'mean', 'count'],
        'quantity': 'sum',
        'discount_percent': 'mean'
    }).round(2)
    
    product_stats.columns = ['Total Revenue', 'Avg Price', 'Transactions', 'Units Sold', 'Avg Discount %']
    product_stats = product_stats.sort_values('Total Revenue', ascending=False)
    
    print(product_stats)
    print(f"\nBest Selling Product: {product_stats['Units Sold'].idxmax()} ({product_stats['Units Sold'].max()} units)")
    print(f"Highest Revenue Product: {product_stats['Total Revenue'].idxmax()} (${product_stats['Total Revenue'].max():,.2f})")
    print()

def regional_analysis(df):
    """
    Analyze sales by region.
    
    Args:
        df (pd.DataFrame): Sales dataset
    """
    print("="*60)
    print("REGIONAL ANALYSIS")
    print("="*60)
    
    region_stats = df.groupby('region').agg({
        'final_price': ['sum', 'mean', 'count'],
        'quantity': 'sum'
    }).round(2)
    
    region_stats.columns = ['Total Revenue', 'Avg Transaction', 'Transactions', 'Units Sold']
    region_stats = region_stats.sort_values('Total Revenue', ascending=False)
    
    print(region_stats)
    print(f"\nTop Region: {region_stats['Total Revenue'].idxmax()} (${region_stats['Total Revenue'].max():,.2f})")
    print()

def temporal_analysis(df):
    """
    Analyze temporal patterns in sales.
    
    Args:
        df (pd.DataFrame): Sales dataset
    """
    print("="*60)
    print("TEMPORAL ANALYSIS")
    print("="*60)
    
    # Monthly analysis
    monthly_revenue = df.groupby('month')['final_price'].sum().round(2)
    print("\nMonthly Revenue:")
    print(monthly_revenue)
    print(f"Best Month: Month {monthly_revenue.idxmax()} (${monthly_revenue.max():,.2f})")
    print(f"Worst Month: Month {monthly_revenue.idxmin()} (${monthly_revenue.min():,.2f})")
    
    # Quarterly analysis
    quarterly_revenue = df.groupby('quarter')['final_price'].sum().round(2)
    print("\nQuarterly Revenue:")
    print(quarterly_revenue)
    print(f"Best Quarter: Q{quarterly_revenue.idxmax()} (${quarterly_revenue.max():,.2f})")
    print()

def category_analysis(df):
    """
    Analyze sales by category.
    
    Args:
        df (pd.DataFrame): Sales dataset
    """
    print("="*60)
    print("CATEGORY ANALYSIS")
    print("="*60)
    
    category_stats = df.groupby('category').agg({
        'final_price': ['sum', 'mean', 'count'],
        'quantity': 'sum',
        'discount_percent': 'mean'
    }).round(2)
    
    category_stats.columns = ['Total Revenue', 'Avg Price', 'Transactions', 'Units Sold', 'Avg Discount %']
    category_stats = category_stats.sort_values('Total Revenue', ascending=False)
    
    print(category_stats)
    print()

def discount_analysis(df):
    """
    Analyze the impact of discounts on sales.
    
    Args:
        df (pd.DataFrame): Sales dataset
    """
    print("="*60)
    print("DISCOUNT IMPACT ANALYSIS")
    print("="*60)
    
    discount_stats = df.groupby('discount_percent').agg({
        'final_price': ['sum', 'mean', 'count'],
        'quantity': 'sum'
    }).round(2)
    
    discount_stats.columns = ['Total Revenue', 'Avg Price', 'Transactions', 'Units Sold']
    
    print(discount_stats)
    
    # Calculate revenue percentage by discount
    total_revenue = df['final_price'].sum()
    print("\nRevenue Distribution by Discount Level:")
    for discount in discount_stats.index:
        revenue = discount_stats.loc[discount, 'Total Revenue']
        percentage = (revenue / total_revenue) * 100
        print(f"  {discount}% discount: ${revenue:,.2f} ({percentage:.2f}% of total revenue)")
    print()

def payment_method_analysis(df):
    """
    Analyze payment method preferences.
    
    Args:
        df (pd.DataFrame): Sales dataset
    """
    print("="*60)
    print("PAYMENT METHOD ANALYSIS")
    print("="*60)
    
    payment_stats = df.groupby('payment_method').agg({
        'final_price': ['sum', 'mean', 'count']
    }).round(2)
    
    payment_stats.columns = ['Total Revenue', 'Avg Transaction', 'Count']
    payment_stats = payment_stats.sort_values('Total Revenue', ascending=False)
    
    print(payment_stats)
    print()

def key_insights(df):
    """
    Generate key insights and recommendations.
    
    Args:
        df (pd.DataFrame): Sales dataset
    """
    print("="*60)
    print("KEY INSIGHTS & RECOMMENDATIONS")
    print("="*60)
    
    # Top performing product
    top_product = df.groupby('product')['final_price'].sum().idxmax()
    top_product_revenue = df.groupby('product')['final_price'].sum().max()
    
    # Top region
    top_region = df.groupby('region')['final_price'].sum().idxmax()
    
    # Discount effectiveness
    avg_revenue_no_discount = df[df['discount_percent'] == 0]['final_price'].mean()
    avg_revenue_with_discount = df[df['discount_percent'] > 0]['final_price'].mean()
    
    # Category leader
    top_category = df.groupby('category')['final_price'].sum().idxmax()
    
    print(f"1. {top_product} is the top revenue generator (${top_product_revenue:,.2f})")
    print(f"2. {top_region} is the strongest market - consider targeted expansion")
    print(f"3. {top_category} category dominates sales - focus inventory accordingly")
    print(f"4. Average transaction without discount: ${avg_revenue_no_discount:.2f}")
    print(f"   Average transaction with discount: ${avg_revenue_with_discount:.2f}")
    print(f"5. Total unique customers: {df['customer_id'].nunique()} - opportunity for retention programs")
    print()

def main():
    """
    Main execution function.
    """
    print("\n" + "="*60)
    print("E-COMMERCE SALES ANALYSIS 2025")
    print("="*60 + "\n")
    
    # Load data
    df = load_data()
    print(f"Dataset loaded successfully: {len(df)} records\n")
    
    # Run all analyses
    basic_statistics(df)
    product_analysis(df)
    regional_analysis(df)
    temporal_analysis(df)
    category_analysis(df)
    discount_analysis(df)
    payment_method_analysis(df)
    key_insights(df)
    
    print("="*60)
    print("Analysis Complete!")
    print("="*60)

if __name__ == "__main__":
    main()
