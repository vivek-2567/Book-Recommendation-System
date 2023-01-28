import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import pickle
from PIL import Image
from streamlit_extras.dataframe_explorer import dataframe_explorer
import plotly.express as px

st.set_page_config(page_title="Book Recommendation", layout="wide")

page_style = '''
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
            '''

st.markdown(page_style,unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: Dark Gray;'>Book Recommendation System</h1>",
            unsafe_allow_html=True)


df = pd.read_csv("Top_popular_books.csv")
books = pd.read_csv("recommend_df.csv").astype(str)
sim_score = pickle.load(open("Similarity.pkl",'rb'))
pt = pickle.load(open("pivot_table.pkl",'rb'))
book_name = pickle.load(open("book_name",'rb'))


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def recommend(book_name):
    index = np.where(pt.index == book_name)[0][0]
    print(index)
    similar_items = sorted(list(enumerate(sim_score[index])), key = lambda x: x[1], reverse = True)[1:11]
    print(similar_items)
    final_ans = []
    for i in similar_items:
        ans = []
        temp_data = books[books['Book-Title'] == pt.index[i[0]]]
        print(pt.index[i[0]])
        ans.extend(temp_data[['Book-Title','Book-Author','Publisher',"Year-Of-Publication","Book-Rating","Image-URL-L"]].values)
        final_ans.extend(ans)
    return final_ans

st.write("##")
selected_tab = option_menu(
    menu_title = None,
    options = ['Top 50 Books', 'Book Recommendations','Tinker with Dataset',"Data Analysis" ,"Get in Touch with Me"],
    icons = ['graph-up-arrow','hand-thumbs-up','funnel','clipboard-data','envelope-open'],
    menu_icon = 'cast',
    default_index = 0,
    orientation = 'horizontal',
    styles={
        "icon": {"font-size": "20px"},
        "nav-link": {"font-size": "18px"}
    }
)
st.write("##")

if selected_tab == "Top 50 Books":

    col1, col2, col3, col4, col5 = st.columns(5)
    for i in range(10):
        with col1:
            st.write(str(i*5+1) + ". " + df['Book-Title'][i*5])
            st.image(df["Image-URL-L"][i*5], width=200)
            st.caption("Author: "+df['Book-Author'][i*5])
            st.caption("Publisher: "+df['Publisher'][i*5])
            st.caption("Year Of P ublication: "+ str(df['Year-Of-Publication'][i*5]))
            st.caption("Rating: "+ str(round(float(df['avg_ratings'][i*5]),2)))

        with col2:
            st.write(str(i*5+2) + ". " + df['Book-Title'][i*5+1])
            st.image(df["Image-URL-L"][i*5+1], width=200)
            st.caption("Author: "+df['Book-Author'][i*5+1])
            st.caption("Publisher: "+df['Publisher'][i*5+1])
            st.caption("Year Of Publication: " + str(df['Year-Of-Publication'][i*5+1]))
            st.caption("Rating: "+ str(round(float(df['avg_ratings'][i*5+1]),2)))
        with col3:
            st.write(str(i*5+3) + ". " + df['Book-Title'][i*5+2])
            st.image(df["Image-URL-L"][i*5+2], width=200)
            st.caption("Author: "+df['Book-Author'][i*5+2])
            st.caption("Publisher: "+df['Publisher'][i*5+2])
            st.caption("Year Of Publication: " + str(df['Year-Of-Publication'][i*5+2]))
            st.caption("Rating: "+ str(round(float(df['avg_ratings'][i*5+2]),2)))
        with col4:
            st.write(str(i*5+4) + ". " + df['Book-Title'][i*5+3])
            st.image(df["Image-URL-L"][i*5+3], width=200)
            st.caption("Author: "+df['Book-Author'][i*5+3])
            st.caption("Publisher: "+df['Publisher'][i*5+3])
            st.caption("Year Of Publication: " + str(df['Year-Of-Publication'][i*5+3]))
            st.caption("Rating: "+ str(round(float(df['avg_ratings'][i*5+3]),2)))
        with col5:
            st.write(str(i*5+5) + ". " + df['Book-Title'][i*5+4])
            st.image(df["Image-URL-L"][i*5+4], width=200)
            st.caption("Author: "+df['Book-Author'][i*5+4])
            st.caption("Publisher: "+df['Publisher'][i*5+4])
            st.caption("Year Of Publication: " + str(df['Year-Of-Publication'][i*5+4]))
            st.caption("Rating: "+ str(round(float(df['avg_ratings'][i*5+4]),2)))


elif selected_tab == 'Book Recommendations':

    selection = st.selectbox(
        "Enter the name of the Book you want recommendations for:",
        sorted(book_name)
    )
    if st.button('Recommend Books !', help='Click on it to get book recommendations'):
        out = recommend(selection)
        col1, col2, col3, col4, col5 = st.columns(5)
        for i in range(2):
            with col1:
                st.write(str(i*5+1) + ". " + out[i*5][0])
                st.image(out[i*5][5], width=200)
                st.caption("Author: "+out[i*5][1])
                st.caption("Publisher: "+out[i*5][2])
                st.caption("Year Of Publication: "+ str(out[i*5][3]))
                st.caption("Rating: "+ str(round(float(out[i*5][4]),2)))
            
            with col2:
                st.write(str(i*5+2) + ". " + out[i*5+1][0])
                st.image(out[i*5+1][5], width=200)
                st.caption("Author: "+out[i*5+1][1])
                st.caption("Publisher: "+out[i*5+1][2])
                st.caption("Year Of Publication: "+ str(out[i*5+1][3]))
                st.caption("Rating: "+ str(round(float(out[i*5+1][4]),2)))

            with col3:
                st.write(str(i*5+3) + ". " + out[i*5+2][0])
                st.image(out[i*5+2][5], width=200)
                st.caption("Author: "+out[i*5+2][1])
                st.caption("Publisher: "+out[i*5+2][2])
                st.caption("Year Of Publication: "+ str(out[i*5+2][3]))
                st.caption("Rating: "+ str(round(float(out[i*5+2][4]),2)))

            with col4:
                st.write(str(i*5+4) + ". " + out[i*5+3][0])
                st.image(out[i*5+3][5], width=200)
                st.caption("Author: "+out[i*5+3][1])
                st.caption("Publisher: "+out[i*5+3][2])
                st.caption("Year Of Publication: "+ str(out[i*5+3][3]))
                st.caption("Rating: "+ str(round(float(out[i*5+3][4]),2)))

            with col5:
                st.write(str(i*5+5) + ". " + out[i*5+4][0])
                st.image(out[i*5+4][5], width=200)
                st.caption("Author: "+out[i*5+4][1])
                st.caption("Publisher: "+out[i*5+4][2])
                st.caption("Year Of Publication: "+ str(out[i*5+4][3]))
                st.caption("Rating: "+ str(round(float(out[i*5+4][4]),2)))


elif selected_tab == "Tinker with Dataset":
    st.markdown('''<h6 style='text-align: center; color: Dark Gray;'>
                    The dataset shown here is not full dataset. It only contains the books that have a average rating of more than 0.0.
                    </h6>''',
            unsafe_allow_html=True)
    df = dataframe_explorer(books[['Book-Title','Book-Author','Year-Of-Publication','Publisher']])
    st.header("")
    col1, col2, col3 = st.columns([1,4,1])
    with col2:
        st.dataframe(df)


elif selected_tab == 'Get in Touch with Me':
    st.write("##")
    col1, col2, col3 = st.columns([1,1,2])
    # st.subheader(":mailbox: Get in Touch With Me...!")
    contact_form = '''
        <form action="https://formsubmit.co/tokas.2sonu@gmail.com" method="POST">
            <input type="hidden" name="_autoresponse" value="Thank You for spending your valuable time on my website. I will contact you soon.">
            <input type="hidden" name="_template" value="table">
            <input type="hidden" name="_next" value="https://vivek-2567-movie-recommendation-system-app-ir5ih5.streamlit.app">
            <input type="text" name="name" id = 'input' placeholder = "Your Name" required>
            <input type="email" name="email" id = 'input' placeholder = "Your Email" required>
            <textarea name = 'message' id = 'input' placeholder = 'Your Message' required></textarea>
            <button onclick="document.getElementById('input').value = ''" type="submit">Send</button>
        </form>
    '''

    with col1:
        st.subheader("Meet the Developer")
        pp = Image.open("profile pic/profile-pic.png")
        st.image(pp, output_format='PNG',width = 230)
        st.write("  Developer : Vivek Goel")


    with col2:
        for _ in range(6):
            st.write("")

        st.write("Connect with me at:")
        st.write("[Github](https://github.com/vivek-2567)")
        st.write("[Linkedin](https://www.linkedin.com/in/vivek-goel-0207/)")
        st.write("Mail me @")
        st.write("[Mail](mailto:vivekgoel0207@gmail.com)")

    with col3:
        st.subheader("Send me a Message :rocket:")
        st.markdown(contact_form,unsafe_allow_html=True)
        local_css("style/style.css")
    

elif selected_tab == "Data Analysis":

    col1, col2 = st.columns(2)

    with col1:

        options = st.multiselect(
            "Select the Publishers to find the number of books published with years",
            pickle.load(open("publisher_multiselect.pkl",'rb')),
            default=['Harlequin']
        )
        # pub_button = st.button(
        #     "Click to check"
        # )

        # if pub_button:
        ans = pd.DataFrame(columns=['Year-Of-Publication','Book-Title','Publisher'])

        books['Year-Of-Publication'] = books['Year-Of-Publication'][books['Year-Of-Publication'] != 'DK Publishing Inc']
        books['Year-Of-Publication'] = books['Year-Of-Publication'][books['Year-Of-Publication'] != '0']
        books['Year-Of-Publication'] = books['Year-Of-Publication'][books['Year-Of-Publication'] != 0]

        for publisher in options:
            h_p_books = books[books['Publisher'] == publisher].groupby("Year-Of-Publication").count()[['Book-Title']].sort_values(['Book-Title'],ascending = False).reset_index().head(15)
            h_p_books['Year-Of-Publication'] = h_p_books['Year-Of-Publication'].astype(int)
            h_p_books = h_p_books.sort_values(['Year-Of-Publication'])
            h_p_books['Publisher'] = publisher
            ans = pd.concat([ans, h_p_books])

        fig = px.line(ans,x = "Year-Of-Publication", y = "Book-Title", color = "Publisher",title="Number of books vs Year of Publications")
        st.plotly_chart(fig,use_container_width=True)


    with col2:
        dataset = books.dropna()
        # dataset['Book-Author'] = dataset['Book-Author'].apply(lambda x: x.lower())

        options_a = st.multiselect(
            "Select the Authors to find the number of books published with years",
            pickle.load(open("author_multiselect.pkl",'rb')),
            default = ['William Shakespeare']
        )

        # aut_button = st.button(
        #     "Click here to check"
        # )

        # if aut_button:
        ans = pd.DataFrame(columns=['Year-Of-Publication','Book-Title','Book-Author'])

        
        dataset['Year-Of-Publication'] = dataset['Year-Of-Publication'][dataset['Year-Of-Publication'] != 'DK Publishing Inc']
        dataset['Year-Of-Publication'] = dataset['Year-Of-Publication'][dataset['Year-Of-Publication'] != '0']
        dataset['Year-Of-Publication'] = dataset['Year-Of-Publication'][dataset['Year-Of-Publication'] != 0]

        for author in options_a:
            df_a = dataset[dataset['Book-Author'] == author].groupby('Year-Of-Publication').count()[['Book-Title']].sort_values(['Book-Title'],ascending = False).reset_index().head(15)
            df_a['Year-Of-Publication'] = df_a['Year-Of-Publication'].astype(int)
            df_a = df_a.sort_values(['Year-Of-Publication'])
            df_a['Book-Author'] = author
            ans = pd.concat([ans,df_a])

        fig = px.line(ans,x = "Year-Of-Publication", y = "Book-Title", color = "Book-Author",title="Number of books vs Year of Publications")
        st.plotly_chart(fig, use_container_width=True)
