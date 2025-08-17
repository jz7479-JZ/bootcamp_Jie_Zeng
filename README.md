# Bootcamp Repository 
## Folder Structure 
- **homework/** → All homework contributions will be submitted here. - **project/** → All project contributions will be submitted here. - **class_materials/** → Local storage for class materials. Never pushed to GitHub.
## Homework Folder Rules 
- Each homework will be in its own subfolder (`homework0`, `homework1`, etc.) - Include all required files for grading. 
## Project Folder Rules 
- Keep project files organized and clearly named. 
## Data Storage

- **Folder Structure**
  - data/raw/ : stores raw ingested files (CSV)
  - data/processed/ : stores processed files (Parquet)

- **Formats**
  - CSV: easy to read and portable
  - Parquet: efficient for analytics and storage

- **Environment Variables**
  - DATA_DIR_RAW and DATA_DIR_PROCESSED are set in `.env`
  - Code loads them with dotenv and uses as base paths

- **Validation**
  - Checks shape consistency
  - Ensures required columns
  - `price` column stays numeric
  - `date` column is datetime

- **Assumptions & Risks**
  - Parquet requires pyarrow or fastparquet
  - CSV assumed UTF-8
  - Validation is basic, more rules may be needed
