import math
import re
import gradio as gr

# Entropy calculation
def calculate_entropy(password):
    length = len(password)
    charset = 0

    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"\d", password):
        charset += 10
    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password):
        charset += 32

    if charset == 0 or length == 0:
        return 0, "❌ Invalid or empty password."

    entropy = round(length * math.log2(charset), 2)
    return entropy, interpret_entropy(entropy)

# Strength interpretation
def interpret_entropy(entropy):
    if entropy < 28:
        return "❌ Very Weak (easily guessable)"
    elif entropy < 36:
        return "⚠️ Weak (somewhat guessable)"
    elif entropy < 60:
        return "✅ Reasonable (okay for general use)"
    elif entropy < 128:
        return "🔐 Strong (secure)"
    else:
        return "🛡️ Very Strong (extremely secure)"

# Function to show in Gradio
def analyze_password(password):
    entropy, strength = calculate_entropy(password)
    return f"🔍 Entropy: {entropy} bits\n\n🔐 Strength: {strength}"

# Create the Gradio interface
iface = gr.Interface(
    fn=analyze_password,
    inputs=gr.Textbox(lines=1, placeholder="Enter your password..."),
    outputs="text",
    title="🔢 Password Entropy Checker",
    description="Calculates password entropy and strength based on character sets and length."
)

iface.launch()
