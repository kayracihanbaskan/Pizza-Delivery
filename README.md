# Pizza Delivery Application

Bu proje, kullanıcıların online pizza siparişi verebilecekleri bir web uygulamasıdır. Python ve Streamlit framework'ü kullanılarak geliştirilmiştir.

## Özellikler

- Ana sayfa üzerinden pizza menüsüne erişim
- Çeşitli pizza seçenekleri ile katalog görüntüleme
- Özel pizza oluşturma imkanı
- Sipariş oluşturma ve takip sistemi

## Proje Yapısı

```
PizzaDelivery/
│
├── HomePage.py          # Ana sayfa uygulaması
├── README.md           # Proje dokümantasyonu
│
├── pages/              # Uygulama sayfaları
│   ├── AddPizza.py     # Özel pizza oluşturma sayfası
│   ├── Catalog.py      # Pizza kataloğu sayfası
│   └── Order.py        # Sipariş sayfası
```

## Kurulum

1. Python'u yükleyin (3.7 veya üzeri)
2. Gerekli kütüphaneleri yükleyin:
```bash
pip install streamlit
```

## Uygulamayı Çalıştırma

Uygulamayı başlatmak için terminal üzerinden aşağıdaki komutu çalıştırın:

```bash
streamlit run HomePage.py
```

## Kullanım

1. Ana sayfadan pizza kataloğuna göz atın
2. İstediğiniz pizzayı seçin veya özel pizza oluşturun
3. Siparişinizi oluşturun ve takip edin


