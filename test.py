# Max Peng 2023
# Delta Encoding
# Test Minnow

import time
import art
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from encoder import encode
from decoder import decode
from trendsEndpoint import getRandomTopCompanyTrends

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

def graph(data):
    columnName = data.columns[0]
    timeseries = data[columnName].tolist()
    print(timeseries)
    data.plot(y=columnName)
    plt.title('Weekly Google Searches')
    plt.xlabel('Date')
    plt.ylabel('Search Interest')
    plt.show()

def main():
    lifecycle = True
    while(lifecycle):
        print("Delta Encoder Minnow")
        print("Max Peng 2023")
        print()

        useCode = ''
        while(not(useCode == 'Y' or useCode == 'N')):   
            useCode = input("Custom Code? [Y/N]")

        if (useCode == 'N'):
            data = getRandomTopCompanyTrends()
            graph(data)
        elif(useCode == 'Y'):
            code = input("What code would you like to use?")
            match code:
                case "ONETOTEN":
                    onetoten = [1,2,3,4,5,6,7,8,9,10]
                    test(onetoten, "ONETOTEN")
                case "RANDOM":
                    random = [6,84,3,5,8,4,7,3,6,13]
                    test(random, "RANDOM")

        lifecycle = input("Again? [Y/N]") == 'Y'
    print("Program exited.")


main()



