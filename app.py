import pandas as pd
from flask import Flask, render_template

# Flask application initialize
app = Flask(__name__)

# --- Data Loading and Pre-processing ---
# Using the specific Rajasthan data file
try:
    # Read the new, cleaned Rajasthan data file
    # Ensure this file (rajasthan_data.csv) is in the root of your Docker context
    df = pd.read_csv("rajasthan_data.csv")

    # Clean data (in case there are NA values in calculation columns)
    # This prevents the division by zero error later
    df["Total_No_of_Active_Workers"] = pd.to_numeric(df["Total_No_of_Active_Workers"], errors='coerce').fillna(0)
    df["Total_No_of_JobCards_issued"] = pd.to_numeric(df["Total_No_of_JobCards_issued"], errors='coerce').fillna(0)
    
    # Filter for the latest month's data if needed, but for simplicity, we'll use all rows for now.

    # Calculate Performance Rate (KPI)
    # Add a small value (1) to the denominator to prevent division by zero if all values are 0
    df["Performance_Rate"] = (
        df["Total_No_of_Active_Workers"] / (df["Total_No_of_JobCards_issued"] + 1)
    ) * 100
    
    # Prepare data for rendering in HTML (convert DataFrame rows to list of dictionaries)
    data = df.to_dict("records")
    
except FileNotFoundError:
    print("ERROR: rajasthan_data.csv not found. Ensure the file is in the correct directory.")
    data = []
except KeyError as e:
    print(f"ERROR: Column not found: {e}. Check CSV column names.")
    data = []
except Exception as e:
    print(f"An unexpected error occurred during data processing: {e}")
    data = []


@app.route("/")
def dashboard():
    # 'districts' is the variable name used in index.html for looping
    return render_template("index.html", districts=data)

if __name__ == "__main__":
    # This block is typically skipped in a Docker/Gunicorn setup but kept for completeness
    app.run(host="0.0.0.0", port=5000)
