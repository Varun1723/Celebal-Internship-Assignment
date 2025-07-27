from pyspark.sql import SparkSession
from pyspark.sql.functions import window, count

def main():
    spark = SparkSession.builder \
        .appName("Query7_TopPickupsLastSeconds") \
        .master("local[*]") \
        .getOrCreate()

    df = spark.readStream \
        .schema("pickup_datetime TIMESTAMP, pickup_zone STRING") \
        .parquet("../data/yellow_tripdata_2018-01.parquet")

    # 10‑second sliding window
    result = df.groupBy(
        window("pickup_datetime", "10 seconds", "5 seconds"),
        "pickup_zone"
    ).agg(count("*").alias("pickup_count"))

    query = result.writeStream \
        .outputMode("complete") \
        .format("console") \
        .option("truncate", False) \
        .start()

    query.awaitTermination()

if __name__=="__main__":
    main()
