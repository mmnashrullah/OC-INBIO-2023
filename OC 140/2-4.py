# membuat folder

import pathlib

namaFolder = r"Folder Baru"

try:
    pathlib.Path(namaFolder).mkdir()
except BaseException as be:
    print("Ada error saat membuat folder", be)
else:
    print("Folder", namaFolder , "berhasil dibuat!")
