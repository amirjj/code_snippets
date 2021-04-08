import shutil


def make_archive():
	shutil.make_archive('another', 'zip', 'sample_data')


def unpack_archive():
	shutil.unpack_archive('sample_data/result.zip', 'files')


if __name__ == '__main__':
	unpack_archive()