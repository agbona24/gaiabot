import requests
import random
import time
import logging
from typing import List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("chatbot.log"),
        logging.StreamHandler()
    ]
)

# Configuration
BASE_URL = "https://tejumola.gaia.domains"  # Updated base URL
MODEL = "qwen2-0.5b-instruct"
MAX_RETRIES = 100  # Essentially infinite retries
RETRY_DELAY = 5  # Seconds between retries
QUESTION_DELAY = 1  # Seconds between successful questions

# Add your own questions here
QUESTIONS = [
    "Explain in extreme detail the quantum mechanical implications of consciousness in biological systems, including potential mathematical frameworks and experimental verification methods.",
    "Describe the complete process of protein folding from first principles, including all relevant thermodynamic considerations and computational modeling approaches.",
    "Develop a comprehensive comparison between classical machine learning architectures and quantum neural networks, including mathematical formulations and practical implementation challenges.",
    "Outline a complete framework for unifying general relativity with quantum field theory, including detailed mathematical proofs and experimental validation procedures.",
    "Explain the entire process of cosmological structure formation from the Big Bang to modern galaxy clusters, including dark matter dynamics and baryonic feedback mechanisms.",
    "Describe in meticulous detail the biochemical pathways involved in neurodegenerative diseases and propose novel therapeutic approaches using CRISPR-based gene editing technologies.",
    "Formulate a complete ethical framework for artificial general intelligence development, including safety protocols, value alignment strategies, and societal impact assessments.",
    "Explain the full mathematical derivation of the Navier-Stokes equations from first principles and propose novel numerical methods for solving turbulent flow problems.",
    "Develop a comprehensive analysis of global economic systems under post-scarcity conditions, including resource allocation models and societal structure transformations.",
    "Describe the complete process of developing a nuclear fusion reactor prototype, including plasma containment strategies, materials science challenges, and energy conversion systems.",
    "Explain in exhaustive detail the epigenetic mechanisms underlying cellular aging and propose experimental interventions for reversing biological age markers.",
    "Formulate a complete theory of everything incorporating consciousness, quantum gravity, and emergent spacetime phenomena with mathematical rigor.",
    "Develop a detailed comparative analysis of all major world religions' cosmological models and their philosophical implications for modern physics.",
    "Explain the complete process of developing artificial photosynthesis systems with higher efficiency than natural photosynthesis, including material selection and catalytic mechanisms.",
    "Describe in meticulous detail the implementation of a fully homomorphic encryption system resistant to quantum computing attacks, including mathematical proofs and performance benchmarks.",
    "Develop a comprehensive plan for Mars colonization including terraforming strategies, ecosystem design, and long-term human adaptation mechanisms.",
    "Explain the complete mathematical framework of string theory including compactification processes and connections to observable particle physics phenomena.",
    "Describe in extreme detail the neurobiological basis of human creativity, including neurotransmitter dynamics, neural network patterns, and evolutionary origins.",
    "Formulate a complete solution to the P vs NP problem with rigorous mathematical proof and computational complexity implications.",
    "Develop a comprehensive analysis of climate change feedback loops including tipping points, mitigation strategies, and geoengineering proposals.",
    "Explain in exhaustive detail the process of developing room-temperature superconductors, including material discovery approaches and theoretical underpinnings.",
    "Describe the complete biochemical pathway of prion propagation and propose novel therapeutic interventions for transmissible spongiform encephalopathies.",
    "Develop a detailed framework for quantum computing error correction in large-scale fault-tolerant systems, including surface code implementations.",
    "Explain the full process of developing brain-computer interfaces with nanoscale resolution, including neural signal processing and biocompatibility challenges.",
    "Formulate a complete theory of consciousness emergence in artificial neural networks, including phenomenological experience and self-awareness metrics.",
    "Describe in meticulous detail the process of developing antiviral therapies using phage display libraries and computational protein design.",
    "Develop a comprehensive model of dark energy's influence on cosmic expansion, including modified gravity theories and observational constraints.",
    "Explain the complete mathematical formulation of quantum machine learning algorithms including complexity analysis and practical implementation challenges.",
    "Describe in extreme detail the process of cellular reprogramming for organ regeneration, including epigenetic remodeling and tissue engineering techniques.",
    "Formulate a complete solution to the black hole information paradox including holographic principle applications and quantum gravity implications."
]


def chat_with_ai(api_key: str, question: str) -> str:
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    messages = [
        {"role": "user", "content": question}
    ]

    data = {
        "model": MODEL,
        "messages": messages,
        "temperature": 0.7
    }

    for attempt in range(MAX_RETRIES):
        try:
            logging.info(f"Attempt {attempt+1} for question: {question[:50]}...")
            response = requests.post(
                f"{BASE_URL}/v1/chat/completions",
                headers=headers,
                json=data,
                timeout=30
            )

            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]

            logging.warning(f"API Error ({response.status_code}): {response.text}")
            time.sleep(RETRY_DELAY)

        except Exception as e:
            logging.error(f"Request failed: {str(e)}")
            time.sleep(RETRY_DELAY)

    raise Exception("Max retries exceeded")

def run_bot(api_key: str):
    while True:  # Outer loop to repeat the questions indefinitely
        random.shuffle(QUESTIONS)
        logging.info(f"Starting chatbot with {len(QUESTIONS)} questions in random order")

        for i, question in enumerate(QUESTIONS, 1):
            logging.info(f"\nProcessing question {i}/{len(QUESTIONS)}")
            logging.info(f"Question: {question}")

            start_time = time.time()
            try:
                response = chat_with_ai(api_key, question)
                elapsed = time.time() - start_time

                # Print the entire response
                print(f"Answer to '{question[:50]}...':\n{response}")

                logging.info(f"Received full response in {elapsed:.2f}s")
                logging.info(f"Response length: {len(response)} characters")

                # Ensure the script waits for the full response before proceeding
                time.sleep(QUESTION_DELAY)  # Wait before asking next question

            except Exception as e:
                logging.error(f"Failed to process question: {str(e)}")
                continue

def main():
    print("Title: GaiaAI Chatbot")
    print("Created by: MEFURY")
    print("Twitter: https://x.com/meefury")
    api_key = input("Enter your API key: ")
    run_bot(api_key)

if __name__ == "__main__":
    main()
