from flask import Flask, jsonify, render_template_string, request
import happybase
import pandas as pd
import io
import base64

app = Flask(__name__)

# Global variable to store the DataFrame
dataframe = None

# Connect to HBase
HBASE_HOST = '172.18.0.4'  # Replace with your HBase host
HBASE_PORT = 9090          # Replace with your HBase Thrift port
TABLE_NAME = 'ecommerce_data_transformed'

# Function to typecast the DataFrame
def typecast_dataframe(df):
    try:
        # Fill missing values with placeholders
        df.fillna({'product:category_code': 'unknown', 'product:brand': 'unknown', 'event:type': 'unknown'}, inplace=True)
        df['event:time'] = pd.to_datetime(df['event:time'], errors='coerce')
        df['event:type'] = df['event:type'].astype(str)
        df['product:id'] = pd.to_numeric(df['product:id'], errors='coerce')
        df['product:category_code'] = df['product:category_code'].astype(str)
        df['product:category_id'] = pd.to_numeric(df['product:category_id'], errors='coerce')
        df['product:brand'] = df['product:brand'].astype(str)
        df['product:price'] = pd.to_numeric(df['product:price'], errors='coerce')
        df['user:id'] = pd.to_numeric(df['user:id'], errors='coerce')
        df['user:session'] = df['user:session'].astype(str)
        return df
    except Exception as e:
        raise ValueError(f"Error in typecasting: {e}")

# Endpoint to load the DataFrame from HBase
@app.route('/')
def load_data():
    global dataframe
    try:
        # Connect to HBase Thrift Server
        connection = happybase.Connection(host=HBASE_HOST, port=HBASE_PORT)
        table = connection.table(TABLE_NAME)

        # Get parameters for row start and batch size
        start_row = request.args.get('start_row', None)
        batch_size = int(request.args.get('batch_size', 1000))

        # Limit rows fetched from HBase
        rows = table.scan(row_start=start_row, limit=batch_size)
        data = [
            {**{k.decode('utf-8'): v.decode('utf-8') for k, v in row.items()}, 'row_key': key.decode('utf-8')}
            for key, row in rows
        ]

        # Create DataFrame from the fetched data
        dataframe = pd.DataFrame(data)

        # Typecast the DataFrame
        dataframe = typecast_dataframe(dataframe)

        html_template = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Data Loaded</title>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css">
            <style>
                body {
                    background: linear-gradient(to right, #f7cac9, #92a8d1);
                    font-family: Arial, sans-serif;
                    color: #34495e;
                }
                .container {
                    background-color: white;
                    border-radius: 10px;
                    padding: 30px;
                    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
                    max-width: 600px;
                    margin: auto;
                    margin-top: 10%;
                }
                h1 {
                    font-weight: bold;
                    color: #34495e;
                }
                .btn-dashboard {
                    background-color: #3498db;
                    color: white;
                    font-size: 1.2rem;
                    padding: 10px 20px;
                    border-radius: 30px;
                    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
                    text-transform: uppercase;
                    transition: all 0.3s ease-in-out;
                    text-decoration: none;
                }
                .btn-dashboard:hover {
                    background-color: #2980b9;
                    box-shadow: 0 6px 16px rgba(0, 0, 0, 0.4);
                }
                .description {
                    margin-top: 20px;
                    font-size: 1rem;
                    color: #7f8c8d;
                }
                .credits {
                    margin-top: 30px;
                    font-size: 0.95rem;
                    color: #34495e;
                    text-align: center;
                    padding: 10px;
                    border-top: 1px solid #ecf0f1;
                    margin-top: 20px;
                }
                .credits span {
                    font-weight: bold;
                }
            </style>
        </head>
        <body>
            <div class="container text-center">
                <h1>Welcome to Our Data Dashboard</h1>
                <p class="description">
                    Explore the insights we've uncovered from the data, including the most viewed brands, 
                    sales distribution, and revenue by brand. Click the button below to dive into our detailed dashboard.
                </p>
                <a href="/dashboard" class="btn-dashboard">View Dashboard</a>
                <div class="credits">
                    Presented by: <span>Muhammad Siddique Khatri, Muhammad Sarim ul Haque, and Raine Ramchand</span>
                </div>
            </div>
        </body>
        </html>
        """
        return html_template

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint for the dashboard
@app.route('/dashboard', methods=['GET'])
def homepage():
    global dataframe
    if dataframe is None:
        return jsonify({"error": "DataFrame not loaded. Please visit / to load data."}), 400

    try:
        # Prepare Data for Charts
        top_viewed = dataframe[dataframe['event:type'] == 'view']
        top_brands = top_viewed.groupby('product:brand').size().sort_values(ascending=False).head(5).to_dict()

        sales_data = dataframe[dataframe['event:type'] == 'purchase']
        top_revenue_brands = sales_data.groupby('product:brand')['product:price'].sum().sort_values(ascending=False).head(5).to_dict()

        event_counts = dataframe['event:type'].value_counts().to_dict()

        # Render HTML with Bootstrap and Chart.js
        html_template = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Dashboard</title>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css">
            <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        </head>
        <body class="bg-light">
            <div class="container mt-5">
                <h1 class="text-center text-primary">Data Analytics Dashboard</h1>
                
                <div class="row mt-5">
                    <div class="col-md-6">
                        <h3 class="text-center">Top Viewed Brands</h3>
                        <ul class="list-group">
                            {"".join([f"<li class='list-group-item d-flex justify-content-between align-items-center'>{brand}<span class='badge bg-primary'>{views}</span></li>" for brand, views in top_brands.items()])}
                        </ul>
                    </div>
                    <div class="col-md-6">
                        <h3 class="text-center">Top 5 Brands by Revenue</h3>
                        <ul class="list-group">
                            {"".join([f"<li class='list-group-item d-flex justify-content-between align-items-center'>{brand}<span class='badge bg-success'>{revenue:.2f}</span></li>" for brand, revenue in top_revenue_brands.items()])}
                        </ul>
                    </div>
                </div>

                <div class="row mt-5">
                    <div class="col-md-6">
                        <h3 class="text-center">Event Distribution</h3>
                        <canvas id="eventChart"></canvas>
                    </div>
                    <div class="col-md-6">
                        <h3 class="text-center">Sales Revenue</h3>
                        <canvas id="revenueChart"></canvas>
                    </div>
                </div>
            </div>

            <script>
                // Event Distribution Chart
                const eventCtx = document.getElementById('eventChart').getContext('2d');
                new Chart(eventCtx, {{
                    type: 'pie',
                    data: {{
                        labels: {list(event_counts.keys())},
                        datasets: [{{
                            data: {list(event_counts.values())},
                            backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4CAF50', '#F39C12'],
                        }}]
                    }}
                }});

                // Revenue Chart
                const revenueCtx = document.getElementById('revenueChart').getContext('2d');
                new Chart(revenueCtx, {{
                    type: 'bar',
                    data: {{
                        labels: {list(top_revenue_brands.keys())},
                        datasets: [{{
                            label: 'Revenue',
                            data: {list(top_revenue_brands.values())},
                            backgroundColor: ['#4CAF50', '#FF6384', '#36A2EB', '#FFCE56', '#8E44AD'],
                        }}]
                    }},
                    options: {{
                        responsive: true,
                        plugins: {{
                            legend: {{
                                display: true
                            }}
                        }}
                    }}
                }});
            </script>
        </body>
        </html>
        """
        return html_template

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
