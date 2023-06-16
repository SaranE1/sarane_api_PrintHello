from flask import Flask

# Create the Flask app
app = Flask(__name__)

# Define the API endpoint
@app.route('/api/printHello', methods=['GET'])
def print_hello():
    return 'Hello'

# Run the Flask app 
if __name__ == '__main__':
    app.run()
