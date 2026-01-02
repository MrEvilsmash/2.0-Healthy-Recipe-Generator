from flask import Flask, render_template, request
import google.generativeai as genai

# Initialize the Flask app
app = Flask(__name__)

# Configure API securely (make sure to set this environment variable in your system)
genai.configure(api_key="AIzaSyAV5Ie7gyXYfW5DB87ei_xSR0Y_Mg8xUow")
mymodel = genai.GenerativeModel('gemini-2.5-flash')
chat = mymodel.start_chat()

# Route for the home page
@app.route('/')
def home():
    return render_template("home.html")
# Route for handling form submissions
@app.route('/submit-form', methods=['POST'])
def submit():
    uinput = request.form.get('user_input')
    dietary_preference = request.form.get('dietary_preference')

    # Craft the prompt for the healthy recipe assistant
    recipe_prompt = f"As a healthy recipe assistant, please provide a healthy recipe suggestion for {uinput} that is {dietary_preference}. Include ingredients, preparation steps, and nutritional information."

    response = chat.send_message(recipe_prompt)
    recipe_text = response.text

    # Split the recipe into lines
    recipe_lines = recipe_text.split('\n')

    # Pass the split lines as recipe_steps to the template
    return render_template('home.html', recipe_steps=recipe_lines)

if __name__ == "__main__":
    app.run(debug=True)
