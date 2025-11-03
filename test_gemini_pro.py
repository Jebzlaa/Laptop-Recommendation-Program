# test_gemini_pro.py - Testing khusus gemini-pro
import google.generativeai as genai
from config import GEMINI_API_KEY, GEMINI_MODEL

def test_gemini_pro_direct():
    """Test langsung gemini-pro"""
    print("🎯 DIRECT TEST GEMINI-PRO")
    print("=" * 40)
    
    try:
        # Configure
        genai.configure(api_key=GEMINI_API_KEY)
        
        # Buat model
        print(f"🔧 Membuat model: {GEMINI_MODEL}")
        model = genai.GenerativeModel(GEMINI_MODEL)
        
        # Test 1: Simple response
        print("\n🧪 Test 1: Simple question...")
        response1 = model.generate_content("Apa kelebihan model gemini-pro? Jawab dalam 2 kalimat.")
        print(f"✅ Response: {response1.text}")
        
        # Test 2: Complex reasoning
        print("\n🧪 Test 2: Complex reasoning...")
        response2 = model.generate_content(
            "Jika budget 10 juta untuk coding, mana yang lebih penting: RAM 16GB atau processor i5? Beri alasan singkat."
        )
        print(f"✅ Response: {response2.text}")
        
        print(f"\n🎉 SEMUA TEST BERHASIL! Gemini-pro dapat digunakan!")
        return True
        
    except Exception as e:
        print(f"❌ TEST GAGAL: {e}")
        return False

if __name__ == "__main__":
    test_gemini_pro_direct()