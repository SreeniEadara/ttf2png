#!/usr/bin/env python
import sys
import os
import subprocess

from fontTools.ttLib import TTFont

def dump_png(char: str, font_path: str, point_size: int, text_path: str, image_path: str):
    ttf = TTFont(font_path, 0, verbose=0, allowVID=0, ignoreDecompileErrors=True, fontNumber=-1)
    char_found = False
    for x in ttf["cmap"].tables:
        for y in x.cmap.items():
            char_unicode = chr(y[0])
            if char_unicode != char:
                continue
            else:
                char_found = True
            char_utf8 = char_unicode.encode('utf_8')
            f = open(text_path, 'bw')
            f.write(char_utf8)
            f.close()
    ttf.close()
    if not char_found:
        raise RuntimeError(f'Character {char} not in TTF {font_path}')
    subprocess.call(["convert", "-font", font_path, "-pointsize", str(point_size), "-background", "rgba(0,0,0,0)", "label:@" + text_path, image_path])
