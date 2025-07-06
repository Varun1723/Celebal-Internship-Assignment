import os
import argparse
import pandas as pd
import pyarrow as pa, pyarrow.parquet as pq
from fastavro import writer, parse_schema
from sqlalchemy import create_engine, text

# — Configuration — 
USER   = "sa"
PASS   = "YourSAPassword"
SERVER = "localhost\\SQLEXPRESS"
DB     = "Northwind"
DRIVER = "ODBC Driver 17 for SQL Server"
OUT    = "data_exports"

def ensure_dir(d):
    os.makedirs(d, exist_ok=True)

def fetch(table, cols="*"):
    url = (
        f"mssql+pyodbc://{USER}:{PASS}@{SERVER}/{DB}"
        f"?driver={DRIVER.replace(' ', '+')}"
    )
    eng = create_engine(url)
    with eng.connect() as conn:
        return pd.read_sql(text(f"SELECT {cols} FROM dbo.{table}"), conn)

def to_csv(df, t):
    df.to_csv(f"{OUT}/{t}.csv", index=False)

def to_parquet(df, t):
    table = pa.Table.from_pandas(df)
    pq.write_table(table, f"{OUT}/{t}.parquet")

def to_avro(df, t):
    fields = []
    for col, dtype in df.dtypes.items():
        if pd.api.types.is_integer_dtype(dtype):
            tp = "long"
        elif pd.api.types.is_float_dtype(dtype):
            tp = "double"
        else:
            tp = "string"
        fields.append({"name": col, "type": ["null", tp], "default": None})
    schema = {"name": t, "type": "record", "fields": fields}
    records = df.where(pd.notnull(df), None).to_dict(orient="records")
    with open(f"{OUT}/{t}.avro", "wb") as out:
        writer(out, parse_schema(schema), records)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--table", required=True)
    p.add_argument("--cols", default="*")
    args = p.parse_args()

    ensure_dir(OUT)
    df = fetch(args.table, args.cols)
    to_csv(df, args.table)
    to_parquet(df, args.table)
    to_avro(df, args.table)
