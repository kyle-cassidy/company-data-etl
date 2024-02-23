# README.md

## Overview

This application is designed to extract, process, and analyze data related to public companies from both structured and unstructured sources. It provides insights through calculated financial ratios, sentiment analysis, and trend identification, culminating in a summary via streamlit dashboard.

## Getting Started

### Prerequisites

Ensure you have the following installed:
- Python 3.x
- Pip (Python package installer)

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/kyle-cassidy/company-data-etl
   ```
2. Navigate to the project directory and Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```


## Seed the Database and Setup Connection


1. Create a `.env` file in the root directory of the project and add the following environment variables:
   ```sh
   DATABASE_URL=postgresql://username:password@localhost:5432/<name-of-your-db>
   ```
2. Run the following command to create the database tables and seed the database with data. Ensure you are in the `backend` directory before executing:
3. 
   ```sh
   python3 seed_db.py 
   ```
   This script should be responsible for setting up your database tables and seeding them with the initial data required for the application to run properly. it may tak a long time to populate the database with the data from the SEC EDGAR and FMP-API clients. 
   ```


## Running the Application

this is currently under construction

## Application Structure

- `backend/api/src`: Contains the Flask application, database models, and API clients.
- `analysis_db `: Jupyter notebooks for data analysis and visualization.
- `backend/api/data/seed`: CSV files used for seeding the database.
  - `backend/api/data/FMP-API`: JSON files containing data from our fmpAPIclient.
  - `backend/api/data/seed`: bulk download of CSV from SEC EDGAR used for seeding the database.
- `backend/api/db/migrations`: SQL scripts for creating the database schema. There are two phases for the database schema:
  - `create_tables_phase_1`: a simplified schema used in the initial development amd analysis phase.
  - `create_tables_phase_2`: database schema that adheres to 3nd normal form. i spent a lot of time designing this schema and it is not yet implemented. i will implement it in the next phase.
- `backend/api/src/clients`: Contains classes for making requests to external APIs and retrieving data from external data sources such as the Financial Modeling Prep API and SEC EDGAR.
- `backend/api/src/utils/adapters`: Contains classes for adapting, transforming, and orchestrating the population of the data retrieved by the clients.
- `backend/api/src/models`: Contains the ORM model classes that represent the tables in the database and include methods for interacting with the database.
- `backend/api/src/__init__.py`: Initializes the Flask application, sets up routes, and configures the database connection. #TODO
- `backend/api/src/db/db.py`: Contains functions for database operations such as connecting to the database, finding records, and building model instances from database records.

## Data Extraction and Processing

The application extracts data from CSV and JSON files, as well as unstructured sources like PDFs or HTML documents. It then cleans, normalizes, and structures the data for analysis.

## Data Analysis - notebook

Basic data analysis is performed using libraries such as Pandas, NumPy, and SciPy. Visualization is done with Matplotlib and Plotly.
- initial analysis can be found in the `analysis_db` jupyter notebook.

## TO BE IMPLEMENTED:

### API Dashboard Output Generation
- flask application to serve an API for the streamlit application and beyond
- streamlit application to visualize the data and insights.

### integrate FMP-API client
- orchestrate scheduling of the FMP-API client to retrieve data from the Financial Modeling Prep API.

### build SEC EDGAR client and adapters
- free sources of company reports and press releases in PDF or HTML format.
- this is a great place to practice NLP and sentiment analysis on management discussion sections of annual reports, 10k's, 10q's, etc.

### unstructured data adapters
- to interact with [[endpoints]], models, postgres
- as mentioned above, this is a great source of interest and i have already done a lot of research into tools and libraries to use for this.
- i will be using the `pdfminer` or `PyPDF2` library to extract text from PDFs and the `beautifulsoup` library to extract text from HTML documents. 


## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.

## Acknowledgments

- SEC EDGAR for providing company reports and press releases.
- Financial Modeling Prep API for providing financial data.

## Contact

For any queries or further assistance, please contact the repository owner.
