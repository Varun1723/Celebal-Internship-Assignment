from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum

def main():
    spark = SparkSession.builder \
        .appName("Query5_TopTwoVendors") \
        .master("local[*]") \
        .getOrCreate()

    df = spark.read.parquet("../data/yellow_tripdata_2018-01.parquet")
    # replace with your target date
    target_date = "2018-01-15"

    df = df.withColumn(
        "Revenue",
        col("fare_amount")
        + col("extra")
        + col("mta_tax")
        + col("improvement_surcharge")
        + col("tip_amount")
        + col("tolls_amount")
        + col("total_amount")
    )

    df.filter(col("pickup_datetime").cast("date") == target_date) \
      .groupBy("VendorID") \
      .agg(
          _sum("Revenue").alias("total_rev"),
          _sum("passenger_count").alias("total_pax"),
          _sum("trip_distance").alias("total_dist")
      ) \
      .orderBy(col("total_rev").desc()) \
      .limit(2) \
      .show(truncate=False)

    spark.stop()

if __name__=="__main__":
    main()
