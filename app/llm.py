from functools import lru_cache

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


MODEL_NAME = "google/flan-t5-base"


@lru_cache(maxsize=1)
def get_model():

    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_NAME
    )

    model = AutoModelForSeq2SeqLM.from_pretrained(
        MODEL_NAME
    )

    return tokenizer, model


def generate_answer(question, context):

    tokenizer, model = get_model()

    prompt = f"""
You are a helpful enterprise knowledge assistant.

Answer the user's question using ONLY the information in the
provided document context.

If the question asks what a document is about, summarize the
main topics found in the context.

Give a clear answer in 2 to 5 sentences.

Do not answer with only a title or a few words.

DOCUMENT CONTEXT:
{context}

USER QUESTION:
{question}

ANSWER:
"""

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=1024
    )

    outputs = model.generate(
        **inputs,
        max_new_tokens=150,
        min_new_tokens=20,
        num_beams=4,
        early_stopping=True
    )

    answer = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return answer.strip()