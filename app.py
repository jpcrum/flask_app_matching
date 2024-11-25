from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

csv_file = 'data/data.csv'
csv_file_output = 'data/data_checked.csv'
data = pd.read_csv(csv_file)
data['Match'] = None  # Add a new column for matches
index_num = 0  # Track the current index


@app.route('/')
def index():
    global index_num
    if index_num >= len(data):
        return "All rows processed! Check the updated CSV."

    # Extract current row data
    row = data.iloc[index_num]
    image_url = row['Image']  # Image URL column in CSV
    name = row['Name']  # Name column
    account_id = row['Account_ID']  # Account_ID column

    return render_template(
        'index.html',
        image_url=image_url,
        name=name,
        account_id=account_id,
        total=len(data),
        current=index_num + 1
    )


@app.route('/match/<decision>')
def match(decision):
    global index_num
    data.at[index_num, 'Match'] = 1 if decision == 'match' else 0
    index_num += 1  # Move to the next row
    if index_num < len(data):
        return redirect(url_for('index'))
    else:
        # Save the updated CSV
        data.to_csv(csv_file_output, index=False)
        return "All rows processed! Check the updated CSV."


if __name__ == '__main__':
    app.run(debug=True)