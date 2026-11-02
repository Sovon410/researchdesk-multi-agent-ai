from agno.agent import Agent
from agno.tools.youtube import YouTubeTools

from backend.config import SelectModel


class YouTubeAgent:
    def _get_model(self):
        model = SelectModel()
        selected_model = model.select_model("ollama-gemma")
        return selected_model.get_model()
    
    def youtube_agent(self) -> Agent:
        return Agent(
            name= "YouTube Agent",
            role= "Gets metadata, captions, and transcripts from YouTube videos.",
            model= self._get_model(),
            tools= [YouTubeTools()],
            instructions= [
                "Fetch the video data and captions before answering anything about a video.",
                "Summarize with key points and approximate timestamps when available.",
                "If captions are unavailable, say so instead of guessing the content.",
                "Include the video title and URL in your answer.",
            ],
            markdown= True
        )



if __name__ == "__main__":
    # agent = YouTubeAgent()
    # youtube_agent = agent.youtube_agent()
    # youtube_agent.print_response(
    #     "Summarize this video: 'YouTube URL'",
    #     stream= True
    # )
    
    pass
