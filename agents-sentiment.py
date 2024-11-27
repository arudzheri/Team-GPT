from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

class SentimentAgent:
    def __init__(self):
        self.prompt = PromptTemplate(
            input_variables=["text"],
            template="Analyze the sentiment of the following text (Positive, Negative, Neutral):\n{text}\n"
        )
        self.llm = OpenAI(model="text-davinci-003")
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def analyze_sentiment(self, text):
        return self.chain.run(text=text)

