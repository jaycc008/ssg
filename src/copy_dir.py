import os
import shutil


def copy_files_recursive(src, dst):
	if not os.path.exists(dst):
		os.mkdir(dst)

	if os.path.exists(src):
		items = os.listdir(src)
		for item in items:
			src_path = os.path.join(src, item)
			dst_path = os.path.join(dst, item)
			if os.path.isfile(src_path):
				shutil.copy(src_path, dst_path)
			else:
				copy_files_recursive(src_path, dst_path)

def copy_files(src, dst):
	shutil.copytree(src, dst)
	