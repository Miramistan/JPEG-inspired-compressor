def get_AC_luminance_chrominance(file_path: str, number: int):

    AC_runSizes = []
    AC_codeWords = []
    AC_codes_dict = {}

    transform_dict = {'0': 0,
                      '1': 1,
                      '2': 2,
                      '3': 3,
                      '4': 4,
                      '5': 5,
                      '6': 6,
                      '7': 7,
                      '8': 8,
                      '9': 9,
                      'A': 10,
                      'B': 11,
                      'C': 12,
                      'D': 13,
                      'E': 14,
                      'F': 15}

    with open(file_path, 'r') as file:
        for runSize_index in range(number):
            runSize = [transform_dict[x.rstrip()] for x in file.readline().split('/')]
            runSize = (runSize[0], runSize[1])
            AC_runSizes.append(runSize)

        for codeWord_index in range(number):
            codeWord = file.readline().rstrip()
            AC_codeWords.append(codeWord)
        
    for AC_code_index in range(number):
        AC_codes_dict[AC_runSizes[AC_code_index]] = AC_codeWords[AC_code_index]

    return AC_codes_dict
