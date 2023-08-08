# Max Peng 2023
# Delta Encoding
# Encoder Minnow

import time

def encode(data):
    encoded = [data[0]]
    for i in range(1,len(data)):
         delta = data[i] - data[i-1]
         encoded.append(delta)
    return encoded

def decode(data):
    decoded = [data[0]]
    for i in range(1,len(data)):
         delta = data[i] + decoded[i-1]
         decoded.append(delta)
    return decoded 



def test(data, code):
    print(" /--------------------/ TESTING " + code + "/--------------------/")

    print("PLAIN: " , *data)
    print("------------------ ENCODED: ")
    encode_start_time = time.time()
    encoded_data = encode(data)
    encode_end_time = time.time()
    encode_time_elapsed = encode_end_time - encode_start_time
    print("Encoded in " , encode_time_elapsed , " seconds.")
    print("Encoded data: " , *encoded_data)
    print("------------------ ENCODED FINISHED")


    print("------------------ DECODED: ")
    decode_start_time = time.time()
    decoded_data = decode(encoded_data)
    decode_end_time = time.time()
    decode_time_elapsed = decode_end_time - decode_start_time
    print("Decoded in " , decode_time_elapsed , " seconds.")
    print("Decoded data: " , *decoded_data)
    print("------------------ DECODED FINISHED")

    print(" /--------------------/ FINISHED TESTING " + code + "/--------------------/")

def main():
    onetoten = [1,2,3,4,5,6,7,8,9,10]
    test(onetoten, "ONETOTEN")

    random = [6,84,3,5,8,4,7,3,6,13]
    test(random, "RANDOM")

   
main()



