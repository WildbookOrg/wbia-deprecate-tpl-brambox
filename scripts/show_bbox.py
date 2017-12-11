#!python

import os
import cv2
import argparse
import brambox.boxes as bbb


def main():
    parser = argparse.ArgumentParser(description='Render bounding boxes on images')
    parser.add_argument('format', choices=bbb.formats.keys(), help='Annotation format')
    parser.add_argument('file', help='Bounding box file, folder or file sequence [path/to/boxes/I%%08d.txt]')
    parser.add_argument('imagefolder', help='Image folder')
    parser.add_argument('--show-labels', action='store_true', help='Show labels next to bounding boxes')
    parser.add_argument('--stride', type=int, default=1, help='Only show every N\'th image')
    parser.add_argument('--offset', type=int, default=0, help='Start with an offset, may be negative')
    parser.add_argument('--class-names', default=None, help="Class label file for annotation formats using indexes rather than class names")

    args = parser.parse_args()

    class_names = None
    if args.class_names is not None:
        class_names = []
        with open(args.class_names) as f:
            class_names = f.read().splitlines()

    # find out image w/h and extension based on one image of the folder
    files = list(bbb.expand(args.imagefolder))
    firstimage = files[0]
    extension = os.path.splitext(firstimage)[1]
    img = cv2.imread(firstimage)

    boxes = bbb.parse(args.format, args.annofile,
                      image_width=img.shape[1],
                      image_height=img.shape[0],
                      class_label_map=args.class_names,
                      stride=args.stride, offset=args.offset)

    print(f'Parsed {len(annotations)} annotation files')
    bbb.show_bounding_boxes(boxes, args.imagefolder, img_ext=extension, show_labels=args.show_labels)

if __name__ == '__main__':
    main()
