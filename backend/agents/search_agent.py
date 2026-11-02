from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools

from backend.config import SelectModel

class SearchAgent:
    def _get_model(self):
        model = SelectModel()
        selected_model = model.select_model("ollama-gemma")
        return selected_model.get_model()
    
    
    def search_agent(self) -> Agent:
        return Agent(
            name= "Search Agent",
            role= "Finds current information on the web via search.",
            model=self._get_model(),
            tools=[
                DuckDuckGoTools(
                    timeout= 30,
                    fixed_max_results= 3
                )
            ],
            instructions= [
                "Use web search for news, current events, and general facts.",
                "Run 2-3 differently worded queries when the first results are thin.",
                "Always include source URLs with each claim.",
                "Prefer recent and authoritative sources; note when sources conflict.",
                "Return a concise summary, not raw search results.",
            ],
            add_datetime_to_context= True,
            timezone_identifier= "Asia/Kolkata",
            markdown= True
        )


if __name__ == "__main__":
    # agent = SearchAgent()
    # search_agent = agent.search_agent()
    # search_agent.print_response(
    #     "Tell me current time and date.",
    #     stream= True
    # )
    
    pass