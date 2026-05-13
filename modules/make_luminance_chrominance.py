from .luminance_chrominance_tables import AC_luminance_table, AC_chrominance_table, \
                                         DC_luminance_table, DC_chrominance_table


def make_AC_luminance(AC):
    return (AC_luminance_table[(AC[0], AC[1])], AC[2])


def make_AC_chrominance(AC):
    return (AC_chrominance_table[(AC[0], AC[1])], AC[2])


def make_DC_luminance(DC):
    return (DC_luminance_table[DC[0]], DC[1])


def make_DC_chrominance(DC):
    return (DC_chrominance_table[DC[0]], DC[1])