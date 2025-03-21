import streamlit as st

data = [
    {"name": "Card 1", "description": "This is the first card.", "badges": ["🔧 Tool", "⭐ Favorite"], "image": "https://placehold.co/400x400"},
    {"name": "Card 2", "description": "This is the second card.", "badges": ["📦 Package", "✅ Completed"], "image": "https://placehold.co/400x400"},
    {"name": "Card 3", "description": "This is the third card.", "badges": ["📝 Note", "🔒 Secure"], "image": "https://placehold.co/400x400"},
    {"name": "Card 4", "description": "This is the fourth card.", "badges": ["📈 Growth", "🚀 Launch"], "image": "https://placehold.co/400x400"},
    {"name": "Card 5", "description": "This is the fifth card.", "badges": ["💡 Idea", "🔍 Research"], "image": "https://placehold.co/400x400"},
]

st.title("Search")

search_term = st.text_input("Search for a card:", "")

filtered_data = [item for item in data if search_term.lower() in item["name"].lower()]

for item in filtered_data:
    with st.container(border=True):
        col1, col2 = st.columns([1, 6])

        with col1: 
            st.image(item["image"], width=170)

        with col2:
            st.write(f"{item['name']}")
            if st.button("Click Me", key=item["name"]):
                st.success(f"You clicked on {item['name']}!")

            st.write(item["description"])

            badges = " ".join(item["badges"])
            st.markdown(f"<span style='color: #007BFF; font-weight: bold;'>{badges}</span>", unsafe_allow_html=True)