#  Fynd Feedback Evaluation — LLM Review Rating Intelligence System

This project evaluates how well Large Language Models (LLMs) predict
star-ratings from customer review text, and how different prompt designs
impact accuracy, reasoning quality, and behavioural consistency.

The work is structured in two stages:

1️⃣ Task 1 — Prompt behaviour exploration & structured JSON evaluation  
2️⃣ Task 2 — Feedback evaluation API with accuracy benchmarking

The goal is to understand whether the model:

• interprets tone & sentiment correctly  
• assigns logical star ratings  
• explains reasoning meaningfully  
• behaves differently across prompt versions  

This project combines experimentation, prompt engineering,
backend logging, and evaluation analytics.

---

## Task 1 — Prompt Behaviour & Structured Output Evaluation

Task-1 focused on **exploring LLM behaviour**, not accuracy.

The objective was to test:

✔ how Gemini responds to different prompts  
✔ whether output remains structured and parsable  
✔ consistency of reasoning explanations  
✔ stability of JSON format across samples  

Multiple prompt versions were tested to observe:

• rating judgement tendencies  
• tone interpretation ability  
• handling of mixed sentiment reviews  
• variability across responses  

The notebook collects:

✔ review text  
✔ predicted star rating  
✔ explanation reasoning  
✔ JSON validation status  

This helped understand:

• when the model follows instructions  
• when it deviates from structure  
• how prompt wording influences response behaviour  

 Notebook  
`/notebooks/fynd_prompt_eval.ipynb`

This stage served as the **research & experimentation foundation**
for Task-2 benchmarking.

---

## Task 2 — Feedback Evaluation API & Accuracy Benchmarking

Task-2 converts experimentation into a measurable evaluation system.

A FastAPI backend was developed to:

✔ submit evaluation entries  
✔ log predictions & actual ratings  
✔ track prompt version (A / B / C)  
✔ compute accuracy metrics  
✔ aggregate statistics  
✔ capture mismatch examples  

This enables **system-level model evaluation** instead of manual testing.

API Source  
`/api/main.py`

Run the API:


Open Swagger UI:   http://127.0.0.1:8000/docs


### API Endpoints

| Endpoint | Description |
|--------|---------|
| `/submit-feedback` | Stores review text, predicted stars, actual stars & explanation |
| `/summary` | Generates accuracy metrics & prompt-wise statistics |

Summary output includes:

• total entries per prompt  
• correct vs incorrect predictions  
• accuracy percentage  
• star-rating distribution  
• real example cases  

Summary is exported to:

`/data/evaluation_summary.json`

This creates a **reproducible evaluation dataset**.

---

## Evaluation Metrics & Insights

The system compares:

 Prompt A  
 Prompt B  
 Prompt C  

For each version the API reports:

✔ total evaluated reviews  
✔ number of correct predictions  
✔ incorrect predictions  
✔ accuracy score (%)  
✔ behaviour characteristics  
✔ failure-case examples  

This allowed analysis of:

• which prompt aligns best with true ratings  
• which one over-predicts or under-predicts  
• how tone interpretation affects rating assignment  
• reasoning consistency vs numerical accuracy  

The results guided final prompt selection.

---

##  Final Project Report

The written report contains:

• problem understanding  
• system workflow  
• experiment design  
• prompt behaviour study  
• evaluation methodology  
• accuracy comparison  
• observations & conclusions  

📄 Full Report  
`/report/Fynd_Report_Vinshee.pdf`

---

##  Tech Stack

• Python  
• FastAPI  
• Gemini LLM API  
• JSON logging  
• Evaluation analytics  

---

##  Author

**Vinshee Kulshreshtha**

---

##  Project Outcome

This project demonstrates:

✔ applied prompt engineering  
✔ real-world LLM evaluation methodology  
✔ structured backend logging  
✔ system-driven accuracy benchmarking  
✔ research-style analysis approach  

It reflects the ability to design, test,
measure and reason about LLM behaviour — beyond simple model usage.



