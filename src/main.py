import os
import shutil
import sys
from copy_dir import copy_files
from generate_html import generate_pages_recursive


def main():
	if len(sys.argv) > 1:
		basepath = sys.argv[1]
	else:
		basepath = "/"
	
	src = "static"
	dst = "docs"
	content = "content"


	if os.path.exists(dst):
		shutil.rmtree(dst)

	copy_files(src, dst)

	generate_pages_recursive(content, "template.html", dst, basepath)


main()