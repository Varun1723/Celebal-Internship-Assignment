from sqlalchemy import create_engine, text

SERVER = "localhost"   # or just "localhost" if that’s your instance
DB     = "Northwind"
DRIVER = "ODBC Driver 17 for SQL Server"

# Note: no USER/PASS needed for Windows auth
conn_str = (
    f"mssql+pyodbc://@{SERVER}/{DB}"
    f"?driver={DRIVER.replace(' ', '+')}"
    f"&trusted_connection=yes"
)
engine = create_engine(conn_str)

with engine.connect() as conn:
    count = conn.execute(text("SELECT COUNT(*) FROM dbo.Customers")).scalar()
    print(f"Customers table has {count} rows.")
