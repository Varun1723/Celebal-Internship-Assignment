from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def main():
    
    spark = SparkSession.builder \
        .appName("NYC Taxi – Add Revenue") \
        .master("local[*]") \
        .getOrCreate()

    
    df = spark.read.parquet("Assignment-8\data\yellow_tripdata_2018-01.parquet")

    
    df_with_rev = df.withColumn(
        "Revenue",
        col("fare_amount")
        + col("extra")
        + col("mta_tax")
        + col("improvement_surcharge")
        + col("tip_amount")
        + col("tolls_amount")
        + col("total_amount")
    )

    df_with_rev.select(
        "fare_amount", "extra", "tip_amount", "total_amount", "Revenue"
    ).show(10, truncate=False)

    spark.stop()

if __name__ == "__main__":
    main()

