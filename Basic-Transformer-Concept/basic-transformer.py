#Install python transformers module first
#this also requires the torch library.
#pip3 install torch torchvision torchaudio transformers

from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Initialize the tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Define a sentence
sentence = "The weather today is"

# Tokenize the sentence and convert it to tensor format
inputs = tokenizer.encode(sentence, return_tensors="pt")

# Generate predictions from the model
predictions = model.generate(inputs, max_length=10, do_sample=True)

# Decode the predictions to readable text
predicted_sentence = tokenizer.decode(predictions[0], skip_special_tokens=True)

print(predicted_sentence)
