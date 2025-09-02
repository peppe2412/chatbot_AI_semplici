import chainlit as cl
import ollama

@cl.on_chat_start
async def on_chat_start():
    """Inizializza la sessione utente con un messaggio del sistema, così da far capire il ruolo del chatbot"""
    cl.user_session.set(
        'message', [{
            'role' : 'system',
            'content' : """
            Sei un assistente AI alla mano, cordiale e simpatico, pronto ad aiutare e rispondere alle domande dell'utente.
            Fornisci risposte ben dettagliate e ben curate, avendo un tono professionale ed amichevole"""
        }],
    )
    await cl.Message(content='Ciao, fammi una domanda!').send()
    
@cl.on_message
async def handle_message(message : cl.Message):
    """
    Gestisce i messaggi inviati dall'utente, li passa al modello e restituisce le risposte.
    Args:   
        message (cl.Message): Messaggio ricevuto dall'utente.
    """
    messages = cl.user_session.get('message', [])
    messages.append({'role':'user', 'content':message.content})
    
    response_message = cl.Message(content='')
    await response_message.send()
    
    try:
        stream = ollama.chat(model='llama3.2', messages=messages, stream=True)
        for chunk in stream:
            await response_message.stream_token(chunk['message']['content'])
            
        messages.append({'role':'assistant', 'content':response_message.content})
        await response_message.update()
    except Exception as e:
        error_message = f'An error occurred: {str(e)}'
        cl.Message(content=error_message).send()
        print(error_message)
        
@cl.on_chat_end
async def on_chat_end():
    """Pulizia e messaggio della fine della chat"""
    await cl.Message(
        content='Buona Gioranta!'
    ).send()
        
    
