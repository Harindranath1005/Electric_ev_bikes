
# 🛵 EV Bike Recommender App

A Streamlit-based web app that recommends **top 5 electric bikes (EVs)** to users based on their personalized preferences such as **price, range, charging time, battery capacity, and more**.

---

## 🚀 Project Purpose

The primary goal of this project is to **recommend electric bikes (EVs)** tailored to a user’s needs using specific input parameters. Unlike traditional auto-portal websites that list vehicle specifications by model, this app takes **user-defined preferences** and computes a **custom rating** to suggest the best bikes available in the market.

---

## ⚙️ Tools & Technologies Used

- **Python** – Core language for data processing and logic
- **Streamlit** – To build the interactive user interface
- **Pandas** – For data manipulation and rating calculations
- **MySQL Connector** – To fetch EV bike data from a MySQL database
- **Min-Max Scaling** – For normalizing parameters for better comparison
- **`.env` File** – For storing sensitive database credentials securely

---

## 🧠 How It Works

1. **User Input:**  
   The app collects the following parameters from the user:
   - 💰 Price  
   - ⚡ Charging Time  
   - 🌀 Torque  
   - 🔋 Battery Capacity  
   - 🛣️ Range  
   - 🚀 Top Speed

2. **Scaling the Input:**  
   - **Min-Max Scaling** is applied to normalize the values.
   - **Reverse scaling** is used for `Price` and `Charging Time` since *lower* values are better for these.

3. **Database Query:**  
   - EV bike data is stored in a **MySQL database**.
   - The app connects to this database using `mysql-connector-python`.
   - Credentials are securely stored in a `.env` file.

4. **Bike Rating Logic:**  
   - For each EV bike in the database, a rating is computed based on the similarity to the user’s preferences.
   - The top 5 bikes with the **highest rating scores** are recommended.

5. **Output:**  
   - The app displays the **Top 5 recommended bikes** with their key specifications in a user-friendly format.

---

## 📥 Input

The app takes **user-defined numeric values** for:
- Price
- Charging Time
- Torque
- Battery Capacity
- Range
- Top Speed

---

## 📤 Output

- Displays a **ranked list of top 5 electric bikes** matching the input preferences.
- Provides detailed specifications for each suggestion.

---

## 👤 Target Audience

This project is ideal for:
- Individuals planning to purchase an electric bike
- EV enthusiasts comparing options
- Anyone looking for data-driven suggestions based on specific needs

---

## 🔒 Security Note

Sensitive information like:
- MySQL host
- User credentials
- Port and password  

are stored in a **`.env` file** and not hardcoded, ensuring privacy and best practices for security.

---

## 🔮 Future Scope

- 💬 **Chat-based Input Interface**  
  Plan to integrate a **chatbot UI** where users can type their preferences in natural language instead of using dropdowns or sliders.

- 📈 **Data Enrichment**  
  Include additional bike parameters such as features, brand reputation, or user reviews.

- 📱 **Mobile-Friendly Layout**  
  Make the app responsive for mobile browsers.

---

## 📦 Requirements

Make sure to install the following dependencies:

```bash
pip install streamlit pandas mysql-connector-python python-dotenv scikit-learn
```

---

## ▶️ Running the App

1. Clone the repository
2. Add a `.env` file with your DB credentials
3. Run the app:

```bash
streamlit run app.py
```
