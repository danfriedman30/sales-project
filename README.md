# sales-project
Sales Project for Software Development Sprint

In this project, I generated some sample sales data for 2023 from a retailer who sells several different categories of products. The data has 8 different categories per record:

-Order ID - unique order identifier
-Date - a string with the order date
-Product - the product name
-Category - the product category
-Quantity - the number of products purchased in the order
-Price - the price paid for each product
-Total Sales - Quantity * Price

My goal was to build a simple streamlit web app that breaks down this sales data by month and category. I want to make this customizable to filter for month and product category. You can find a scatterplot for each combination of sales and quantity, a histogram for distribution of sales, and a bar chart best used for category comparison.



HOW TO ACCESS REMOTELY:
The app can be found on Render by using an internet browser and visiting https://sales-project-zp1b.onrender.com/

HOW TO RUN LOCALLY:

1- Clone the Repository: Open a terminal and enter the command git clone https://github.com/danfriedman30/sales-project/tree/main, then run the command cd <directory with the repository>

2- Set up the environment: check that python is installed by typing python3 into the terminal, then create the virtual enviornment with the command python -m venv env

3- Activate the virtual environment: on Windows the command is .\env\Scripts\Activate, on Mac/Linux the command is source env/bin/activate

4- View and install the necessary packages: use the command pip install -r requirements.txt

5- Run the streamlit app: use the command streamlit run app.py

6- View the application: open a web browser and use the address http://localhost:8051
