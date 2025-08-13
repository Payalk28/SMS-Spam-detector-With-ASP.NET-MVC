# SMS-Spam-Detector



## 📱 SMS Spam Detector – Project Overview

This project is a **machine learning-based classifier** designed to automatically detect whether an incoming SMS message is **spam (unwanted, promotional, or fraudulent)** or **ham (legitimate)**. It’s ideal for building filters for messaging apps, customer support platforms, or telecom services.

---

### ⚙️ How It Works

- 🧹 **Data Cleaning**: The system removes unnecessary columns and cleans textual data for processing.
- 📊 **Vectorization**: Messages are converted into numerical format using **CountVectorizer**, allowing the algorithm to understand and compare texts.
- 🧠 **Model Training**: A **Multinomial Naive Bayes** classifier learns from thousands of labeled SMS messages.
- 🎯 **Live Prediction**: You can type a message, and the model instantly tells you whether it’s spam.
- 🌥️ **WordCloud Visualization**: Common keywords from spam and ham messages are shown using visual clouds—helpful for spotting patterns.

---

### 📈 Performance

- **Training Accuracy**: ~99.41%
- **Testing Accuracy**: ~98.56%
- Reliable performance even with short and informal text messages.

---

### 💡 Why This Project Matters

Spam messages can be annoying, misleading, and even dangerous. This system helps:
- 🛡️ **Protect users from fraud and scams**
- 💌 **Improve user experience by reducing message clutter**
- 🔍 **Support research and development of smart text filters**

---

### 🔧 Tech Stack

- Python 🐍  
- scikit-learn  
- pandas & numpy  
- matplotlib & wordcloud  
- Jupyter Notebook  

