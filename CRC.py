import pandas as pd
import numpy as np


def xor_operation(a, b):
    """Performs XOR on two binary strings."""
    result = ""
    for i in range(len(b)):  # XOR only on the length of the divisor (CRC bits)
        if a[i] == b[i]:
            result += "0"
        else:
            result += "1"
    return result


def crc(binary_data, crc_bits):
    # Append the appropriate number of zeros to the binary data
    augmented_data = binary_data + "0" * (len(crc_bits) - 1)
    print(f"Initial augmented data: {augmented_data}")
    
    crc_length = len(crc_bits)
    
    # Perform XOR from the left and remove leading zeros
    current_data = augmented_data[:crc_length]
    augmented_data = augmented_data[crc_length:]  # Start after the initial slice
    
    while len(current_data) >= len(crc_bits):
        print(f"\nCurrent data: {current_data}")
        if current_data[0] == '1':  # We only XOR if the first bit is 1
            # Perform XOR with the divisor (crc_bits)
            current_data = xor_operation(current_data, crc_bits)
            print(f"XOR result: {current_data}")
        else:
            # If the first bit is 0, we just shift over and continue
            # No need to XOR with zeros explicitly, just drop leading zeros
            current_data = current_data[1:]
            print(f"Shifted data (leading zero removed): {current_data}")
        
        # Remove leading zeros after XOR
        current_data = current_data.lstrip('0')
        
        # Append the next bit from augmented_data if it exists
        if len(augmented_data) > 0:
            current_data += augmented_data[0]
            augmented_data = augmented_data[1:]
    
    # The remainder is the CRC result (last bits left after division)
    crc_result = current_data.zfill(len(crc_bits) - 1)
    print(f"\nFinal CRC: {crc_result}")
    return crc_result


# Direct execution without name == main
binary_data = input("Enter the binary data: ")
crc_bits = input("Enter the CRC bits (divisor): ")
crc(binary_data, crc_bits)




#1101011011
#1011