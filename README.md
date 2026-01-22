# Generative AI with LangChain 🦜🔗

Welcome to the **Generative AI with LangChain** repository! This project serves as a comprehensive collection of tutorials, code examples, and practical implementations designed to master Generative AI applications using the LangChain framework.

Whether you are exploring Large Language Models (LLMs), building chatbots, or implementing Retrieval-Augmented Generation (RAG) systems, this structured curriculum covers essential components and advanced techniques.

## 📚 Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Technologies & Tools](#technologies--tools)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Setup](#environment-setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## 🧐 Overview

This repository is organized into sequential modules, guiding you from the basics of LangChain models to building complex applications like a YouTube Video Chatbot. Each folder contains specific topics and runnable code examples.

## 📂 Repository Structure

| Module | Description |
| :--- | :--- |
| **1_LangchainModels** | Exploration of LLMs, Chat Models, and Embedding Models including OpenAI, Gemini, and Anthropic. |
| **2_LangchainPrompts** | Techniques for effective prompt engineering using PromptTemplates and ChatPromptTemplates. |
| **3_LangchainStructuredOutput** | Handling structured outputs and ensuring type-safe responses from models. |
| **4_LangchainOutputParsers** | Parsing raw model outputs into usable formats (JSON, Lists, etc.). |
| **5_LangchainChains** | Building sequences of calls (Chains) to perform complex tasks. |
| **6_LangchainRunnables** | Leveraging the LangChain Expression Language (LCEL) for composable chains. |
| **7_LangchainDocumentLoaders** | Loading data from various sources (PDFs, Web, etc.) for processing. |
| **8_LangchainTextSplitters** | Splitting large documents into manageable chunks for embeddings. |
| **9_LangchainVectorStores** | Storing and searching embeddings using Vector Databases like ChromaDB and FAISS. |
| **10_LangchainRetrievers** | Advanced retrieval techniques to fetch relevant context for LLMs. |
| **11_RAG** | End-to-end Retrieval-Augmented Generation examples, including a **YouTube Chatbot**. |

## 🛠 Technologies & Tools

- **Core Framework**: [LangChain](https://python.langchain.com/)
- **LLMs & APIs**: OpenAI (GPT-4), Google Gemini (PaLM), Anthropic (Claude), HuggingFace.
- **Vector Databases**: ChromaDB, FAISS.
- **Utilities**: NumPy, Pandas, Scikit-learn, Beautiful Soup, PyPDF.
- **Frontend**: Streamlit (for building interactive apps).
- **Environment**: Python-dotenv.

## 🚀 Getting Started

Follow these steps to set up the project locally.

### Prerequisites

- Python 3.10+ installed on your machine.
- API Keys for the providers you intend to use (e.g., `OPENAI_API_KEY`, `GOOGLE_API_KEY`).

### Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/MdTalha17/GenerativeAI.git
    cd GenerativeAI
    ```

2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Environment Setup

Create a `.env` file in the root directory to store your API keys securely. You can refer to the `requirements.txt` to see which packages require keys (e.g., OpenAI, Google, Anthropic).

```env
OPENAI_API_KEY="your-openai-api-key"
GOOGLE_API_KEY="your-google-api-key"
ANTHROPIC_API_KEY="your-anthropic-api-key"
HF_TOKEN="your-huggingface-token"
```

## 🏃 Usage

Navigate to any specific module folder and run the Python scripts or Jupyter notebooks.

**Example: Running a Chat Model script**
```bash
cd 1_LangchainModels
# Run specific python scripts
python test.py 
```

**Example: Running the Streamlit Chatbot**
```bash
cd 11_RAG/YoutubeChatbot
streamlit run rag_chatbot.ipynb 
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the terms of the [LICENSE](LICENSE) file.