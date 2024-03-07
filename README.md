# README.md

## Overview

This application is designed to extract, process, and analyze data related to public companies from both structured and unstructured sources. It provides insights through calculated financial ratios, sentiment analysis, and trend identification, culminating in a summary via streamlit dashboard and chatbot.

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
2. Navigate to the project directory
   ```sh
   python3 -m venv venv
   ```
3. Activate env
   ```sh
   source venv/bin/activate
   ```
5. Install the required dependencies
   ```
   pip3 install -r requirements.txt
   ```
   * note: if you would like to use jupyter notebook to run interactive cells, you will need to install the jupyter notebook package in your venv as well. to do so, run the following command in your terminal or command prompt:
   
   `pip3 install jupyter`

## The Application
the application is designed to extract, process, and analyze data related to public companies from both structured and unstructured sources. currently it collects, transforms, translates structured data and  provides insights through calculated financial ratios, sentiment analysis, and trend identification, culminating in a summary via streamlit.

*update*: a demonstration chatbot is live on the streamlit dashboard. it is a simple chatbot that can answer questions about uber and lyft 10-k financial documents. it is designed to be a simple demonstration of the potential for a chatbot to provide insights and answer questions about unstructured data.

### Set your OpenAI API KEY

Set your OPENAI_API_KEY environment variable in .env (located at the root level) or
Run the following command in your terminal, replacing <enter-your-key-here> with your API key.

- on a mac: `echo "export OPENAI_API_KEY=<enter-your-key-here>" >> ~/.zshrc`
- Update the shell with the new variable: `source ~/.zshrc` (or restart your shell)
- windows: `setx OPENAI_API_KEY "<enter-your-key-here>" 

Detailed instructions can be found here: https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety

### Running the Application

1. Notebook analysis can be found in the `analysis_sqlite.ipynb` notebook at the root of the project.
   
2. Run the Flask API backend and Streamlit dashboard frontend app in your prefered terminal or command prompt, navigate to the root of the project and run the following command to launch everything at once:

   ```sh
   python3 main.py
   ```

alternatively, you can run the backend and frontend separately:

1. Run the Flask application:
   ```sh
   python3 run_backend.py
   ```

2. Run the Streamlit application:
 
   ```sh
   python3 run_frontend.py
   ```

**note**: the streamlit application is still in development but it is functional and contains basic visualizations and a chatbot. it is designed to serve as a dashboard for the Flask application and beyond. there is still lots of potential here.


## Application Structure
note: the repo has been restructured to better organize the codebase. the following is a brief overview of the new structure:

```sh
.
├── README.md
├── requirements.txt
├── main.py
├── src
│   ├── frontend
│   │   ├── dashboard # contains the streamlit application and the chatbot.
│   │   ├── API # empty directory for future development and code organization.
│   │   ├── __init__.py # initializes the streamlit application and sets up routes.
        |── data # seed pdf for chatbot demo
        ├── llm # llm chatbot logic: ingestion, tokenization, and response generation.
        ├── storage # persist indexed datastore 

│   ├── backend
│   │   ├── server.py # imports the Flask application and runs it.
│   │   ├── app
│   │   │   ├── 
│   │   │   ├── api  # Contains the Flask application, database models, and API clients.
│   │   │   ├── data
│   │   │   │   ├── FMP-API  # JSON files containing data from our fmpAPIclient.
│   │   │   │   │   └── FMP-client-output
│   │   │   │   ├── migrations  # SQL scripts for creating the database schema.
│   │   │   │   │   ├── phase_1  # a simplified schema used in the initial development and analysis phase.
│   │   │   │   │   │   └── 
│   │   │   │   │   └── phase_2  # database schema that adheres to 3rd normal form.
│   │   │   │   │       └──
│   │   │   │   ├── seed  #data used for seeding the database.
│   │   │   │   │   └── SEC-EDGAR 
│   │   │   │   │       ├── companyfacts 
│   │   │   ├── clients # Contains classes for making requests to external APIs 
|   |   |   |           # and retrieving data from external data sources such as the Financial Modeling Prep API and SEC EDGAR.
│   │   │   ├── utils
│   │   │   │   ├── adapters  # Contains classes for adapting, transforming, and orchestrating the population of the data retrieved by the clients.
│   │   │   ├── models  # Contains the ORM model classes that represent the tables in the database and include methods for interacting with the database.
│   │   │   ├── __init__.py  # Initializes the Flask application, sets up routes, and configures the database connection.
│   │   │   ├── db
│   │   │       ├── db.py  # DEPRICATED: Contains my old ORM functions for database operations such as connecting to the database, finding records, and building model instances from database records.

## what's next?
- develop the chatbot to be more robust and capable of answering more complex questions. agentic behavior and more robust RAG architecture.
- data preprocessing and feature engineering for the financial data. clean data is the foundation of any good model.
- automate the scraping, api calls, and data ingestion
- deploy phase 2 schema designed to third normal form
- setup XML to MD conversion for the chatbot to access company reports and press releases in real time
- develop a more robust and interactive dashboard with more visualizations and insights
- refactor the dashboard: pull out functions and classes into separate files and directories
- there is always more to do. the sky is the limit...

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.

## Acknowledgments

- SEC EDGAR for providing company reports and press releases.
- Financial Modeling Prep API for providing financial data.

## Contact

For any queries or further assistance, please contact the repository owner.



   docker build -t company-data-etl:prod -f Dockerfile . 
   docker run -it --rm --entrypoint /bin/bash --env-file=.flaskenv --name company-data-etl-prod company-data-etl:prod



