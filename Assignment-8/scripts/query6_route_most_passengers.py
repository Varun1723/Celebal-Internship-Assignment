from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum

def main():
    spark = SparkSession.builder \
        .appName("Query6_RouteMostPassengers") \
        .master("local[*]") \
        .getOrCreate()

    df = spark.read.parquet("../data/yellow_tripdata_2018-01.parquet")

    df.groupBy("pickup_zone","dropoff_zone") \
      .agg(_sum("passenger_count").alias("total_pax")) \
      .orderBy(col("total_pax").desc()) \
      .limit(1) \
      .show(truncate=False)

    spark.stop()

if __name__=="__main__":
    main()
