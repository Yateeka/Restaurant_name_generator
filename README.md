# Restaurant Name Generator

This project generates a restaurant name along with a menu based on a cuisine selected by the user. It utilizes **Langchain** to interact with OpenAI's GPT model to generate both a restaurant name and menu items.

## Requirements

Make sure to install the required dependencies. You can use the `requirements.txt` file for installation.

### `requirements.txt`
```plaintext
openai
dotenv
langchain
streamlit
```

To install these packages, run:
```bash
pip install -r requirements.txt
```

## Setup

1. **Create a `.env` file**:  
   In the root directory of the project, create a `.env` file to store your OpenAI API key:
   ```bash
   API_KEY=your-openai-api-key
   ```

2. **Streamlit App**:  
   The application uses Streamlit for the frontend, allowing users to select a cuisine and generate a restaurant name along with menu items.

## How it works

1. **Cuisine Selection**:  
   The user selects a cuisine from the sidebar, which can be one of the following options:
   - "Indian"
   - "Italian"
   - "Mexican"
   - "Lebanese"
   - "Australian"

2. **Generate Restaurant Name and Menu**:  
   Once a cuisine is selected, the app generates:
   - A **restaurant name** based on the selected cuisine.
   - A **menu** with 5 items corresponding to the restaurant name.

3. **Display Results**:  
   After generating the restaurant name and menu, the results are displayed in the main section of the page.

## Running the Application

To run the application locally, use the following command:

```bash
streamlit run main.py
```

This will launch the app in your default web browser.

---

### Code Explanation

1. **Langchain Helper (`lang_chain_helper.py`)**:
   This script contains the `generate_restaurant_name_items` function that interacts with OpenAI's GPT API through Langchain:
   - It takes in a `cusine` as input.
   - The function generates a **restaurant name** using a prompt template for the cuisine.
   - It then generates a **menu** based on the generated restaurant name using another prompt template.
   - These operations are performed using `LLMChain` and `SequentialChain` in Langchain for seamless processing.

2. **Streamlit Frontend (`main.py`)**:
   The main Streamlit app file allows users to interact with the system:
   - Users can choose a cuisine from a dropdown in the sidebar.
   - The app calls the `generate_restaurant_name_items` function to get a name and menu based on the selected cuisine.
   - The results are displayed in a clean and simple interface using Streamlit components like `st.sidebar`, `st.header`, and `st.write`.

---

## Example Output

- **Cuisine**: Italian  
  **Generated Restaurant Name**: "La Dolce Vita"  
  **Menu Items**:
  - Spaghetti Bolognese
  - Margherita Pizza
  - Lasagna
  - Fettuccine Alfredo
  - Tiramisu

---

## Troubleshooting

- **API Key Issues**:  
  Ensure that your `.env` file contains a valid OpenAI API key.
  
- **Missing Packages**:  
  If you encounter errors regarding missing packages, make sure to run `pip install -r requirements.txt` to install all dependencies.
