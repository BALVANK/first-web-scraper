ram_listesi = [
    {
        "baslik": "Corsair Vengeance 16GB DDR5 6000MHz",
        "normal_fiyat": 3000,
        "indirimli_fiyat": 1800,
        "link": "https://example.com/ram1"
    },
    {
        "baslik": "Kingston Fury Beast 8GB DDR4 3200MHz",
        "normal_fiyat": 1000,
        "indirimli_fiyat": 750,
        "link": "https://example.com/ram2"
    },
    {
        "baslik": "G.Skill Ripjaws 32GB DDR5 5600MHz",
        "normal_fiyat": 4500,
        "indirimli_fiyat": 4200,
        "link": "https://example.com/ram3"
    }
]

def firsat_analiz_et(normal, indirimli):
    indirim_orani = ((normal - indirimli) / normal) * 100
    
    if indirim_orani >= 36:
        yildiz = "⭐⭐⭐⭐⭐ [Sıcak Fırsat!]"
    elif indirim_orani >= 21:
        yildiz = "⭐⭐⭐⭐ [Ciddi İndirim]"
    elif indirim_orani >= 10:
        yildiz = "⭐⭐ [Makul Fırsat]"
    else:
        yildiz = "⭐ [Düşük İndirim]"
        
    return round(indirim_orani, 1), yildiz

for ram in ram_listesi:
    oran, yildiz_etiketi = firsat_analiz_et(ram["normal_fiyat"], ram["indirimli_fiyat"])
    
    if oran >= 20:
        print(f"🔥 BİLDİRİM ATILACAK ÜRÜN YAKALANDI:")
        print(f"Ürün: {ram['baslik']}")
        print(f"Eski Fiyat: {ram['normal_fiyat']} TL | Yeni Fiyat: {ram['indirimli_fiyat']} TL")
        print(f"İndirim Oranı: %{oran}")
        print(f"Derece: {yildiz_etiketi}")
        print(f"Link: {ram['link']}")
        print("=" * 50)
    else:
        print(f"❌ Pas geçildi (İndirim düşük - %{oran}): {ram['baslik']}")
        print("-" * 50)