# 🎤 NextGen AI Voice API

**NextGen AI Voice** হলো একটি ওপেনসোর্স প্রজেক্ট, যেখানে আপনি সহজেই আপনার রেকর্ড করা ভয়েস Enhance করতে পারবেন এবং বাংলা টেক্সটকে ভয়েসে রূপান্তর করতে পারবেন।

---

## ✨ ফিচারসমূহ (Features)

✅ রেকর্ড করা ভয়েস ক্লিয়ার ও নোয়েজ-মুক্ত করা  
✅ বাংলা টেক্সট → ন্যাচারাল ভয়েস  
✅ ফ্রি FastAPI সার্ভার (Render.com-এ হোস্ট করা যাবে)  
✅ Adsterra সহ HTML অ্যাপ এর জন্য প্রস্তুত

---

## 🚀 API Routes

### `/enhance`
- 📤 `POST` অডিও ফাইল পাঠান (`audio/*`)
- 📥 Enhanced (noise reduced) অডিও ফাইল পাবেন

### `/tts`
- 📤 `POST` ফর্ম ডেটাতে `text` পাঠান (বাংলা)
- 📥 পাবেন: `.mp3` ভয়েস ফাইল

---

## 🔧 ইনস্টলেশন (লোকাল রান করতে চাইলে)
```bash
git clone https://github.com/your-username/nextgen-ai-voice-api.git
cd nextgen-ai-voice-api
docker build -t nextgen-voice .
docker run -p 8080:8080 nextgen-voice
