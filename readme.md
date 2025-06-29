# Kudos Project

A simple web app for giving and receiving kudos within your organization.

---

## Features

- Users can log in and give kudos (with a message) to others in their organization.
- Each user gets 3 kudos per week (does not accumulate).
- See kudos you’ve received and given.
- Demo data generation for quick testing.

---

## Prerequisites

- Python 3.8+
- Node.js (v16+ recommended) and npm

---

## Backend Setup (Django)

1. **Clone the repository and enter the project directory:**
    ```sh
    git clone <your-repo-url>
    cd kudos_project
    ```

2. **Install Python dependencies:**
    ```sh
    pip install -r requirements.txt
    ```
    *(If `requirements.txt` is missing, install manually: `pip install django djangorestframework django-cors-headers`)*

3. **Apply migrations:**
    ```sh
    python manage.py makemigrations kudos_app
    python manage.py migrate
    ```

4. **Generate demo data:**
    ```sh
    python manage.py generate_demo_data
    ```

5. **Run the Django server on `localhost`:**
    ```sh
    python manage.py runserver localhost:8000
    ```

---

## Frontend Setup (React)

1. **Open a new terminal and navigate to the frontend directory:**
    ```sh
    cd kudos-frontend
    ```

2. **Install dependencies:**
    ```sh
    npm install
    ```

3. **Start the React development server:**
    ```sh
    npm start
    ```
    The app will open at [http://localhost:3000](http://localhost:3000).

---

## Using the App

1. **Login:**
    - Use one of the demo users generated (e.g., `user_1_1` with password `password`).
    - You can find more demo usernames in the Django admin or by checking the database.

2. **Give Kudos:**
    - After logging in, use the "Give Kudos" form to select a recipient and enter a message.
    - You can give up to 3 kudos per week.

3. **View Kudos:**
    - See the kudos you’ve received and given in the respective sections.

4. **Logout:**
    - Use the logout button to end your session.

---

## Troubleshooting

- **CORS or Cookie Issues:**  
  Make sure you always use `localhost` (not `127.0.0.1`) for both backend and frontend URLs.
- **Session Not Working:**  
  Ensure Django is started with `python manage.py runserver localhost:8000` and not `127.0.0.1:8000`.
- **Demo Users:**  
  If you forget the demo usernames, re-run `python manage.py generate_demo_data` to reset demo data.

---

## Development Notes

- Backend API is at `http://localhost:8000/api/`
- Frontend runs at `http://localhost:3000/`
- All demo data is randomly generated each time you run the management command.

---

##