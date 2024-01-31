# Import libraries
from flask import Flask, request, url_for, redirect, render_template

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
transactions = [
        {'id': 1, 'date': '2023-06-01', 'amount': 100},
        {'id': 2, 'date': '2023-06-02', 'amount': -200},
        {'id': 3, 'date': '2023-06-03', 'amount': 300}
        ]

# Read operation
@app.route('/')
def get_transactions():
    return render_template("transactions.html", transactions=transactions)

# Create operation
@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'GET':
        return render_template("form.html")
    elif request.method == 'POST':
        new_transaction_id = len(transactions)+1
        new_transaction_date = request.form.get('date')
        new_transaction_amount = float(request.form.get('amount'))
        new_transaction = {
        'id': new_transaction_id, 
        'date': new_transaction_date, 
        'amount': new_transaction_amount
        }
        transactions.append(new_transaction)
        return redirect(url_for('get_transactions'))
    else:
        return {"message": "Bad request"}, 500

# Update operation
@app.route('/edit/<int:transaction_id>', methods=['GET', 'POST'])
def edit_transaction(transaction_id):
    if request.method == 'GET':
        return render_template("edit.html", transaction=transactions[transaction_id-1])
    elif request.method == 'POST':
        curr_transaction_index = transaction_id-1
        new_transaction_date = request.form.get('date')
        new_transaction_amount = float(request.form.get('amount'))
        new_transaction = {
        'id': transaction_id, 
        'date': new_transaction_date, 
        'amount': new_transaction_amount
        }
        transactions[curr_transaction_index] = new_transaction
        return redirect(url_for('get_transactions'))
    else:
        return {"message": "Bad request"}, 500
        
    
# Delete operation
@app.route('/delete/<int:transaction_id>')
def delete_transaction(transaction_id):
    curr_transaction_index = transaction_id-1
    del transactions[curr_transaction_index]
    for id, transaction in enumerate(transactions):
        transactions[id]['id'] = id+1
    return redirect(url_for('get_transactions'))

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
