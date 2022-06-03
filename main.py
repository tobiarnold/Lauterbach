import sys
from streamlit import cli as stcli
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import altair as alt
import seaborn as sns
def main():
    st.set_page_config(page_title="Lauterbach Fanpage", page_icon="😷", layout="centered")
    st.title("Lauterbach und seine Tweets 😷")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(' ')
    with col2:
        st.write("**Für Simon F. Fanboy #1**")
    with col3:
        st.write(' ')
    col1, col2, col3 = st.columns(3)
    with col1:
       st.write("")
    with col2:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/2021-12-07_Unterzeichnung_des_Koalitionsvertrages_der_20._Wahlperiode_des_Bundestages_by_Sandro_Halank%E2%80%93025.jpg/800px-2021-12-07_Unterzeichnung_des_Koalitionsvertrages_der_20._Wahlperiode_des_Bundestages_by_Sandro_Halank%E2%80%93025.jpg", "Der Boss",width=150)
    with col3:
        st.write("")
    st.markdown("""---""")
    fan = st.checkbox("Bist du ein Lauterbach Fan Boy? 😍")
    if fan:
        st.title("👩‍💻 Tabelle mit allen Tweets")
        st.markdown(""" 
           - Tabelle lässt sich mit Klick auf eine der Spaltenüberschriften sortieren.
           - Zur Filterung können einzelne oder mehrere Wörter verwendet werden. 
           - Mit dem x rechts neben dem Wort im Filter können Wörter wieder entfernt werden.
           """)
        st.write("Tabelle lässt sich mit Klick auf eine der Spaltenüberschriften sortieren")
        df = pd.read_csv(r"https://raw.githubusercontent.com/tobiarnold/Lauterbach/main/df_karl_new.csv", delimiter=";")
        options = st.multiselect("Nach welchen Wörtern soll die Tabelle gefiltert werden?",
                                         ["afd", "affenpocken", "corona", "covid", "deutschland","impfung", "kinder", "lockdown", "merkel", "studie", "trump", "welle"])
        df_option = df
        df_option = df_option[df_option["Text"].str.contains('|'.join(options))]
        st.dataframe(df_option)
        anzahl_tweets = df_option.Text.count()
        st.write("Anzahl der tweets in der Tabelle:", anzahl_tweets )
        st.markdown("""---""")
        st.title("📚 Wordcloud")
        count_wc = st.slider("Aus wie vielen Wörtern soll die Wordcloud bestehen?", 1, 100, 50)
        st.markdown(""" 
        - Die Wordcloud ändert sich je nach Filterung der Tabelle.
        - Falls die Wordcloud nicht dargestellt werden kann den Slider noch einmal betätigen.
        """)
        sns.set_style("whitegrid")
        df_wordcloud = pd.read_csv(r"https://raw.githubusercontent.com/tobiarnold/Lauterbach/main/df_karl_bereinigt.csv", delimiter=";",encoding="utf8")
        df_wordcloud = df_wordcloud[["Text"]]
        df_wordcloud["Text"] = df_wordcloud["Text"].astype(str)
        df_wordcloud = df_wordcloud[df_wordcloud["Text"].str.contains('|'.join(options))]
        try:
            fig, ax1 = plt.subplots()
            text = " ".join(i for i in df_wordcloud.Text)
            stopwords_wordcloud = ['aber', 'alle', 'allem', 'allen', 'aller', 'alles', 'als', 'also', 'am', 'an', 'ander', 'andere', 'anderem', 'anderen', 'anderer', 'anderes', 'anderm', 'andern', 'anderr', 'anders', 'auch', 'auf', 'aus', 'bei', 'bin', 'bis', 'bist', 'da', 'damit', 'dann', 'der', 'den', 'des', 'dem', 'die', 'das', 'dass', 'daß', 'derselbe', 'derselben', 'denselben', 'desselben', 'demselben', 'dieselbe', 'dieselben', 'dasselbe', 'dazu', 'dein', 'deine', 'deinem', 'deinen', 'deiner', 'deines', 'denn', 'derer', 'dessen', 'dich', 'dir', 'du', 'dies', 'diese', 'diesem', 'diesen', 'dieser', 'dieses', 'doch', 'dort', 'durch', 'ein', 'eine', 'einem', 'einen', 'einer', 'eines', 'einig', 'einige', 'einigem', 'einigen', 'einiger', 'einiges', 'einmal', 'er', 'ihn', 'ihm', 'es', 'etwas', 'euer', 'eure', 'eurem', 'euren', 'eurer', 'eures', 'für', 'gegen', 'gewesen', 'hab', 'habe', 'haben', 'hat', 'hatte', 'hatten', 'hier', 'hin', 'hinter', 'ich', 'mich', 'mir', 'ihr', 'ihre', 'ihrem', 'ihren', 'ihrer', 'ihres', 'euch', 'im', 'in', 'indem', 'ins', 'ist', 'jede', 'jedem', 'jeden', 'jeder', 'jedes', 'jene', 'jenem', 'jenen', 'jener', 'jenes', 'jetzt', 'kann', 'kein', 'keine', 'keinem', 'keinen', 'keiner', 'keines', 'können', 'könnte', 'machen', 'man', 'manche', 'manchem', 'manchen', 'mancher', 'manches', 'mein', 'meine', 'meinem', 'meinen', 'meiner', 'meines', 'mit', 'muss', 'musste', 'nach', 'nicht', 'nichts', 'noch', 'nun', 'nur', 'ob', 'oder', 'ohne', 'sehr', 'sein', 'seine', 'seinem', 'seinen', 'seiner', 'seines', 'selbst', 'sich', 'sie', 'ihnen', 'sind', 'so', 'solche', 'solchem', 'solchen', 'solcher', 'solches', 'soll', 'sollte', 'sondern', 'sonst', 'über', 'um', 'und', 'uns', 'unsere', 'unserem', 'unseren', 'unser', 'unseres', 'unter', 'viel', 'vom', 'von', 'vor', 'während', 'war', 'waren', 'warst', 'was', 'weg', 'weil', 'weiter', 'welche', 'welchem', 'welchen', 'welcher', 'welches', 'wenn', 'werde', 'werden', 'wie', 'wieder', 'will', 'wir', 'wird', 'wirst', 'wo', 'wollen', 'wollte', 'würde', 'würden', 'zu', 'zum', 'zur', 'zwar', 'zwischen']
            stopwords_wordcloud.extend(("müssen", "wäre", "mehr", "zeigt", "heute", "daher", "geht", "ab", "zb", "f", "u", "oft", "kommt",
                                     "darf", "hätte", "daher", "geben", "viele", "via", "gut", "gute", "beim","schon"))
            wordcloud = WordCloud(background_color="black", stopwords=stopwords_wordcloud, colormap="Paired",max_words=count_wc)
            wordcloud.generate(text)
            ax1.imshow(wordcloud, interpolation="bilinear")
            ax1.axis("off")
            st.write(fig)
        except:
            st.write("Wordcloud kann nicht dargestellt werden.")
        st.markdown("""---""")
        st.title("📊 Diagramme")
        st.write("Anzahl Tweets pro Tag von Karl Lauterbach.")
        df["Datum"] = pd.to_datetime(df["Datum"])
        df_count = df.groupby(df["Datum"].dt.date).size().reset_index(name="Count")
        line = alt.Chart(df_count).mark_line().encode(x="Datum:T", y="Count",color=alt.value("#1DA1F2"),tooltip=["Datum:T","Count:Q"]).interactive()
        st.altair_chart(line, use_container_width=True)
        st.write("Summe likes der Tweets von Karl Lauterbach pro Tag.")
        line = alt.Chart(df).mark_line().encode(x="Datum:T", y="likes", color=alt.value("#1DA1F2"),
                                                      tooltip=["Datum:T", "likes:Q"]).interactive()
        st.altair_chart(line, use_container_width=True)
        df_zeit=df
        df_zeit["Uhrzeit des Tweets"] = pd.to_datetime(df_zeit["Uhrzeit des Tweets"])
        df_zeit["Hour"] = df_zeit["Uhrzeit des Tweets"].dt.strftime("%H")
        st.write("Anzahl der Tweets von Lauterbach nach Uhrzeit.")
        fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(9, 3))
        sns.countplot(x="Hour", data=df_zeit, color="#1DA1F2",
                      order=["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15","16", "17","18", "19", "20", "21", "22", "23"])
        plt.xlabel("Uhrzeit")
        plt.ylabel("Anzahl Tweets")
        st.pyplot(fig)
        st.write("Tage an denen Lauterbach twittert.")
        fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(9, 3))
        sns.countplot(x="Wochentag", data=df, color="#1DA1F2",
                      order=["Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Samstag","Sonntag"])
        plt.xlabel("Wochentag")
        plt.ylabel("Anzahl Tweets")
        st.pyplot(fig)
        st.markdown("""---""")
if __name__ == '__main__':
    if st._is_running_with_streamlit:
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())

