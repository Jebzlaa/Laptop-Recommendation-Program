import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyCgQ0g-jdQFVuX12GUnJaw4ke4wKhfiO6k"

# Database Laptop Lengkap 0-30 Juta
LAPTOPS = [
    # 🔥 BUDGET 3-5 JUTAAN (Entry Level)
    {
        "nama": "TECNO MegaBook S1",
        "harga": "Rp 4,500,000",
        "spek": "Intel Core i3 | 8GB | 256GB SSD",
        "keterangan": "Spek lumayan untuk harga murah, cocok coding dasar",
        "kategori": ["coding", "kuliah", "budget"]
    },
    {
        "nama": "ASUS Vivobook 15 A1502VA", 
        "harga": "Rp 4,999,000",
        "spek": "Intel Core i3 | 4GB | 512GB SSD",
        "keterangan": "SSD besar, perlu upgrade RAM untuk coding",
        "kategori": ["kuliah", "budget", "upgradeable"]
    },
    {
        "nama": "Acer Extensa 15",
        "harga": "Rp 3,999,000",
        "spek": "Intel Celeron | 4GB | 256GB SSD", 
        "keterangan": "Sangat murah, hanya untuk tugas ringan",
        "kategori": ["browsing", "sekolah", "budget"]
    },

    # 💰 BUDGET 5-7 JUTAAN (Best Budget)
    {
        "nama": "ASUS Vivobook Go 14",
        "harga": "Rp 5,999,000", 
        "spek": "AMD Ryzen 5 | 8GB | 512GB SSD",
        "keterangan": "Performance terbaik di kelas 6 jutaan",
        "kategori": ["coding", "kuliah", "kerja", "best-budget"]
    },
    {
        "nama": "Lenovo IdeaPad 3 14",
        "harga": "Rp 5,500,000",
        "spek": "Intel Core i3 | 8GB | 512GB SSD",
        "keterangan": "Harga terjangkau, spek seimbang untuk coding",
        "kategori": ["coding", "kuliah", "kerja"]
    },
    {
        "nama": "HP Laptop 15s", 
        "harga": "Rp 5,800,000",
        "spek": "Intel Core i3 | 8GB | 512GB SSD",
        "keterangan": "Build quality bagus, layar lega 15 inci",
        "kategori": ["kuliah", "kerja", "entertainment"]
    },

    # ⚡ BUDGET 7-10 JUTAAN (Mid-Range)
    {
        "nama": "ASUS Vivobook 15",
        "harga": "Rp 8,000,000", 
        "spek": "Intel i5 | 8GB | 512GB SSD",
        "keterangan": "All-rounder terbaik untuk mahasiswa & pekerja",
        "kategori": ["coding", "kuliah", "kerja", "all-rounder"]
    },
    {
        "nama": "Acer Aspire 5", 
        "harga": "Rp 8,500,000",
        "spek": "AMD Ryzen 5 | 8GB | 512GB SSD",
        "keterangan": "Performance tangguh untuk coding & multitasking", 
        "kategori": ["coding", "kerja", "multitasking"]
    },
    {
        "nama": "Lenovo IdeaPad 3",
        "harga": "Rp 7,500,000",
        "spek": "Intel i3 | 8GB | 256GB SSD", 
        "keterangan": "Hemat dengan performa cukup untuk development",
        "kategori": ["coding", "kuliah", "budget"]
    },
    {
        "nama": "Dell Inspiron 15",
        "harga": "Rp 9,500,000",
        "spek": "Intel i5 | 16GB | 512GB SSD",
        "keterangan": "RAM 16GB, cocok untuk virtual machine & coding berat",
        "kategori": ["coding", "vm", "multitasking"]
    },

    # 🚀 BUDGET 10-15 JUTAAN (High Mid-Range)
    {
        "nama": "Lenovo ThinkPad E14",
        "harga": "Rp 12,500,000",
        "spek": "Intel i5 | 16GB | 512GB SSD", 
        "keterangan": "Keyboard legendaris, tangguh, cocok untuk programmer",
        "kategori": ["coding", "programming", "professional"]
    },
    {
        "nama": "HP Pavilion 15",
        "harga": "Rp 11,000,000",
        "spek": "AMD Ryzen 7 | 16GB | 512GB SSD",
        "keterangan": "Performance tinggi untuk development & desain",
        "kategori": ["coding", "desain", "multitasking"]
    },
    {
        "nama": "ASUS Zenbook 14",
        "harga": "Rp 13,500,000", 
        "spek": "Intel i7 | 16GB | 1TB SSD",
        "keterangan": "Premium ultrabook, ringan dan powerful",
        "kategori": ["coding", "premium", "portable"]
    },

    # 💎 BUDGET 15-20 JUTAAN (Premium)
    {
        "nama": "Apple MacBook Air M1",
        "harga": "Rp 15,000,000",
        "spek": "Apple M1 | 8GB | 256GB SSD",
        "keterangan": "Efisien, cocok untuk iOS development & creative work",
        "kategori": ["coding", "desain", "ios-dev", "premium"] 
    },
    {
        "nama": "Dell XPS 13",
        "harga": "Rp 18,500,000", 
        "spek": "Intel i7 | 16GB | 512GB SSD",
        "keterangan": "Design premium, performance excellent untuk programmer",
        "kategori": ["coding", "programming", "premium"]
    },
    {
        "nama": "Lenovo ThinkPad T14",
        "harga": "Rp 17,000,000",
        "spek": "Intel i7 | 16GB | 1TB SSD",
        "keterangan": "Laptop legenda untuk professional & hardcore coding",
        "kategori": ["coding", "professional", "business"]
    },

    # 🏆 BUDGET 20-30 JUTAAN (Flagship)
    {
        "nama": "Apple MacBook Pro 14 M3", 
        "harga": "Rp 25,000,000",
        "spek": "Apple M3 | 16GB | 512GB SSD", 
        "keterangan": "Performance monster untuk professional developer",
        "kategori": ["coding", "desain", "video-editing", "flagship"]
    },
    {
        "nama": "Dell XPS 15",
        "harga": "Rp 22,000,000",
        "spek": "Intel i9 | 32GB | 1TB SSD", 
        "keterangan": "Workstation portable, bisa handle apapun",
        "kategori": ["coding", "ai-development", "3d-rendering", "flagship"]
    },
    {
        "nama": "ASUS ROG Zephyrus",
        "harga": "Rp 28,000,000",
        "spek": "AMD Ryzen 9 | 32GB | 2TB SSD | RTX 4060",
        "keterangan": "Gaming + Development, untuk game dev & AI research",
        "kategori": ["coding", "gaming", "ai", "game-dev", "flagship"]
    },
    {
        "nama": "Framework Laptop 16",
        "harga": "Rp 26,500,000", 
        "spek": "AMD Ryzen 7 | 32GB | 1TB SSD",
        "keterangan": "Modular, bisa di-upgrade semuanya, future-proof",
        "kategori": ["coding", "upgradeable", "future-proof", "flagship"]
    },
    {
        "nama": "Lenovo ThinkPad X1 Carbon",
        "harga": "Rp 24,000,000",
        "spek": "Intel i7 | 32GB | 1TB SSD",
        "keterangan": "Business flagship terbaik, ultra portable & powerful",
        "kategori": ["coding", "business", "professional", "flagship"]
    }
]