import mysql.connector
from mysql.connector import Error

def DatabaseStats():
    #mysql -h database-1.clqxqhhe6wft.us-east-1.rds.amazonaws.com -P 3306 -u admin -p'Data608-Project'
    connection = mysql.connector.connect(
        host='database-1.clqxqhhe6wft.us-east-1.rds.amazonaws.com',
        user='admin',
        password='Data608-Project',
        database='' # Optional: leave out to create DB first
        )
    
    if connection.is_connected():
        db_info = info = connection.server_info
        print(f"Connected to MySQL Server version: {db_info}")
        cursor = connection.cursor()
        
        #select database to use
        cursor.execute("USE CHESSBOT")

        #define table to look at
        table_name = 'games'

        cursor.execute("SELECT COUNT(*) FROM games")
        result = cursor.fetchone()
                
        return {result[0]}

from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    user_input = ""
    prev_input = ""
    prev_input_str = ""
    New_value = 0
    New_value_str = ""
    ShowValue = ""
    if request.method == 'POST':
        # Capture data from the form input named 'content'
        user_input = request.form.get('content')
        prev_input = request.form.get('previous')
        prev_input_str = request.form.get('previousStr')

    if user_input:
        New_value = int(user_input) +  int(prev_input)
        New_value_str = prev_input_str + user_input

    ShowValue = New_value_str
        
    SaveValue = str(New_value)
    # Simple HTML with a form and a display area
    return f'''
        <h1>Flask Doubling Calculator </h1>
        <h1>Database Table: games conta34gt4tgvtrins: {DatabaseStats()} entries </h1>
        <form method="POST">
            <input type="text" name="content" placeholder="Enter digits here.." required>
            <input type="text" hidden name="previous" value="{New_value}">
            <input type="text" hidden name="previousStr" value="{New_value_str}">
            <button type="submit">Submit</button>
            
        </form>
        
        {"<h3>You typed: " + user_input + "</h3>" if user_input else ""}
        {"<h3>Running sum is: " + SaveValue + "</h3>" if New_value else ""}
        {"<h3>Running sum (string) is: " + New_value_str + "</h3>" if New_value_str else ""}
        
    '''



if __name__ == '__main__':
    app.run(debug=True)
