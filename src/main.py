import os


def main():
	src = "static"
	copy_dir(src, "")

def copy_dir(src, dst):
	if os.path.exists(src):
		print(os.listdir(src))		


main()