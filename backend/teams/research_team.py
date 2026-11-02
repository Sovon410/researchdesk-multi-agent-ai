from agno.team import Team

from backend.config import SelectModel
from backend.agents.browser_agent import BrowserAgent
from backend.agents.finance_agent import FinanceAgent
from backend.agents.search_agent import SearchAgent
from backend.agents.web_researcher import WebResearcher
from backend.agents.youtube_agent import YouTubeAgent


class ResearchTeam:
    def _get_model(self):
        model = SelectModel()
        selected_model = model.select_model("ollama-gpt")
        return selected_model.get_model()
    
    
    def research_team(self) -> Team:
        return Team(
            name= "Research Team",
            model= self._get_model(),
            members= [
                BrowserAgent().browser_agent(),
                FinanceAgent().finance_agent(),
                SearchAgent().search_agent(),
                WebResearcher().web_researcher(),
                YouTubeAgent().youtube_agent()    
            ],
            instructions= [
                "You are the coordinator. Delegate to the member whose role fits the request.",
                "Stock/company market questions -> Finance Agent.",
                "YouTube links or video questions -> YouTube Agent.",
                "Unknown info or news -> Search Agent; then Web Researcher to read the best URLs.",
                "Only use the Browser Agent if the user asks to open a page.",
                "Combine member outputs into one final answer with sources.",
            ],
            show_members_responses= True,
            markdown= True
        )
        
        

if __name__ == "__main__":
    # team = ResearchTeam()
    # research_team = team.research_team()
    # research_team.print_response(
    #     "Find the latest news on NVIDIA and give me its current stock overview.",
    #     stream= True
    # )
    
    pass