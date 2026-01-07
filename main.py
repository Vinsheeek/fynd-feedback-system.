from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import json
from pathlib import Path
from collections import defaultdict


DATA_FILE = Path("feedback_results.json")


app = FastAPI()

# ---------- MODELS (Put class here) ----------
class FeedbackRequest(BaseModel):
    review_text: str
    predicted_stars: Optional[int] = None
    actual_stars: Optional[int] = None
    explanation: Optional[str] = None
    prompt_version: Optional[str] = "A"

# ---------- ROUTES ----------
@app.get("/")
def home():
    return {"message": "Fynd Feedback System API running 🚀"}


@app.post("/submit-feedback")
def submit_feedback(data: FeedbackRequest):

    entry = data.model_dump()

    # load existing file
    if DATA_FILE.exists():
        existing = json.loads(DATA_FILE.read_text())
    else:
        existing = []

    # append new record
    existing.append(entry)

    # save file
    DATA_FILE.write_text(json.dumps(existing, indent=4))

    return {
        "status": "saved",
        "entries": len(existing)
    }

@app.get("/summary")
def get_summary():

    if not DATA_FILE.exists():
        return {"message": "No feedback data found"}

    data = json.loads(DATA_FILE.read_text())

    results = defaultdict(lambda: {
        "total_entries": 0,
        "correct": 0,
        "incorrect": 0,
        "accuracy_percent": 0,
        "star_counts": defaultdict(int),
        "examples": []
    })

    for entry in data:
        v = entry.get("prompt_version", "Unknown")

        predicted = entry.get("predicted_stars")
        actual = entry.get("actual_stars")

        results[v]["total_entries"] += 1
        results[v]["star_counts"][predicted] += 1

        # classification accuracy only when actual exists
        if actual is not None:
            if predicted == actual:
                results[v]["correct"] += 1
            else:
                results[v]["incorrect"] += 1

                # store only 3 mistakes per prompt
                if len(results[v]["examples"]) < 3:
                    results[v]["examples"].append({
                        "review": entry["review_text"],
                        "predicted": predicted,
                        "actual": actual,
                        "explanation": entry.get("explanation", "")
                    })

    # compute accuracy %
    for v in results:
        total_eval = results[v]["correct"] + results[v]["incorrect"]

        if total_eval > 0:
            results[v]["accuracy_percent"] = round(
                (results[v]["correct"] / total_eval) * 100, 2
            )

    return results
