# streamlit_app.py
import time
from pathlib import Path
import pandas as pd
import streamlit as st

from apriori import apriori, generate_rules, Transaction

DATA_DIR = Path("data")

def load_transactions(path: Path):
    df = pd.read_csv(path)
    transactions = []
    for items_str in df["items"]:
        items = [x.strip() for x in str(items_str).split(",") if x.strip()]
        transactions.append(items)
    return transactions

def dataset_stats(transactions):
    n = len(transactions)
    all_items = sorted({item for t in transactions for item in t})
    m = len(all_items)
    avg_len = sum(len(t) for t in transactions) / n if n > 0 else 0.0
    return n, m, avg_len, all_items

st.set_page_config(page_title="Apriori Demo", page_icon="🛒", layout="wide")
st.title("🛒 Apriori Algorithm Demo")

st.write("Explore Apriori on sparse vs dense datasets. Change the support threshold and observe runtime.")

st.sidebar.header("Settings")
dataset_choice = st.sidebar.radio("Dataset", ("Sparse market basket", "Dense market basket"))
min_support = st.sidebar.slider("Minimum support", 0.05, 0.8, 0.3, 0.05)
min_conf = st.sidebar.slider("Minimum confidence", 0.1, 1.0, 0.6, 0.05)
min_lift = st.sidebar.slider("Minimum lift", 0.5, 3.0, 1.0, 0.1)
run_button = st.sidebar.button("Run Apriori")

data_path = DATA_DIR / ("market_sparse.csv" if dataset_choice == "Sparse market basket" else "market_dense.csv")
transactions = load_transactions(data_path)
n, m, avg_len, all_items = dataset_stats(transactions)

st.subheader("📦 Dataset summary")
c1, c2, c3 = st.columns(3)
c1.metric("Transactions (n)", n)
c2.metric("Unique items (m)", m)
c3.metric("Avg basket size (k_avg)", f"{avg_len:.2f}")
st.caption(f"Sample items: {', '.join(all_items[:8])} ...")

if run_button:
    with st.spinner("Running Apriori..."):
        start = time.perf_counter()
        frequent_itemsets = apriori(transactions, min_support=min_support)
        elapsed = time.perf_counter() - start

    if frequent_itemsets:
        sizes = [len(s) for s in frequent_itemsets.keys()]
        max_k = max(sizes)
        st.subheader("Frequent itemsets found")
        st.write(f"Total: {len(frequent_itemsets)}")
        st.write(f"Max itemset size (k): {max_k}")
    else:
        max_k = 0
        st.subheader("No frequent itemsets found")

    st.subheader("⏱ Runtime")
    st.write(f"{elapsed:.3f} seconds")

    if frequent_itemsets:
        rules = generate_rules(frequent_itemsets, min_confidence=min_conf, min_lift=min_lift)
        st.subheader("Top Rules")
        if not rules:
            st.info("No rules passed thresholds.")
        else:
            rows = []
            for ante, cons, sup, conf, lift in rules[:10]:
                rows.append({
                    "Rule": f"{', '.join(sorted(ante))} → {', '.join(sorted(cons))}",
                    "Support": round(sup, 3),
                    "Confidence": round(conf, 3),
                    "Lift": round(lift, 3),
                })
            st.table(pd.DataFrame(rows))
else:
    st.info("Click Run Apriori to begin.")
