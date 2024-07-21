# Medical-Chatbot
A medical chatbot that answers user queries by retrieving relevant information from a collection of medical documents using LangChain, Pinecone, and Meta's Llama2 model.

## Table of Contents

- [Introduction](#medical-chatbot)
- [Methodology](#methodology)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Website Screenshots](#website-screenshots)

## Methodology

The medical chatbot project employs a multi-step approach to deliver accurate and relevant responses to user queries:

1. **Data Ingestion and Processing**
   - The project begins by ingesting and processing a collection of medical PDFs.
   - Text is extracted from these PDFs and split into manageable chunks.

2. **Embedding Generation**
   - The extracted text chunks are embedded using HuggingFace's pre-trained model to capture their semantic meanings.

3. **Storage in Pinecone**
   - The generated embeddings are stored in Pinecone for efficient and scalable vector search.

4. **Response Generation**
   - For generating responses, the chatbot utilizes Meta's Llama2 model.
   - The model queries Pinecone to retrieve the most relevant document snippets based on user input.

5. **Integration with Flask**
   - The entire system is integrated into a Flask web application.
   - This provides an interactive interface for real-time communication with users.

This methodology ensures that the chatbot can process complex medical documents and deliver accurate, contextually relevant responses to user queries.


## Tech Stack

- **Python**
- **LangChain**
- **Flask**
- **Meta Llama2**
- **Pinecone**

## Installation

### Steps

1. **Clone the repository**

    ```bash
    https://github.com/shikharrajat/Medical-Chatbot.git
    cd Medical-Chatbot
    ```

2. **Create a conda environment**

    ```bash
    conda create -n env python=3.8 -y
    conda activate env
    ```

3. **Install the requirements**

    ```bash
    pip install -r requirements.txt
    ```

4. **Create a .env file**

    Create a `.env` file in the root directory and add your Pinecone credentials:

    ```
    PINECONE_API_KEY="your_pinecone_api_key"
    ```

5. **Download the quantized Llama2 model**

    Download the Llama2 model (`llama-2-7b-chat.ggmlv3.q4_0.bin`) from the [HuggingFace link](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main) and place it in the `model` directory.

## Usage

1. **Run the indexing script**

    ```bash
    python store_index.py
    ```

2. **Start the Flask application**

    ```bash
    python app.py
    ```

3. **Open your browser and go to**

    ```bash
    http://localhost:8080
    ```

## Website Screenshots

![Chat Interface 1](https://github.com/shikharrajat/Medical-Chatbot/blob/main/images/chat%20interface%201.png)

![Chat Interface 2](https://github.com/shikharrajat/Medical-Chatbot/blob/main/images/chat%20interface%202.png)
