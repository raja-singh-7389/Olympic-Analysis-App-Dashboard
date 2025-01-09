Data Analyzer for Everyone 🧞‍♂️

A Streamlit-based application for exploring and analyzing datasets with ease.

Overview

This application provides an intuitive interface to upload, analyze, and visualize data. It supports both user-uploaded files and built-in datasets. With multiple visualization options and statistical summaries, it simplifies data analysis for everyone.

Features
	•	Upload your own CSV or Excel files.
	•	Use preloaded datasets:
	1.	Diabetes
	2.	Heart Disease
	3.	Parkinsons
	4.	Tips
	5.	Titanic
	•	Basic Information:
	•	Dataset summary (rows, columns, and data types).
	•	Statistical description of numerical data.
	•	Top/Bottom Rows Viewer: View specific rows from the dataset.
	•	Value Counts: Analyze column-wise value distributions with visualizations.
	•	Group By Operations: Summarize data using operations like sum, max, min, count, and median.
	•	Dynamic Visualizations:
	•	Bar Chart
	•	Line Chart
	•	Scatter Plot
	•	Pie Chart
	•	Sunburst Chart
	•	Histogram
	•	Boxplot

Files Included
	•	app.py: Main application script.
	•	requirements.txt: List of required Python libraries.
	•	Built-in datasets:
	•	diabetes.csv
	•	heart.csv
	•	parkinsons.csv
	•	tips.csv
	•	titanic.csv

Dependencies
	•	streamlit
	•	pandas
	•	plotly
	•	openpyxl

Install all dependencies using the following command:

pip install -r requirements.txt

Screenshots
	•	Home Page:
Displays options to upload a file or choose a built-in dataset.
	•	Dataset Summary:
View dataset shape, column names, and statistical descriptions.
	•	Visualizations:
Create dynamic charts based on grouped data or value counts.

License

This project is licensed under the MIT License.

Acknowledgments
	•	Streamlit
	•	Plotly
	•	Pandas Documentation
