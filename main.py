from dotenv import load_dotenv

load_dotenv()


from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch
from langchain.agents import create_agent
from langchain.tools import tool
#from tavily import TavilyClient
from langchain_tavily import TavilySearch
from langchain_core.messages import HumanMessage
from schemas import AgentResponse

# tavilty = TavilyClient()

# @tool
# def search(query: str) -> str:
#     """
#     Tool that searchs over internet
#     Args:query (str): The query to search for
#     Returns:
#     The serch result
#     """
#     print(f"Searching for {query}")   
#     return tavilty.search(query=query)

llm= ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

tools = [TavilySearch]
agent = create_agent(llm, tools)

def main():
    print("Hello form langchain-course!")
    result = agent.invoke({"messages":HumanMessage(content="Search for top 3 skills for AI engineer in 2026 to get a job on linkedin open jobs")})
    print(result['messages'][-1].content)


if __name__ == "__main__":
    main()
