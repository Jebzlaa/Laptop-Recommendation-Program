from ui_console import tampilkan_menu, tampilkan_semua_laptop, cari_berdasarkan_budget
from computer_ai import konsultasi_gemini

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih (1-4): ").strip()
        
        if pilihan == "1":
            tampilkan_semua_laptop()
        elif pilihan == "2":
            cari_berdasarkan_budget()
        elif pilihan == "3":
            konsultasi_gemini()
        elif pilihan == "4":
            print("👋 Terima kasih!")
            break
        else:
            print("❌ Pilihan tidak valid!")

if __name__ == "__main__":
    main()