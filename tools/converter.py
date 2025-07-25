"""
Dolar to Türk Lirası
"""
from langchain.tools import tool
import requests

@tool
def convert_usd_to_try(amount: float) -> str:
    """
    Doları Türk Lirasına çevirir.
    
    Args:
        amount (float): Dolar miktarı.
    
    Returns:
        str: Çevrilmiş Türk Lirası miktarı.
    """
    try:
        if isinstance(amount, str):
            amount = float("". join(filter(lambda x : x.isdigit() or x == '.', amount)))

        url = "https://api.coingecko.com/api/v3/simple/price?ids=usd&vs_currencies=try"

        response = requests.get(url)

        if response.status_code != 200:
            raise Exception("API isteği başarısız oldu.")
        
        data = response.json()
        rate = data['usd']['try']

        result = amount * rate

        return f"{amount} USD = {result:2f} TRY (Kur: {rate: .2f})"

    except Exception as e:
        return f"Hata: {str(e)}"

if __name__ == "__main__":
    print(convert_usd_to_try.invoke({"amount": 500}))  













