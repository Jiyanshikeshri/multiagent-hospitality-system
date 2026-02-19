import streamlit as st
from services.travel_service import generate_travel_plan
from memory_manager import (
    save_memory,
    load_memory,
    create_new_session,
    get_all_sessions,
    update_session_title
)

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="AI Travel Planner", layout="wide")
st.title("✈️ AI Travel Planner")

# -----------------------------
# SESSION INIT
# -----------------------------
if "active_session" not in st.session_state:
    st.session_state.active_session = create_new_session()

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("💬 Conversations")

# ➕ New Chat Button
if st.sidebar.button("➕ New Chat"):
    st.session_state.active_session = create_new_session()
    st.rerun()

# Load all sessions
sessions = get_all_sessions()

for session in sessions:
    if st.sidebar.button(
        session["title"], 
        key=session["id"]
    ):
        st.session_state.active_session = session["id"]
        st.rerun()

st.markdown("---")

# -----------------------------
# LOAD CHAT HISTORY
# -----------------------------
chat_history = load_memory(st.session_state.active_session)

for role, message in chat_history:
    if role == "user":
        st.markdown(f"**🧑 You:** {message}")
    else:
        st.markdown(f"**🤖 Assistant:** {message}")

# -----------------------------
# USER INPUT
# -----------------------------
user_input = st.chat_input("Ask your travel assistant...")

if user_input:

    # Format history for LLM
    formatted_history = "\n".join(
        [f"{role}: {message}" for role, message in chat_history]
    )

    full_prompt = f"""
You are an intelligent AI Travel Planner.

Previous Conversation:
{formatted_history}

User: {user_input}
Assistant:
"""

    # Generate AI response
    ai_response = generate_travel_plan(full_prompt)

    # 🔥 Auto-update title if first message
    if len(chat_history) == 0:
        update_session_title(
            st.session_state.active_session,
            user_input[:50]  # limit title length
        )

    # Save messages
    save_memory(st.session_state.active_session, user_input, "user")
    save_memory(st.session_state.active_session, ai_response, "assistant")

    st.rerun()
