#!/bin/bash

# Environment Variables
HBASE_CONTAINER_NAME="hbase-master"
NAMENODE_CONTAINER_NAME="hadoop-namenode"
HBASE_COMMAND="hbase org.apache.hadoop.hbase.mapreduce.ImportTsv"
HDFS_DIRECTORY="/ecommerce-data-transformed-batches"
HBASE_TABLE="ecommerce_data_transformed"
COLUMN_MAPPINGS="HBASE_ROW_KEY,event:time,event:type,product:category_id,product:category_code,product:brand,product:price,user:id,user:session"
NEW_FILENAME="t_file.csv"

# Find the CSV file in the HDFS directory
CSV_FILE=""
FILES=$(docker exec $NAMENODE_CONTAINER_NAME hdfs dfs -ls hdfs://hadoop-namenode:9000$HDFS_DIRECTORY)
while read -r line; do
  # Extract the last word (file path) from each line
  file_path=$(echo $line | rev | cut -d' ' -f1 | rev)
  # Check if the file path ends with .csv
  if [[ $file_path == *.csv ]]; then
    CSV_FILE=$file_path
    break
  fi
done <<< "$FILES"

# Check if a CSV file was found
if [ -z "$CSV_FILE" ]; then
  echo "No CSV file found in $HDFS_DIRECTORY."
  exit 1
fi

# Debug: Print the found CSV file
echo "Found CSV file: $CSV_FILE"

# Rename the found CSV file to the new name
docker exec $NAMENODE_CONTAINER_NAME hdfs dfs -mv "$CSV_FILE" "hdfs://hadoop-namenode:9000$HDFS_DIRECTORY/$NEW_FILENAME"

# Debug: Print confirmation of renaming
if [ $? -eq 0 ]; then
  echo "Renamed $CSV_FILE to $HDFS_DIRECTORY/$NEW_FILENAME"
else
  echo "Failed to rename $CSV_FILE to $HDFS_DIRECTORY/$NEW_FILENAME"
  exit 1
fi

# Import the renamed CSV file into HBase
docker exec -it $HBASE_CONTAINER_NAME bash -c "$HBASE_COMMAND -Dimporttsv.separator=, -Dimporttsv.columns='$COLUMN_MAPPINGS' $HBASE_TABLE hdfs://hadoop-namenode:9000$HDFS_DIRECTORY/$NEW_FILENAME"

# Check if the import was successful
if [ $? -eq 0 ]; then
  echo "Data successfully imported into HBase table: $HBASE_TABLE"
else
  echo "Failed to import data into HBase table: $HBASE_TABLE"
  exit 1
fi
