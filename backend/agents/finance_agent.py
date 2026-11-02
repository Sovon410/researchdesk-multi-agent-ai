from agno.agent import Agent
from agno.tools.yfinance import YFinanceTools

from backend.config import SelectModel


class FinanceAgent:
    def _get_model(self):
        model = SelectModel()
        selected_model = model.select_model("ollama-gemma")
        return selected_model.get_model()
    
    def finance_agent(self) -> Agent:
        return Agent(
            name= "Finance Agent",
            role= "Provides stock prices, fundamentals, analyst data, and company info.",
            model= self._get_model(),
            tools= [YFinanceTools()],
            instructions= [
                "Use ticker symbols; if the user gives a company name, resolve the ticker first.",
                "Present numbers in tables, with currency and the date of the data.",
                "Cover price, market cap, P/E, and recent trend for stock overviews.",
                "State clearly that this is informational, not financial advice.",
                "Never invent figures; if the tool returns nothing, say so.",
            ],
            markdown= True
        )


if __name__ == "__main__":
    # agent = FinanceAgent()
    # finance_agent = agent.finance_agent()
    # finance_agent.print_response(
    #     "What's the NVIDIA's current stocks price?",
    #     stream= True
    # )
    
    pass