# Simple-GBM


Bu skor median değerine göre iki sınıfa ayrılmıştır:

- 1 → Başarılı ürün
- 0 → Başarısız ürün

---

## ⚠️ Data Leakage Analizi

İlk modelde `rating` ve `rating_count` kullanıldığı için çok yüksek doğruluk (%99) elde edilmiştir.

Ancak bu durum **data leakage** olarak değerlendirilmiştir çünkü hedef değişken bu özelliklerden türetilmiştir.

Bu nedenle:

- `rating`
- `rating_count`

modelden çıkarılmış ve gerçekçi bir model kurulmuştur.

---

## 🤖 Kullanılan Modeller

- Logistic Regression (baseline)
- Gradient Boosting Machine (GBM)

---

## 📈 Model Performansı

### Leak içeren model:

- Logistic Regression: %96
- GBM: %99

### Leak kaldırıldıktan sonra:

- Logistic Regression: %54
- GBM: %68

---

## 🔍 Önemli Bulgular

- Fiyat ve indirim bilgileri tek başına sınırlı tahmin gücüne sahiptir
- Ürün başarısında **kullanıcı etkileşimi (yorum sayısı)** kritik rol oynamaktadır
- GBM, doğrusal modellere göre daha iyi performans göstermiştir

---

## 💡 İş (Business) İçgörüleri

- Kullanıcılar indirim oranlarına duyarlıdır
- Nihai fiyat (discounted price) en önemli faktördür
- Ancak gerçek başarıyı belirleyen ana unsur kullanıcı geri bildirimidir

---

## 🚀 Gelecek Çalışmalar

- API kullanılarak gerçek zamanlı veri çekme
- Yorum metinlerinden sentiment analizi ekleme
- Daha gelişmiş modeller (XGBoost, LightGBM)
- Hyperparameter tuning

---

## 🧠 Kullanılan Teknolojiler

- Python
- Pandas
- NumPy
- Scikit-learn

---

## 📎 Not

Bu proje eğitim ve öğrenme amaçlı yapılmıştır. Gerçek satış verisi bulunmadığı için başarı metriği tahmini olarak oluşturulmuştur.
