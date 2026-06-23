# Universal Data File Cleaning Pipeline

A sleek, interactive web application that turns raw, messy data into production-ready Excel spreadsheets. Instead of writing rigid, hardcoded cleaning scripts, this app detects your dataset's columns dynamically and lets you configure custom data manipulation rules directly from a graphical user interface.

## Live Demo
(Link will be posted here shortly)

## ✨ Key Features
- **Dynamic File Ingestion:** Upload any standard CSV file regardless of structure or column naming schemes.
- **Visual Mapping UI:** Side-by-side interface splitting advanced configurations from interactive data previews.
- **Numeric & Currency Pipeline:** Instantly strip string artifacts (like `$`, commas, or spaces) and securely cast variables into clean float or integer types.
- **Anomaly Correction:** Automatically isolate negative numeric anomalies and convert them to clean NaN markers.
- **In-Memory Buffer Management:** Efficiently compiles and streams `.xlsx` files using `io.BytesIO` without writing temp files to disk, optimizing multi-user server performance.

## 🛠️ Tech Stack
- **Frontend Framework:** Streamlit
- **Data Architecture:** Pandas, Numpy
- **Excel Formatting Engine:** Openpyxl

## Local Installation
1. Clone this repository:
```bash
   git clone [https://github.com/oxygenazeem/universal-data-cleaning-pipeline.git](https://github.com/oxygenazeem/universal-data-cleaning-pipeline.git)
```
2. Install the dependencies:
```bash
pip install -r requirements.txt
```
3. Spin up the application locally
```bash
python -m streamlit run app.py
```

---

## License & Distribution

This software is distributed under the MIT license. See `LICENSE` for more information.
