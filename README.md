# README.md

## Overview

This application is designed to extract, process, and analyze data related to public companies from both structured and unstructured sources. It provides insights through calculated financial ratios, sentiment analysis, and trend identification, culminating in a summary via a Streamlit dashboard and chatbot.

## Getting Started

### Prerequisites

Ensure Docker and Docker Compose are installed on your system. For installation instructions, refer to the [Docker documentation](https://docs.docker.com/get-docker/) and [Docker Compose documentation](https://docs.docker.com/compose/install/).

### Installation

1. Clone the repository:
   
   ```sh
   git clone https://github.com/kyle-cassidy/company-data-etl
   ```

2. Navigate to the project directory:
   ```sh
   cd company-data-etl
   ```


### Running the Application with Docker Compose
> Note: As mentioned above, ensure Docker and Docker Compose are installed on your system.

To launch the application stack (both the backend Flask API and the Streamlit dashboard frontend), run the following command from the root of the project:

   ```sh
   docker-compose up --build
   ```

This command builds and starts the containers as defined in the `docker-compose.yaml` file. The Streamlit dashboard will be accessible at `http://localhost:8501`, and the Flask API will be accessible at `http://localhost:8000`.


### Stopping the Application

To stop and remove all the containers defined in the `docker-compose.yaml` file, use:

   ```sh
   docker-compose down
   ```

If you want to remove the volumes along with the containers, add the `--volumes` flag:

   ```sh
   docker-compose down --volumes
   ```

## Benefits of Using Docker and Docker Compose

- **Simplicity**: Define your application stack in a YAML file and start your entire stack with a single command.
- **Environment Consistency**: Docker containers ensure that your application runs the same way in every environment.
- **Development Efficiency**: Quickly start, stop, and rebuild services. Easily share your application by sharing the Dockerfile and docker-compose.yaml files.
- **Isolation**: Each service runs in its own container, ensuring that it is isolated from other services.

## Application Structure

The repository has been restructured to better organize the codebase. Below is a brief overview of the new structure:

```plaintext
.
├── README.md
├── docker-compose.yaml
├── src
│   ├── frontend
│   │   ├── dashboard # contains the Streamlit application and the chatbot.
│   │   ├── data # seed pdf for chatbot demo. TODO: integrate pdf upload/SEC EDGAR API/integration with tabular structured data.
│   │   ├── llm # WIP: llm chatbot logic: ingestion, tokenization, and response generation.
│   │   ├── storage # persist indexed datastore. TODO: integrate with vector database. 
│   ├── backend
│   │   ├── server.py # imports the Flask application and runs it.
│   │   ├── app
│   │   │   ├── data
│   │   │   │   ├── FMP-API  # JSON files containing data from our fmpAPIclient.
│   │   │   │   ├── migrations  # SQL scripts for creating the database schema.
│   │   │   │   ├── seed  # Data used for seeding the database.
│   │   │   ├── clients # Contains classes for making requests to external APIs.
│   │   │   ├── utils # Contains adapter classes to transform incoming data into the format expected by the models.
│   │   │   ├── models  # Contains the ORM model classes that represent the tables in the database.
│   │   │   ├── __init__.py  # Initializes the Flask application, sets up routes, and configures the database connection.
```

## Technology Stack

This section outlines the technology stack used in the application. Understanding the stack is crucial for development, maintenance, and scaling purposes.

### Backend

#### Frameworks and Libraries
- **Flask**: A lightweight WSGI web application framework used to serve the API endpoints.
- **SQLite (migrating to postgres)**: The database used for storing and querying data. Chosen for its simplicity and ease of integration with Python.
- **SQLAlchemy**: An ORM (Object-Relational Mapping) tool used to interact with the database using Python code instead of SQL queries.

### Frontend

- **Streamlit**: An open-source app framework used for creating beautiful, custom web apps for machine learning and data science projects. It serves as the dashboard frontend.


## What's Next?

- Develop the chatbot to be more robust and capable of answering more complex questions.
- Data preprocessing and feature engineering for the financial data.
- Automate the scraping, API calls, and data ingestion.
- Deploy phase 2 schema designed to third normal form.
- Setup XML to MD conversion for the chatbot to access company reports and press releases in real-time.
- Develop a more robust and interactive dashboard with more visualizations and insights.
- Explore adding more services to application stack, such as a database or a caching service.
- Integrate Docker and Docker Compose into a CI/CD pipeline for automated testing and deployment.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.

## Acknowledgments

- SEC EDGAR for providing company reports and press releases.
- Financial Modeling Prep API for providing financial data.

## Contact

For any queries or further assistance, please contact the repository owner.