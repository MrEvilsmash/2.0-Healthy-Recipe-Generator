
import google.generativeai as genai

# Configure API securely
genai.configure(api_key="AIzaSyAV5Ie7gyXYfW5DB87ei_xSR0Y_Mg8xUow")
mymodel = genai.GenerativeModel('gemini-1.5-flash')
chat = mymodel.start_chat()

# Test sending a message
recipe_prompt = "Please provide a healthy recipe for salad that is vegan."
response = chat.send_message(recipe_prompt)
print(response.text)