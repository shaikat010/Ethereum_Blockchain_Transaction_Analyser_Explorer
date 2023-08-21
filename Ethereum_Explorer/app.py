from flask import Flask, render_template,request
from web3 import Web3


app = Flask(__name__)
w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/3beb35814f274c01996224de0c825f95"))


@app.route('/')
def index():
    latest_block_number = w3.eth.blockNumber
    connection_status = w3.isConnected()
    return render_template('index.html',block=latest_block_number, connection = connection_status)

@app.route('/process_form', methods=['POST'])
def process_form():
    input_text = request.form.get('inputField') # Get the value from the input field
    input_text = str(input_text)
    transaction = w3.eth.get_transaction(input_text)  
    # transaction = str(transaction)
    latest_block_number = w3.eth.blockNumber
    connection_status = w3.isConnected()
    # You can now process the input_text as needed, e.g., save it to a database, perform calculations, etc.
    #return "Data received and processed: " + input_text
    return render_template('index.html', input = transaction,block=latest_block_number, connection = connection_status)

if __name__ == '__main__':
    app.run(debug=True)

