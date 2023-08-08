# Max Peng 2023
# Delta Encoding
# Decoder Minnow

def decode(data):
    decoded = [data[0]]
    for i in range(1,len(data)):
         delta = data[i] + decoded[i-1]
         decoded.append(delta)
    return decoded 

