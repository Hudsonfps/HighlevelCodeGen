from flask import Flask, request, jsonify
import os  
import openai
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()    

@app.route('/openai_chat', methods=['POST'])
def openai_chat():  
    user_input = request.json['user_input']
    openai.api_type = os.environ['OPENAI_API_TYPE']  
    openai.api_base = os.environ['OPENAI_API_BASE']  
    openai.api_version = os.environ['OPENAI_API_VERSION']  
    openai.api_key = os.environ['OPENAI_API_KEY']  

    message_text = [{"role":"system","content":"Given the following user requirements, please generate the appropriate code that will fulfill these needs. Make sure to have a high level explanation to that, like this one code break down and high level explanation. The user requirements are as follows:"},    
                    {"role":"user","content":user_input}]   

    completion = openai.ChatCompletion.create(  
      engine="gpt-4-32k",  
      messages = message_text,  
      temperature=0,  
      max_tokens=2000,  
      top_p=0.95,  
      frequency_penalty=0,  
      presence_penalty=0,  
      stop=None  
    )  
    return jsonify(completion.choices[0].message['content'])

if __name__ == "__main__":
    app.run(debug=True)
