import streamlit as st
from datetime import datetime

# ---------- MENU DATA ----------
Category = {
    "Meals": [("Kerala Veg Meals", 70), ("Fish Curry Meals", 110), ("Beef Curry Meals", 130), ("Chicken Curry Meals", 120)],
    "Non Veg Dishes": [("Kerala Chicken Roast", 140), ("Nadan Beef Fry", 150), ("Fish Fry (Pomfret/Avoli)", 160), ("Egg Curry", 60)],
    "Veg Dishes": [("Thoran (Cabbage/Beans)", 30), ("Avial", 40), ("Sambar", 25), ("Parippu Curry", 25)],
    "Snacks": [("Pazham Pori", 15), ("Uzhunnu Vada", 12), ("Parippu Vada", 10), ("Egg Puffs", 20)],
    "Beverages": [("Chaya (Tea)", 10), ("Kattan Chaya", 8), ("Nannari Sarbath", 15), ("Lime Juice", 20)]
}

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="RestoCafe Ordering System", page_icon="🍴", layout="centered")

st.markdown("""
    <h1 style='text-align: center; color: #d6336c;'>🍽️ RestoCafe Ordering System</h1>
    <p style='text-align: center;'>Welcome to our cozy cafe! Choose your items and we'll generate your bill.</p>
    <hr>
""", unsafe_allow_html=True)

# ---------- SESSION STATE ----------
if 'cart' not in st.session_state:
    st.session_state.cart = {}

# ---------- CUSTOMER NAME ----------
customer_name = st.text_input("👤 Enter your name:")

# ---------- SELECT CATEGORY ----------
category_selected = st.selectbox("📂 Select a food category:", list(Category.keys()))

# ---------- SHOW ITEMS ----------
items = Category[category_selected]
item_names = [item[0] for item in items]
selected_item = st.selectbox("🍛 Select an item:", item_names)
price = [price for name, price in items if name == selected_item][0]

qty = st.number_input("🔢 Select quantity:", min_value=1, step=1)

# ---------- ADD TO CART ----------
if st.button("➕ Add to Cart"):
    if selected_item in st.session_state.cart:
        st.session_state.cart[selected_item][0] += qty
    else:
        st.session_state.cart[selected_item] = [qty, price]
    st.success(f"✅ Added {qty} x {selected_item} to your cart!")

# ---------- DISPLAY CART ----------
if st.session_state.cart:
    st.subheader("🛒 Your Cart")
    cart_data = []
    total = 0
    for item, (qty, price) in st.session_state.cart.items():
        subtotal = qty * price
        total += subtotal
        cart_data.append([item, qty, price, subtotal])

    st.table(
        {
            "Item": [x[0] for x in cart_data],
            "Quantity": [x[1] for x in cart_data],
            "Unit Price (₹)": [x[2] for x in cart_data],
            "Total (₹)": [x[3] for x in cart_data],
        }
    )

    # ---------- BILLING ----------
    if st.button("🧾 Generate Bill"):
        st.success("🎉 Order Placed Successfully!")
        st.markdown("---")
        st.markdown(f"### 🧾 Final Bill for {customer_name}")
        st.markdown(f"**🕒 Date & Time:** {datetime.now().strftime('%d-%m-%Y %I:%M %p')}")
        st.markdown("---")
        for item, (qty, price) in st.session_state.cart.items():
            st.markdown(f"- **{item}** x {qty} = ₹{qty * price}")
        st.markdown(f"### 💰 Grand Total: ₹{total}")
        st.markdown("---")
        st.balloons()
else:
    st.info("Your cart is empty. Start adding some items!")

# ---------- RESET ----------
if st.button("🧹 Clear Cart"):
    st.session_state.cart = {}
    st.rerun()
