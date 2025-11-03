import google.generativeai as genai
from config import GEMINI_API_KEY, LAPTOPS

def konsultasi_gemini():
    """Konsultasi flexible - bisa jawab pertanyaan umum dan rekomendasi laptop"""
    print("\n🤖 GEMINI AI ASSISTANT")
    print("=" * 50)
    
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        
        try:
            model = genai.GenerativeModel('gemini-2.5-flash')
            print("✅ Gemini 2.5 Flash siap!")
        except:
            model = genai.GenerativeModel('gemini-pro')
            print("✅ Gemini Pro siap!")
        
    except Exception as e:
        print(f"❌ Gagal setup Gemini: {e}")
        return

    laptop_data = ""
    for laptop in LAPTOPS:
        laptop_data += f"- {laptop['nama']}: {laptop['harga']} | {laptop['spek']} | {laptop['keterangan']}\n"
    
    print("\n💬 Anda bisa bertanya tentang:")
    print("   • Rekomendasi laptop (contoh: 'laptop untuk coding budget 10 juta')")
    print("   • Pertanyaan umum tentang AI/teknologi")
    print("   • Pertanyaan lainnya")
    print("   Ketik 'keluar' untuk kembali\n")
    
    while True:
        pertanyaan = input("🎯 Pertanyaan: ").strip()
        
        if pertanyaan.lower() == 'keluar':
            break
            
        if not pertanyaan:
            continue
            
        try:
            contents = f"""
            Anda adalah asisten AI yang helpful dan informatif.

            INFORMASI LAPTOP TERSEDIA (jika dibutuhkan):
            {laptop_data}

            PERTANYAAN USER: "{pertanyaan}"

            INSTRUKSI:
            - Jika pertanyaan tentang rekomendasi laptop, gunakan data laptop di atas dan berikan rekomendasi yang spesifik
            - Jika pertanyaan umum tentang AI, teknologi, atau topik lainnya, jawablah dengan informatif
            - Jika pertanyaan di luar konteks, tetap jawab dengan sopan dan helpful
            - Gunakan bahasa Indonesia yang natural dan mudah dipahami

            JAWABAN:
            """
            
            print("\n🔄 AI menganalisis...")
            response = model.generate_content(contents=contents)
            
            print("\n" + "=" * 60)
            print("🤖 RESPONSE:")
            print("=" * 60)
            print(response.text)
            print("=" * 60)
            
        except Exception as e:
            print(f"❌ Error: {e}")