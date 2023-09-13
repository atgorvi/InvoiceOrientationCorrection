import argparse

import cv2

from src.orientation_correction import correct_orientation
from src.utils import save_from_numpy

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-img", "--image_path", type=str, help="Path to the image.", required=True
    )
    parser.add_argument(
        "-s", "--save_path", type=str, help="Save correction result", required=False, default="correction_result.png"
    )

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    image = cv2.imread(args.image_path)
    correction_angle, corrected_image = correct_orientation(image)
    if args.save_path:
        save_from_numpy(args.save_path, corrected_image)
