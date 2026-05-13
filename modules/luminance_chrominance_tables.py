from .get_luminance_chrominance import get_AC_luminance_chrominance

DC_luminance_table = {0: '00',
                      1: '010',
                      2: '011',
                      3: '100',
                      4: '101',
                      5: '110',
                      6: '1110',
                      7: '11110',
                      8: '111110',
                      9: '1111110',
                      10: '11111110',
                      11: '111111110'}

DC_chrominance_table = {0: '00',
                        1: '01',
                        2: '10',
                        3: '110',
                        4: '1110',
                        5: '11110',
                        6: '111110',
                        7: '1111110',
                        8: '11111110',
                        9: '111111110',
                        10: '1111111110',
                        11: '11111111110'}


AC_chrominance_table = get_AC_luminance_chrominance('chrominance AC.txt', 162)
AC_luminance_table = get_AC_luminance_chrominance('luminance AC.txt', 162)
