# JivanMitra: Your AI Elder Companion 🤖

<img src="https://github.com/SiddardhaShayini/JivanMitra-An-AI-Elder-Companion/blob/main/logo.png" alt="Logo" width="200"/>

**JivanMitra** (जीवनमित्र, "Friend for Life") is an empathetic, voice-first AI companion designed to support the elderly in India. It offers companionship, timely reminders, and a simple, accessible interface, helping to combat loneliness and improve daily well-being.

-----

## The Problem: A Growing Epidemic of Loneliness

In India, a significant number of elders face a silent but growing challenge: **loneliness and neglect**. As families become more nuclear and geographical distances grow, many of our seniors find themselves living alone. This isolation leads to severe consequences:

  * **Mental Health Decline:** Increased rates of depression, anxiety, and a feeling of being forgotten.
  * **Physical Health Risks:** Forgetting to take critical medications on time, missing meals, and a lack of motivation for physical activity.
  * **The Digital Divide:** Modern solutions are often app-based and complex, leaving behind elders who are not digitally literate.

This issue affects not just the elders themselves but also their loving families who struggle to provide constant support from afar.

-----

## The Solution: An Empathetic Voice Companion

**JivanMitra** is designed to bridge this gap by being a simple, supportive, and culturally-aware friend. It's not just another digital assistant; it's a companion built specifically for the needs of Indian elders.
<img src="https://github.com/SiddardhaShayini/JivanMitra-An-AI-Elder-Companion/blob/main/img.png" alt="Users" width="200"/>

### Key Features ✨

  * **Voice-First Interaction:** No typing, no complicated apps. Users can simply speak to JivanMitra in their natural language (**English, Hindi, or Telugu**).
  * **Emotional Companionship:** JivanMitra can engage in friendly conversations, narrate stories from the Panchatantra or Ramayana, share spiritual quotes from the Gita, or simply listen.
  * **Smart Reminders:** Users can set verbal reminders for medicines, appointments, meals, or daily prayers, and JivanMitra will provide a confirmation.
  * **Culturally Rooted:** The AI's personality is modeled to be like a caring grandchild, deeply rooted in Indian culture, values, and traditions.

-----
![Screenshot 1](https://github.com/SiddardhaShayini/JivanMitra-An-AI-Elder-Companion/blob/main/Screenshot%202025-09-01%20113012.png)
![Screenshot 2](https://github.com/SiddardhaShayini/JivanMitra-An-AI-Elder-Companion/blob/main/Screenshot%202025-09-01%20113137.png)
-----
## How to Run the Application

Follow these steps to set up and run the JivanMitra web application on your local machine.

### Prerequisites

  * Python 3.8+
  * A Google Gemini API Key

### Step 1: Clone the Repository

First, clone this project's repository to your local machine.

```bash
git clone https://github.com/your-username/jivanmitra-app.git
cd jivanmitra-app
```

### Step 2: Set Up the Environment

It's recommended to use a virtual environment to manage dependencies.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

Create a file named `requirements.txt` and add the following lines to it:

```
streamlit
google-generativeai
python-dotenv
streamlit-mic-recorder
gtts
```

Now, install all the required libraries using pip:

```bash
pip install -r requirements.txt
```

### Step 4: Configure Your API Key

1.  Create a new file in the project's root directory named `.env`.
2.  Open the `.env` file and add your Gemini API key in the following format:

<!-- end list -->

```
GEMINI_API_KEY="your_api_key_goes_here"
```

### Step 5: Run the Streamlit App

You're all set\! Run the following command in your terminal to start the application:

```bash
streamlit run app.py
```

The application will automatically open in a new tab in your web browser. You can now interact with JivanMitra\!
