import pandas as pd 
import mysql.connector

# 1 . Conexion con la basse de datos HeidiSQL
conn  = mysql.connector.connect(
    host= "localhost",
    user = "root",
    password = "Mamapapa2004",
    database = "sales_project"
)

# 2. SQL Query para identificar tendencias (Requeriment: optimized SQL)
query = """
SELECT category, SUM(amount) AS total_revenue
FROM daily_sales
GROUP BY category
ORDER BY total_revenue DESC;
"""

# 3. Cargar datos en el DATAFRAME de Pandas
print(query)
try:
    df = pd.read_sql(query, conn)
except Exception as e:
    print("Error SQL:", e)
#4. Mostrar Reporte basico (Requeriment: support insights)
print("--- Sales Report By Category ---")
print(df)

conn.close()