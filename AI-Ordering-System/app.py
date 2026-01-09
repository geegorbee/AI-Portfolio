import streamlit as st
import pandas as pd
from datetime import datetime
import os
from openai import OpenAI

st.set_page_config(page_title="Berg's AI Ordering (Demo)", page_icon="🍦", layout="centered")

# --- Simple in-memory menu (swap to JSON later) ---
MENU = pd.DataFrame([
    {"item":"Vanilla", "type":"flavor", "vegan":False, "gluten_free":True, "price":3.50},
    {"item":"Chocolate", "type":"flavor", "vegan":False, "gluten_free":True, "price":3.75},
    {"item":"Strawberry", "type":"flavor", "vegan":False, "gluten_free":True, "price":3.75},
    {"item":"Blueberry", "type":"flavor", "vegan":False, "gluten_free":True, "price":3.85},
    {"item":"Mango Sorbet", "type":"flavor", "vegan":True, "gluten_free":True, "price":3.95},
    {"item":"Waffle Cone", "type":"cone", "vegan":False, "gluten_free":False, "price":1.25},
    {"item":"Sugar Cone", "type":"cone", "vegan":False, "gluten_free":False, "price":1.00},
    {"item":"GF Cone", "type":"cone", "vegan":False, "gluten_free":True, "price":1.50},
    {"item":"Hot Fudge", "type":"topping", "vegan":False, "gluten_free":True, "price":0.75},
    {"item":"Sprinkles", "type":"topping", "vegan":True, "gluten_free":True, "price":0.50},
    {"item":"Crushed Oreos","type":"topping", "vegan":False, "gluten_free":False, "price":0.65},
])

# --- LLM setup (optional). If no key is set, we use a rule-based fallback ---
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_KEY) if OPENAI_KEY else None

def menu_context_from_df(df: pd.DataFrame) -> str:
    rows = []
    for _, r in df.iterrows():
        rows.append(
            "{item} ({typ}): ${price:.2f} | vegan={vegan} | gluten_free={gf}".format(
                item=r["item"],
                typ=r["type"],
                price=float(r["price"]),
                vegan=bool(r["vegan"]),
                gf=bool(r["gluten_free"]),
            )
         )
    return "\n".join(rows)

MENU_CONTEXT = menu_context_from_df(MENU)

SYSTEM_PROMPT = """You are Berg's Ice Cream ordering assistant.
Answer ONLY about Berg's menu, toppings, cones, specials, dietary info (vegan/gluten-free), hours, and pickup/delivery instructions.
If you don't see an item in the provided menu context, say it's not available.
Keep answers short, helpful, and friendly. Do not take payments or ask for sensitive info. Offer a suggested order when appropriate.
"""

def rule_based_answer(q: str) -> str:
    ql = (q or "").lower()
    parts = []
    # quick dietary checks
    if "vegan" in ql:
        vegan_items = MENU[MENU["vegan"] == True]["item"].tolist()
        parts.append("Vegan options: " + (", ".join(vegan_items) if vegan_items else "none listed."))
    if "gluten" in ql:
        gf_items = MENU[MENU["gluten_free"] == True]["item"].tolist()
        parts.append("Gluten-free items: " + (", ".join(gf_items) if gf_items else "none listed."))
    # simple contains
    hits = MENU[MENU["item"].str.lower().str.contains(ql, na=False)] if ql else pd.DataFrame()
    if not parts and not hits.empty:
        parts.append("Matching items: " + ", ".join(hits["item"].tolist()))
    if not parts:
        parts.append("I can help with flavors, cones, toppings, vegan/gluten-free, and building an order.")
    return " ".join(parts)

def llm_answer(q: str) -> str:
    if not client:
        return rule_based_answer(q)

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": f"""Here is the current menu (source of truth):
---
{MENU_CONTEXT}
---

Customer question: {q}
Remember: if something isn't in the menu, say it's not available."""
        },
    ]
    try:
        # You can use any capable model you have access to; small/cheap works fine for this.
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.2,
        )
        return resp.choices[0].message.content.strip()
    except Exception as e:
        # Fall back gracefully if API issues
        return rule_based_answer(q) + f" (Note: LLM unavailable: {e})"
def filter_menu(query: str):
    q = (query or "").lower().strip()
    df = MENU.copy()

    if "vegan" in q:
        df = df[df["vegan"] == True]

    if "gluten" in q:
        df = df[df["gluten_free"] == True]

    if "topping" in q:
        df = df[df["type"] == "topping"]

    if "cone" in q:
        df = df[df["type"] == "cone"]

    # basic keyword match
    known = {"vegan","gluten","gluten free","cone","topping","menu","flavors","flavours"}
    if q and q not in known:
        df = df[df["item"].str.lower().str.contains(q)]

    return df

def recommend(flavor: str):
    f = flavor.lower()
    if "chocolate" in f:
        return ["Hot Fudge", "Sprinkles"]
    if "vanilla" in f:
        return ["Hot Fudge", "Crushed Oreos"]
    if "mango" in f:
        return ["Sprinkles"]
    if "blueberry" in f:
        return ["Sprinkles"]
    if "strawberry" in f:
        return ["Sprinkles", "Hot Fudge"]
    return ["Sprinkles"]

st.title("🍦 Berg's AI Ordering (Demo)")
st.write("Ask questions, browse the menu, and build an order. (Demo only – no payments)")

# --- Q&A / search ---
st.subheader("Ask a question or search the menu")
q = st.text_input("Try: 'vegan', 'gluten', 'toppings', 'chocolate', 'cone', or a flavor name")
results = filter_menu(q)
st.dataframe(
    results[["item","type","vegan","gluten_free","price"]]
      .rename(columns={"item":"Item","type":"Type","vegan":"Vegan","gluten_free":"Gluten-free","price":"$"}),
    width="stretch"
)

# --- Conversational assistant ---
st.subheader("Chat with Berg's Assistant")

if "chat" not in st.session_state:
    st.session_state["chat"] = [
        {
            "role": "assistant",
            "content": "Hi! Ask me about flavors, toppings, vegan or gluten-free options, or let me help build an order."
        }
    ]

for m in st.session_state["chat"]:
    with st.chat_message(m["role"]):
       st.markdown(m["content"])

user_msg = st.chat_input("Ask a question (e.g., 'Do you have dairy-free?' or 'What goes well with chocolate?')")
if user_msg:
    st.session_state["chat"].append({"role": "user", "content": user_msg})
    with st.chat_message("user"):
        st.markdown(user_msg)

    answer = llm_answer(user_msg)
    st.session_state["chat"].append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
       st.markdown(answer)

# --- Build an order ---
st.subheader("Build your order")
flavors = MENU[MENU["type"]=="flavor"]["item"].tolist()
cones = MENU[MENU["type"]=="cone"]["item"].tolist()
tops = MENU[MENU["type"]=="topping"]["item"].tolist()

col1, col2 = st.columns(2)
with col1:
    flavor = st.selectbox("Choose a flavor", flavors)
    cone = st.selectbox("Choose a cone", cones)
with col2:
    qty = st.number_input("Quantity", 1, 20, 1)
    chosen_tops = st.multiselect("Toppings (optional)", tops)

st.caption(f"Suggestions for **{flavor}**: {', '.join(recommend(flavor))}")

def price_of(name):
    return float(MENU[MENU["item"]==name]["price"].iloc[0])

subtotal = qty * (price_of(flavor) + price_of(cone) + sum(price_of(t) for t in chosen_tops))

cust_name = st.text_input("Your name")
pickup = st.selectbox("Pickup or Delivery?", ["Pickup", "Delivery"])
notes = st.text_area("Notes (allergies, time, etc.)")

if "orders" not in st.session_state:
    st.session_state["orders"] = []

if st.button("Add to cart"):
    st.session_state["orders"].append({
        "time": datetime.now().isoformat(timespec="seconds"),
        "name": cust_name or "Guest",
        "flavor": flavor,
        "cone": cone,
        "toppings": chosen_tops,
        "qty": int(qty),
        "pickup": pickup,
        "notes": notes,
        "subtotal": round(subtotal, 2),
    })
    st.success("Added to cart!")

st.subheader("🧾 Cart")
if st.session_state["orders"]:
    df = pd.DataFrame(st.session_state["orders"])
    st.table(df[["time","name","qty","flavor","cone","toppings","pickup","subtotal"]])
    total = round(df["subtotal"].sum(), 2)
    st.write(f"**Total:** ${total:.2f}")
    if st.button("Place order (demo)"):
        st.info("Order captured (demo). In production, this would send to POS / print a ticket / email.")
else:
    st.write("Your cart is empty.")

st.markdown("---")
st.caption("Demo: local data only. Next steps: POS integration, real-time specials, allergy filtering, SMS confirmations.")