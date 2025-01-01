🚀 Ecommerce Big Data Analytics Pipeline
Uncovering insights with real-time and batch processing



📋 Table of Contents
Introduction
Dataset and Assumptions
Technology Stack and Architecture
Features
Project Flow
Setup and Installation
Scripts and Usage
Docker Containers
Contributors
📖 Introduction
In this project, we designed and implemented a Big Data Analytics Pipeline to handle and analyze ecommerce data efficiently. This pipeline combines real-time processing with batch analytics, leveraging technologies like Kafka, HBase, HDFS, Spark, and Flask for creating dashboards. The system is designed to process data rapidly while ensuring persistence for large-scale batch queries.

📊 Dataset and Assumptions
Dataset
The dataset comprises ecommerce transactions, including information about users, products, events, and pricing.

Key Assumptions
The platform requires real-time updates for immediate insights.
Batch analytics on large datasets provide deeper trends.
Data cleaning and transformation are applied for consistency.
A unique row identifier is added for easy querying.
🛠 Technology Stack and Architecture
This project utilizes the following technologies:

Kafka: Real-time data ingestion.
HDFS: Batch storage for large-scale analytics.
HBase: Optimized for low-latency, random-access queries.
Spark: SQL-based querying and in-memory computation.
Flask: Visualization and BI dashboard development.


🚩 Features
Real-time ingestion and batch storage
BI dashboards with interactive visualizations.
SQL querying via Spark for in-memory performance.
Supports both large-scale and targeted analytics.
🔄 Project Flow
Data Ingestion: Kafka ingests data into HDFS for batch analytics and HBase for low-latency access.
Data Cleaning & Transformation: Data is cleaned using PySpark scripts.
Query Engine: Spark queries the dataset for analytics.
BI Dashboard: Flask visualizes the processed data interactively.
⚙️ Setup and Installation
Prerequisites
Docker and Docker Compose
Python 3.x
Java 8+
Hadoop setup for HDFS commands
Installation Steps
Clone the repository:

bash
Copy code
git clone https://github.com/your-repo-link.git  
cd ecommerce-analytics  
Pull and run Docker containers:

bash
Copy code
docker-compose up -d  
Build and run the Flask app:

bash
Copy code
cd flask  
docker build -t flask-hbase-app .  
docker run -p 8000:8000 flask-hbase-app  
Access the dashboard:
Navigate to http://localhost:8000 in your browser.

📜 Scripts and Usage
Key Scripts
Script Name	Description
hbase_load.py	Script to load data into HBase.
hdfs_write.py	Script for writing to HDFS.
import_to_hbase.sh	Shell script for HBase import.
kafka_producer.py	Kafka producer for real-time ingestion.
dashboard.py	Flask application for BI dashboards.
JAR Files
All necessary JARs for Spark-HBase integration are available in the /spark folder.

🐳 Docker Containers
Container Name	Description	Docker Hub Link
spark-worker	Spark worker node.	Docker Hub
spark-master	Spark master node.	Docker Hub
hbase-master	HBase master node.	Docker Hub
hbase-regionserver	HBase region server.	Docker Hub
flask-hbase-app	Flask BI application.	Docker Hub
👥 Contributors
Muhammad Siddique Khatri
Muhammad Sarim ul Haque
Raine Ramchand
📄 Notes
Ensure the network is set up correctly for Kafka, HBase, and Spark communication.
For issues, refer to the Wiki or contact contributors.
🌟 Show Your Support
If you found this project helpful, consider giving it a star 🌟 on GitHub!

