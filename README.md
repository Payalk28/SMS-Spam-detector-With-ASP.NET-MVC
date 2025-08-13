SMS-Spam-Detector
📱 SMS Spam Detector – Project Overview
This project is a full-stack application designed to automatically detect whether an incoming SMS message is spam (unwanted, promotional, or fraudulent) or ham (legitimate). It combines a powerful machine learning model built with Python and a user-friendly web interface created using ASP.NET MVC. This setup is ideal for building a robust and accessible messaging filter.

⚙️ How It Works
🧹 Data Cleaning: The system's Python backend removes unnecessary columns and cleans textual data for processing.

📊 Vectorization: Messages are converted into a numerical format using CountVectorizer, which allows the algorithm to understand and compare texts.

🧠 Model Training: A Multinomial Naive Bayes classifier learns from thousands of labeled SMS messages to recognize spam patterns.

🖥️ Frontend Web App: The ASP.NET MVC application provides a web form where users can input text messages.

🎯 Live Prediction: The ASP.NET frontend sends the user's message to the Python backend via an API call. The Python model then instantly classifies the message and sends the prediction back to the frontend to be displayed to the user.

🌥️ WordCloud Visualization: Common keywords from spam and ham messages are shown using visual clouds—helpful for spotting patterns.

📈 Performance
Training Accuracy: ~99.41%

Testing Accuracy: ~98.56%

The model demonstrates reliable performance even with short and informal text messages.

💡 Why This Project Matters
Spam messages can be annoying, misleading, and even dangerous. This full-stack system helps:

🛡️ Protect users from fraud and scams

💌 Improve user experience by reducing message clutter

🔍 Support research and development of smart text filters

🔧 Tech Stack
Python 🐍

scikit-learn

pandas & numpy

matplotlib & wordcloud

Jupyter Notebook

ASP.NET MVC 🖥️

C#
