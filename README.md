# Yatırım Uzmanı AI Agent

Bu proje, yatırım ile ilgili soruları analiz eden ve en güncel bilgileri sunan bir yapay zeka yatırım danışmanıdır. Langchain ve Gemini 2.0 Flash teknolojileri ile geliştirilmiştir.

## Özellikler

- **Dolar/TL Çevirisi:** USD miktarını güncel kur ile Türk Lirasına çevirir.
- **Hisse Senedi Bilgisi:** Finnhub API üzerinden hisse senedi fiyatlarını getirir.
- **İnternetten Arama:** DuckDuckGo aracı ile güncel haber ve bilgileri bulur.
- **Profesyonel Yanıtlar:** Yatırım kararını kullanıcıya bırakır, sadece tavsiye verir.

## Kurulum

1. Depoyu bilgisayarınıza klonlayın.
2. Gerekli Python paketlerini yükleyin:
    ```sh
    pip install -r requirements.txt
    ```
3. `.env` dosyasındaki API anahtarlarını doldurun.

## Kullanım

Ana dosyayı çalıştırın:
```sh
python agent_main.py
```
Sorularınızı Türkçe veya İngilizce sorabilirsiniz. Çıkmak için `exit`, `quit` veya `q` yazın.

## Dosya Yapısı

- `agent_main.py`: Ana uygulama dosyası.
- `tools/converter.py`: Dolar/TL çevirici.
- `tools/market_api.py`: Hisse senedi bilgisi aracı.
- `tools/search_tool.py`: İnternet arama aracı.
- `.env`: API anahtarları.
- `requirements.txt`: Gerekli Python paketleri.

## API Anahtarları

- Finnhub ve Google API anahtarlarınızı `.env` dosyasına ekleyin.
