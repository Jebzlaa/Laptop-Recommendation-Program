import streamlit as st
import google.generativeai as genai
from config import LAPTOPS, GEMINI_API_KEY # Ambil data laptop dan API key dari config

# ==============================================================================
# KONFIGURASI DAN FUNGSI HELPER
# ==============================================================================

# Konfigurasi Halaman Streamlit
st.set_page_config(
    page_title="AI Laptop",
    page_icon="🛒",
    layout="centered",
    initial_sidebar_state="auto"
)

# Fungsi utilitas untuk memformat harga (dari UI HTML sebelumnya, sangat berguna)
def format_rupiah(number_str):
    """Mengonversi string harga menjadi format Rupiah yang rapi."""
    try:
        num = int(''.join(filter(str.isdigit, str(number_str))))
        return f"Rp {num:,.0f}".replace(",", ".")
    except:
        return number_str # Kembalikan apa adanya jika gagal

# Setup Model Gemini
# Lakukan sekali dan simpan di cache agar tidak setup berulang kali
@st.cache_resource
def setup_gemini_model():
    """Menginisialisasi dan mengembalikan model GenerativeAI."""
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-2.5-flash-preview-09-2025')
        return model
    except Exception as e:
        st.error(f"❌ Gagal menginisialisasi Gemini: {e}")
        return None

model = setup_gemini_model()

# Siapkan data laptop untuk prompt AI (cache agar cepat)
@st.cache_data
def get_laptop_data_string():
    """Mengubah list laptop menjadi string untuk prompt AI."""
    laptop_data = ""
    for laptop in LAPTOPS:
        laptop_data += f"- {laptop['nama']}: {laptop['harga']} | {laptop['spek']} | {laptop['keterangan']}\n"
    return laptop_data

# ==============================================================================
# FUNGSI UNTUK SETIAP "HALAMAN"
# ==============================================================================

def render_menu_utama():
    """Menampilkan tombol menu utama."""
    st.header("Pilih Layanan")
    
    if st.button("📋 Lihat Semua Laptop", use_container_width=True, type="primary"):
        st.session_state.view = 'semua_laptop'
        st.rerun() # Muat ulang skrip untuk pindah halaman
        
    if st.button("💵 Cari Berdasarkan Budget", use_container_width=True, type="primary"):
        st.session_state.view = 'cari_budget'
        st.rerun()
        
    if st.button("🤖 Konsultasi dengan AI", use_container_width=True, type="primary"):
        st.session_state.view = 'konsultasi_ai'
        st.rerun()

def render_semua_laptop():
    """Menampilkan daftar semua laptop."""
    st.header(f"📋 Daftar Semua Laptop ({len(LAPTOPS)})")
    
    for laptop in LAPTOPS:
        with st.expander(f"**{laptop['nama']}** - {format_rupiah(laptop['harga'])}"):
            st.markdown(f"**Spesifikasi:** {laptop['spek']}")
            st.markdown(f"**Keterangan:** {laptop['keterangan']}")
            tags = ", ".join(laptop['kategori'])
            st.markdown(f"**Kategori:** `{tags}`")
            
    if st.button("⬅️ Kembali ke Menu"):
        st.session_state.view = 'menu'
        st.rerun()

def render_cari_budget():
    """Menampilkan halaman pencarian berdasarkan budget."""
    st.header("💵 Cari Berdasarkan Budget")
    
    # Gunakan number_input untuk validasi angka yang mudah
    budget = st.number_input(
        "Masukkan budget maksimal Anda (contoh: 8000000)", 
        min_value=0, 
        step=500000, 
        format="%d"
    )
    
    if st.button("🔍 Cari Laptop"):
        if budget > 0:
            found_laptops = []
            for laptop in LAPTOPS:
                try:
                    # Bersihkan string harga dan konversi ke integer
                    harga_angka = int(laptop['harga'].replace("Rp ", "").replace(",", "").replace(".", ""))
                    if harga_angka <= budget:
                        found_laptops.append(laptop)
                except ValueError:
                    continue # Abaikan laptop dengan format harga salah
            
            st.subheader(f"🔍 Hasil untuk budget {format_rupiah(str(budget))} ({len(found_laptops)} ditemukan)")
            
            if not found_laptops:
                st.warning("❌ Tidak ada laptop yang sesuai budget.")
            else:
                for laptop in found_laptops:
                    st.markdown(f"**🔹 {laptop['nama']}** ({format_rupiah(laptop['harga'])})")
                    st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;*Spek: {laptop['spek']}*")
        else:
            st.error("Masukkan angka budget yang valid!")

    if st.button("⬅️ Kembali ke Menu"):
        st.session_state.view = 'menu'
        st.rerun()

def get_gemini_response(pertanyaan):
    """Memanggil API Gemini dengan prompt yang disiapkan."""
    if not model:
        return "❌ Model AI tidak berhasil dimuat. Silakan periksa API key dan konfigurasi."
        
    laptop_data_str = get_laptop_data_string()
    
    # Ini adalah prompt yang sama dengan di computer_ai.py
    contents = f"""
    Anda adalah asisten AI yang helpful dan informatif.

    INFORMASI LAPTOP TERSEDIA (jika dibutuhkan):
    {laptop_data_str}

    PERTANYAAN USER: "{pertanyaan}"

    INSTRUKSI:
    - Jika pertanyaan tentang rekomendasi laptop, gunakan data laptop di atas dan berikan rekomendasi yang spesifik
    - Jika pertanyaan umum tentang AI, teknologi, atau topik lainnya, jawablah dengan informatif
    - Jika pertanyaan di luar konteks, tetap jawab dengan sopan dan helpful
    - Gunakan bahasa Indonesia yang natural dan mudah dipahami

    JAWABAN:
    """
    
    try:
        response = model.generate_content(contents=contents)
        return response.text
    except Exception as e:
        return f"❌ Terjadi kesalahan saat menghubungi AI: {e}"

def render_konsultasi_ai():
    """Menampilkan antarmuka chat dengan AI."""
    st.header("🤖 Konsultasi dengan Gemini AI")
    st.caption("Tanyakan tentang rekomendasi laptop atau pertanyaan umum tentang teknologi.")

    if st.button("⬅️ Kembali ke Menu"):
        st.session_state.view = 'menu'
        st.rerun()
        
    # Inisialisasi riwayat chat jika belum ada
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Tampilkan pesan-pesan sebelumnya
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Input chat dari pengguna
    if prompt := st.chat_input("Tulis pertanyaan Anda di sini..."):
        # Tambahkan pesan pengguna ke riwayat dan tampilkan
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Dapatkan dan tampilkan respons AI
        with st.chat_message("assistant"):
            with st.spinner("🤖 AI sedang menganalisis..."):
                response_text = get_gemini_response(prompt)
                st.markdown(response_text)
                
        # Tambahkan respons AI ke riwayat
        st.session_state.messages.append({"role": "assistant", "content": response_text})

# ==============================================================================
# LOGIKA UTAMA APLIKASI
# ==============================================================================

# Judul utama aplikasi
st.title("🛒 AI Laptop Advisor")

# Inisialisasi "view" atau halaman di session state
if 'view' not in st.session_state:
    st.session_state.view = 'menu'

# Router sederhana untuk menampilkan halaman yang sesuai
if st.session_state.view == 'menu':
    render_menu_utama()
elif st.session_state.view == 'semua_laptop':
    render_semua_laptop()
elif st.session_state.view == 'cari_budget':
    render_cari_budget()
elif st.session_state.view == 'konsultasi_ai':
    render_konsultasi_ai()