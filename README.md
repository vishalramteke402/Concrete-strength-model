🧱 Concrete Compressive Strength Prediction using Machine Learning

This project is a Streamlit-based web application that predicts the compressive strength of concrete (in MPa) using a trained machine learning model. The app takes concrete mix proportions as input and returns the estimated compressive strength, making it useful for civil engineers, researchers, construction analysts, and students working in materials science or ML applications in civil engineering.

📌 Project Overview

Concrete strength depends on multiple factors such as cement composition, aggregates, water content, and curing age. Traditionally, predicting the compressive strength requires lab experiments, curing for several days, and physical testing.

This project provides a data-driven solution using a regression model trained on concrete mixtures. The app predicts strength instantly and can help with:

Preliminary concrete mix design

Material optimization

Quality assessment

Research simulations

Educational demonstrations

🧠 Machine Learning Model

The ML model was trained on a dataset containing the following features:

Feature	Description
cement	Cement content (kg/m³)
slag	Blast furnace slag (kg/m³)
flyash	Fly ash (kg/m³)
water	Water content (kg/m³)
superplasticizer	Chemical admixture (kg/m³)
coarseaggregate	Coarse aggregate quantity (kg/m³)
fineaggregate	Fine aggregate quantity (kg/m³)
age	Age of concrete (days)

The target variable:

csMPa → Concrete compressive strength (in MPa)

The trained model is saved as a pickle file:

concrete strength pkl model

🚀 Features of the Application

🟦 Interactive UI built with Streamlit

⚡ Instant prediction of concrete strength

📥 User inputs via numerical fields

🧱 Accurate regression model trained on real data

💡 Beginner-friendly & production-ready code

📂 Project Structure
📁 Concrete-Strength-Predictor/
│── app.py
│── concrete strength pkl model
│── requirements.txt
│── README.md

⚙️ How the Model Works

The ML pipeline typically includes:

Data preprocessing

Feature scaling (if applied)

Train-test split

Regression model training (RandomForest / LinearRegression / XGBoost etc.)

Model evaluation using RMSE, R²

Pickle file creation

Your Streamlit app loads the saved model and predicts strength using:

prediction = model.predict([[cement, slag, flyash, water, superplasticizer,
                             coarseaggregate, fineaggregate, age]])

🛠️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/yourusername/Concrete-Strength-Predictor.git
cd Concrete-Strength-Predictor

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit App
streamlit run app.py

📌 Usage Instructions

Open the app in your browser after running Streamlit.

Enter the material quantities such as cement, slag, fly ash, water, aggregates, etc.

Enter the age of concrete (in days).

Click the Predict Strength button.

The app displays the predicted compressive strength (MPa).

🎯 Applications

Civil engineering mix design

Construction quality monitoring

Research in materials science

Academic ML projects

Real-time on-field decision support

🔍 Model Input Example
Cement: 300 kg/m³
Slag: 50 kg/m³
Fly Ash: 60 kg/m³
Water: 180 kg/m³
Superplasticizer: 8.5 kg/m³
Coarse Aggregate: 950 kg/m³
Fine Aggregate: 750 kg/m³
Age: 28 days


Predicted strength might look like:

Strength: 42.75 MPa

📦 Dependencies
streamlit
numpy
scikit-learn


(Additional libraries may be required depending on your model.)

🧩 Future Enhancements

📊 Add data visualizations

📈 Add model training notebook

🔄 Allow uploading CSV for batch predictions

🎨 Add sliders with realistic bounds

☁️ Deploy to Streamlit Cloud / Render / HuggingFace
