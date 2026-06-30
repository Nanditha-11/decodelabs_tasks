# DecodeLabs AI Recommendation Logic — Project 3
**Project Name:** AI Recommendation System  

---

## 📌 Project Overview
This project is part of the **DecodeLabs Industrial Training program (Project 3)**. 

It implements a terminal-based career recommendation system utilizing pandas and set intersection logic. The application is consolidated into a single script that runs entirely within the terminal, listing available career paths, prompting the user for their interests, parsing and confirming the input, and calculating the exact match score (count of matching interest tags) to output the top 3 recommendations along with the specific interests that matched.

---

## ⚙️ Features
1. **Native Data Integration**: Embedded career paths and interest keywords directly inside the script using a structured Python list of dictionaries, loaded into a Pandas DataFrame.
2. **Interests Parsing**: Sanitizes and standardizes user-entered comma-separated interest tags (ignoring case, whitespace, and empty strings).
3. **Set Intersection Matching**: Computes similarity using mathematical set intersection (`set(user_interests) & set(tags)`) to retrieve exact overlap.
4. **Ranked Recommendations**: Sorts and ranks matching skills in descending order based on the count of matched interests.
5. **Interest-Level Breakdown**: Displays the exact matched interests alongside the match score for the top 3 career recommendations.

---

## 📁 File Structure
```text
C:\Users\nandi\Documents\AI Project 3\
└── recommender.py   # Direct Python AI Recommendation System
```

---

## 🚀 How to Run the Recommendation System

Since this recommendation system requires external data analysis packages, make sure you have `pandas` installed.

1. Open your terminal or Command Prompt in the project directory.
2. Run the recommendation system using Python:
   ```bash
   python recommender.py
   ```

---

## 📊 Execution Phase Details

The steps executed sequentially by the system are detailed below:

| Execution Phase | Step & Implementation | Detail / Metrics |
|---|---|---|
| **1. Input Data** | Define Dataset | Loads a total of 6 career skills and 31 interest tags represented in a native Python list of dictionaries, loaded into a Pandas DataFrame. |
| **2. Interactive Listing** | Display Available Areas | Lists all 6 available skill areas (e.g. Machine Learning, Frontend, DevOps) for user visibility before prompt. |
| **3. Input Collection** | Interactive Comma-Separated Input | Accepts user interests, strips whitespace, converts to lowercase, and filters out empty inputs. |
| **4. Input Validation** | Empty Check | Checks for empty interest list and exits gracefully if no interests are provided. |
| **5. Processing** | Set Intersection | Intersects user interests with career tags to find common items $|\text{Interests}_{\text{User}} \cap \text{Tags}_{\text{Skill}}|$. |
| **6. Metric Evaluation** | Match Score | Computes the count of matched elements as the recommendation score. |
| **7. Sorting** | Ranked Sort | Sorts the recommendations in descending order of their Match Score. |
| **8. Output Presentation** | Detailed Recommendations | Inputting 'ai, python' recommends Machine Learning (Match Score: 2) and Deep Learning (Match Score: 2) out of 3 total displayed. |
