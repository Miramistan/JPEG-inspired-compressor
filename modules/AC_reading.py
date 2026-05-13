import numpy as np


def AC_reading(file_path: str, diction: dict, start_point: int, bit_start: int):

    with open(file_path, 'rb+') as file:
        file.seek(start_point)

        data = file.read(5)
        stringed = ''
        #print(data)

        bit_index = bit_start
        end_flag = False

        for byte_index in range(5):

            while bit_index > 0:
                bit = 1 if data[byte_index] & (bit_index) else 0

                bit_index //= 2

                stringed += str(bit)

                if stringed in diction.keys():
                    nulls, category = diction[stringed]
                    #print(stringed, diction[stringed], end=' ')
                    
                    end_flag = True
                    break
                
            if end_flag:
                break
            
            bit_index = 2**7

        bit_start_shift = np.log2(bit_start) if bit_start >= 1 else 0
        place = start_point + int((len(stringed) + 7 - bit_start_shift) / 8)
        
        file.seek(place)

        length_number = int(category / 8) + 2

        #print(len(stringed), length_number)

        data = file.read(length_number)

        #print(data)

        stringed = ''

        if bit_index < 1:
            bit_index = 128

        #bit_index //= 2

        #print(int(len(stringed) / 8), length_number, bit_index)

        counter = 0
        end_flag = False
        byte_place, bit_place = 0, bit_index

        if category > 0:
            for byte_index in range(length_number):

                while bit_index > 0:
                    if counter >= category:
                        byte_place, bit_place = byte_index, bit_index
                        end_flag = True
                        break

                    #print(counter)

                    bit = 1 if data[byte_index] & (bit_index) else 0

                    bit_index //= 2
                    stringed += str(bit)
                    counter += 1
                
                if end_flag:
                    break

                bit_index = 128

            value = int(stringed, 2) if stringed[0] != '0' else \
                    int(stringed, 2) - 2**category + 1
        else:
            value = 0

        #print(stringed, nulls, value)

        place = place + byte_place
        
        return ((place, bit_place), (nulls, value))
