import tkinter as tk
from tkinter import Entry, scrolledtext
from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-1_5")
model = AutoModelForCausalLM.from_pretrained(
    "microsoft/phi-1_5", trust_remote_code=True)
def generate_response(message):
    inputs = tokenizer(message, return_tensors='pt', truncation=True)
    outputs = model.generate(
        **inputs,
        max_length=150,
        pad_token_id=tokenizer.eos_token_id
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response
def on_send(event=None):
    message = user_input.get()
    if message:
        chat_window.configure(state=tk.NORMAL)
        chat_window.insert(tk.END, f"You: {message}\n")
        chat_window.configure(state=tk.DISABLED)
        user_input.delete(0, tk.END)
        response = generate_response(message)
        chat_window.configure(state=tk.NORMAL)
        chat_window.insert(tk.END, f"WebIdeasBot: {response}\n")
        chat_window.configure(state=tk.DISABLED)
window = tk.Tk()
window.title("WebIdeasBot")
chat_window = scrolledtext.ScrolledText(
    window, width=80, height=20, state=tk.DISABLED)
chat_window.pack()
user_input = Entry(window, width=80)
user_input.pack()
user_input.focus_set()
user_input.bind("<Return>", on_send)
window.mainloop()
