# Run this in Google Colab first to test the model before building the app.
# Step 1: Install libraries (run this in a Colab cell)
# !pip install transformers sentencepiece textstat

from transformers import pipeline
import textstat

# Load the pretrained grammar correction model
corrector = pipeline("text2text-generation", model="vennify/t5-base-grammar-correction")

# Try it on a few test sentences
test_sentences = [
    "She dont like going to school everyday.",
    "I has three cat and they are very cute.",
    "Yesterday I go to market for buy vegetables.",
]

for sentence in test_sentences:
    input_text = "grammar: " + sentence
    result = corrector(input_text, max_length=256)
    corrected = result[0]['generated_text']
    fluency = textstat.flesch_reading_ease(sentence)

    print("Original :", sentence)
    print("Corrected:", corrected)
    print("Fluency score:", fluency)
    print("-" * 50)
