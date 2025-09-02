from langchain_ollama import ChatOllama

llm = ChatOllama(model='llama3.2')

result = llm.invoke('Qual è il tuo animale preferito? Quale vorresti essere?')
print(result)