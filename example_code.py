import zmq

# set up zeroMQ, set up a socket for requests.
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect('tcp://localhost:5558')

# example data
data = """
Bella|Dog|Poodle|3|12|Healthy|Sedentary|Dry Food, 2 cups BID
Meow|Cat|Siamese|2|9|Healthy|Moderately Active|Wet Food, 1 can BID
"""

# send data
socket.send_string(data.strip())

# response
response = socket.recv_string()
print(f"Response: {response}")