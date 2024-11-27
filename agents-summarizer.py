from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

class SummarizerAgent:
    def __init__(self):
        self.prompt = PromptTemplate(
            input_variables=["text"],
            template="Summarize the following text:\n{text}\n"
        )
        self.llm = OpenAI(model="text-davinci-003")
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def summarize(self, text):
        return self.chain.run(text=text)

