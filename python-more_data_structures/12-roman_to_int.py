#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dig = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M":1000}
    int_val = 0
    fin_val = 0
    for rom_val in roman_string:
        init_rom = roman_dig[rom_val]

        if init_rom >= fin_val:
            int_val += init_rom
            fin_val = init_rom
        else:
            int_val -= init_rom
            
    return int_val
