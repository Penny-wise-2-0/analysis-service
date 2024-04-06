# Pennywise Analysis Service

The Analysis Microservice is a backend component of the Pennywise Personal Finance App responsible for performing data analysis on financial data stored in the database. It operates on data ingested by the Pennywise Ingest Service, transforming it into actionable insights for users.

## Functionalities

- **Data Analysis:** Utilizes the Pandas library to conduct in-depth analysis on financial data, including transaction history, account balances, and budget information.
- **Data Formatting:** Formats analyzed data into structured formats suitable for visualization and reporting, enhancing its readability and interpretability.
- **Integration with Ingested Data:** Integrates seamlessly with the financial data ingested by the Pennywise Finance Ingest Service, leveraging the processed data for analysis.
- **Visualization Support:** Sends ready-to-use formatted data  for seamless data visualization

## Implementation

Implemented in Python, the Analysis Microservice leverages the Pandas library for efficient data analysis and manipulation. It interacts with the database through SQLAlchemy to retrieve and process financial data stored by the ingest service, while using flask as a lightwieght server option.

## Purpose

The primary purpose of the Analysis Microservice is to provide users with valuable insights into their financial health. By analyzing their financial data and presenting it in a comprehensible format, the microservice empowers users to make informed decisions regarding budgeting, spending habits, and financial planning.

## Disclaimer

The Pennywise Analysis Service is developed for private, personal use as a component of the Pennywise personal finance application. It is tailored specifically to the developer's individual financial management need. This service and its codebase are not intended for commercial distribution, replication, or use and do not offer any warranties or guarantees.
