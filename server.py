from flask import Flask, send_from_directory, jsonify, request

app = Flask(__name__)

# Serve index.html from the root directory
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Serve static images from the 'images' folder
@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory('images', filename)

# Endpoint to handle order submissions
@app.route('/submit_order', methods=['POST'])
def submit_order():
    data = request.json
    name = data['name']                # Match this with the index.html input name
    address = data['address']          # Changed from roll_number to address
    phone = data['phone']              # Changed from department to phone
    order_summary = data['order_summary']
    total_bill = data['total_bill']

    # Prepare the message for response
    message = f"Order received from {name} at {address}, Phone: {phone}.<br>" \
              f"Order Summary:<br>{order_summary}Total Bill: Rs {total_bill}."

    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run the server on all interfaces, port 5000
