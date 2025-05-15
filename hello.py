from preswald import connect, get_df, query, table, text, plotly
import plotly.express as px

# 1. Load the dataset
connect()  # Initialize connection to preswald.toml data sources
df = get_df("youtube-videos")  # Load dataset

# 2. Query or manipulate the data
sql = "SELECT * FROM `youtube-videos` WHERE `Video views` > 3000000"
filtered_df = query(sql, "youtube-videos")

# 3. Build an interactive UI
text("# YouTube Video Analytics")
text("Explore videos with over 3 million views.")
table(filtered_df, title="Popular YouTube Videos")

# 4. Create a visualization
fig = px.scatter(df,
                 x="Likes",
                 y="Video views",
                 title="Likes vs Views on YouTube Videos",
                 labels={"Likes": "Number of Likes", "Views": "Number of Views"},
                 hover_data=["Video"])

fig.update_traces(marker=dict(size=5, color='lightblue', opacity=0.6))
fig.update_layout(
    template='plotly_white',
    xaxis_tickangle=-45
)

plotly(fig)




