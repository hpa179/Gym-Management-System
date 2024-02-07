from flask import Flask, jsonify,render_template, request
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import markdown2
from sqlalchemy.exc import OperationalError, ProgrammingError
import pandas as pd
import os
import sys
from tabulate import tabulate
from sqlalchemy import create_engine, text
from IPython.display import display, Markdown
from datetime import datetime
import pymysql
import traceback

app = Flask(__name__)

config_map = {
    'user': 'CMSC508_USER',
    'password': 'CMSC508_PASSWORD',
    'host': 'CMSC508_HOST',
    'database': 'GYM_DB_NAME'
}

load_dotenv()

config = {}
for key in config_map.keys():
    config[key] = os.getenv(config_map[key])

engine_uri = f"mysql+pymysql://{config['user']}:{config['password']}@{config['host']}/{config['database']}"

try:
    cnx = create_engine(engine_uri)
except Exception as e:
    msg = str(e).replace(") (", ")\n(")
    df = pd.DataFrame({'Query error': [msg]})  # Include the actual error message
    print(msg)

def my_sql_wrapper(query):
    try:
        df = pd.read_sql(query, cnx)
    except Exception as e:
        df = pd.DataFrame({'Query error': ["(see error message above)"]})
        msg = str(e).replace(") (", ")\n(")
        print(msg)
    return df

# Endpoint that shows tables
@app.route('/api/tables')
def api_show_tables():
    df = my_sql_wrapper("show tables")
    records = df.to_dict(orient='records')
    return jsonify(records)

# Endpoint that shows all the data inside the specified table
@app.route('/api/<table_name>')
def api_show_table(table_name):
    valid_tables = ['employees', 'gym', 'members', 'equipment', 
                    'owner', 'payments', 'sessions', 'supplier']
    if table_name in valid_tables:
        query = f"SELECT * FROM {table_name}"
        df = my_sql_wrapper(query)
        records = df.to_dict(orient='records')
        return jsonify(records)
    else:
        return jsonify({"error": "Invalid table name"}), 404
    
# Endpoint that deletes from table
@app.route('/api/employees/delete', methods=['POST'])
def delete_employee_via_post():
    employee_id = request.form.get('employee_id')
    if not employee_id:
        return jsonify({"error": "No employee_id provided"}), 400

    try:
        # Connect to the database
        connection = cnx.connect()
        # Start a transaction
        transaction = connection.begin()
        try:
            # The SQL query to delete the employee
            query = text("DELETE FROM employees WHERE Employee_ID = :employee_id")
            result = connection.execute(query, {'employee_id': employee_id})

            # Check if any row is deleted
            if result.rowcount > 0:
                transaction.commit()  # Commit the changes if the delete was successful
                return jsonify({"success": f"Employee with ID {employee_id} deleted"}), 200
            else:
                transaction.rollback()  # Rollback if no rows were deleted
                return jsonify({"error": f"No employee found with ID {employee_id}"}), 404
        except Exception as e:
            transaction.rollback()  # Rollback in case of any other exception
            raise
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()
        
# Endpoint to update table name
@app.route('/api/tables/update', methods=['POST'])
def rename_table():
    data = request.get_json()
    old_name = data.get('old_name')
    new_name = data.get('new_name')

    if not old_name or not new_name:
        return jsonify({"error": "Both old_name and new_name are required"}), 400

    # Building the SQL statement for renaming a table
    rename_statement = text(f"RENAME TABLE {old_name} TO {new_name};")

    with cnx.connect() as connection:
        try:
            # Start a transaction
            with connection.begin():
                # Execute the RENAME TABLE statement
                connection.execute(rename_statement)
                return jsonify({"success": f"Table '{old_name}' renamed to '{new_name}'"}), 200
        except Exception as e:
            # If there is an error, it will be caught here
            return jsonify({"error": str(e)}), 500
        
# Endpoints to filter through each table
@app.route('/api/employees/filter', methods=['GET'])
def api_filter_employees():
    min_timesheet = request.args.get('min_timesheet', type=int)
    max_timesheet = request.args.get('max_timesheet', type=int)

    if min_timesheet is not None and max_timesheet is not None:
        # Construct the query with parameter placeholders
        query = f"SELECT * FROM employees WHERE timesheet BETWEEN {min_timesheet} AND {max_timesheet}"
        try:
            # Call the my_sql_wrapper with the complete query
            df = my_sql_wrapper(query)
            records = df.to_dict(orient='records')
            return jsonify(records)
        except Exception as e:
            print(e)  # Print the error message to the server's log
            return jsonify({"error": "An error occurred while processing your request"}), 500
    else:
        return jsonify({"error": "Please provide both min_timesheet and max_timesheet parameters"})

if __name__ == '__main__':
    app.run(debug=True)