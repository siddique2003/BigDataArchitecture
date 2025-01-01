# 🚀 **Ecommerce Big Data Analytics Pipeline**  
*Uncovering insights with real-time and batch processing*

![Architecture](https://github.com/your-repo-link/architecture.jpg)

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
In this project, we designed and implemented a **Big Data Analytics Pipeline** to handle and analyze ecommerce data efficiently. This pipeline combines real-time processing with batch analytics, leveraging technologies like Kafka, HBase, HDFS, Spark, and Flask for creating dashboards. The system is designed to process data rapidly while ensuring persistence for large-scale batch queries.

---

## 📊 **Dataset and Assumptions**  

### Dataset  
The dataset comprises ecommerce transactions, including information about users, products, events, and pricing.  

### Key Assumptions  
- The platform requires **real-time updates** for immediate insights.  
- **Batch analytics** on large datasets provide deeper trends.  
- Data cleaning and transformation are applied for consistency.  
- A **unique row identifier** is added for easy querying.  

---

## 🛠 **Technology Stack and Architecture**  
This project utilizes the following technologies:  
- **Kafka:** Real-time data ingestion.  
- **HDFS:** Batch storage for large-scale analytics.  
- **HBase:** Optimized for low-latency, random-access queries.  
- **Spark:** SQL-based querying and in-memory computation.  
- **Flask:** Visualization and BI dashboard development.

![Pipeline Architecture](https://github.com/your-repo-link/architecture.jpg)  

---

## 🚩 **Features**  
- **Real-time ingestion and batch storage**  
- **BI dashboards** with interactive visualizations.  
- **SQL querying via Spark** for in-memory performance.  
- Supports **both large-scale and targeted analytics**.  

---

## 🔄 **Project Flow**  

1. **Data Ingestion:** Kafka ingests data into HDFS for batch analytics and HBase for low-latency access.  
2. **Data Cleaning & Transformation:** Data is cleaned using PySpark scripts.  
3. **Query Engine:** Spark queries the dataset for analytics.  
4. **BI Dashboard:** Flask visualizes the processed data interactively.

---

## ⚙️ **Setup and Installation**  

### Prerequisites  
- Docker and Docker Compose  
- Python 3.x  
- Java 8+  
- Hadoop setup for HDFS commands  

### Installation Steps  

1. Clone the repository:  
   ```bash  
   git clone https://github.com/your-repo-link.git  
   cd ecommerce-analytics  
