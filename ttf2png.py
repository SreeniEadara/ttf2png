#!/usr/bin/env python
import sys
import os
import subprocess

from fontTools.ttLib import TTFont

def dump_png(font_path: str, font_size: int, text_path: str, image_path: str):
    ttf = TTFont(font_path, 0, verbose=0, allowVID=0, ignoreDecompileErrors=True, fontNumber=-1)
    for x in ttf["cmap"].tables:
        for y in x.cmap.items():
            char_unicode = chr(y[0])
            char_utf8 = char_unicode.encode('utf_8')
            char_name = y[1]
            f = open(os.path.join(text_path, char_name + '.txt'), 'w')
            f.write(char_utf8)
            f.close()
    ttf.close()
    subprocess.call(["convert", "-font", font_path, "-pointsize", font_size, "-background", "rgba(0,0,0,0)", "label:@" + text_path, image_path])

