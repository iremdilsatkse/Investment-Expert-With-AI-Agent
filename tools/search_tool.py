"""
DuckDuck Go Search Langchain küütphanesi içeriisnde gelir.
"""
from langchain_community.tools import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()

if __name__ == "__main__":
    query = "çeyrek altın fiyatı ne kadar"
    result = search.invoke(query)
    print(f"Arama sonucu: \n{result}") 
















