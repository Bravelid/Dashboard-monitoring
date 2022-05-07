def ekstrak():
    """
tanggal  :07 Mei 2022
waktu : 00:21:45 WIB
magnitudo :3.6
kedalaman : 10 km
lokasi : 8.16 LS - 113.10 BT
Pusat gempa berada :  di darat 14 km barat daya Lumajang
Dirasakan (Skala MMI) : III-IV Pasirian, III-IV Pronojiwo, III-IV Sendupuro, III-IV Candipuro, III-IV Pasrujambe
    :return:
    """
    hasil = dict()
    hasil["tanggal"] = "07 Mei 2022"
    hasil["waktu"] = "00:21:45 WIB"
    hasil["magnitudo"] = 3.6
    hasil["kedalaman"] = "10 km"
    hasil["lokasi"] = {"LS": 8.16, "bt": 113.10}
    hasil["pusatgempa"] = "di darat 14 km barat daya Lumajang"
    hasil["dirasakan"] = "III-IV Pasirian, III-IV Pronojiwo, III-IV Sendupuro, III-IV Candipuro, III-IV Pasrujambe"
    return hasil


def tampilkandata(hasil):
    print("INGFO MASSEH")
    print(f"tanggal = {hasil['tanggal']}")
    print(f"waktu = {hasil['waktu']}")
    print(f"magnitudo = {hasil['magnitudo']}")
    print(f"kedalaman = {hasil['kedalaman']}")
    print(f"lokasi = {hasil['lokasi']}")
    print(f"pusat gempa = {hasil['pusatgempa']}")
    print(f"dirasakan = {hasil['dirasakan']}")


if __name__ == "__main__":
    print("ingfo diterima")
    result = ekstrak()
    tampilkandata(result)
