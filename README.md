# Chicago Analysis

## Overview
Chicago Analysis explores crime, socio-economic indicators, and school data in Chicago. The project demonstrates **data processing, SQL querying, visualization, geospatial analysis**, and **dashboard deployment**.

The final **interactive dashboard** is deployed and accessible here: [https://chicago-analysis.onrender.com](https://chicago-analysis.onrender.com).

---

## Project Highlights
- **Data Preparation:** Load 3 CSV files into DataFrames and create a database.  
- **SQL Queries:** Extract insights about crime, schools, and socio-economic indicators.  
- **Visualizations:** Bar plots, scatter plots, heatmaps, and geospatial maps with Mapbox.  
- **Dashboard:** Interactive Dash app showing key insights, deployed on Render.

---

## Tech Stack
Python, Pandas, Plotly, Dash, SQLite (or other DB), Git, Render

---

## Run Locally
```bash
pip install -r requirements.txt
gunicorn src.app:server
