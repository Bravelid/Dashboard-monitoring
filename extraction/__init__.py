from bs4 import BeautifulSoup
import requests



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
    try :
        content = requests.get("https://www.bmkg.go.id")
    except Exception :
        return None
    if content.status_code == 200 :
        print(content.text)
        hasil = dict()
        hasil["tanggal"] = "07 Mei 2022"
        hasil["waktu"] = "00:21:45 WIB"
        hasil["magnitudo"] = 3.6
        hasil["kedalaman"] = "10 km"
        hasil["lokasi"] = {"LS": 8.16, "bt": 113.10}
        hasil["pusatgempa"] = "di darat 14 km barat daya Lumajang"
        hasil["dirasakan"] = "III-IV Pasirian, III-IV Pronojiwo, III-IV Sendupuro, III-IV Candipuro, III-IV Pasrujambe"
        return hasil
    else:
        return None


def tampilkandata(result):
    if result is None :
         print("Tidak ada data Gempa")
         return
    print(f"tanggal = {result['tanggal']}")
    print(f"waktu = {result['waktu']}")
    print(f"magnitudo = {result['magnitudo']}")
    print(f"kedalaman = {result['kedalaman']}")
    print(f"lokasi = {result['lokasi']}")
    print(f"pusat gempa = {result['pusatgempa']}")
    print(f"dirasakan = {result['dirasakan']}")

