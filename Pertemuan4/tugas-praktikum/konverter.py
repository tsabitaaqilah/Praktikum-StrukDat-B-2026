from kurs import data_kurs

def konversi_ke_idr(jumlah, kode_mata_uang):
    if kode_mata_uang == "IDR":
        return jumlah
    return jumlah * data_kurs[kode_mata_uang]

def konversi_dari_idr(jumlah_idr, kode_tujuan):
    if kode_tujuan == "IDR":
        return jumlah_idr
    return jumlah_idr / data_kurs[kode_tujuan]