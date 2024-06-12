# Personal Assistant

## Overview

This project is a personal learning assistant application built using OpenAI's GPT-3.5-turbo model. The assistant is designed to help users understand and learn various topics by providing explanations, summaries, and answers to questions.

## Features

- **Interactive Interface**: A simple and user-friendly interface built with Streamlit.
- **AI-Powered Responses**: Uses OpenAI's GPT-3.5-turbo model to generate responses to user prompts.
- **Educational Support**: Assists users in understanding topics, summarizing content, and suggesting additional resources.

## Setup

### Prerequisites

- Python 3.7 or higher
- Streamlit
- OpenAI API Key

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/balytskard/personal_tutor.git
    cd personal_tutor
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Set up your OpenAI API key in Streamlit's secrets management:
    - Create a `.streamlit` directory in the root of your project if it doesn't already exist.
    - Inside the `.streamlit` directory, create a `secrets.toml` file.
    - Add your OpenAI API key to `secrets.toml`:
      ```toml
      [openai]
      api_key = "your-openai-api-key"
      ```

### Running the Application

To run the application, use the following command:
```sh
streamlit run personal_assistant.py
