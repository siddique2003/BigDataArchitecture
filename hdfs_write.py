import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Set environment variables for Hadoop
os.environ["HADOOP_HOME"] = "C:\\hadoop"
os.environ["PATH"] += os.pathsep + os.path.join(os.environ["HADOOP_HOME"], "bin")

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("HDFS to Spark with File Progress Tracking") \
    .config("spark.hadoop.fs.defaultFS", "hdfs://172.18.0.4:9000") \
    .config("spark.hadoop.dfs.client.use.datanode.hostname", "true") \
    .getOrCreate()

try:
    print("Spark session created")

    # HDFS Directory Path
    hdfs_dir_path = "hdfs://172.18.0.4:9000/ecommerce-data2"

    # List files in the HDFS directory
    file_list = spark._jvm.org.apache.hadoop.fs.FileSystem.get(
        spark._jsc.hadoopConfiguration()
    ).listStatus(spark._jvm.org.apache.hadoop.fs.Path(hdfs_dir_path))

    print("Files in HDFS directory:")
    for file in file_list:
        print(file.getPath().getName())

    # Process each file individually to track progress
    for file in file_list:
        file_path = file.getPath().toString()
        print(f"Processing file: {file_path}")

        # Read the file into a DataFrame
        df = spark.read.option("header", "false").csv(file_path)

        # Log the number of rows read
        row_count = df.count()
        print(f"Number of rows in {file_path}: {row_count}")

        # Perform transformations (example)
        transformed_df = df.withColumnRenamed("_c0", "timestamp") \
                           .withColumnRenamed("_c1", "action") \
                           .withColumnRenamed("_c2", "product_id")
        print(f"Transformations completed for {file_path}:")
        transformed_df.show(5)

        # Save transformed data back to HDFS (optional)
        output_path = f"hdfs://172.18.0.4:9000/ecommerce-data2/output/{file.getPath().getName()}"
        transformed_df.write.csv(output_path, header=True, mode="overwrite")
        print(f"Transformed data saved to: {output_path}")

except Exception as e:
    print(f"Error occurred: {e}")

finally:
    # Stop the Spark session
    spark.stop()
