from agno.agent import Agent
from agno.tools.webbrowser import WebBrowserTools

from backend.config import SelectModel

class BrowserAgent:
    def _get_model(self):
        model = SelectModel()
        selected_model = model.select_model("ollama-gemma")
        return selected_model.get_model()
    
    def browser_agent(self) -> Agent:
        return Agent(
            name= "Browser Agent",
            role= "Opens web pages in the user's browser when they want to view something.",
            model= self._get_model(),
            tools= [WebBrowserTools()],
            instructions= [
                "Open a page only when the user explicitly wants to view it.",
                "Confirm the exact URL you opened.",
                "Do not use this agent to read or scrape content; that is the Web Researcher's job.",    
            ],
            markdown= True
        )


if __name__ == "__main__":
    # agent = BrowserAgent()
    # browser_agent = agent.browser_agent()

    # browser_agent.print_response(
    #     "Open YouTube.",
    #     stream= True
    # )
    
    pass