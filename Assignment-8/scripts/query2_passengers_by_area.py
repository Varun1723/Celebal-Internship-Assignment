from pyspark.sql import SparkSession
from pyspark.sql.functions import round, col, sum as _sum

def main():
    # 1) Start Spark
    spark = SparkSession.builder \
        .appName("NYC Taxi – Passengers by Area") \
        .master("local[*]") \
        .getOrCreate()

    # 2) Read Parquet
    df = spark.read.parquet("../data/yellow_tripdata_2018-01.parquet")

    # 3) Define grid “area” by rounding pickup coords
    df_cells = df.withColumn("pickup_lat_2", round(col("pickup_latitude"), 2)) \
                 .withColumn("pickup_lon_2", round(col("pickup_longitude"), 2))

    # 4) Aggregate total passengers per cell
    df_area = df_cells.groupBy("pickup_lat_2", "pickup_lon_2") \
                      .agg(_sum("passenger_count").alias("total_passengers"))

    # 5) Order descending and show top 20
    df_area.orderBy(col("total_passengers").desc()) \
           .show(20, truncate=False)

    spark.stop()

if __name__ == "__main__":
    main()
