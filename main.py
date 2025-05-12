import streamlit as st
from  streamlit_autorefresh import st_autorefresh
from streamlit_option_menu import option_menu
import folium
from streamlit_folium import st_folium
from datetime import datetime

#--Constants--#
MAIN_IMG_PATH = "images/top.jpg"
WEDDING_IMG_PATH = "images/sep.jpg"
PARTY_IMG_PATH = "images/top.jpg"
OUR_HISTORY_IMG_PATH = "images/top.jpg"
BEST_MOMENTS_IMG_PATH = "images/top.jpg"
WISHES_IMG_PATH = "images/top.jpg"
ORG_IMAGE_PATH = "images/top.jpg"
INFO_IMG_PATH = "images/top.jpg"
REFRESH_INTERVAL = 5000

def page_main_setup() -> None:

    st.set_page_config(layout="wide")

    hide_deploy_button = """
        <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
        </style>
    """
    st.markdown(hide_deploy_button, unsafe_allow_html=True)

    # st.markdown(
    #     """
    #     <style>
    #     .block-container {
    #         background-color: #ffebcd;
    #         padding: 20px;
    #         border-radius: 10px;
    #     }
    #     </style>
    #     """,
    #     unsafe_allow_html=True
    # )

def top_image(path:str) -> None:

    # # Container
    # cont = st.container(key="top_img")
    #
    # with cont:
    #     st.image(path, use_container_width=True)

    # URL do obrazka tła (można użyć lokalnej ścieżki)
    background_image_url = path

    # CSS do kontenera z obrazkiem
    st.markdown(
        f"""
        <style>
            /* Usunięcie marginesów Streamlit */
            .block-container {{
                padding: 0;
                margin: 0;
                max-width: 100%;
            }}

            /* Kontener na obrazek */
            .image-container {{
                width: 100vw; /* Cała szerokość ekranu */
                height: auto; /* Automatyczna wysokość (proporcjonalnie) */
                display: flex;
                justify-content: center;
                align-items: center;
                position: relative;
            }}

            /* Obrazek jako tło */
            .image-container img {{
                width: 100%; /* Szerokość na cały ekran */
                height: 300px; /* Zachowanie proporcji */
                object-fit: contain; /* Dopasowanie bez rozciągania */
            }}

            /* Tekst na obrazku */
            .text-overlay {{
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                font-size: 50px;
                font-weight: bold;
                color: white;
                text-shadow: 3px 3px 6px black;
            }}
        </style>

        <div class="image-container">
            <img src="{background_image_url}" />
            <div class="text-overlay" id="countdown">Czas: 10s</div>
        </div>
        """,
        unsafe_allow_html=True
    )

def page_auto_refresh(interval:int) -> None:
    _ = st_autorefresh(interval=interval, limit=None, key="auto-refresh")

def menu() -> any:

    # Container
    cont = st.container(key="menu")

    with cont:
        # Option menu
        selected = option_menu(
            menu_title=None,
            options=["Ślub", "Wesele", "Plan", "Prezenty", "Księga gości", "Kontakt"],
            menu_icon=["ring"],
            default_index=0,
            orientation="horizontal",
            styles={
                "container": {
                    "display": "flex",
                    "justify-content": "center",
                    "width": "80%",
                    "background-color": "transparent",
                    "margin": "auto",
                },
                "nav-link": {
                    "font-size": "18px",
                    "text-align": "center",
                    "padding": "10px",
                    "color": "green",
                },
                "nav-link-selected": {
                    "background-color": "transparent",
                    "color": "green",
                },
            }
        )

    return selected

def mini_image_wedding(path:str) -> None:

    # Container
    cont = st.container(key="wedding_img")

    with cont:
        # Columns declaration
        _, col, _ = st.columns(3)

        # Content
        with col:
            st.image(path)

def wedding_section() -> None:

    # Container
    cont = st.container(key="wedding_section")
    # script = """<div id = 'chat_outer'></div>"""
    # st.markdown(script, unsafe_allow_html=True)

    with cont:

        # Columns declaration
        _, col, _ = st.columns(3)

        with col:
            st.title("Ślub")

            inner_col1, inner_col2 = st.columns(2)

            with inner_col1:
                st.write("[img] 23.08.2025 [img] 15:30")
                st.write("[img] Kościół im. MB Radosnej, ul. Kościuszki 2, Katowice")

            with inner_col2:
                map_ = folium.Map(location=[52.2298, 21.0118], zoom_start=13)
                folium.Marker([52.2298, 21.0118], popup="Kościół Św. Piotra").add_to(map_)

                st.markdown('<div class="map-container">', unsafe_allow_html=True)
                st_folium(map_, key="map1", width=300, height=200)
                st.markdown('</div>', unsafe_allow_html=True)

                st.markdown('</div>', unsafe_allow_html=True)

def mini_image_party(path:str):

    # Container
    cont = st.container(key="party_img")

    with cont:
        # Columns declaration
        _, col, _ = st.columns(3)

        # Content
        with col:
            st.image(path)

def party_section() -> None:

    # Container
    cont = st.container(key="party_section")

    with cont:
        # Columns declaration
        _, col, _ = st.columns(3)

        with col:

            inner_col1, inner_col2 = st.columns(2)

            with inner_col1:

                st.title("Wesele")

                st.text("Po ślubie zapraszamy na przyjęcie weselne. Przewidujemy wspaniałą zabawę do białego rana! :)")
                st.text("[img] Restauracja Zamkowa, ul. 3 maja 8, Pszczyna")

            with inner_col2:
                map_ = folium.Map(location=[52.2298, 21.0118], zoom_start=13)
                folium.Marker([52.2298, 21.0118], popup="Sala weselna").add_to(map_)

                st.markdown('<div class="map-container">', unsafe_allow_html=True)
                st_folium(map_, key="map2", width=300, height=250)
                st.markdown('</div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

def middle_image(path:str) -> None:

    # Container
    cont = st.container(key="mid_img")

    with cont:
        st.image(path, use_container_width=True)

def mini_image_our_history(path:str) -> None:
    # Container
    cont = st.container(key="oh_img")

    with cont:
        # Columns declaration
        _, col, _ = st.columns(3)

        # Content
        with col:
            st.image(path)

def our_history_section():

    # Container
    cont = st.container(key="oh_section")

    with cont:

        # Columns declaration
        _, col, _ = st.columns(3)

        with col:

            st.title("Nasza historia")
            st.text("Poznaliśmy się zupełnie przypadkowo! Oboje czekaliśmy na przystanku autobusowym, kiedy ja (czyli Alicja) zorientowałam się, że nie zabrałam z domu telefonu komórkowego, co za pech! W telefonie miała bilet miesięczny, a niestety w portfelu brak gotówki, aby kupić bilet u kierowcy... Rozejrzałam się zatem dookoła i wypatrzyłam Olka. Stał niedaleko i słuchał muzyki na słuchawkach. Podeszłam nieśmiało i zapytałam, czy mógłby mnie poratować kilkoma złotymi na bilet. I tak zaczęła się nasza znajomość, która trwa to dziś! Nadal często jeździmy autobusem z tego przystanku... :)")
            st.text("")

def mini_image_best_moments(path:str) -> None:
    # Container
    cont = st.container(key="bm_img")

    with cont:
        # Columns declaration
        _, col, _ = st.columns(3)

        # Content
        with col:
            st.image(path)

def best_moments_section():

    # Container
    cont = st.container(key="bm_section")

    with cont:

        # Columns declaration
        _, col, _ = st.columns(3)

        with col:

            st.markdown(
                """
                <style>
                .stContainer {
                    background-color: #aaaaaa;
                    padding: 20px;
                    border-radius: 10px;
                }
                </style>
                """, unsafe_allow_html=True
            )

            st.title("Najlepsze wspólne chwile")
            st.text("")

        inner_col1, inner_col2, inner_col3, inner_col4, inner_col5 = st.columns(5)

        with inner_col1:
            st.image("images/top.jpg")
        with inner_col2:
            st.image("images/top.jpg")
        with inner_col3:
            st.image("images/top.jpg")
        with inner_col4:
            st.image("images/top.jpg")
        with inner_col5:
            st.image("images/top.jpg")

def party_plan_section():

    # Container
    cont = st.container(key="pp_section")

    with cont:

        # Columns declaration
        _, col, _ = st.columns(3)

        with col:

            st.title("Plan wesela")
            st.text("14:00 - ślub")
            st.text("15:00 - przyjazd na salę weselną")
            st.text("15:15 - składanie życzeń Parze Młodej")
            st.text("16:00 - obiad")
            st.text("17:00 - pierwszy taniec i rozpoczęcie zabawy")
            st.text("19:00 - tort")
            st.text("21:00 - I kolacja")
            st.text("22:00 - niespodzianka dla gości! :)")
            st.text("00:00 - oczepiny")
            st.text("01:00 - II kolacja")
            st.text("04:00 - zakończenie zabawy")

def mini_image_wishes(path:str) -> None:
    # Container
    cont = st.container(key="w_img")

    with cont:
        # Columns declaration
        _, col, _ = st.columns(3)

        # Content
        with col:
            st.image(path)

def wishes_section():

    # Container
    cont = st.container(key="w_section")

    with cont:

        # Columns declaration
        _, col, _ = st.columns(3)

        with col:

            st.title("Zamiast kwiatów, będzie nam miło otrzymać:")
            st.text("")
            st.text("Marzymy o tym, by mieć wlasną domową piwniczkę pełną win, dlatego będzie nam miło, jeśli otrzymamy butelkę tego trunku :)")
            st.text("")
            st.text("Uwielbiamy ksiązki i marzymy o obszernej domowej biblioteczce, będziemy wdzięczni za upominek w formie pozycji bibliograficznej :)")
            st.text("")
            st.text("esteśmy słodyczoholikami, dlatego zamiast kwiatów prosimy o słodki podarunek :)")
            st.text("")
            st.text("Pragniemy, aby swoim szczęściem podzielić się z innymi, więc w ramach prezentu prosimy o wpłaty na konto Fundacji Małe Dzieci: 1100 1100 1100 1100 1100.")
            st.text("")
            st.text("17:00 - pierwszy taniec i rozpoczęcie zabawy")
            st.text("")

def mini_image_org(path:str) -> None:
    # Container
    cont = st.container(key="org_img")

    with cont:
        # Columns declaration
        _, col, _ = st.columns(3)

        # Content
        with col:
            st.image(path)

def org_section():

    # Container
    cont1 = st.container(key="org_section1")
    cont2 = st.container(key="org_section2")

    with cont1:

        # Columns declaration
        _, col, _ = st.columns(3)

        with col:

            st.title("Kilka spraw organizacyjnych")

            inner_col1, inner_col2 = st.columns(2)

            with inner_col1:
                st.text("Dojazd")
                st.text("")
                st.text("Zapewniamy transport spod kościoła na salę weselną. Po Północy będą również kursowały busy, odwożące gości do domu z sali weselnej.")

            with inner_col2:
                st.text("Dzieci")
                st.text("")
                st.text("Zapraszamy na wesele wszystkie maluchy! Od 18:00 do 21:00 na sali będzie animator na wesele, który zajmie się pociechami.")

            st.text("")

    with cont2:

        # Columns declaration
        _, col, _ = st.columns(3)

        with col:

            inner_col1, inner_col2 = st.columns(2)

            with inner_col1:
                st.text("Nocleg")
                st.text("")
                st.text("Rezerwujemy pokoje dla naszych gości w Hotelu ABC w Pszczynie. Prosimy o kontakt z nami, jeśli potrzebujecie noclegów :)")

            with inner_col2:
                st.text("Poprawiny")
                st.text("")
                st.text("Następnego dnia zapraszamy na poprawiny - również do Restauracji Zamkowej w Pszczynie. Zabawę rozpoczynamy o godzinie 14:00.")

    st.title("")

def info_section(graphic_path:str) -> None:

    # Container
    cont = st.container(key="info_section")

    with cont:

        # Columns declaration
        _, col, _ = st.columns(3)

        with col:

            inner_col1, inner_col2 = st.columns(2)

            with inner_col1:
                st.image(graphic_path)

            with inner_col2:

                st.header("Zajrzyjcie tu po weselu...")
                st.text("Zamieścimy tu materiały z ceremonii i wspólnej zabawy. Nie możemy się doczekać!")

def film_yt_section() -> None:

    # Container
    cont = st.container(key="f_yt_section")

    with cont:

        # Columns declaration
        _, col, _ = st.columns(3)

        with col:
            st.title("Zobaczcie nasz cudowny film:")
            st.text("[Film]")

def contact_section() -> None:

    # Container
    cont = st.container(key="contact_section")

    with cont:

        # Columns declaration
        _, col, _ = st.columns(3)

        with col:
            st.title("Kontakt w razie pytań:")

            inner_col1, inner_col2, inner_col3 = st.columns(3)

            with inner_col1:
                st.text("[img]")

            with inner_col2:
                st.text("Panna młoda - Justyna Ciołek")
                st.text("[img] 667 171 156")

            with inner_col3:
                st.image("images/top.jpg")



if __name__ == "__main__":

    page_main_setup()
    page_auto_refresh(REFRESH_INTERVAL)
    top_image(MAIN_IMG_PATH)
    menu()
    mini_image_wedding(WEDDING_IMG_PATH)
    wedding_section()
    mini_image_party(PARTY_IMG_PATH)
    party_section()
    middle_image(MAIN_IMG_PATH)
    our_history_section()
    mini_image_best_moments(BEST_MOMENTS_IMG_PATH)
    best_moments_section()
    party_plan_section()
    mini_image_wishes(WISHES_IMG_PATH)
    wishes_section()
    mini_image_org(ORG_IMAGE_PATH)
    org_section()
    info_section(INFO_IMG_PATH)
    film_yt_section()
    contact_section()
