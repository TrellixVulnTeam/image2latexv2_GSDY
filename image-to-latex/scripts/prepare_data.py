
import sys
import os
sys.path.append(os.path.abspath('./'))#包所在的根目录

import os
import subprocess
from pathlib import Path
from tqdm import tqdm

import image_to_latex.data.utils as utils


METADATA = {
    "im2latex_formulas.norm.lst": "http://lstm.seas.harvard.edu/latex/data/im2latex_formulas.norm.lst",
    "im2latex_validate_filter.lst": "http://lstm.seas.harvard.edu/latex/data/im2latex_validate_filter.lst",
    "im2latex_train_filter.lst": "http://lstm.seas.harvard.edu/latex/data/im2latex_train_filter.lst",
    "im2latex_test_filter.lst": "http://lstm.seas.harvard.edu/latex/data/im2latex_test_filter.lst",
    "formula_images.tar.gz": "http://lstm.seas.harvard.edu/latex/data/formula_images.tar.gz",
}
# PROJECT_DIRNAME = Path(__file__).resolve().parents[2]
DATA_DIRNAME = Path('/data/zzengae/jwwang/final_project')
RAW_IMAGES_DIRNAME = DATA_DIRNAME / "physics_formula_images"
PROCESSED_IMAGES_DIRNAME = DATA_DIRNAME / "formula_images_processed"
VOCAB_FILE = DATA_DIRNAME  / "vocab1.json"


def main():
    # DATA_DIRNAME.mkdir(parents=True, exist_ok=True)
    # cur_dir = os.getcwd()
    # os.chdir(DATA_DIRNAME)

    # # Download images and grouth truth files
    # for filename, url in METADATA.items():
    #     if not Path(filename).is_file():
    #         utils.download_url(url, filename)

    # # # Unzip
    # if not RAW_IMAGES_DIRNAME.exists():
    #     RAW_IMAGES_DIRNAME.mkdir(parents=True, exist_ok=True)
        # utils.extract_tar_file("formula_images.tar.gz")

    # Extract regions of interest
    # print(RAW_IMAGES_DIRNAME)
    # if not PROCESSED_IMAGES_DIRNAME.exists():
    #     PROCESSED_IMAGES_DIRNAME.mkdir(parents=True, exist_ok=True)
    # print("Cropping images...")
    # a=RAW_IMAGES_DIRNAME.glob("*.png")
    # for image_filename in tqdm(a):
    #     cropped_image = utils.crop(image_filename, padding=8)
    #     if not cropped_image:
    #         continue
    #     cropped_image.save(PROCESSED_IMAGES_DIRNAME / image_filename.name)

    # Clean the ground truth file
    cleaned_file = "/data/zzengae/jwwang/final_project/physic/im2latex_formulas.norm.new.lst"
    # if not Path(cleaned_file).is_file():
    #     print("Cleaning data...")
    #     script = Path(__file__).resolve().parent / "find_and_replace.sh"
    #     subprocess.call(["sh", f"{str(script)}", "../data/math_210421/im2latex_formulas.norm.lst", cleaned_file])

    # Build vocabulary
    if not VOCAB_FILE.is_file():
        print("Building vocabulary...")
    all_formulas = utils.get_all_formulas(cleaned_file)
    # _, train_formulas = utils.get_split(all_formulas, "../data/math_210421/im2latex_train_filter.lst")
    tokenizer = utils.Tokenizer()
    tokenizer.train(all_formulas)
    # print(';aa')
    tokenizer.save(VOCAB_FILE)
    # # os.chdir(cur_dir)


if __name__ == "__main__":
    main()
