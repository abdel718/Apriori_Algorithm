🛒 Apriori Algorithm — Demo & Assignment

This repository contains a complete educational demonstration of the Apriori algorithm, including:

A clean implementation of Apriori (apriori.py)

A Streamlit-based interactive demo (streamlit_app.py)

Two market-basket datasets (sparse and dense)

A hands-on assignment for students (assignment_full.md)

This repo is suitable for:

Teaching Apriori in university courses

Demonstrating association-rule mining

Showing the impact of support thresholds

Comparing sparse vs dense datasets

Running simple experiments and generating rules

📂 Repository Structure

Apriori_Algorithm/
│
├── apriori.py — Apriori algorithm implementation
├── streamlit_app.py — Streamlit demo app
├── assignment_full.md — Full student assignment
│
└── data/
  ├── market_sparse.csv — Sparse dataset
  └── market_dense.csv — Dense dataset

🚀 Running the Streamlit Demo
1. Install dependencies

pip install streamlit pandas

2. Launch the interactive app

streamlit run streamlit_app.py

You will see:

Dataset summary (n, m, avg basket size)

Frequent itemsets based on support threshold

Runtime comparisons

Association rules (support, confidence, lift)

📘 Assignment (for students)

The file assignment_full.md includes:

Understanding the Apriori source code

Running experiments on dense and sparse datasets

Measuring how min_support affects runtime and itemsets

Reflecting on Apriori’s time & space complexity

Students will connect theory, implementation, and real-world behavior.

📊 Datasets
Sparse dataset

Smaller baskets (2–4 items)

Fewer frequent itemsets

Faster Apriori performance

Dense dataset

Larger baskets (5–9+ items)

Many overlapping items

Demonstrates combinational explosion

🧠 What Apriori Demonstrates

Support, confidence, and lift

Candidate generation & pruning

Performance issues on dense data

Impact of support threshold

Level-wise search strategy
