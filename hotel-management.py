from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
from customtkinter import CTkScrollableFrame
import customtkinter as ctk
import tkinter as tk

# Koneksi ke database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="perhotelan2"
)
mycursor = mydb.cursor()

# Fungsi untuk menambah data tamu
def tambah_data_tamu():
    id = entry_id.get()
    nama = entry_nama.get()
    no_hp = entry_no_hp.get()
    alamat = entry_alamat.get()

    sql = "INSERT INTO tamu (id, nama, no_hp, alamat) VALUES (%s, %s, %s, %s)"
    val = (id, nama, no_hp, alamat)

    mycursor.execute(sql, val)
    mydb.commit()

    # Mengosongkan field input setelah data ditambahkan
    entry_id.delete(0, END)
    entry_nama.delete(0, END)
    entry_no_hp.delete(0, END)
    entry_alamat.delete(0, END)
    messagebox.showinfo("Success", "data tamu berhasil ditambahkan")

# Fungsi untuk menambah data transaksi
def tambah_data_transaksi():
    id_transaksi = entry_id_transaksi.get()
    idFK = entry_idFK.get()
    no_kamarFK = entry_no_kamarFK.get()
    jumlah_hari = entry_jumlah_hari.get()

    # Mendapatkan harga_perhari dari tabel 'kamar' berdasarkan no_kamarFK
    sql = "SELECT harga_perhari FROM kamar WHERE no_kamar = %s"
    val = (no_kamarFK,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    harga_perhari = result[0] if result else 0

    total_harga = int(jumlah_hari) * harga_perhari
    jenis_pembayaran = entry_jenis_pembayaran.get()

    sql = "INSERT INTO transaksi (id_transaksi, idFk, no_kamar, jumlah_hari, total_harga, jenis_pembayaran) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (id_transaksi, idFK, no_kamarFK, jumlah_hari, total_harga, jenis_pembayaran)

    mycursor.execute(sql, val)
    mydb.commit()

    # Mengosongkan field input setelah data ditambahkan
    entry_id_transaksi.delete(0, END)
    entry_idFK.delete(0, END)
    #entry_no_kamarFK.option_clear(0, END)
    entry_jumlah_hari.delete(0, END)
    entry_jenis_pembayaran.delete(0, END)
    messagebox.showinfo("Success", "data tabu berhasil ditambahkan")


# Fungsi untuk mengubah data tamu berdasarkan ID
def ubah_data_tamu():
    id = entry_id_ubah.get()
    nama = entry_nama_ubah.get()
    no_hp = entry_no_hp_ubah.get()
    alamat = entry_alamat_ubah.get()

    sql = "UPDATE tamu SET nama = %s, no_hp = %s, alamat = %s WHERE id = %s"
    val = (nama, no_hp, alamat, id)

    mycursor.execute(sql, val)
    mydb.commit()

    # Mengosongkan field input setelah data diubah
    entry_id_ubah.delete(0, END)
    entry_nama_ubah.delete(0, END)
    entry_no_hp_ubah.delete(0, END)
    entry_alamat_ubah.delete(0, END)
    messagebox.showinfo("Success", "data tamu berhasil diubah")

# Fungsi untuk mengubah data transaksi berdasarkan ID Transaksi
def ubah_data_transaksi():
    id_transaksi = entry_id_transaksi_ubah.get()
    idFK = entry_idFK_ubah.get()
    no_kamarFK = entry_no_kamarFK_ubah.get()
    jumlah_hari = entry_jumlah_hari_ubah.get()

    # Mendapatkan harga_perhari dari tabel 'kamar' berdasarkan no_kamarFK
    sql = "SELECT harga_perhari FROM kamar WHERE no_kamar = %s"
    val = (no_kamarFK,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    harga_perhari = result[0] if result else 0

    total_harga = int(jumlah_hari) * harga_perhari
    jenis_pembayaran = entry_jenis_pembayaran_ubah.get()

    sql = "UPDATE transaksi SET idFk = %s, no_kamar = %s, jumlah_hari = %s, total_harga = %s, jenis_pembayaran = %s WHERE id_transaksi = %s"
    val = (idFK, no_kamarFK, jumlah_hari, total_harga, jenis_pembayaran, id_transaksi)

    mycursor.execute(sql, val)
    mydb.commit()

    # Mengosongkan field input setelah data diubah
    entry_id_transaksi_ubah.delete(0, END)
    entry_idFK_ubah.delete(0, END)
    # entry_no_kamarFK_ubah.delete(0, END)
    entry_jumlah_hari_ubah.delete(0, END)
    entry_jenis_pembayaran_ubah.delete(0, END)
    messagebox.showinfo("Success", "data transaksi berhasil diubah")


# Fungsi untuk menghapus data tamu berdasarkan ID
def hapus_data_tamu():
    del_tamu = messagebox.askquestion("HAPUS DATA", "Apakah kamu ingin melanjutkan?")
    if del_tamu == 'yes':
        id = entry_id_hapus.get()

        sql = "DELETE FROM tamu WHERE id = %s"
        val = (id,)

        mycursor.execute(sql, val)
        mydb.commit()

        # Mengosongkan field input setelah data dihapus
        entry_id_hapus.delete(0, END)
        messagebox.showinfo("Success", "Data tamu berhasil dihapus")
    else:
        messagebox.showinfo("Dibatalkan", "Proses dibatalkan")

# Fungsi untuk menghapus data transaksi berdasarkan ID Transaksi
def hapus_data_transaksi():
    del_transaksi = messagebox.askquestion("HAPUS DATA", "Apakah kamu ingin melanjutkan?")
    if del_transaksi == 'yes':
        
        id_transaksi = entry_id_transaksi_hapus.get()

        sql = "DELETE FROM transaksi WHERE id_transaksi = %s"
        val = (id_transaksi,)

        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("Information", "Data transaksi berhasil dihapus")

    # Mengosongkan field input setelah data dihapus
        entry_id_transaksi_hapus.delete(0, END)
    else:
        messagebox.showinfo("dibatalkan", "Proses dibatalkan")

def tampilkan_data():
    frame_scroll.clipboard_clear()  # Menghapus konten frame sebelumnya

    sql = "SELECT tamu.id,transaksi.id_transaksi,tamu.no_hp,tamu.nama,tamu.alamat,transaksi.no_kamar, kamar.tipe_kamar,transaksi.jumlah_hari,transaksi.jenis_pembayaran,transaksi.total_harga FROM tamu,kamar,transaksi WHERE tamu.id=transaksi.idFk AND transaksi.no_kamar=kamar.no_kamar "
    mycursor.execute(sql)
    result = mycursor.fetchall()
    
    # Menghapus semua widget dalam frame_scroll
    for widget in frame_scroll.winfo_children():
        widget.destroy()

    # Mendapatkan daftar nama atribut
    attribute_names = [desc[0] for desc in mycursor.description]

    # Menampilkan nama atribut
    for j, attribute_name in enumerate(attribute_names):
        Label(frame_scroll, text=attribute_name +
              "      ").grid(row=0, column=j)

    # Menampilkan data ke dalam frame scrollable
    for i, data in enumerate(result):
        for j, value in enumerate(data):
            Label(frame_scroll, text=value).grid(row=i+1, column=j)

    # Membandingkan hasil query sebelumnya dengan hasil query yang baru
    if 'previous_result' not in locals():
        previous_result = result
    elif result != previous_result:
        previous_result = result

    # Memperbarui tampilan setiap 5 detik
    root.after(5000, tampilkan_data)

# Membuat window utama
root = Tk()
root.geometry("1280x400")
frame_scroll = Frame(root)
frame_scroll.grid()
root.title("HOTEL MANAGEMENT SYSTEM")
root.resizable(False,False)

mycursor = mydb.cursor()

# def tampilkan_data():
#    # Menghapus konten frame sebelumnya

#     sql = "SELECT tamu.id,transaksi.id_transaksi,tamu.no_hp,tamu.nama,tamu.alamat,transaksi.no_kamar, kamar.tipe_kamar,transaksi.jumlah_hari,transaksi.jenis_pembayaran,transaksi.total_harga FROM tamu,kamar,transaksi WHERE tamu.id=transaksi.idFk AND transaksi.no_kamar=kamar.no_kamar "
#     mycursor.execute(sql)
#     result = mycursor.fetchall()

#     # Mendapatkan daftar nama atribut
#     attribute_names = [desc[0] for desc in mycursor.description]
    
#     new_window = tk.Toplevel(root)
#     new_window.title("Data Tamu")
        
#     # Mendapatkan ukuran jendela
#     window_width = new_window.winfo_width()
#     window_height = new_window.winfo_height()

#     # Mendapatkan ukuran layar
#     screen_width = new_window.winfo_screenwidth()
#     screen_height = new_window.winfo_screenheight()

#  # Menghitung posisi x dan y untuk jendela agar berada di tengah layar
#     position_x = int((screen_width - window_width) / 2)
#     position_y = int((screen_height - window_height) / 2)

#     # Mengatur posisi jendela
#     new_window.geometry(f"+{position_x}+{position_y}")

#     # Membuat frame scrollable di dalam jendela baru
#     frame_scroll = tk.Frame(new_window)
#     frame_scroll.pack(fill="both", expand=True)
#     frame_scroll.clipboard_clear()  

#     # Menampilkan nama atribut
#     for j, attribute_name in enumerate(attribute_names):
#         Label(frame_scroll, text=attribute_name + "      ").grid(row=0, column=j)

#     # Menampilkan data ke dalam frame scrollable
#     for i, data in enumerate(result):
#         for j, value in enumerate(data):
#             Label(frame_scroll, text=value).grid(row=i+1, column=j)


            

# Membuat menu tambah data tamu
Label(root, text="Tambah Data Tamu").grid(row=0, column=0)
Label(root, text="ID").grid(row=1, column=0)
entry_id = Entry(root)
entry_id.grid(row=1, column=1)
Label(root, text="Nama").grid(row=2, column=0)
entry_nama = Entry(root)
entry_nama.grid(row=2, column=1)
Label(root, text="No HP").grid(row=3, column=0)
entry_no_hp = Entry(root)
entry_no_hp.grid(row=3, column=1)
Label(root, text="Alamat").grid(row=4, column=0)
entry_alamat = Entry(root)
entry_alamat.grid(row=4, column=1)
Button(root, text="Tambah Data Tamu", command=tambah_data_tamu).grid(row=5, column=0, columnspan=2)

# Membuat menu tambah data transaksi
Label(root, text="Tambah Data Transaksi").grid(row=6, column=0)
Label(root, text="ID Transaksi").grid(row=7, column=0)
entry_id_transaksi = Entry(root)
entry_id_transaksi.grid(row=7, column=1)
Label(root, text="ID").grid(row=8, column=0)
entry_idFK = Entry(root)
entry_idFK.grid(row=8, column=1)
Label(root, text="No Kamar").grid(row=9, column=0)
# entry_no_kamarFK = Entry(root)
entry_no_kamarFK = ctk.CTkOptionMenu(root, dynamic_resizing=False, values= ['A01', 'A02','A03', 'B01', 'B02', 'B03','C01', 'C02', 'C03' ] )
entry_no_kamarFK.grid(row=9, column=1)

Label(root, text="Jumlah Hari").grid(row=10, column=0)
entry_jumlah_hari = Entry(root)
entry_jumlah_hari.grid(row=10, column=1)
Label(root, text="Jenis Pembayaran").grid(row=11, column=0)
entry_jenis_pembayaran = Entry(root)
entry_jenis_pembayaran.grid(row=11, column=1)
Button(root, text="Tambah Data Transaksi", command=tambah_data_transaksi).grid(row=12, column=0, columnspan=2)

# Membuat menu ubah data tamu
Label(root, text="Ubah Data Tamu").grid(row=0, column=2)
Label(root, text="ID").grid(row=1, column=2)
entry_id_ubah = Entry(root)
entry_id_ubah.grid(row=1, column=3)
Label(root, text="Nama").grid(row=2, column=2)
entry_nama_ubah = Entry(root)
entry_nama_ubah.grid(row=2, column=3)
Label(root, text="No HP").grid(row=3, column=2)
entry_no_hp_ubah = Entry(root)
entry_no_hp_ubah.grid(row=3, column=3)
Label(root, text="Alamat").grid(row=4, column=2)
entry_alamat_ubah = Entry(root)
entry_alamat_ubah.grid(row=4, column=3)
Button(root, text="Ubah Data Tamu", command=ubah_data_tamu).grid(row=5, column=2, columnspan=2)

# Membuat menu ubah data transaksi
Label(root, text="Ubah Data Transaksi").grid(row=6, column=2)
Label(root, text="ID Transaksi").grid(row=7, column=2)
entry_id_transaksi_ubah = Entry(root)
entry_id_transaksi_ubah.grid(row=7, column=3)
Label(root, text="ID").grid(row=8, column=2)
entry_idFK_ubah = Entry(root)
entry_idFK_ubah.grid(row=8, column=3)

Label(root, text="No Kamar").grid(row=9, column=2)
# entry_no_kamarFK_ubah = Entry(root)
entry_no_kamarFK_ubah = ctk.CTkOptionMenu(root, dynamic_resizing=False, values= ['A01', 'A02','A03', 'B01', 'B02', 'B03','C01', 'C02', 'C03' ] )
entry_no_kamarFK_ubah.grid(row=9, column=3)

Label(root, text="Jumlah Hari").grid(row=10, column=2)
entry_jumlah_hari_ubah = Entry(root)
entry_jumlah_hari_ubah.grid(row=10, column=3)
Label(root, text="Jenis Pembayaran").grid(row=11, column=2)
entry_jenis_pembayaran_ubah = Entry(root)
entry_jenis_pembayaran_ubah.grid(row=11, column=3)
Button(root, text="Ubah Data Transaksi", command=ubah_data_transaksi).grid(row=12, column=2, columnspan=2)

# Membuat menu hapus data tamu
Label(root, text="Hapus Data Tamu").grid(row=0, column=4)
Label(root, text="ID").grid(row=1, column=4)
entry_id_hapus = Entry(root)
entry_id_hapus.grid(row=1, column=5)
Button(root, text="Hapus Data Tamu", command=hapus_data_tamu).grid(row=2, column=4, columnspan=2)

# Membuat menu hapus data transaksi
Label(root, text="Hapus Data Transaksi").grid(row=3, column=4)
Label(root, text="ID Transaksi").grid(row=4, column=4)
entry_id_transaksi_hapus = Entry(root)
entry_id_transaksi_hapus.grid(row=4, column=5)
Button(root, text="Hapus Data Transaksi", command=hapus_data_transaksi).grid(row=5, column=4, columnspan=2)

# Membuat menu tampilkan data
Label(root, text="Data Tamu dan Transaksi").grid(row=6, column=4)
frame_scroll = CTkScrollableFrame(root, width=720)
frame_scroll.grid(row=7, column=4, rowspan=6, columnspan=2)
Button(root, text="Tampilkan Data", command=tampilkan_data).grid(row=13, column=4, columnspan=2)

root.mainloop()


