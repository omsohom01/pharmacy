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

    # Print the submitted details to the console
    print(f"Received Order Details:")
    print(f"Name: {name}")
    print(f"Address: {address}")        # Updated to match the input field
    print(f"Phone: {phone}")            # Updated to match the input field
    print(f"Order Summary: {order_summary}")
    print(f"Total Bill: Rs {total_bill}")

    # Response message to be sent back to the client
    response_message = (
        f"Order Summary:<br>{order_summary}<br>"
        f"Total Bill: Rs {total_bill}<br>"
        f"Customer Name: {name}<br>"
        f"Address: {address}<br>"         # Updated to match the input field
        f"Phone No: {phone}"              # Updated to match the input field
    )

    return jsonify({"message": response_message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
