# School Management Software

This is a comprehensive school management software designed to handle all aspects of school administration, from student and staff management to fee collection and examinations.

## Prerequisites

Before you begin, ensure you have the following installed:

*   **Python 3.x:** For the backend server.
*   **Node.js and npm:** For the frontend application.
*   **SQLite:** The database used for this project.

## Getting Started

Follow these steps to get the application up and running:

### 1. Set Up the Database

The database schema is defined in `database_schema.sql`. To create the database and tables, you will need to use the `sqlite3` command-line tool.

```bash
sqlite3 school.db < database_schema.sql
```

This will create a `school.db` file in the root directory of the project.

### 2. Set Up the Backend

The backend is a Flask application. To get it running, follow these steps:

1.  **Navigate to the backend directory:**
    ```bash
    cd school_management/backend/app
    ```

2.  **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: I will create the `requirements.txt` file in the next step.)*

3.  **Run the Flask server:**
    ```bash
    python main.py
    ```

The backend server will now be running on `http://localhost:5000`.

### 3. Set Up the Frontend

The frontend is a React application. To get it running, follow these steps:

1.  **Navigate to the frontend directory:**
    ```bash
    cd school_management/frontend
    ```

2.  **Install the required Node.js packages:**
    ```bash
    npm install
    ```

3.  **Run the React development server:**
    ```bash
    npm start
    ```

The frontend application will now be running on `http://localhost:3000` and will open automatically in your browser.

## Using the `run.sh` Script

To simplify the setup process, you can use the `run.sh` script located in the root directory. This script will automate the database setup and dependency installation.

```bash
bash run.sh
```

After running the script, you will still need to start the backend and frontend servers manually in separate terminal windows, as described above.
