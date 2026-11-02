from agno.agent import Agent
from agno.tools.website import WebsiteTools
from agno.tools.websearch import WebSearchTools

from backend.config import SelectModel


class WebResearcher:
    def _get_model(self):
        model = SelectModel()
        selected_model = model.select_model("ollama-gemma")
        return selected_model.get_model()
    
    
    def web_researcher(self) -> Agent:
        return Agent(
            name= "Web Researcher",
            role= "Reads and extracts information from specific web page URLs.",
            model= self._get_model(),
            tools=[
                WebSearchTools(
                    backend="auto",
                    fixed_max_results=5 
                ),
                WebsiteTools()
            ],
            instructions=[
                "Search the internet before beginning research.",
                "Use WebSearchTools to discover relevant sources.",
                "Only read URLs returned by the search tool or explicitly provided by the user.",
                "Never invent, fabricate, or generate placeholder URLs.",
                "Do not use URLs such as https://arxiv.org/IgnoreMe.",
                "Use WebsiteTools to extract relevant information from legitimate URLs.",
                "Prefer reliable and authoritative sources.",
                "Extract only information relevant to the user's question.",
                "If a website fails to load, report the failure rather than guessing.",
                "Summarize findings in your own words.",
                "Always provide the source URLs."
            ],
            add_datetime_to_context= True,
            timezone_identifier= "Asia/Kolkata",
            markdown= True
        )
        

if __name__ == "__main__":
    # agent = WebResearcher()
    # web_researcher = agent.web_researcher()
    # web_researcher.print_response(
    #     "Make a quick research on RAG.",
    #     stream= True
    # )
    
    pass