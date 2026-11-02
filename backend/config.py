from abc import ABC, abstractmethod
from pathlib import Path

from dotenv import load_dotenv
from agno.models.nvidia import Nvidia
from agno.models.ollama import Ollama

load_dotenv(Path(__file__).resolve().parent / ".env", override=True)


class Model(ABC):
    @abstractmethod
    def get_model(self):
        pass

# class ModelGemma(Model):
#     def get_model(self):
#         return Nvidia(
#             id= "google/gemma-4-31b-it",
#             base_url= "https://integrate.api.nvidia.com/v1"
#         )
    
# class ModelGPTOSS(Model):
#     def get_model(self):
#         return Nvidia(
#             id="openai/gpt-oss-20b",
#             base_url= "https://integrate.api.nvidia.com/v1"
#         )
    
# class ModelGLMFlash(Model):
#     def get_model(self):
#         return Nvidia(
#             id= "z-ai/glm-5.3-flash",
#             base_url= "https://integrate.api.nvidia.com/v1"
#         )

# class ModelDeepseekFlash(Model):
#     def get_model(self):
#         return Nvidia(
#             id= "deepseek-ai/deepseek-v4.1-flash",
#             base_url= "https://integrate.api.nvidia.com/v1"
#         )
    
# class ModelMinimax(Model):
#     def get_model(self):
#         return Nvidia(
#             id= "minimaxai/minimax-m3.1-flash",
#             base_url= "https://integrate.api.nvidia.com/v1"
#         )


class OllamaGptOss(Model):
    def get_model(self):
        return Ollama(
            id= "gpt-oss:120b"
        )


class OllamaQwen(Model):
    def get_model(self):
        return Ollama(
            id= "gemma4:31b-cloud"
        )
    

class SelectModel:
    def __init__(self):
        self._available_models = {
            # "gemma" : ModelGemma,
            # "gpt" : ModelGPTOSS,
            # "glm" : ModelGLMFlash,
            # "deepseek" : ModelDeepseekFlash,
            # "minimax" : ModelMinimax
            "ollama-gpt" : OllamaGptOss,
            "ollama-gemma" : OllamaQwen
        }
    def select_model(self, model_name: str) -> Model:
        available_model_name = self._available_models.get(model_name.lower())
        if not available_model_name:
            raise ValueError (f"Unsupported model: {model_name}")
        return available_model_name()



if __name__ == "__main__":
    # model = SelectModel()
    # model_gpt = model.select_model("gpt")
    # print(type(model_gpt))
    
    pass