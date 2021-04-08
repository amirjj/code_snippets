import zipfile


def create_archive():
	zip = zipfile.ZipFile('sample_data/result.zip', 'w')
	zip.write('sample_data/testimg.jpg')
	zip.write('sample_data/test.txt')
	zip.close()


# With Context Manager
def create_archive_cm():
	with zipfile.ZipFile('sample_data/result.zip', 'w') as my_zip:
		my_zip.write('sample_data/testimg.jpg')
		my_zip.write('sample_data/test.txt')


# Compress
def compress_cm():
	with zipfile.ZipFile('sample_data/result.zip', 'w', compression = zipfile.ZIP_DEFLATED) as my_zip:
		my_zip.write('sample_data/testimg.jpg')
		my_zip.write('sample_data/test.txt')


def decompress_cm():
	with zipfile.ZipFile('sample_data/result.zip', 'r',) as my_zip:
		print(my_zip.namelist())
		my_zip.extractall('files')
		my_zip.extract('sample_data/test.txt')


def other_actions():
	print(zipfile.is_zipfile('sample_data/result.zip'))


if __name__ == "__main__":
	decompress_cm()

