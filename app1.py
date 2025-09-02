from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key='ollama')

response = client.chat.completions.create(
    model='llama3.2',
    messages=[
    {
        'role' : 'system',
        'content' : """Sei un assistente virtuale di una agenzia di viaggi molto alla mano e soprattutto simpatico.
        Adatto a fornire i giusti consigli ai clienti, sui loro viaggi escursioni ecc.. """
    },
    {
        'role' : 'user',
        'content' : """Ciao, io e la mia ragazza (ormai moglie) ci siamo sposati e vorremo andare in viaggio di nozze.
        Quali sono le mete più ambite a tema di viaggi balneari, vorrei anche sapere dove potremmo alloggiare"""
    },
],
)

print(response.choices[0].message.content)