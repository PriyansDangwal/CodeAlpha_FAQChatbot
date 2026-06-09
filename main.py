import customtkinter as ctk

from chatbot import get_best_answer
from faq_data import FAQS

# ---------------- SETTINGS ---------------- #

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ---------------- APP ---------------- #

root = ctk.CTk()
root.title("College Admission FAQ Bot")
root.geometry("800x600")

# ---------------- FUNCTIONS ---------------- #

def ask_question():

    question = question_entry.get().strip()

    if not question:
        return

    answer = get_best_answer(question, FAQS)

    chat_box.insert(
        "end",
        f"\n👤 You:\n{question}\n\n🤖 Bot:\n{answer}\n"
    )

    question_entry.delete(0, "end")

def clear_chat():
    chat_box.delete("1.0", "end")

# ---------------- TITLE ---------------- #

title = ctk.CTkLabel(
    root,
    text="🎓 College Admission FAQ Bot",
    font=("Arial", 26, "bold")
)

title.pack(pady=20)

# ---------------- CHAT BOX ---------------- #

chat_box = ctk.CTkTextbox(
    root,
    width=750,
    height=350,
    corner_radius=15,
    font=("Arial", 15)
)

chat_box.pack(pady=10)

chat_box.insert(
    "end",
    "🤖 Welcome!\nAsk any question regarding admissions.\n"
)

# ---------------- INPUT FRAME ---------------- #

input_frame = ctk.CTkFrame(root)

input_frame.pack(
    fill="x",
    padx=20,
    pady=15
)

question_entry = ctk.CTkEntry(
    input_frame,
    placeholder_text="Type your question here...",
    height=45,
    font=("Arial", 14)
)

question_entry.pack(
    side="left",
    fill="x",
    expand=True,
    padx=10,
    pady=10
)

send_button = ctk.CTkButton(
    input_frame,
    text="Send",
    width=120,
    command=ask_question
)

send_button.pack(
    side="left",
    padx=10
)

# ---------------- BOTTOM BUTTONS ---------------- #

clear_button = ctk.CTkButton(
    root,
    text="Clear Chat",
    command=clear_chat,
    fg_color="red"
)

clear_button.pack(pady=10)

# ---------------- RUN ---------------- #

root.mainloop()