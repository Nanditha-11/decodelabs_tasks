import pandas as pd

print("======================================")
print("    AI RECOMMENDATION SYSTEM")
print("======================================")

# Data Inside Code
data = [
    {"skill": "Machine Learning", "interests": "ai, python, data, math, algorithms"},
    {"skill": "Data Science", "interests": "data, python, statistics, analysis, sql"},
    {"skill": "Deep Learning", "interests": "ai, neural networks, tensorflow, pytorch, python"},
    {"skill": "Backend Development", "interests": "java, apis, databases, programming, sql"},
    {"skill": "Frontend Development", "interests": "html, css, javascript, react, design"},
    {"skill": "DevOps", "interests": "aws, docker, kubernetes, ci/cd, cloud, automation"}
]

# Load into DataFrame
df = pd.DataFrame(data)

# Display Available Skills
print("\nAvailable Skill Areas:")
for skill in df["skill"]:
    print("-", skill)

# User Input
user_input = input("\nEnter your interests (comma separated): ")

user_interests = [
    interest.strip().lower()
    for interest in user_input.split(",")
    if interest.strip()
]

# Check Empty Input
if len(user_interests) == 0:
    print("\nPlease enter at least one interest.")
    exit()

print("\nYour Interests:")
for interest in user_interests:
    print("-", interest)

# Calculate Match Scores
recommendations = []

for _, row in df.iterrows():

    tags = [
        tag.strip().lower()
        for tag in row["interests"].split(",")
    ]

    matched = set(user_interests) & set(tags)

    score = len(matched)

    recommendations.append({
        "skill": row["skill"],
        "score": score,
        "matches": list(matched)
    })

# Sort Recommendations
recommendations.sort(
    key=lambda x: x["score"],
    reverse=True
)

# Display Results
print("\n======================================")
print("      TOP RECOMMENDATIONS")
print("======================================")

found = False

for item in recommendations[:3]:

    if item["score"] > 0:

        found = True

        print(f"\nSkill Area : {item['skill']}")
        print(f"Match Score: {item['score']}")
        print("Matched Interests:")

        for match in item["matches"]:
            print("-", match)

if not found:
    print("\nNo matching recommendations found.")

print("\nThank you for using the Recommendation System!")
