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

def main():
    onetoten = [1,2,3,4,5,6,7,8,9,10]
    test(onetoten, "ONETOTEN")

    
main()



