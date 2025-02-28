import os
import shutil
from copy_dir import copy_files
from generate_html import generate_page, generate_pages_recursive


def main():
	src = "static"
	dst = "public"

	if os.path.exists(dst):
		shutil.rmtree(dst)

	copy_files(src, dst)

	generate_pages_recursive("content", "template.html", dst)


main()