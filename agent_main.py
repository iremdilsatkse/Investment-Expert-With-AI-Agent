"""
AI Agent ile Yatırım Uzmanı
Sorulan yatırım sorularını anlayıp, doğru kaynaklardan bilgi toplayarak yatırımcıya net ve güncel bilgi sunabilen akıllı bir yatırım danışmanı.
    - dolar bugün kaç tl
    - borsa ne durumda
    - altın fiyatları ne kadar

Kullanıcıdan gelen soruları analiz eder.
Gerkli olduğunda internetten arama yapar, kur çevirisi gerçekleştirir, hisse bilgisi alır.
Bunları profesyonel bir dil ile yapar.
"""
"""
Langchain, GEMINI 2.0 Flash teknolojilerini kullanır.
- CoinGecko API'si ile kripto para bilgisi alır.
- Finnhub API'si ile hisse senedi bilgisi alır.
- DuckDuckGo internetten arama yapar.
"""
from langchain.agents import initialize_agent, AgentType
from langchain_google_genai  import ChatGoogleGenerativeAI
from tools.search_tool import search
from tools.converter import convert_usd_to_try
from tools.market_api import get_stock_info

from dotenv import load_dotenv
import os

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

# LLM
llm = ChatGoogleGenerativeAI(
    model = "gemini-2.0-flash",
    temperature = 0.7,
    google_api_key = os.getenv("GOOGLE_API_KEY")
)

# Araçlar
tools = [
    search,
    convert_usd_to_try,
    get_stock_info
]

investment_prompt = PromptTemplate.from_template(
    """
    You are an expert investment advisor.
    You answer investment-related questions in a professional manner.
    You can use the following tools to provide accurate and up-to-date information:
    - Search the internet for the latest news and information.
    - Convert USD to TRY using the latest exchange rates.
    - Get stock information using the Finnhub API.
    
    Rules:
    - Answering without understanding the question is not allowed.
    - Use the tools if necessary.
    - Don't let the user make an investment decision, just give advice.
    - Provide clear and concise answers.
    - If you don't know the answer, say "I don't know" instead of making up an answer.

    Question: {input}
    
    """
)

# LLM Zinciri
llm_chain = LLMChain(
    llm = llm,
    prompt = investment_prompt
)

# AI Agent tanımlama
agent = initialize_agent(
    tools = tools,
    llm = llm,
    agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose = True
)

if __name__ == "__main__":
    print("Yatırım Uzmanı AI Agent'a hoş geldiniz!")
    print("Sorularınızı sorabilirsiniz. Çıkmak için 'exit', 'quit' veya 'q' yazın.")
    while True:
        user_input = input("Soru: ")
        if user_input.lower() in ["exit", "quit", "q"]:
            print("Çıkılıyor...")
            break
        
        try:
            # AI Agent ile cevap alma
            response = agent.invoke({"input": user_input})
        
            print(f"Cevap: {response}")
        except Exception as e:
            print(f"Hata oluştu: {e}")
























