# 🌟 **Ecommerce Big Data Analytics Pipeline**  

[![Real-Time Streaming](https://img.shields.io/badge/Real--Time-Streaming-FF5733?style=for-the-badge&logo=apache-kafka)](https://hub.docker.com/u/msiddique2003)  
[![Batch Processing](https://img.shields.io/badge/Batch-Processing-blue?style=for-the-badge&logo=apache-hadoop)](https://hub.docker.com/u/msiddique2003)  
[![HBase Queries](https://img.shields.io/badge/HBase-Queries-green?style=for-the-badge&logo=apache-hbase)](https://hub.docker.com/u/msiddique2003)  
[![Interactive Dashboard](https://img.shields.io/badge/Interactive-Dashboard-purple?style=for-the-badge&logo=flask)](http://localhost:8000)  

---

## 📋 **Table of Contents**  

- [Introduction](#introduction)  
- [Dataset and Assumptions](#dataset-and-assumptions)  
- [Technology Stack and Architecture](#technology-stack-and-architecture)  
- [Features](#features)  
- [Project Flow](#project-flow)  
- [Setup and Installation](#setup-and-installation)  
- [Scripts and Usage](#scripts-and-usage)  
- [Docker Containers](#docker-containers)  
- [Contributors](#contributors)  

---

## 📖 **Introduction**  

Welcome to the **Ecommerce Big Data Analytics Pipeline**!  
Our project combines the power of **real-time streaming**, **batch processing**, and **data visualization** to analyze and make sense of ecommerce data.  
Through this pipeline, you'll explore how to handle **real-time ingestion** with Kafka, process data with Spark, and visualize insights on a **dynamic dashboard**.

---

## 📊 **Dataset and Assumptions**  

### Dataset  

- **Users**: Identifiers and session details.  
- **Products**: IDs, brands, and categories.  
- **Events**: Views, purchases, and timestamps.  

### Assumptions  

- The pipeline supports **real-time updates** for low-latency analytics.  
- Data is stored in a **dual-layer architecture** for efficient querying:  
  - **HDFS**: For batch-based large-scale analytics.  
  - **HBase**: For quick, random-access analytics.  

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
