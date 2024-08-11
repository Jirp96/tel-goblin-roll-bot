import constants
import google.generativeai as genai

class RadIA:
    def __init__(self, apikey) -> None:        
        genai.configure(api_key=apikey)
        self.model = genai.GenerativeModel('gemini-pro')
        self.chat = self.model.start_chat(
            history=[
                {"role": "model", "parts": constants.RAD_IA_CONTEXT},
            ]
        )
    def generate_response(self, message):
        try:
            response = self.chat.send_message(message, generation_config=genai.types.GenerationConfig(
                max_output_tokens=200
            ),)
            return response.text            
        except Exception as e:
            return "Ocurrió un error, intenta de nuevo: {0}".format(str(e))        
        
    