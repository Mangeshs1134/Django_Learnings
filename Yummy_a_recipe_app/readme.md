# Yummy - Recipe Sharing App 🍲

Yummy is a Django-based web application that allows users to browse, share, and manage recipes. Designed with a focus on simplicity and user experience, Yummy offers features for food enthusiasts to explore and organize their favorite recipes easily.

---

## 🚀 Features

### 🍲 Recipe Management
- **Browse Recipes**: View a collection of recipes with detailed ingredients and instructions.
- **Search & Filter**: Search recipes by name or filter them by categories and ingredients.
- **User Contributions**: Add, edit, and delete your own recipes.

### 🔒 Authentication
- Secure login and signup using Django's built-in authentication system.
- Session management for personalized user experiences.

### 📺 Responsive Design
- Clean, user-friendly interface built with Django templates and Bootstrap.
- Mobile-first design to ensure compatibility across all devices.

---

## 🛠️ Tech Stack

### Backend:
- **Django**: For managing server-side logic and database operations.

### Frontend:
- **HTML/CSS**: For structuring and styling web pages.
- **Bootstrap**: For responsive design and UI components.

### Database:
- **SQLite**: Lightweight and easy-to-use database for development.

---

## 📚 Project Structure

```
Yummy/
├── yummy/                      # Django project settings
│   ├── settings.py             # Configuration for the project
│   ├── urls.py                 # URL routing for the project
│   ├── wsgi.py                 # WSGI entry point for the project
│
├── recipes/                    # Main app for managing recipes
│   ├── templates/recipes/      # HTML templates for recipe pages
│   ├── static/recipes/         # Static files (CSS, JS, images)
│   ├── models.py               # Database models for recipes
│   ├── views.py                # Logic for handling user requests
│   ├── urls.py                 # App-level routing
│   └── admin.py                # Django admin configuration
│
├── users/                      # App for user authentication and profiles
│   ├── templates/users/        # HTML templates for user-related pages
│   ├── models.py               # User models
│   ├── views.py                # Logic for user authentication
│   ├── urls.py                 # App-level routing
│   └── forms.py                # Forms for user input
│
├── db.sqlite3                  # SQLite database file
└── manage.py                   # Command-line utility for managing the project
```

---

## 📺 Installation & Setup

### Prerequisites:
- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

### Steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Mangeshs1134/yummy-recipe-app.git
   cd yummy-recipe-app
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the app**:
   Open your browser and navigate to `http://127.0.0.1:8000/`.

---

## 🔧 Usage

1. **Homepage**: Browse featured recipes and explore categories.
2. **Search**: Use the search bar to find specific recipes.
3. **Authentication**: Log in or sign up to contribute your own recipes.
4. **Manage Recipes**: Add, edit, or delete recipes from your profile dashboard.

---

## 🏆 Key Features in Action

- **Dynamic Recipe Pages**: View detailed information, including preparation steps and ingredients.
- **Secure Authentication**: Ensure only registered users can add or manage recipes.
- **Responsive UI**: Navigate seamlessly on desktop and mobile devices.

---

## 🔼 Future Enhancements

- **Ratings & Reviews**: Allow users to rate and review recipes.
- **Social Sharing**: Enable sharing recipes directly to social media platforms.
- **Advanced Filters**: Add filtering options for dietary preferences and cooking time.

---

## 🚀 Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request.

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push the branch.
4. Submit a pull request describing your changes.

---

## 📥 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Mangesh Gupta**  
- [GitHub](https://github.com/Mangeshs1134)  
- [LinkedIn](https://www.linkedin.com/in/mangesh-gupta-30b14b227/)

