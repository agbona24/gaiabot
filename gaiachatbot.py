import requests
import time

# Configuration
BASE_URL = "https://Tejumola.gaia.domains"
MODEL = "qwen2-0.5b-instruct"

# Function to interact with the AI API
def chat_with_ai(prompt):
    url = f"{BASE_URL}/v1/chat/completions"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 500
    }

    try:
        response = requests.post(url, json=data, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "No response received from AI.")
    
    except requests.exceptions.Timeout:
        return "Error: The request timed out. The AI server may be slow or unreachable."
    
    except requests.exceptions.ConnectionError:
        return "Error: Network issue detected. Check your internet connection and try again."
    
    except requests.exceptions.HTTPError as e:
        return f"Error: HTTP {e.response.status_code} - {e.response.text}. The server responded with an issue."
    
    except requests.exceptions.RequestException as e:
        return f"Error: A request error occurred - {str(e)}"
    
    except Exception as e:
        return f"Error: An unexpected issue occurred - {str(e)}"

# List of refined questions
questions = [
    "Explain the quantum mechanical relationship between consciousness and biological systems, detailing mathematical models and experimental validation methods.",
    "Describe the complete process of protein folding from first principles, considering thermodynamics and computational modeling techniques.",
    "Compare classical machine learning architectures with quantum neural networks, including mathematical formulations and practical challenges.",
    "Outline a possible framework for unifying general relativity with quantum field theory, providing mathematical insights and experimental validation.",
    "Explain how cosmological structures formed from the Big Bang to modern galaxies, incorporating dark matter dynamics and baryonic feedback effects.",
    "Detail the biochemical pathways involved in neurodegenerative diseases and suggest potential CRISPR-based therapeutic strategies.",
    "Formulate an ethical framework for developing artificial general intelligence, considering safety measures, value alignment, and societal impact.",
    "Provide a step-by-step mathematical derivation of the Navier-Stokes equations and propose novel numerical methods for turbulence modeling.",
    "Analyze the global economy under post-scarcity conditions, covering resource allocation models and potential societal transformations.",
    "Describe the development of a nuclear fusion reactor prototype, addressing plasma containment, material science, and energy conversion.",
    "Explain the epigenetic mechanisms driving cellular aging and propose experimental interventions for reversing biological markers of aging.",
    "Develop a unified theory of everything integrating consciousness, quantum gravity, and emergent spacetime phenomena with mathematical precision.",
    "Compare major world religions' cosmological models and discuss their philosophical implications for modern physics.",
    "Describe the process of artificial photosynthesis and how it can surpass natural efficiency, considering material selection and catalysis.",
    "Explain how to build a fully homomorphic encryption system resistant to quantum computing attacks, with mathematical proofs and performance benchmarks.",
    "Create a strategic plan for Mars colonization, covering terraforming, ecosystem engineering, and long-term human adaptation strategies.",
    "Provide a detailed mathematical overview of string theory, including compactification and its connection to observable particle physics.",
    "Analyze the neurobiological basis of human creativity, covering neurotransmitter functions, neural activity patterns, and evolutionary origins.",
    "Formulate a solution to the P vs NP problem, including rigorous mathematical proof and its implications for computational complexity.",
    "Examine climate change feedback loops, tipping points, and the feasibility of geoengineering as a mitigation strategy.",
    "Discuss the development of room-temperature superconductors, including theoretical principles and material discovery approaches.",
    "Explain the biochemical mechanisms behind prion diseases and suggest potential therapeutic interventions for treating them.",
    "Develop an advanced error correction framework for large-scale quantum computing, incorporating surface codes and fault tolerance.",
    "Describe the process of creating high-resolution brain-computer interfaces, covering neural signal processing and biocompatibility.",
    "Propose a theory explaining the emergence of consciousness in artificial neural networks, considering self-awareness and computational phenomenology.",
    "Outline the use of phage display libraries and computational protein design for developing antiviral therapies.",
    "Analyze the role of dark energy in cosmic expansion, including its relationship with modified gravity theories and observational constraints.",
    "Provide a mathematical breakdown of quantum machine learning algorithms, focusing on complexity analysis and practical implementation.",
    "Explain how cellular reprogramming enables organ regeneration, detailing epigenetic remodeling and tissue engineering advances.",
    "Propose a resolution to the black hole information paradox, integrating holography, quantum gravity, and entropy considerations."
]

# Looping through questions indefinitely
while True:
    for question in questions:
        print(f"Question: {question}")
        answer = chat_with_ai(question)
        print(f"AI Response: {answer}\n")
        time.sleep(60)  # Wait 1 minute before asking the next question
