from config import LAPTOPS

def tampilkan_semua_laptop():
    print("\n" + "="*50)
    print("📋 DAFTAR SEMUA LAPTOP")
    print("="*50)
    for laptop in LAPTOPS:
        print(f"\n🔹 {laptop['nama']}")
        print(f"   💰 {laptop['harga']}")
        print(f"   ⚙️  {laptop['spek']}")
        print(f"   📝 {laptop['keterangan']}")
    print("="*50)

def cari_berdasarkan_budget():
    print("\n💵 CARI BERDASARKAN BUDGET")
    try:
        budget = int(input("Masukkan budget maksimal (contoh: 8000000): "))
        print(f"\n🔍 Hasil pencarian untuk budget Rp {budget:,}:")
        
        found = False
        for laptop in LAPTOPS:
            harga_angka = int(laptop['harga'].replace("Rp ", "").replace(",", ""))
            if harga_angka <= budget:
                print(f"\n🔹 {laptop['nama']}")
                print(f"   💰 {laptop['harga']}")
                print(f"   ⚙️  {laptop['spek']}")
                found = True
        
        if not found:
            print("❌ Tidak ada laptop yang sesuai budget.")
            
    except ValueError:
        print("❌ Masukkan angka yang valid!")

def tampilkan_menu():
    print("\n" + "="*50)
    print("🛒 AI LAPTOP ADVISOR")
    print("="*50)
    print("1. Lihat Semua Laptop")
    print("2. Cari Berdasarkan Budget")
    print("3. Konsultasi dengan AI")
    print("4. Keluar")
    print("="*50)