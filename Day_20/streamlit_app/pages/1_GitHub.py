import streamlit as st
import requests
import pandas as pd

st.title("🙅‍♂️ GitHub Profile Analyzer")
username = st.text_input("GitHub Username","mhassan6119")
if st.button("🔎 Analyze"):
    with st.spinner("Fetching data..."):
        token = "Your-Github-Token"
        headers = {
            "Authorization":f"token{token}",
            "Accept":"application/vnd.github.v3+json"
        }
        #Profile
        profile = requests.get(
            f"https://api.github.com/users/{username}", headers=headers
        ).json()
        
        # Repos
        repos = requests.get(
            f"https://api.github.com/users/{username}/repos", headers=headers
        ).json()
    if "message" in profile:
        st.error("❌ User not found!")
    else:
        # Metrics row
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("📦 Repos",profile.get("public_repos"))
        col2.metric("👥 Followers", profile.get("followers"))
        col3.metric("👣 Following", profile.get("following"))
        col4.metric("⭐ Gists", profile.get("public_gists"))

        st.markdown("---")

        #Profile Info
        col1,col2 = st.columns(2)
        with col1:
            st.subheader("🗒️ Profile Info")
            st.write(f"**Naem:**{profile.get('name','N/A')}")
            st.write(f"**Bio:**{profile.get('bio','N/A')}")
            st.write(f"**Location:**{profile.get('location','N/A')}")
            st.write(f"**Joined:**{profile.get('created_at','')[:10]}")

        with col2:
            st.subheader("📊 Language Stats")
            # Language distribution
            langauges = {}
            for repo in repos:
                lang = repo.get("language")
                if lang:
                    langauges[lang] = langauges.get(lang,0) + 1
            if langauges:
                df_lang = pd.DataFrame(
                    list(langauges.items()),
                    columns=["Language","Count"]
                )
                st.bar_chart(df_lang.set_index("Language"))
        st.markdown("---")

        # Repos table
        st.subheader("📦 Repositories")
        repo_data = []
        for repo in repos:
            repo_data.append({
                "Name":repo['name'],
                "Language":repo.get("language","N/A"),
                "Stars": repo["stargazers_count"],
                "Forks":repo['forks_count'],
            })
            df = pd.DataFrame(repo_data)
            df = df.sort_values("Stars",ascending=False)
            st.dataframe(df,use_container_width=True)