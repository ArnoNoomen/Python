#!/usr/bin/python3

import os
import sys
import glob
import argparse
import pathlib
from PIL import Image

def main():
    parser = argparse.ArgumentParser(description='image1')
    parser.add_argument('--dir', dest='dir', action='store', required=True)
    parser.add_argument('--pdf', dest='pdf', action='store')
    args = parser.parse_args()
    if not os.path.exists(args.dir):
        print('directory bestaat niet')
        sys.exit(1)
    if args.pdf is None:
        path1 = pathlib.PurePath(args.dir)
        filename = path1.name + '.pdf'
    else:
        filename, file_extension = os.path.splitext(args.pdf)
        if file_extension == "":
            filename = filename + '.pdf'
        else:
            filename = filename + file_extension

    files = map(os.path.basename, glob.glob(args.dir + '/*.jpg'))
    images = [
        Image.open(args.dir + "/" + f)
        for f in files
    ]
    pdf_path = args.dir + "/" + filename

    images[0].save(
        pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
    )
if __name__ == "__main__":
    main()
