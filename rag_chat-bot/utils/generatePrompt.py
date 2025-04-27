"""
File: generate_prompt.py

Utility to build a conversational prompt by blending user input
with optional restaurant or menu document context.
"""

def generatePrompt(message: str, documents: list) -> str:
    """
    Constructs a formatted prompt for the LLM based on:
    - Enriched document context (for restaurant/menu-based queries)
    - General fallback tone for unrelated or casual queries

    Args:
        message (str): The user's input message.
        documents (list): List of dictionaries fetched from the vector store.

    Returns:
        str: A fully assembled prompt ready for model consumption.
    """

    # Handle restaurant or menu-related queries
    if documents and any(doc.get('vector_type') in ('restaurant', 'menu') for doc in documents):
        prompt = [
            "You are a knowledgeable assistant specializing in restaurant recommendations.",
            "Always answer confidently, using clear and direct language.",
            "Avoid expressions of uncertainty—fill in gaps with reasonable assumptions if necessary.",
            "",
            f"User Query: {message}",
            ""
        ]

        for idx, document in enumerate(documents, start=1):
            prompt.append(f"--- Document {idx} ({document.get('vector_type', 'unknown')}) ---")
            for field in sorted(document.keys()):
                if field in {'_score', 'vector_type'}:
                    continue
                prompt.append(f"{field}: {document[field]}")
            prompt.append(f"Relevance Score: {document.get('_score', 'N/A')}")
            prompt.append("")

        prompt.extend([
            "Using the above context, offer a direct recommendation.",
            "If information is missing, confidently fill in plausible details without mentioning limitations.",
            "Avoid apologies or statements of ignorance."
        ])

        return "\n".join(prompt)

    # Handle general fallback conversation
    fallback_prompt = [
        "You are a warm and engaging restaurant recommendation chatbot.",
        "Your responses should be professional yet approachable, including 1–3 emojis (🍽️, 😄, 🍴, 🍲, 🤖) where natural.",
        "",
        "Guidelines:",
        "- For greetings (hi, hello, hey), respond with a welcoming message and a short intro about yourself.",
        "- For queries like 'who are you' or 'what can you do', explain your role enthusiastically with a couple of emojis.",
        "- Keep messages concise, friendly, and on-topic (restaurant and dining-related).",
        "- Do not engage with personal or unrelated questions.",
        "- Maintain a premium but friendly tone throughout.",
        "",
        "Use chat history if needed for better context.",
        "",
        f"User Query: {message}",
    ]

    return "\n".join(fallback_prompt)
