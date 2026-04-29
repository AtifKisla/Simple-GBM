
Bu skor median değerine göre iki sınıfa ayrılmıştır:

- 1 → Başarılı ürün
- 0 → Başarısız ürün

---

## ⚠️ Data Leakage Analizi

İlk modelde `rating` ve `rating_count` kullanıldığı için %99 doğruluk elde edilmiştir.

Ancak bu durum **data leakage** olarak değerlendirilmiştir çünkü hedef değişken bu özelliklerden türetilmiştir.

Bu nedenle:

- `rating`
- `rating_count`

modelden çıkarılmış ve daha gerçekçi bir model kurulmuştur.

---

## 🤖 Kullanılan Modeller

- Logistic Regression (baseline)
- Gradient Boosting Classifier (GBM)
- XGBoost (advanced boosting)

---

## 📈 Model Performansı

### Leak içeren model:

- Logistic Regression: %96
- GBM: %99

### Leak-free model:

- Logistic Regression: %54
- GBM: %68
- XGBoost: %64

---

## 🔍 Önemli Bulgular

- Fiyat ve indirim bilgileri tek başına sınırlı tahmin gücüne sahiptir
- Ürün başarısında kullanıcı davranışları (yorumlar) kritik rol oynamaktadır
- GBM, doğrusal modellere göre daha iyi performans göstermiştir

---

## 💡 İş İçgörüleri

- Kullanıcılar nihai fiyata (discounted price) duyarlıdır
- İndirim oranı satın alma davranışını etkiler
- Ancak gerçek başarıyı belirleyen ana faktör kullanıcı etkileşimidir

---

## 🚀 Gelecek Çalışmalar

- API ile gerçek zamanlı veri entegrasyonu
- Yorum metinlerinden sentiment analizi
- Model tuning (hyperparameter optimization)
- Daha büyük veri setleri ile test

---

## 🧠 Kullanılan Teknolojiler

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost

---

## 📎 Not

Bu proje eğitim amaçlı geliştirilmiştir. Gerçek satış verisi bulunmadığı için başarı metriği tahmini olarak oluşturulmuştur.
