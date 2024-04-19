import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from warnings import filterwarnings
filterwarnings('ignore')


st.set_page_config(page_title="Indian Premier League", page_icon="🏏")
st.title("Indian Premier League")
# Load IPL dataset
df= pd.read_csv(r"C:\Users\deepa\python & ML documents\Machine learning Notes\ML Assignments\Streamlit Files\IPL\ipl.csv")
deliveries = pd.read_csv(r"C:\Users\deepa\python & ML documents\Machine learning Notes\ML Assignments\Streamlit Files\IPL\IPL_Ball_by_Ball_2008_2022.csv")
match_data = pd.read_csv(r"C:\Users\deepa\python & ML documents\Machine learning Notes\ML Assignments\Streamlit Files\IPL\IPL_Matches_2008_2022.csv")
auctions = pd.read_csv(r"C:\Users\deepa\python & ML documents\Machine learning Notes\ML Assignments\Streamlit Files\IPL\auction.csv")
total_df = match_data.merge(deliveries, how="inner")
team_mapping = {"Rising Pune Supergiant": "Rising Pune Supergiants",
                    "Kings XI Punjab": "Punjab Kings",
                    "Delhi Daredevils": "Delhi Capitals",
                    "Delhi Dardevils": "Delhi Capitals"
                    }

# Rename team names using replace()
deliveries["BattingTeam"] = deliveries["BattingTeam"].replace(team_mapping)
match_data[["Team1","Team2","TossWinner","WinningTeam"]] = match_data[["Team1","Team2","TossWinner","WinningTeam"]].replace(team_mapping)
total_df[["Team1","Team2","TossWinner","WinningTeam","BattingTeam"]] = total_df[["Team1","Team2","TossWinner","WinningTeam","BattingTeam"]].replace(team_mapping)

@st.cache_data
def load_data():
    # Load your IPL dataset here
    data = pd.read_csv(r"C:\Users\deepa\python & ML documents\Machine learning Notes\ML Assignments\Streamlit Files\IPL\IPL_Matches_2008_2022.csv")
    return data


# Sidebar for navigation

x=st.sidebar.radio("pages",["Home", "Match Analysis","Player Stats", "Batting Stats","Bowling Stats", "Auction Analysis","battervsbowler" ])
if x=="Home":
    st.image(r"C:\Users\deepa\python & ML documents\Machine learning Notes\ML Assignments\Streamlit Files\IPL\download (1).png")
    data = load_data()
    # st.title("IPL Analytics and Prediction Dashboard")
    st.title("Welcome to the IPL Analytics Dashboard! Explore different analytics and insights.")
    st.write("""The Indian Premier League (IPL), also known as the TATA IPL for sponsorship reasons, 
             is a men's Twenty20 (T20) cricket league held annually in India. 
             Founded by the BCCI in 2007, the league features ten city-based franchise teams.
             The IPL usually takes place during the summer, between March and May each year. 
             It has an exclusive window in the ICC Future Tours Programme, 
             resulting in fewer international cricket tours occurring during the IPL seasons.""")
    st.write("""The IPL is the most popular cricket league in the world; in 2014, it ranked sixth in average attendance among all sports leagues.
             In 2010, the IPL became the first sporting event to be broadcast live on YouTube.
             Inspired by the success of the IPL, other Indian sports leagues have been established. 
             In 2022, the league's brand value was estimated at ₹90,038 crore (US$11 billion).""")
    st.header("History")
    st.subheader("Inspired by a rival")
    st.write("""In 2007, Zee Entertainment Enterprises founded the Indian Cricket League (ICL).
              The ICL was not recognized by the Board of Control for Cricket in India (BCCI) or the International Cricket Council (ICC).
              Moreover, the BCCI was unhappy about its committee members joining the ICL executive board.
              In response, the BCCI increased the prize money for its domestic tournaments and imposed lifetime bans on players who joined the rival league, which it considered a rebel league.""")
    st.subheader("Foundation")
    st.write("""On 13 September 2007, following India's victory at the 2007 T20 World Cup, the BCCI announced a franchise based Twenty20 cricket competition known as the Indian Premier League.
              The inaugural season was scheduled to start in April 2008, commencing with a "high-profile ceremony" in New Delhi. BCCI Vice-president Lalit Modi, who led the IPL initiative, 
             provided details of the tournament, including its format, prize money, franchise revenue system, and squad composition rules. The league, to be managed by a seven-man governing council,
              would also serve as the qualifying mechanism for that year's Champions League Twenty20.""")

    st.write("""To determine team ownership, an auction for the franchises was held on 24 January 2008. 
              The league officially commenced in April 2008, featuring Chennai Super Kings (CSK), Mumbai Indians (MI), Delhi Daredevils (DD), Kings XI Punjab (KXIP), Deccan Chargers (DC), Rajasthan Royals (RR), Kolkata Knight Riders (KKR), and Royal Challengers Bangalore (RCB).""")
    
    st.image(r"https://m.economictimes.com/thumb/msid-98015672,width-1200,height-1200,resizemode-4,imgsize-97698/ipl.jpg", caption='IPL Trophy')

if x=="Match Analysis":
    # Example match analysis visualization (highest scores)
    st.subheader("Most Run Scores in IPL")
    highest_scores = deliveries.groupby('batter')['batsman_run'].sum().sort_values(ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=highest_scores.index, y=highest_scores.values)
    plt.xticks(rotation=45)
    plt.xlabel("Batsman")
    plt.ylabel("Total Runs")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

    

   
    st.subheader("Top Wicket-Takers in IPL")
    top_wicket_takers = deliveries.groupby('bowler')['isWicketDelivery'].sum().sort_values(ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_wicket_takers.index, y=top_wicket_takers.values,color="#34ebcf")
    plt.xticks(rotation=45)
    plt.xlabel("Bowler")
    plt.ylabel("Total Wickets")
    st.pyplot()

  
    

    # Additional pages
# with tab3:

#     seasons = total_df["Season"].unique()

#     stats_by_season = {}
#     for season in seasons:
#         season_data = total_df[total_df["Season"] == season]
#         stats_by_batter = {}

#         for batter_stat in ["Most Runs", "Highest Scores", "Best Batting Average", "Best Batting Strike Rate", "Most Hundreds", "Most Fifties", "Most Fours", "Most Sixes", "Most Nineties"]:
#             if batter_stat == "Most Runs":
#                 stats = season_data.groupby('batter')['batsman_run'].sum().reset_index().sort_values(by='batsman_run', ascending=False).head(15)
#             elif batter_stat == "Highest Scores":
#                 stats = season_data.groupby(['ID', 'batter'])['batsman_run'].max().reset_index().sort_values(by='batsman_run', ascending=False).head(15)
#             elif batter_stat == "Best Batting Average":
#                 stats = season_data.groupby('batter').apply(lambda x: x['batsman_run'].sum() / x['isWicketDelivery'].sum() if x['isWicketDelivery'].sum() > 0 else 0).reset_index(name='batting_avg').sort_values(by='batting_avg', ascending=False).head(15)
#             elif batter_stat == "Best Batting Strike Rate":
#                 stats = season_data.groupby('batter').apply(lambda x: (x['batsman_run'].sum() / x['ballnumber'].sum()) * 100 if x['ballnumber'].sum() > 0 else 0).reset_index(name='batting_sr').sort_values(by='batting_sr', ascending=False).head(15)
#             elif batter_stat == "Most Hundreds":
#                 stats = season_data.groupby('batter').apply(lambda x: (x['batsman_run'].sum() >= 100).sum()).reset_index(name='100s').sort_values(by='100s', ascending=False).head(15)
#             elif batter_stat == "Most Fifties":
#                 stats = season_data.groupby('batter').apply(lambda x: (x['batsman_run'].sum() >= 50).sum()).reset_index(name='50s').sort_values(by='50s', ascending=False).head(15)
#             elif batter_stat == "Most Fours":
#                 stats = season_data[season_data['batsman_run'] == 4].groupby('batter').size().reset_index(name='4s').sort_values(by='4s', ascending=False).head(15)
#             elif batter_stat == "Most Sixes":
#                 stats = season_data[season_data['batsman_run'] == 6].groupby('batter').size().reset_index(name='6s').sort_values(by='6s', ascending=False).head(15)
#             elif batter_stat == "Most Nineties":
#                 stats = season_data[season_data['batsman_run'] >= 90].groupby('batter').size().reset_index(name='90s').sort_values(by='90s', ascending=False).head(15)

#             stats_by_batter[batter_stat] = stats

#         stats_by_season[season] = stats_by_batter
            
   
#     selected_season = st.selectbox("Select a season", seasons)
#     selected_stat = st.selectbox("Batting", list(stats_by_season[selected_season].keys()))   
#     st.subheader(f"{selected_stat} in {selected_season}")
#     st.table(stats_by_season[selected_season][selected_stat])
    
# with tab4:

#     seasons1 = total_df["Season"].unique()
#     stats_by_season1 = {}

#     for season in seasons1:
#         season_data = total_df[total_df["Season"] == season]
#         stats_by_bowler = {}

#         for bowler_stat in ["Most Wickets", "Best Bowling Average", "Best Bowling", "Most 5 Wickets Haul", "Best Economy", "Best Bowling Strike Rate"]:
#             if bowler_stat == "Most Wickets":
#                 stat = season_data.groupby('bowler')['isWicketDelivery'].sum().reset_index(name='wickets').sort_values(by='wickets', ascending=False).head(15)
#             elif bowler_stat == "Best Bowling Average":
#                 stat = season_data.groupby('bowler').apply(lambda x: x['batsman_run'].sum() / x['isWicketDelivery'].sum() if x['isWicketDelivery'].sum() > 0 else 0).reset_index(name='bowling_avg').sort_values(by='bowling_avg').head(15)
#             elif bowler_stat == "Best Bowling":
#                 stat = season_data.groupby('bowler').apply(lambda x: x[x['isWicketDelivery'] == 1]['batsman_run'].sum()).reset_index(name='best_bowling').sort_values(by='best_bowling', ascending=False).head(15)
#             elif bowler_stat == "Most 5 Wickets Haul":
#                 stat = season_data.groupby(['ID', 'bowler']).apply(lambda x: (x['isWicketDelivery'] == 1).sum()).reset_index(name='5_wickets').sort_values(by='5_wickets', ascending=False).head(15)
#             elif bowler_stat == "Best Economy":
#                 stat = season_data.groupby('bowler').apply(lambda x: x['batsman_run'].sum() / (x['ballnumber'].sum() / 6) if (x['ballnumber'].sum() / 6) > 0 else 0).reset_index(name='economy').sort_values(by='economy').head(15)
#             elif bowler_stat == "Best Bowling Strike Rate":
#                 stat = season_data.groupby('bowler').apply(lambda x: (x['isWicketDelivery'].sum() / (x['ballnumber'].sum() / 6)) * 100 if (x['ballnumber'].sum() / 6) > 0 else 0).reset_index(name='strike_rate').sort_values(by='strike_rate').head(15)
#             stats_by_bowler[bowler_stat] = stat

#         stats_by_season1[season] = stats_by_bowler
            
   
#     selected_season = st.selectbox("Select a season", seasons1)
#     selected_stat1 = st.selectbox("Bowling", list(stats_by_season1[selected_season].keys()))
   
#     st.subheader(f"{selected_stat1} in {selected_season}")
#     st.table(stats_by_season1[selected_season][selected_stat1])


if x=="Batting Stats":
    seasons = total_df["Season"].unique()

    stats_by_season = {}
    for season in seasons:
        season_data = total_df[total_df["Season"] == season]
        stats_by_batter = {}

        for batter_stat in ["Most Runs", "Highest Scores", "Best Batting Average", "Best Batting Strike Rate", "Most Hundreds", "Most Fifties", "Most Fours", "Most Sixes", "Most Nineties"]:
            if batter_stat == "Most Runs":
                stats = season_data.groupby('batter')['batsman_run'].sum().reset_index().sort_values(by='batsman_run', ascending=False).head(15)
            elif batter_stat == "Highest Scores":
                stats = season_data.groupby(['ID', 'batter'])['batsman_run'].max().reset_index().sort_values(by='batsman_run', ascending=False).head(15)
            elif batter_stat == "Best Batting Average":
                stats = season_data.groupby('batter').apply(lambda x: x['batsman_run'].sum() / x['isWicketDelivery'].sum() if x['isWicketDelivery'].sum() > 0 else 0).reset_index(name='batting_avg').sort_values(by='batting_avg', ascending=False).head(15)
            elif batter_stat == "Best Batting Strike Rate":
                stats = season_data.groupby('batter').apply(lambda x: (x['batsman_run'].sum() / x['ballnumber'].sum()) * 100 if x['ballnumber'].sum() > 0 else 0).reset_index(name='batting_sr').sort_values(by='batting_sr', ascending=False).head(15)
            elif batter_stat == "Most Hundreds":
                stats = season_data.groupby('batter').apply(lambda x: (x['batsman_run'].sum() >= 100).sum()).reset_index(name='100s').sort_values(by='100s', ascending=False).head(15)
            elif batter_stat == "Most Fifties":
                stats = season_data.groupby('batter').apply(lambda x: (x['batsman_run'].sum() >= 50).sum()).reset_index(name='50s').sort_values(by='50s', ascending=False).head(15)
            elif batter_stat == "Most Fours":
                stats = season_data[season_data['batsman_run'] == 4].groupby('batter').size().reset_index(name='4s').sort_values(by='4s', ascending=False).head(15)
            elif batter_stat == "Most Sixes":
                stats = season_data[season_data['batsman_run'] == 6].groupby('batter').size().reset_index(name='6s').sort_values(by='6s', ascending=False).head(15)
            elif batter_stat == "Most Nineties":
                stats = season_data[season_data['batsman_run'] >= 90].groupby('batter').size().reset_index(name='90s').sort_values(by='90s', ascending=False).head(15)


            stats_by_batter[batter_stat] = stats

        stats_by_season[season] = stats_by_batter

    selected_season_batting = st.selectbox("Select a season (Batting)", seasons)
    selected_stat_batting = st.selectbox("Batting Statistic", list(stats_by_season[selected_season_batting].keys()))

    st.subheader(f"{selected_stat_batting} in {selected_season_batting}")
    st.table(stats_by_season[selected_season_batting][selected_stat_batting])

    # Visualization for Batting Statistic
    if selected_stat_batting == "Most Runs":
        plt.figure(figsize=(10, 6))
        plt.bar(stats_by_season[selected_season_batting][selected_stat_batting]['batter'], stats_by_season[selected_season_batting][selected_stat_batting]['batsman_run'])
        plt.xlabel('Batter')
        plt.xticks(rotation=45)
        plt.ylabel('Runs')
        plt.title('Most Runs by Batter')
        st.pyplot(plt)
    # Add other visualizations for different batting statistics...

if x=="Bowling Stats":
    seasons1 = total_df["Season"].unique()
    stats_by_season1 = {}

    for season in seasons1:
        season_data = total_df[total_df["Season"] == season]
        stats_by_bowler = {}

        for bowler_stat in ["Most Wickets", "Best Bowling Average", "Best Bowling", "Best Economy"]:
            if bowler_stat == "Most Wickets":
                stat = season_data.groupby('bowler')['isWicketDelivery'].sum().reset_index(name='wickets').sort_values(by='wickets', ascending=False).head(15)
           
            elif bowler_stat == "Best Bowling":
                stat = season_data.groupby('bowler').apply(lambda x: x[x['isWicketDelivery'] == 1]['batsman_run'].sum()).reset_index(name='best_bowling').sort_values(by='best_bowling', ascending=False).head(15)
            
                stat = season_data.groupby(['ID', 'bowler']).apply(lambda x: (x['isWicketDelivery'] == 1).sum()).reset_index(name='5_wickets').sort_values(by='5_wickets', ascending=False).head(15)
            elif bowler_stat == "Best Economy":
                stat = season_data.groupby('bowler').apply(lambda x:6* (x['batsman_run'].sum() / (x['ballnumber'].sum() / 6)) if (x['ballnumber'].sum() / 6) > 0 else 0).reset_index(name='economy').sort_values(by='economy').head(15)
            

            stats_by_bowler[bowler_stat] = stat

        stats_by_season1[season] = stats_by_bowler

    selected_season_bowling = st.selectbox("Select a season (Bowling)", seasons1)
    selected_stat_bowling = st.selectbox("Bowling Statistic", list(stats_by_season1[selected_season_bowling].keys()))

    st.subheader(f"{selected_stat_bowling} in {selected_season_bowling}")
    st.table(stats_by_season1[selected_season_bowling][selected_stat_bowling])

    # Visualization for Bowling Statistic
    if selected_stat_bowling == "Most Wickets":
        plt.figure(figsize=(10, 6))
        plt.bar(stats_by_season1[selected_season_bowling][selected_stat_bowling]['bowler'], stats_by_season1[selected_season_bowling][selected_stat_bowling]['wickets'])
        plt.xlabel('Bowler')
        plt.ylabel('Wickets')
        plt.xticks(rotation=45)
        plt.title('Most Wickets by Bowler')
        st.pyplot(plt)
    elif selected_stat_bowling == "Best Bowling Average":
        plt.figure(figsize=(10, 6))
        plt.bar(stats_by_season1[selected_season_bowling][selected_stat_bowling]['bowler'], stats_by_season1[selected_season_bowling][selected_stat_bowling][season_data.groupby('bowler')['isWicketDelivery'].sum().reset_index(name='wickets').sort_values(by='wickets', ascending=False).head(15)])
        plt.xlabel('Bowler')
        plt.ylabel('Wickets')
        plt.title("Best Bowling Average")
        st.pyplot(plt)
#     elif selected_stat_bowling == "Best Bowling":
#         plt.figure(figsize=(10, 6))
#         plt.bar(stats_by_season1[selected_season_bowling][selected_stat_bowling]['bowler'], stats_by_season1[selected_season_bowling][selected_stat_bowling]['wickets'])
#         plt.xlabel('Bowler')
#         plt.ylabel('Wickets')
#         plt.title('Most Wickets by Bowler')
#         st.pyplot(plt)
#     elif selected_stat_bowling == "Most 5 Wickets Haul":
#         plt.figure(figsize=(10, 6))
#         plt.bar(stats_by_season1[selected_season_bowling][selected_stat_bowling]['bowler'], stats_by_season1[selected_season_bowling][selected_stat_bowling]['wickets'])
#         plt.xlabel('Bowler')
#         plt.ylabel('Wickets')
#         plt.title('Most Wickets by Bowler')
#         st.pyplot(plt)
#     elif selected_stat_bowling == "Best Economy":
#         plt.figure(figsize=(10, 6))
#         plt.bar(stats_by_season1[selected_season_bowling][selected_stat_bowling]['bowler'], stats_by_season1[selected_season_bowling][selected_stat_bowling]['wickets'])
#         plt.xlabel('Bowler')
#         plt.ylabel('Wickets')
#         plt.title('Most Wickets by Bowler')
#         st.pyplot(plt)
#     elif selected_stat_bowling == "Best Bowling Strike Rate":
#         plt.figure(figsize=(10, 6))
#         plt.bar(stats_by_season1[selected_season_bowling][selected_stat_bowling]['bowler'], stats_by_season1[selected_season_bowling][selected_stat_bowling]['wickets'])
#         plt.xlabel('Bowler')
#         plt.ylabel('Wickets')
#         plt.title('Most Wickets by Bowler')
#         st.pyplot(plt)

        
# with tab5:
    
#     # Example team insights visualization (team performances over seasons)
#     st.subheader("Team Performances Over Seasons")
#     team_performance = match_data.groupby(['Season', 'WinningTeam'])['WinningTeam'].count().unstack()
#     st.table(team_performance)
#     plt.figure(figsize=(12, 8))
#     sns.heatmap(team_performance, cmap="YlGnBu", annot=True, fmt="g")
#     plt.title("Number of Wins by Teams Over Seasons")
#     st.set_option('deprecation.showPyplotGlobalUse', False)
#     st.pyplot()


if x=="Auction Analysis":
    team_mapping = {"Rising Pune Supergiant": "Rising Pune Supergiants",
                    "Kings XI Punjab": "Punjab Kings",
                    "Delhi Daredevils": "Delhi Capitals",
                    "Delhi Dardevils": "Delhi Capitals"
                    }

    # Rename team names using replace()
    auctions['Team'] = auctions['Team'].replace(team_mapping)
    # Display raw data or additional analysis as needed
    st.write(auctions)  # Display raw data
    filtered_auction_data = auctions[(auctions['Year'] >= 2013) & (auctions['Year'] <= 2023)]

    # Convert 'Winning bid' column to numeric if needed
    filtered_auction_data['Winning bid'] = pd.to_numeric(filtered_auction_data['Winning bid'], errors='coerce')

    # Calculate average auction prices per year for each player
    avg_prices = filtered_auction_data.groupby(['Year', 'Player'])['Winning bid'].mean().reset_index()

    

    # Visualization - Bar chart for total spending per year
    total_spending = filtered_auction_data.groupby('Year')['Winning bid'].sum().reset_index()
    fig_total_spending = px.bar(total_spending, x='Year', y='Winning bid', color='Year',
                                labels={'x': 'Year', 'y': 'Total Spending'},
                                title='Total Spending in IPL Auctions per Year')
    st.plotly_chart(fig_total_spending)

    # Analysis 1: Team Spending Analysis
    st.subheader('Total Team Spending Analysis')
    team_spending = filtered_auction_data.groupby('Team')['Winning bid'].sum().sort_values(ascending=False)
    st.bar_chart(team_spending,color='#52f280')

    # Analysis 2: Player Price Distribution
    plt.figure(figsize=(8, 6))
    plt.hist(filtered_auction_data['Winning bid'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Player Price Distribution')
    plt.xlabel('Winning Bid (in Crores)')
    plt.ylabel('Frequency')
    plt.grid(axis='y', alpha=0.75)
    st.pyplot(plt)

    # Convert 'Winning bid' and 'Base price' columns to numeric if needed
    filtered_auction_data['Winning bid'] = pd.to_numeric(filtered_auction_data['Winning bid'], errors='coerce')
    filtered_auction_data['Base price'] = pd.to_numeric(filtered_auction_data['Base price'], errors='coerce')

    # Calculate profit
    filtered_auction_data['Profit'] = filtered_auction_data['Winning bid'] - filtered_auction_data['Base price']

    # Visualization - Bar chart for top performing players based on profit
    st.subheader("Top performing players based on profit")
    top_players_profit = filtered_auction_data.groupby('Player')['Profit'].mean().nlargest(10)
    st.bar_chart(top_players_profit,color='#f79a05')
if x=="battervsbowler":
    data = pd.read_csv(r"C:\Users\deepa\python & ML documents\Machine learning Notes\ML Assignments\Streamlit Files\IPL\IPL_Ball_by_Ball_2008_2022.csv")
    batsmen = data["batter"].unique()
    bowlers = data["bowler"].unique()
    
    
    st.header("batter vs bowler")
    cols1, cols2 = st.columns([2, 2])
    with cols1:
        batsman_player = st.selectbox("Select a batsman:", batsmen)
    with cols2:
        bowler_player = st.selectbox("Select a bowler:", bowlers)
    

    filtered_data = data[(data['batter'] == batsman_player) & (data['bowler'] == bowler_player)]
    wickets_data = data[(data['batter'] == batsman_player) & (data['bowler'] == bowler_player) & (data['kind'].notnull())]

    
    total_wickets = len(wickets_data)

    
    balls_bowled = len(filtered_data)
    total_runs = filtered_data['batsman_run'].sum()
    strike_rate = round((total_runs / balls_bowled) * 100, 2)
    total_runs_scored = filtered_data['batsman_run'].sum()
    total_dot_balls = len(filtered_data[filtered_data['total_run'] == 0])


    cols1, cols2= st.columns([2, 2])
    with cols1:
        st.subheader("runs scored")
        st.metric("runs scored",total_runs_scored)
        st.subheader("strike rate")
        st.metric("SR", strike_rate)
        st.subheader("dot balls")
        st.metric("dot balls",total_dot_balls)
    with cols2:
        st.subheader("Balls  Bowled")
        st.metric("Balls Bowled", balls_bowled)
        st.subheader("wickets")
        st.metric("wickets",total_wickets)

if x=="Player Stats":

    batsmen_stats = pd.read_csv(r"C:\Users\deepa\python & ML documents\Machine learning Notes\ML Assignments\Streamlit Files\IPL\batting_123.csv")
    bowler_stats = pd.read_csv(r"C:\Users\deepa\python & ML documents\Machine learning Notes\ML Assignments\Streamlit Files\IPL\bowling_summary.csv")
    player_names = set(batsmen_stats["Player"]).intersection(bowler_stats["Player"])

    # Create a Streamlit selectbox for player selection
    selected_player = st.selectbox("Select a player:", list(player_names))

    # Filter the data based on selected player for batting stats
    player_batting_data = batsmen_stats[batsmen_stats["Player"] == selected_player]
    if not player_batting_data.empty:
        player_batting_data = player_batting_data.iloc[0]  # Select the first row
        # Extract player batting statistics
        matches_played = player_batting_data["Matches"]
        innings = player_batting_data["Innings"]
        runs = player_batting_data["Runs"]
        balls_faced = player_batting_data["Balls"]
        fours = player_batting_data["4s"]
        sixes = player_batting_data["6s"]
        boundaries = player_batting_data["Boundary"]
        thirtys = player_batting_data["30s"]
        fiftys = player_batting_data["50s"]
        hundreds = player_batting_data["100s"]
        average = "{:.2f}".format(player_batting_data["avg"])  # Format to 2 decimal places
        strike_rate = "{:.2f}".format(player_batting_data["strike_rate"])  # Format to 2 decimal places
        highest_score = player_batting_data["highest_score"]

        # Display the selected player's batting statistics
        st.write("Batting Career Summary")
        cols1, cols2, cols3, cols4 = st.columns([4, 4, 4, 4])
        with cols1:
            st.metric("Matches", matches_played)
            st.metric("Runs", runs)
            st.metric("Highest Score", highest_score)

        with cols2:
            st.metric("Innings", innings)
            st.metric("Average", average)
            st.metric("Strike Rate", strike_rate)

        with cols3:
            st.metric("Balls", balls_faced)
            st.metric("4's", fours)
            st.metric("6's", sixes)

        with cols4:
            st.metric("Boundaries", boundaries)
            st.metric("30's", thirtys)
            st.metric("50's", fiftys)
            st.metric("100's", hundreds)
    else:
        st.write("No batting statistics available for the selected player.")

    # Filter the data based on selected player for bowling stats
    player_bowling_data = bowler_stats[bowler_stats["Player"] == selected_player]
    if not player_bowling_data.empty:
        player_bowling_data = player_bowling_data.iloc[0]  # Select the first row
        # Extract player bowling statistics
        matches_played_bowler = player_bowling_data["Matches"]
        balls_bowled = player_bowling_data["balls"]
        runs = player_bowling_data["runs"]
        wickets = player_bowling_data["wickets"]
        economy_rate = "{:.2f}".format(player_bowling_data["economy_rate"])  # Format to 2 decimal places
        three_wickets = player_bowling_data["3w"]
        five_wickets = player_bowling_data["5w"]

        # Display the selected player's bowling statistics
        st.write("Bowling Career Summary")
        cols1, cols2, cols3, cols4 = st.columns([4, 4, 4, 4])
        with cols1:
            st.metric("Matches", matches_played_bowler)
            st.metric("Wickets", wickets)

        with cols2:
            st.metric("Balls", balls_bowled)
            st.metric("3 Wickets", three_wickets)

        with cols3:
            st.metric("Runs", runs)
            st.metric("5 Wickets", five_wickets)
            
        with cols4:
            st.metric("Economy Rate", economy_rate)
    else:
        st.write("No bowling statistics available for the selected player.")