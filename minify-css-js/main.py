import argparse
import os
import pathlib
import csscompressor
from jsmin import jsmin

parser = argparse.ArgumentParser(description='Process files in a directory.')
parser.add_argument('dir_path', help='Path to the directory to process')

args = parser.parse_args()

for root, dirs, files in os.walk(args.dir_path):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        file_type = pathlib.Path(file_path).suffix[1:]

        if file_type == 'css':
            # Process CSS file
            with open(file_path, 'r') as f:
                css_content = f.read()
            minified_css = csscompressor.compress(css_content)

            with open(os.path.join(root, file_name), 'w') as f:
                f.write(minified_css)

        elif file_type == 'js':
            # Process JS file
            with open(file_path, 'r') as f:
                js_content = f.read()
            minified_js = jsmin(js_content.strip())

            with open(os.path.join(root, file_name), 'w') as f:
                f.write(minified_js)
