from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, col

def main():
    spark = SparkSession.builder \
        .appName("FlattenAndWriteTable") \
        .master("local[*]") \
        .getOrCreate()

    # Read your (possibly nested) Parquet
    df = spark.read.parquet("../data/yellow_tripdata_2018-01.parquet")

    # Example: if you have a JSON struct column `extras` and an array `tags`
    df_flat = df \
        .select(
            "*",
            col("extras.someField").alias("extra_someField"),
            explode(col("tags")).alias("tag")
        ) \
        .drop("extras","tags")

    # Write out as external Parquet table
    output_path = "../data/flat_taxi_data"
    df_flat.write.mode("overwrite") \
        .format("parquet") \
        .option("path", output_path) \
        .saveAsTable("default.flat_taxi_data")

    spark.stop()

if __name__=="__main__":
    main()
