import os
import shutil
from copy_dir import copy_files
from utils import extract_title


def main():
	src = "static"
	dst = "public"

	if os.path.exists(dst):
		shutil.rmtree(dst)

	copy_files(src, dst)


main()