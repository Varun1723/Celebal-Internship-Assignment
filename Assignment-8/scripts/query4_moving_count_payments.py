from pyspark.sql import SparkSession
from pyspark.sql.functions import window, count

def main():
    spark = SparkSession.builder \
        .appName("Query4_MovingCountPayments") \
        .master("local[*]") \
        .getOrCreate()

    df = spark.readStream \
        .schema("""
            payment_type INT,
            pickup_datetime TIMESTAMP
        """) \
        .parquet("../data/yellow_tripdata_2018-01.parquet")

    result = df.groupBy(
        window("pickup_datetime", "5 minutes", "1 minute"),
        "payment_type"
    ).agg(count("*").alias("payment_count"))

    query = result.writeStream \
        .outputMode("complete") \
        .format("console") \
        .option("truncate", False) \
        .start()

    query.awaitTermination()

if __name__=="__main__":
    main()
