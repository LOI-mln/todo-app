📝 To-Do App

A modern task management web application built with Flask, Bootstrap, and Neumorphism design, featuring:
	•	✅ Add, categorize, and prioritize tasks
	•	🎨 Light/Dark mode toggle
	•	📂 Category filters (Work, Personal, Other)
	•	✔️ Mark tasks as completed and manage them in a collapsible section
	•	🗑️ Bulk delete all completed tasks
	•	💎 Clean, neumorphic UI with responsive design

⸻

⚡ Features
	•	Add Tasks: Create tasks with title, category, and priority.
	•	Filter by Category: Show only tasks from “Work”, “Personal”, or “Other”.
	•	Dark Mode: Toggle between light and dark themes (saved in localStorage).
	•	Completed Tasks: Collapsible section to keep finished tasks organized.
	•	Clear Completed: Delete all completed tasks with a single click.
	•	Neo/Neumorphism UI: Soft shadows and modern aesthetic for a polished look.

⸻

🛠️ Tech Stack
	•	Backend: Flask (Python)
	•	Database: SQLite (via SQLAlchemy)
	•	Frontend: HTML5, Bootstrap 5, Custom CSS (Neumorphism design)
	•	Icons/Styling: Bootstrap Icons + Emojis

⸻

🚀 Getting Started

1. Clone the repo

git clone https://github.com/your-username/neo-todo-dashboard.git
cd neo-todo-dashboard

2. Create a virtual environment

python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

3. Install dependencies

pip install -r requirements.txt

4. Run the app

flask run

Then open: http://127.0.0.1:5000/ in your browser.

⸻

📂 Project Structure

todo-app/
│
├── app.py              # Main Flask app
├── models.py           # SQLAlchemy models
├── requirements.txt    # Python dependencies
├── static/
│   └── style.css       # Custom CSS (neumorphism + dark mode)
└── templates/
    └── index.html      # Main frontend template


⸻

📸 Screenshots

Light Mode

<img width="1104" height="718" alt="Capture d’écran 2025-09-05 à 14 25 33" src="https://github.com/user-attachments/assets/c5586abb-3866-48eb-956c-cb0e15d16e11" />


Dark Mode

<img width="1104" height="718" alt="Capture d’écran 2025-09-05 à 14 25 28" src="https://github.com/user-attachments/assets/dccab13d-21e0-40d7-b698-b1f894e9e50b" />


⸻

🧑‍💻 Future Improvements
	•	User authentication (login & signup)
	•	Task deadlines & reminders
	•	Progress dashboard with charts
	•	Drag-and-drop task reordering
	•	REST API for mobile/React frontend

⸻

📜 License

This project is free to use or improve just ⭐️ this repo
