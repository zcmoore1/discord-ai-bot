import ast
import google.generativeai as genai


def instantiate_model(api_key, model_name):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name)
    return model

def make_playlist(model, prompt):
    inst = "Given the following description, construct a list of real songs that satisfy the description provided. \
        Your answer should be formatted as a flat python list, with each item as the name of an artist and their song, like so: [\"Michael Jackson - Thriller\"]"
    prompt = f"[inst]{inst}[/inst]\nDescription: {prompt}\n"
    response = model.generate_content(prompt).text
    print(response)
    try:
        response = get_list_literal(response)
    except Exception as e:
        print(e)
        response = "sorry, i failed :)"

    return response

def get_list_literal(s: str) -> list:
    s = '[' + s.split('[')[1].split(']')[0] + ']'
    return ast.literal_eval(s)
    
