import pandas as pd
import streamlit as st 
import plotly.express as px


df = pd.read_csv('2023_sales_data.csv')

df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

twenty_four_records = df[df['Date'].dt.year == 2024]
df = df.drop(twenty_four_records.index)

# Streamlit app title
st.title("Sales Data Dashboard")

# Checkbox for filtering by Category
show_category = st.checkbox("Filter by Category")
if show_category:
    category_choice = st.selectbox("Select a category:", df["Category"].unique())
    df = df[df["Category"] == category_choice]

# Checkbox for enabling Month/Year filter
show_time_filter = st.checkbox("Filter by Month/Year")
if show_time_filter:
    filter_type = st.radio("Select filter type:", ("Month", "Year"))
    if filter_type == "Month":
        month_choice = st.selectbox("Select a month:", sorted(df["Month"].unique()))
        df = df[df["Month"] == month_choice]
    else:
        year_choice = st.selectbox("Select a year:", sorted(df["Year"].unique()))
        df = df[df["Year"] == year_choice]

# Scatter plot: Total Sales vs Quantity
st.subheader("Total Sales vs Quantity")
fig_scatter = px.scatter(
    df, x="Quantity", y="Total Sales", color="Category", 
    title="Scatter Plot of Total Sales vs Quantity",
    hover_data=["Month"]  # Include Month in hover tooltip
)
st.plotly_chart(fig_scatter)

# Histogram: Distribution of Total Sales
st.subheader("Distribution of Total Sales")
fig_hist = px.histogram(
    df, x="Total Sales", nbins=30, 
    title="Histogram of Total Sales"
)
st.plotly_chart(fig_hist)

# Bar Chart: Total Sales for Each Month by Product Category
st.subheader("Product Category Sales")
df_grouped = df.groupby(["Month", "Category"])["Total Sales"].sum().reset_index()
fig_bar = px.bar(
    df_grouped,
    x="Month", y="Total Sales", color="Category",
    title="Total Sales per Month by Product Category",
    barmode="group"
)
st.plotly_chart(fig_bar)
