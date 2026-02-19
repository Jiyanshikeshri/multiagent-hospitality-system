from db import get_connection
import uuid

# -----------------------------
# SESSION MANAGEMENT
# -----------------------------

def create_new_session():
    conn = get_connection()
    cursor = conn.cursor()

    session_id = str(uuid.uuid4())
    title = "New Chat"

    query = "INSERT INTO sessions (id, title) VALUES (%s, %s)"
    cursor.execute(query, (session_id, title))
    conn.commit()

    cursor.close()
    conn.close()

    return session_id


def get_all_sessions():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM sessions ORDER BY created_at DESC")
    sessions = cursor.fetchall()

    cursor.close()
    conn.close()

    return sessions


# -----------------------------
# CHAT MEMORY
# -----------------------------

def save_memory(session_id, message, role):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO chat_memory (session_id, role, message)
    VALUES (%s, %s, %s)
    """

    cursor.execute(query, (session_id, role, message))
    conn.commit()

    cursor.close()
    conn.close()


def load_memory(session_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT role, message 
    FROM chat_memory 
    WHERE session_id = %s 
    ORDER BY id ASC
    """

    cursor.execute(query, (session_id,))
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return results

def update_session_title(session_id, title):
    conn = get_connection()
    cursor = conn.cursor()

    query = "UPDATE sessions SET title = %s WHERE id = %s"
    cursor.execute(query, (title[:50], session_id))  # limit to 50 chars
    conn.commit()

    cursor.close()
    conn.close()
