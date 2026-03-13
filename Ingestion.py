import obtain as ob
import decompress as dc
import parse as pa
import cleanup as cu

#The user selects a file (month/year) to load into the database. 
#App connects to Lichess and downloads the compressed Data file
#App decompresses the Data file on EBS storage
#App parses the Data file for each chess game
#If game matches load conditions, 
#Then parse the moves value to make database-ready
#Insert Game data  and obtain game_id
#Insert Moves data with game_id
#Repeat till the end of the file
#Clean up the EBS, downloaded files, and uncompressed file
#Send Metrics and Remaining Space to the user

from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    fruitsSelected = ""
    if request.method == 'POST':
        # Capture data from the form input named 'content'
        fruitsSelected = request.form.get('fruits')

    # Simple HTML with a form and a display area
    return f'''
        <h1>Data Ingestion for Chess Bot</h1>
        <form method="POST">
            <label for="fruits">Choose a fruit:</label>
            <select name="fruits" id="fruits">
              <option value="apple">Apple</option>
              <option value="banana">Banana</option>
              <option value="cherry">Cherry</option>
            </select>
            <button type="submit">Submit</button>
        </form>
        
        {"<h3>You selection: " + fruitsSelected + "</h3>" if fruitsSelected else ""}
        
    '''