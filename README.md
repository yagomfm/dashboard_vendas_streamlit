# 📊 Sales Dashboard — Streamlit

Interactive web application for sales data analysis, built with Python and Streamlit. The project consumes data from a REST API, processes it with Pandas, and displays dynamic visualizations with Plotly.

🔗 **[Access the live app]([https://dashboardvendasapp-26madzvlan6mmsphb6xtjy.streamlit.app/](https://dashboard-vendas-yagomfm.streamlit.app/))**

---

## 🖥️ Features

- **Sales Dashboard** with filters by region, year, and seller
- Visualizations of **revenue** and **sales volume** by state, month, and category
- Interactive **geographic map** with scatter plot across South America
- **Top sellers** ranking by revenue and number of sales
- **Raw Data** page with advanced multi-field filters
- **Download** filtered table as `.csv`
- Custom visual theme

---

## 📁 Project Structure

```
dashboard_streamlit/
│
├── Dashboard.py          # Main page with charts and metrics
├── pages/
│   └── Dados_brutos.py   # Data exploration and download page
├── .streamlit/
│   └── config.toml       # Theme settings
├── requirements.txt      # Project dependencies
└── .gitignore
```

---

## 🛠️ Tech Stack

| Technology | Usage |
|---|---|
| [Python](https://www.python.org/) | Core language |
| [Streamlit](https://streamlit.io/) | Web app framework |
| [Pandas](https://pandas.pydata.org/) | Data manipulation and filtering |
| [Plotly Express](https://plotly.com/python/plotly-express/) | Interactive charts |
| [Requests](https://requests.readthedocs.io/) | REST API consumption |

---

## ▶️ Running Locally

**Requirements:** Python 3.10+

```bash
# Clone the repository
git clone https://github.com/yagomfm/dashboard_streamlit.git
cd dashboard_streamlit

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run Dashboard.py
```

---

## 📡 Data Source

Data is fetched in real time from a public REST API:

```
https://labdados.com/produtos
```

The API supports filtering by **region** and **year** via query string.

---

## 📚 About

Project developed as part of the **Data Science** track at [Alura](https://www.alura.com.br/), in the **Streamlit — Level 1** course, covering:

- Getting started with Streamlit and environment setup
- Building dashboards with interactive charts
- Interactivity with filters and widgets
- Deploying the app to Streamlit Cloud

---

## 👤 Author

**Yago Mar**  
[![GitHub](https://img.shields.io/badge/GitHub-yagomfm-181717?logo=github)](https://github.com/yagomfm)
