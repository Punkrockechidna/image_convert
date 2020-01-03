import sys
from pathlib import Path
from PIL import Image

# grab first arguement and second (folders)
# jpg_folder = sys.argv[1]
# png_folder = sys.argv[2]
# print(jpg_folder)
# print(png_folder)
jpg_folder = 'pokedex'
png_folder = 'converted'


# check if second exists, create if not
def find_folder(folder):
    # print(folder)
    folder_path = Path(folder)
    # print(folder_path)
    if folder_path.is_dir():
        return True
    else:
        Path(f'{folder}').mkdir(parents=True, exist_ok=True)


print(find_folder(png_folder))
# loop through pokedex and convert all to png
def loop_folder_jpgs:
    
# save to new folder
