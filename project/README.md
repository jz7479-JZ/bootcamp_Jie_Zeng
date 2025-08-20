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
