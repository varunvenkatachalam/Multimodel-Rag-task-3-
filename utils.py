import openai

# Use the OpenAI API key for ChatGPT
openai.api_key = "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"

def generate_response(query, relevant_text, relevant_images):
    context = "\n".join(relevant_text)
    prompt = f"""Context: {context}

    Query: {query}

    Relevant image paths: {relevant_images}

    Please provide a response to the query based on the given context and mention any relevant images by their paths.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers questions based on the provided context."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000
    )

    return response['choices'][0]['message']['content']

def multi_modal_rag(pdf_path, query):
    try:
        text_content, image_list = parse_pdf(pdf_path)
        process_text(text_content)
        process_images(image_list)

        relevant_text, relevant_images = process_query(query)
        response = generate_response(query, relevant_text, relevant_images)
        
        return {
            'response': response,
            'relevant_text': relevant_text,
            'relevant_images': relevant_images
        }
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise
