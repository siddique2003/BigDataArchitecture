# 🌟 **Ecommerce Big Data Analytics Pipeline**

[![Real-Time Streaming](https://img.shields.io/badge/Real--Time-Streaming-FF5733?style=for-the-badge&logo=apache-kafka)](https://hub.docker.com/u/msiddique2003)  
[![Batch Processing](https://img.shields.io/badge/Batch-Processing-blue?style=for-the-badge&logo=apache-hadoop)](https://hub.docker.com/u/msiddique2003)  
[![HBase Queries](https://img.shields.io/badge/HBase-Queries-green?style=for-the-badge&logo=apache-hbase)](https://hub.docker.com/u/msiddique2003)  
[![Interactive Dashboard](https://img.shields.io/badge/Interactive-Dashboard-purple?style=for-the-badge&logo=flask)](http://localhost:8000)  

---

## 📋 **Table of Contents**

- [📖 Introduction](#-introduction)  
- [📊 Dataset and Assumptions](#-dataset-and-assumptions)  
- [🛠 Technology Stack and Architecture](#-technology-stack-and-architecture)  
- [🚩 Features](#-features)  
- [🔄 Project Flow](#-project-flow)  
- [⚙️ Setup and Installation](#️-setup-and-installation)  
- [📜 Scripts and Usage](#-scripts-and-usage)  
- [🐳 Docker Containers](#-docker-containers)  
- [👥 Contributors](#-contributors)  

---

## 📖 **Introduction**

Welcome to the **Ecommerce Big Data Analytics Pipeline**!  
This project demonstrates how to implement a **scalable data pipeline** to handle **real-time streaming**, **batch processing**, and **data visualization** for ecommerce datasets. The aim is to process a high volume of data while ensuring low latency for real-time analytics and efficient querying for business intelligence (BI).

By leveraging technologies like **Kafka**, **HDFS**, **HBase**, and **Spark**, this pipeline processes, transforms, and queries the data while making it accessible through a visually interactive **Flask dashboard**.

---

## 📊 **Dataset and Assumptions**

### Dataset

We used the dataset [Ecommerce Churn](https://www.kaggle.com/datasets/saiparthas/ecommerce-churn), available on Kaggle.  

- **File Size**: 5.67GB after decompression.  
- **Key Fields**:  
  - User information (IDs, sessions).  
  - Product information (categories, brands, prices).  
  - Event information (timestamps, event types like view/purchase).  

### Assumptions

- Real-time updates are necessary for low-latency analytics.  
- Data is stored in a **dual-layer architecture** for:  
  - Batch processing (HDFS).  
  - Real-time analytics (HBase).  
- Transformations and cleaning are performed on the dataset to ensure unique identifiers and consistency.  

---

## 🛠 **Technology Stack and Architecture**

### Architecture Overview

![Pipeline Architecture](https://github.com/siddique2003/BigDataArchitecture/blob/main/architecture.jpg)

### Key Components

- **Kafka**: Ingests real-time data streams.  
- **HDFS**: Stores data for batch processing.  
- **HBase**: Supports random-access reads for real-time analytics.  
- **Spark**: Performs in-memory data processing and querying.  
- **Flask**: Hosts the **interactive BI dashboard**.  

---

## 🚩 **Features**

✨ Real-time streaming with Kafka.  
✨ Batch processing for comprehensive analytics.  
✨ Interactive dashboard for visualization.  
✨ SQL querying for seamless data exploration.  
✨ Scalable design for large datasets.  

---

## 🔄 **Project Flow**

1. **Ingestion**: Kafka ingests data from an external source.  
2. **Storage**:  
   - **HDFS**: Batch processing and large-scale data transformation.  
   - **HBase**: Random-access for focused analytics.  
3. **Transformation**: PySpark cleanses and processes raw data.  
4. **Querying**: Spark SQL is used to run analytics queries.  
5. **Visualization**: Flask serves dynamic dashboards for end-users.  

---

## ⚙️ **Setup and Installation**

### Prerequisites

- **Docker** and **Docker Compose** installed.  
- **Python 3.x** environment.  
- **Java 8+** runtime.  

### Installation

1. Clone this repository:  
   ```bash
   git clone https://github.com/siddique2003/BigDataAnalyticsPipeline.git  
   cd BigDataAnalyticsPipeline

2. Pull Docker images and start services:
   ```bash
    docker-compose up -d

3. Build the Flask app:
   ```bash
   cd flask  
   docker build -t flask-hbase-app .  
   docker run -p 8000:8000 flask-hbase-app  

4. Access the dashboard:
  Navigate to http://localhost:8000 in your browser.

## 📜 Key Scripts

| **Script Name**      | **Description**                              |
|-----------------------|----------------------------------------------|
| `hbase_load.py`       | Loads data into HBase.                      |
| `hdfs_write.py`       | Writes data to HDFS.                        |
| `kafka_producer.py`   | Streams data into Kafka.                    |
| `dashboard.py`        | Flask app that serves the dashboard.        |
| `import_to_hbase.sh`  | Automates HBase data import processes.       |

## 🐳 Docker Containers

| **Container Name**      | **Description**                       | **Docker Hub Link**                                                     |
|--------------------------|---------------------------------------|-------------------------------------------------------------------------|
| **spark-worker**         | Spark worker node.                   | [View on DockerHub](https://hub.docker.com/repository/docker/msiddique2003/spark-worker)         |
| **spark-master**         | Spark master node.                   | [View on DockerHub](https://hub.docker.com/repository/docker/msiddique2003/spark-master)         |
| **hbase-master**         | HBase master node.                   | [View on DockerHub](https://hub.docker.com/repository/docker/msiddique2003/hbase-master)         |
| **hbase-regionserver**   | HBase region server.                 | [View on DockerHub](https://hub.docker.com/repository/docker/msiddique2003/hbase-regionserver)   |
| **zookeeper**            | Manages distributed coordination.    | [View on DockerHub](https://hub.docker.com/repository/docker/msiddique2003/zookeeper)            |
| **kafka**                | Handles real-time data streams.      | [View on DockerHub](https://hub.docker.com/repository/docker/msiddique2003/kafka)                |

## 👥 Contributors

| **Contributor Name**          | **Role**                       |
|--------------------------------|---------------------------------|
| **Muhammad Siddique Khatri**  | Data Engineer & BI Expert      |
| **Muhammad Sarim ul Haque**   | Data Engineer                  |
| **Raine Ramchand**            | Data Engineer                  |


