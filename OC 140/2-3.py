# hapus file secara aman
from send2trash import send2trash

namaFile = "test1.txt"

try:
    send2trash(namaFile)
except BaseException as be:
    print("Ada error saat menghapus file", be)
else:
    print("File", namaFile , "berhasil dihapus!")