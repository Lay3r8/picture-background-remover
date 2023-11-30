#!/home/simon/.pyenv/versions/picture-background-remover/bin/python
"""
usage: main.py [-h] image_path

Remove background from image

positional arguments:
  image_path  Path of the image to use as source

options:
  -h, --help  show this help message and exit
"""
from argparse import ArgumentParser, Namespace as ArgsNamespace
from datetime import datetime
from pathlib import Path
from rembg import remove
from PIL import Image


def get_timestamp() -> str:
    """Returns a ISO 8601 timestamp with locale TZ info"""
    return datetime.now().astimezone().replace(microsecond=0).isoformat()


def parse_script_args() -> ArgsNamespace:
    """Parse the script arguments"""
    parser = ArgumentParser(description="Remove background from image")
    parser.add_argument("image_path", type=Path, help="Path of the image to use as source", default=False)
    script_args = parser.parse_args()
    return script_args


def main():
    """Main"""
    args = parse_script_args()
    img_path = args.image_path
    print(f"Processing image: {img_path}")
    img = Image.open(img_path)
    output = remove(img)
    output_path = Path(f"output-{img_path.stem}-{get_timestamp()}.png")
    print(f"Saving output to: {output_path.absolute()}")
    output.save(output_path, "PNG")


if __name__ == '__main__':
    main()
