import zmq

# set up zeroMQ, create a socket to receive requests.
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind('tcp://*:5558')

# indicate the server is listening
print("Txt File Server is Listening....")

while True:
    # receive string from client
    message = socket.recv_string()
    print(f"Received Data: {message}")

    # split into each pet record
    pets = message.split("\n")

    # open a txt file and save the data with labels
    with open("pet_data.txt", "w") as file:
        # go over each pet logged
        for pet in pets:
            # each element is split using "|"
            data = pet.split("|")
            # format the data
            file.write(f"Pet Name: {data[0]}\n")
            file.write(f"Species: {data[1]}\n")
            file.write(f"Breed: {data[2]}\n")
            file.write(f"Age (years): {data[3]}\n")
            file.write(f"Weight (lbs): {data[4]}\n")
            file.write(f"Health Details: {data[5]}\n")
            file.write(f"Activity Details: {data[6]}\n")
            file.write(f"Feeding Details: {data[7]}\n")
            file.write("\n")

    # print that the file was created
    print("txt file created")
    socket.send_string("Txt file created")

    # indicate the server is listening
    print("Txt File Server is Listening....")
