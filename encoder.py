# Max Peng 2023
# Delta Encoding
# Encoder Minnow

def encode(data):
    encoded = [data[0]]
    for i in range(1,len(data)):
         delta = data[i] - data[i-1]
         encoded.append(delta)
    return encoded
