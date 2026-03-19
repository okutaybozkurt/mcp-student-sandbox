# Gizemli Modül

## Genel Bakış
`mystery_module.py`, şu formdaki ikinci dereceden denklemleri çözmek için bir fonksiyon sağlar:

\[ ax^2 + bx + c = 0 \]

Bu modül, denklemin köklerini bulmak için ikinci dereceden denklem formülünü kullanır.

## Fonksiyon Dokümantasyonu

### `fn_x(a: float, b: float, c: float) -> tuple[float, float] | None`

#### Amaç
İkinci dereceden bir denklemin köklerini ikinci dereceden denklem formülü ile hesaplar.

#### Parametreler
- `a` (float): \(x^2\)'nin katsayısı. Sıfır olmamalıdır.
- `b` (float): \(x\)'in katsayısı.
- `c` (float): Sabit terim.

#### Dönen Değer
- Eğer diskriminant \(d = b^2 - 4ac\) negatif değilse, iki kökü içeren bir demet \((kök1, kök2)\) döner.
- Eğer diskriminant negatifse (gerçek kök yoksa), `None` döner.

## Kullanım Örneği
```python
from mystery_module import fn_x

# 2x^2 + 4x - 6 = 0 denklemini çöz
a, b, c = 2, 4, -6
roots = fn_x(a, b, c)
if roots:
    print(f"Kökler: {roots[0]}, {roots[1]}")
else:
    print("Gerçek kök yok.")
```

## Sınırlamalar ve Köşe Durumları
- Eğer diskriminant negatifse, fonksiyon `None` döner ve bu, gerçek köklerin olmadığını belirtir.
- Eğer `a` sıfırsa, fonksiyon `ZeroDivisionError` hatası verir çünkü ikinci dereceden denklem formülü doğrusal denklemler için tanımsızdır.
- Fonksiyon, tüm girdilerin sayısal olduğunu varsayar. Sayısal olmayan girdiler `TypeError` hatasına neden olur.

## Notlar
Bu modül, temel ikinci dereceden denklem çözümü için uygundur ancak karmaşık kökleri veya sembolik hesaplamayı desteklemez.