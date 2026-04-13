import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -----------------------------
# SETUP
# -----------------------------
# Create folder to save graphs
os.makedirs("graphs", exist_ok=True)

# Set style
sns.set(style="whitegrid")

# -----------------------------
# LOAD DATA
# -----------------------------
try:
    df = pd.read_csv("youtube.csv")
    print("Dataset loaded successfully!")
except:
    print("Error: Make sure youtube.csv is in the same folder.")
    exit()

# -----------------------------
# DATA PREPROCESSING
# -----------------------------
# Remove missing values
df.dropna(inplace=True)

# Convert date columns (if present)
if 'publish_date' in df.columns:
    df['publish_date'] = pd.to_datetime(df['publish_date'], dayfirst=True, errors='coerce')

# -----------------------------
# BASIC INFO
# -----------------------------
print("\nDataset Info:")
print(df.info())

print("\nFirst 5 rows:")
print(df.head())

# -----------------------------
# 1. TOP 10 MOST VIEWED VIDEOS
# -----------------------------
top_views = df.sort_values(by='views', ascending=False).head(10)

plt.figure(figsize=(10,5))
sns.barplot(x='views', y='title', data=top_views)
plt.title("Top 10 Most Viewed Videos")
plt.tight_layout()
plt.savefig("graphs/top_views.png")
plt.close()

# -----------------------------
# 2. CORRELATION HEATMAP
# -----------------------------
corr = df[['views','likes','comment_count']].corr()

plt.figure(figsize=(6,4))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation between Views, Likes, Comments")
plt.tight_layout()
plt.savefig("graphs/correlation.png")
plt.close()

# -----------------------------
# 3. VIEWS VS LIKES SCATTER
# -----------------------------
plt.figure(figsize=(6,4))
sns.scatterplot(x='views', y='likes', data=df)
plt.title("Views vs Likes")
plt.tight_layout()
plt.savefig("graphs/views_vs_likes.png")
plt.close()

# -----------------------------
# 4. TOP CHANNELS
# -----------------------------
top_channels = df.groupby('channel_title')['views'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
top_channels.plot(kind='bar')
plt.title("Top Channels by Total Views")
plt.tight_layout()
plt.savefig("graphs/top_channels.png")
plt.close()

# -----------------------------
# 5. ENGAGEMENT RATE
# -----------------------------
df['engagement'] = (df['likes'] + df['comment_count']) / df['views']

top_engagement = df.sort_values(by='engagement', ascending=False).head(10)

plt.figure(figsize=(10,5))
sns.barplot(x='engagement', y='title', data=top_engagement)
plt.title("Top Videos by Engagement Rate")
plt.tight_layout()
plt.savefig("graphs/engagement.png")
plt.close()

# -----------------------------
# 6. COUNTRY ANALYSIS
# -----------------------------
if 'publish_country' in df.columns:
    country_views = df.groupby('publish_country')['views'].sum().sort_values(ascending=False).head(10)

    plt.figure(figsize=(10,5))
    country_views.plot(kind='bar')
    plt.title("Top Countries by Views")
    plt.tight_layout()
    plt.savefig("graphs/country_analysis.png")
    plt.close()

# -----------------------------
# DONE
# -----------------------------
print("\nAll graphs generated successfully!")
print("Check 'graphs' folder.")