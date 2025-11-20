# Assignment: Exploring the Apriori Algorithm

##  Goal

In this assignment, you will explore how the **Apriori algorithm** behaves on:

- a **sparse** market-basket dataset, and
- a **dense** market-basket dataset,

and how runtime + frequent itemsets change when you vary the **minimum support threshold**.

You do **not** need to implement Apriori — the code is provided.  
You only need to understand parts of it, run experiments, and reflect on results.

---

# 📁 Part 0 — Setup

1. Clone or download the repository.
2. Make sure the folder contains:

```
apriori.py
streamlit_app.py
data/market_sparse.csv
data/market_dense.csv
assignment.md
```

3. Install required libraries:

```bash
pip install streamlit pandas
```

4. Run the demo:

```bash
streamlit run streamlit_app.py
```

---

#  Part 1 — Understand the Apriori Code

Create a file named **answers_part1.md** and answer:

### 1️⃣ Candidate Generation  
- Which function generates **candidate k-itemsets (Ck)** from L(k−1)?  
- Describe the join step in 1–2 sentences.

### 2️⃣ Pruning  
- Which function applies the **Apriori Principle**?  
- Explain how infrequent subsets are used to prune.

### 3️⃣ Support Counting  
- Which function scans transactions to count support?  
- How does the membership test work?

---

#  Part 2 — Experiments: Sparse vs Dense

Use the Streamlit app to run experiments on:

- `market_sparse.csv`
- `market_dense.csv`

Try at least **three** min_support values (e.g., 0.40, 0.30, 0.20).

Record for each run:

- Dataset  
- min_support  
- Runtime (s)  
- Number of frequent itemsets  
- Max k  

Use a table such as:

| Dataset | min_support | Runtime (s) | # Frequent itemsets | Max k |
|--------|------------:|------------:|---------------------:|------:|
| sparse | 0.40        |             |                      |       |
| dense  | 0.30        |             |                      |       |

Save as **results.csv**.

---

#  Part 3 — Reflection (Short Answer)

Create **answers_part3.md** with 5–8 sentences addressing:

### 1️⃣ Effect of lowering support  
What happens to runtime, number of itemsets, and max k?

### 2️⃣ Sparse vs Dense  
How do the effects differ?

### 3️⃣ Match with theory  
Does this match Apriori’s expected behavior?

---

# 📤 What to Submit

```
answers_part1.md
results.csv or answers_part2.md
answers_part3.md
```

---
