"""
Finhub API ile hisse senedi bilgilerini alır.
"""
from langchain.tools import tool
import requests
import os
from dotenv import load_dotenv

load_dotenv()

@tool
def get_stock_info(ticker: str) -> str:
    """
    Hisse senedi bilgilerini alır.
    
    Args:
        ticker (str): Hisse senedi sembolü.
    
    Returns:
        str: Hisse senedi bilgileri.
    """
    try:
        if not ticker:
            raise ValueError("Ticker sembolü boş olamaz.")

        api_key = os.getenv("FINNHUB_API_KEY")
        if not api_key:
            raise ValueError("API key bulunamadı.")

        # hisse senedi fiyatlarını alan url
        url = f"https://finnhub.io/api/v1/quote?symbol={ticker}&token={api_key}"

        response = requests.get(url)

        if response.status_code != 200:
            raise Exception("API isteği başarısız oldu.")
        
        data = response.json()

        """
        Güncel fiyat (c)
        Açılış fiyatı (o)
        En yüksek fiyat (h)
        En düşük fiyat(l)
        """

        current_price = data.get('c')
        open_price = data.get('o')
        high_price = data.get('h')
        low_price = data.get('l')

        return (
            f"{ticker} için fiyat bilgileri: \n"
            f" - Güncel Fiyat: {current_price} USD\n"
            f" - Açılış Fiyatı: {open_price} USD\n"
            f" - Gün içinde En yüksek Fiyat: {high_price} USD\n"
            f" - Gün içinde En düşük Fiyat: {low_price} USD\n"
            )

    except Exception as e:
        return f"Hata: {str(e)}"

if __name__ == "__main__":
    print(get_stock_info.invoke({"ticker": "AAPL"}))












