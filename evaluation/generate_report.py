import os
import pandas as pd

RESULTS_FILE = "evaluation/results.csv"
REPORT_FILE = "evaluation/evaluation_report.txt"

if not os.path.exists(RESULTS_FILE):
    raise FileNotFoundError(
        "No evaluation results found. Run evaluate_rag.py first."
    )

df = pd.read_csv(RESULTS_FILE)

if df.empty:
    raise ValueError("Evaluation results file is empty.")

avg_faithfulness = df["faithfulness"].mean()
avg_relevancy = df["answer_relevancy"].mean()

report = f"""
========================================
       RAG EVALUATION REPORT
========================================

Questions Evaluated : {len(df)}

Average Faithfulness:
{avg_faithfulness:.4f}

Average Answer Relevancy:
{avg_relevancy:.4f}

----------------------------------------
PER-QUESTION RESULTS
----------------------------------------
"""

for _, row in df.iterrows():
    report += f"""
Question:
{row['question']}

Faithfulness: {row['faithfulness']:.4f}
Answer Relevancy: {row['answer_relevancy']:.4f}
Status: {row['status']}

----------------------------------------
"""

with open(REPORT_FILE, "w", encoding="utf-8") as f:
    f.write(report)

print(report)
print(f"\nReport saved to: {REPORT_FILE}")