# test_model.py - Untuk testing model yang available
import google.generativeai as genai
from config import GEMINI_API_KEY

def test_all_models():
    """Test semua model yang available"""
    try:
        genai.configure(api_key=GEMINI_API_KEY)

        print("🔍 Testing semua model yang tersedia...")
        print("=" * 50)

        models = genai.list_models()
        working_models = []

        for model in models:
            if 'generateContent' in model.supported_generation_methods:
                try:
                    print(f"\n🧪 Testing: {model.name}")
                    test_model = genai.GenerativeModel(model.name)
                    response = test_model.generate_content("Halo, tes koneksi. Jawab: OK")
                    print(f"✅ BERHASIL: {model.name}")
                    working_models.append(model.name)
                except Exception as e:
                    print(f"❌ GAGAL: {model.name} - {e}")

        print("\n" + "=" * 50)
        print("📋 MODEL YANG BERHASIL:")
        for model in working_models:
            print(f"🎯 {model}")

        return working_models

    except Exception as e:
        print(f"❌ Error: {e}")
        return []

if __name__ == "__main__":
    test_all_models()