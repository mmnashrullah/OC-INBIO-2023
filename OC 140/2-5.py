# hapus folder secara aman
from send2trash import send2trash

namaFolder = r"Folder Baru"

try:
    send2trash(namaFolder)
except BaseException as be:
    print("Ada error saat menghapus folder", be)
else:
    print("Folder", namaFolder , "berhasil dihapus!")