from transformers import pipeline

# Load the summarization pipeline only once when the server starts
summarizer = pipeline(
    "summarization",
    model="google/flan-t5-base"
)


def summarize_text(text: str):
    try:
        result = summarizer(
            text,
            max_length=120,
            min_length=40,
            do_sample=False
        )

        return result[0]["summary_text"]

    except Exception as e:
        return f"Error: {str(e)}"