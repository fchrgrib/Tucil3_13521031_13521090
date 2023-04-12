# Tucil3_13521031_13521090
> Tugas Kecil Strategi Algoritma ke-3 adalah praktek implementasi algoritma UCS dan A* pada pencarian jalan terdekat dalam suatu graf.

## Struktur Folder
- `src` berisi sourcecode program.
- `test` berisi input testing untuk program.
- `doc` berisi laporan dengan format pdf.

## Program Environment
- Visual Studio Code
- Python 3.10.11
- Flask beserta dependencies-nya
- Google Chrome Web Browser
- JS Google Map API (https://maps.googleapis.com/maps/api/js)

## Cara Setup Enviroment dan Menjalankan Program
1. Change Directory ke `../Tucil_13521031_13521090/src`
2. jalankan perintah `python3 -m venv venv`
3. jalankan perintah `venv\Scripts\activate`
4. jalankan perintah `pip install flask`
5. jalankan perintah `python app.py` pada venv yang telah dijalankan pada perintah sebelumnya
6. ctrl+click link yang tertera pada terminal atau buka `http://127.0.0.1:5000` pada web browser
7. jika ingin mengubah port yang digunakan pergi ke `src/app.py` kemudian tambahkan `port=[port]` pada app.run(), lalu ubah API key pada `src/templates/index.html` menjadi API key yang dapat memberi akses pada port tersebut, kemudian lakukan tahap sebelumnya.

## Cara Menggunakan
1. Ketik lokasi pada searchbar diatas map, lalu tekan 'Go'
2. Doubleclick pada ujung jalan atau persimpangan jalan untuk menambah simpul
2. Klik kanan pada simpul untuk menghapus simpul tersebut
3. Klik 2 simpul untuk menambah garis ketetanggaan
4. klik 2 simpul yang sudah memiliki garis untuk menghapus garis ketetanggaan
5. Hover pada simpul untuk melihat ID simpul dan masukkan pada origin dan destination untuk memulai pencarian
6. Pilih UCS atau A* sebagai algoritma pencarian
7. tekan 'Find Path' untuk mencari jalan terdekat
8. jika ingin melakukan pencarian terhadap data yang telah ada, anda dapat memasukkan file.txt dengan format pada tautan yang tertera pada program dengan cara 'drag and drop' pada kotak yang telah tersedia
9. pastikan untuk mencentang checkbox 'File input calculation' bila menggunakan file

## Identitas Pembuat
naninani - 13521031 - K3
Tobias Natalio Sianipar - 13521090 - K2
