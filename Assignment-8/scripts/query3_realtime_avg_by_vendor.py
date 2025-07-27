from pyspark.sql import SparkSession
from pyspark.sql.functions import window, avg

def main():
    spark = SparkSession.builder \
        .appName("Query3_RealtimeAvgByVendor") \
        .master("local[*]") \
        .getOrCreate()

    # read as a stream
    df = spark.readStream \
        .schema("VendorID INT, pickup_datetime TIMESTAMP, fare_amount DOUBLE") \
        .parquet("../data/yellow_tripdata_2018-01.parquet")

    # sliding window of 1 minute, advance every 30 seconds
    result = df.groupBy(
        window("pickup_datetime", "1 minute", "30 seconds"),
        "VendorID"
    ).agg(
        avg("fare_amount").alias("avg_fare"),
        avg("fare_amount").alias("avg_revenue")
    )

    query = result.writeStream \
        .outputMode("complete") \
        .format("console") \
        .option("truncate", False) \
        .start()

    query.awaitTermination()

if __name__=="__main__":
    main()
