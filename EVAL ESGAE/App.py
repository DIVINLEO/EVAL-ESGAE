from timeit import main
import streamlit as st
import pandas as pd
import plotly.express as px
import psycopg2
import hashlib
import time
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_option_menu import option_menu
from numerize.numerize import numerize
import os
# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to create a PostgreSQL connection with context manager
def create_connection():
    return psycopg2.connect(
        dbname="PerfprofESGAE",
        user="postgres",
        password="2024",
        host="localhost",
        port="5432"
    )

# Function to load data from PostgreSQL
def load_data(conn):
    try:
        data = {}
        tables = ['étudiants', 'enseignants', 'note', 'classes', 'matière', 'inscription', 'semestre', 'enseigne']
        
        for table in tables:
            query = f"SELECT * FROM {table}"
            df = pd.read_sql(query, conn)
            data[table] = df

        return data
    except Exception as e:
        st.error(f"Erreur de chargement des données : {e}")
        return {}

# Function to verify user credentials
def verify_user(email, password, conn):
    try:
        query = "SELECT * FROM utilisateurs WHERE adresse_mail = %s AND mot_de_passe = %s"
        df = pd.read_sql(query, conn, params=(email, hash_password(password)))
        if not df.empty:
            return True, df.iloc[0]['nom_complet']  # Return the user's full name as well
        else:
            return False, None
    except Exception as e:
        st.error(f"Erreur de vérification des informations de connexion : {e}")
        return False, None

# Function to register a new user
def register_user(name, email, password, phone, conn):
    try:
        hashed_password = hash_password(password)
        query = "INSERT INTO utilisateurs (nom_complet, adresse_mail, mot_de_passe, telephone) VALUES (%s, %s, %s, %s)"
        cursor = conn.cursor()
        cursor.execute(query, (name, email, hashed_password, phone))
        conn.commit()
        cursor.close()
        return True
    except Exception as e:
        st.error(f"Erreur d'inscription de l'utilisateur : {e}")
        return False

# Page de connexion et d'inscription
def login_register_page():
    st.markdown(
        """
        <style>
        . *,
        *::before,
        *::after {
            box-sizing: border-box;
        }
          body {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background-color: #f0f2f6;
        }
        }
        .full-page {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .form-container {
            background: #fff;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            max-width: 400px;
            width: 100%;
            text-align: center;
        }
        .form-container h1, .form-container h2 {
            color: #333;
        }
        .form-container .radio-container {
            margin: 1rem 0;


        .forms-section {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }

        .section-title {
            font-size: 32px;
            letter-spacing: 1px;
            color: #fff;
        }

        .forms {
            display: flex;
            align-items: flex-start;
            margin-top: 30px;
        }

        .form-wrapper {
            animation: hideLayer .3s ease-out forwards;
        }

        .form-wrapper.is-active {
            animation: showLayer .3s ease-in forwards;
        }

        @keyframes showLayer {
            50% {
                z-index: 1;
            }
            100% {
                z-index: 1;
            }
        }

        @keyframes hideLayer {
            0% {
                z-index: 1;
            }
            49.999% {
                z-index: 1;
            }
        }

        .switcher {
            position: relative;
            cursor: pointer;
            display: block;
            margin-right: auto;
            margin-left: auto;
            padding: 0;
            text-transform: uppercase;
            font-family: inherit;
            font-size: 16px;
            letter-spacing: .5px;
            color: #999;
            background-color: transparent;
            border: none;
            outline: none;
            transform: translateX(0);
            transition: all .3s ease-out;
        }

        .form-wrapper.is-active .switcher-login {
            color: #fff;
            transform: translateX(90px);
        }

        .form-wrapper.is-active .switcher-signup {
            color: #fff;
            transform: translateX(-90px);
        }

        .underline {
            position: absolute;
            bottom: -5px;
            left: 0;
            overflow: hidden;
            pointer-events: none;
            width: 100%;
            height: 2px;
        }

        .underline::before {
            content: '';
            position: absolute;
            top: 0;
            left: inherit;
            display: block;
            width: inherit;
            height: inherit;
            background-color: currentColor;
            transition: transform .2s ease-out;
        }

        .switcher-login .underline::before {
            transform: translateX(101%);
        }

        .switcher-signup .underline::before {
            transform: translateX(-101%);
        }

        .form-wrapper.is-active .underline::before {
            transform: translateX(0);
        }

        .form {
            overflow: hidden;
            min-width: 260px;
            margin-top: 50px;
            padding: 30px 25px;
            border-radius: 5px;
            transform-origin: top;
        }

        .form-connexion {
            animation: hideLogin .3s ease-out forwards;
        }

        .form-wrapper.is-active .form-login {
            animation: showLogin .3s ease-in forwards;
        }

        @keyframes showLogin {
            0% {
                background: #d7e7f1;
                transform: translate(40%, 10px);
            }
            50% {
                transform: translate(0, 0);
            }
            100% {
                background-color: #fff;
                transform: translate(35%, -20px);
            }
        }

        @keyframes hideLogin {
            0% {
                background-color: #fff;
                transform: translate(35%, -20px);
            }
            50% {
                transform: translate(0, 0);
            }
            100% {
                background: #d7e7f1;
                transform: translate(40%, 10px);
            }
        }

        .form-inscription {
            animation: hideSignup .3s ease-out forwards;
        }

        .form-wrapper.is-active .form-signup {
            animation: showSignup .3s ease-in forwards;
        }

        @keyframes showSignup {
            0% {
                background: #d7e7f1;
                transform: translate(-40%, 10px) scaleY(.8);
            }
            50% {
                transform: translate(0, 0) scaleY(.8);
            }
            100% {
                background-color: #fff;
                transform: translate(-35%, -20px) scaleY(1);
            }
        }

        @keyframes hideSignup {
            0% {
                background-color: #fff;
                transform: translate(-35%, -20px) scaleY(1);
            }
            50% {
                transform: translate(0, 0) scaleY(.8);
            }
            100% {
                background: #d7e7f1;
                transform: translate(-40%, 10px) scaleY(.8);
            }
        }

        .form fieldset {
            position: relative;
            opacity: 0;
            margin: 0;
            padding: 0;
            border: 0;
            transition: all .3s ease-out;
        }

        .form-login fieldset {
            transform: translateX(-50%);
        }

        .form-signup fieldset {
            transform: translateX(50%);
        }

        .form-wrapper.is-active fieldset {
            opacity: 1;
            transform: translateX(0);
            transition: opacity .4s ease-in, transform .35s ease-in;
        }

        .form legend {
            position: absolute;
            overflow: hidden;
            width: 1px;
            height: 1px;
            clip: rect(0 0 0 0);
        }

        .input-block {
            margin-bottom: 20px;
        }

        .input-block label {
            font-size: 14px;
            color: #a1b4b4;
        }

        .input-block input {
            display: block;
            width: 100%;
            margin-top: 8px;
            padding-right: 15px;
            padding-left: 15px;
            font-size: 16px;
            line-height: 40px;
            color: #3b4465;
            background: #eef9fe;
            border: 1px solid #cddbef;
            border-radius: 2px;
        }

        .form [type='submit'] {
            opacity: 0;
            display: block;
            min-width: 120px;
            margin: 30px auto 10px;
            font-size: 18px;
            line-height: 40px;
            border-radius: 25px;
            border: none;
            transition: all .3s ease-out;
        }

        .form-wrapper.is-active .form [type='submit'] {
            opacity: 1;
            transform: translateX(0);
            transition: all .4s ease-in;
        }

        .btn-login {
            color: #fbfdff;
            background: #a7e245;
            transform: translateX(-30%);
        }

        .btn-signup {
            color: #a7e245;
            background: #fbfdff;
            box-shadow: inset 0 0 0 2px #a7e245;
            transform: translateX(30%);
              }
        .form-container h1, .form-container h2 {
            color: #333;
          }
        .form-container {
            background: #fff;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            max-width: 400px;
            width: 100%;
            text-align: center;    
        }
        .form-container .radio-container {
            margin: 1rem 0;
        }
        .title, .intro {
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="full-page">', unsafe_allow_html=True)
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    
    st.markdown('<h1 class="title">Bienvenue à EVAL ESGAE</h1>', unsafe_allow_html=True)
    st.markdown('<p class="intro">Veuillez vous connecter ou vous inscrire pour continuer.</p>', unsafe_allow_html=True)

    option = st.radio("Choisissez une option", ['Se connecter', 'S\'inscrire'], key="option", index=0)
    
    if option == 'Se connecter':
        st.subheader("Connexion")
        email = st.text_input("Email", key="login-email")
        password = st.text_input("Mot de passe", type="password", key="login-password")

        if st.button("Se connecter", key="login-button"):
            with create_connection() as conn:
                success, user_name = verify_user(email, password, conn)
                if success:
                    st.success(f"Connexion réussie. Bienvenue, {user_name}!")
                    st.session_state['logged_in'] = True
                    st.session_state['user_name'] = user_name
                    st.session_state['user_email'] = email
                else:
                    st.error("Email ou mot de passe incorrect")
    else:
        st.subheader("Inscription")
        name = st.text_input("Nom Complet", key="signup-name")
        email = st.text_input("Email", key="signup-email")
        password = st.text_input("Mot de passe", type="password", key="signup-password")
        phone = st.text_input("Téléphone", key="signup-phone")

        if st.button("S'inscrire", key="signup-button"):
            with create_connection() as conn:
                if register_user(name, email, password, phone, conn):
                    st.success("Inscription réussie. Vous pouvez maintenant vous connecter.")
                else:
                    st.error("Erreur lors de l'inscription. Veuillez réessayer.")

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

import streamlit as st
import pandas as pd
import plotly.express as px
import os
# Fonction pour créer une connexion à la base de données PostgreSQL
def create_connection():
    # Implémentation de la connexion (remplacez cela par votre propre logique de connexion)
    pass

# Définition de la fonction app_page avec les ajustements pour une mise en page optimisée
def app_page(data):
    st.markdown(
        """
        <style>
        .title {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 30px;
        }
        .title h1 {
            flex-grow: 1;
            text-align: center;
            margin: 0;
        }
        .spacer {
            width: 100px; /* Espace pour les logos */
        }
        .metric-box {
            border: 2px solid #4CAF50;
            border-radius: 10px;
            padding: 10px;
            margin: 5px;
            text-align: center;
            background-color: #F5F5F5;
        }
        .filter-box {
            border: 1px solid #dcdcdc;
            padding: 10px;
            border-radius: 10px;
            background-color: #f9f9f9;
        }
        </style>
        """, unsafe_allow_html=True
    )

    # Titre principal centré avec espaces pour logos
   

# Affichage du titre principal centré
    
    title_style = """
    <style>
    .title {
        text-align: center;
    }
    </style>
    """
    st.markdown(title_style, unsafe_allow_html=True)
    # Utilisation de st.columns pour organiser les éléments
    col1, col2, col3 = st.columns([5, 7, 3])  # Colonnes pour espacement

    # Logo 001.png à gauche
    with col1:
     st.image('img/001.png', width=200)

    # Titre au centre
    with col2:
     st.title('Tableau de Bord Performances Enseignants')

    # Logo 002.png à droite du titre

     

    # Afficher le nom de l'utilisateur si connecté
    if 'user_name' in st.session_state:
        st.write(f"Bienvenue, {st.session_state['user_name']}!")
    else:
        st.write("Bienvenue!")

    # Connexion à la base de données
    conn = create_connection()
    
    # Chargement des données depuis PostgreSQL (utilisation des données du paramètre `data`)
    classes = data.get('classes')
    matieres = data.get('matière')
    enseignants = data.get('enseignants')
    etudiants = data.get('étudiants')
    programmes = data.get('programme')
    inscriptions = data.get('inscription')
    notes = data.get('note')
    enseigne = data.get('enseigne')

    # Filtre déroulant pour afficher les informations des tables
    with st.expander("Dérouler les Informations", expanded=False):
        table_name = st.selectbox("Sélectionnez la table à afficher", options=list(data.keys()))
        df_selection = data[table_name]
        st.write(f"**Affichage de :** {table_name}")
        st.dataframe(df_selection)
    
    # Afficher les statistiques globales avec CSS
    st.markdown("## Indicateurs ")
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.markdown('<div class="metric-box"><strong>Total Étudiants</strong><br>' + str(etudiants.shape[0]) + '</div>', unsafe_allow_html=True)
    col2.markdown('<div class="metric-box"><strong>Total Enseignants</strong><br>' + str(enseignants.shape[0]) + '</div>', unsafe_allow_html=True)
    col3.markdown('<div class="metric-box"><strong>Total Matières</strong><br>' + str(matieres.shape[0]) + '</div>', unsafe_allow_html=True)
    col4.markdown('<div class="metric-box"><strong>Total Notes</strong><br>' + str(notes.shape[0]) + '</div>', unsafe_allow_html=True)
    col5.markdown('<div class="metric-box"><strong>Total Classes</strong><br>' + str(classes.shape[0]) + '</div>', unsafe_allow_html=True)

    

    # Organisation en deux colonnes pour les visualisations
    col1, col2 = st.columns(2)

    with col1:
        # Graphique en Secteurs (Pie Chart) - Répartition des Évaluations par Enseignant
        pie_data = notes['id_enseignant'].value_counts().reset_index()
        pie_data.columns = ['id_enseignant', 'count']
        pie_data = pie_data.merge(enseignants, left_on='id_enseignant', right_on='id_enseignant')
        fig1 = px.pie(pie_data, values='count', names='nom', title='Répartition des Évaluations par Enseignant')
        st.plotly_chart(fig1, use_container_width=True)

        # Graphique à Aires (Area Chart) - Moyenne des Notes par Matière
        area_data = notes.groupby('id_matière')['note'].mean().reset_index()
        area_data = area_data.merge(matieres, left_on='id_matière', right_on='id_matière')
        fig2 = px.area(area_data, x='nom_matière', y='note', title='Moyenne des Notes par Matière')
        st.plotly_chart(fig2, use_container_width=True)

        # Graphique en Nuage de Points (Scatter Plot) - Évolution des Notes par Étudiant
        scatter_data = notes.merge(etudiants, on='id_étudiant')
        fig3 = px.scatter(scatter_data, x='date_évaluation', y='note', color='nom', title='Évolution des Notes par Étudiant')
        st.plotly_chart(fig3, use_container_width=True)

    with col2:
        # Graphique en Courbes (Line Chart) - Taux de Réussite des Étudiants par Enseignant
        pass_rate_query = """
        SELECT id_enseignant, 
               SUM(CASE WHEN note >= 10 THEN 1 ELSE 0 END) / COUNT(*) AS taux_reussite
        FROM note
        GROUP BY id_enseignant
        """
        pass_rate = pd.read_sql(pass_rate_query, conn)
        pass_rate = pass_rate.merge(enseignants, left_on='id_enseignant', right_on='id_enseignant')
        fig4 = px.line(pass_rate, x='nom', y='taux_reussite', title="Taux de Réussite des Étudiants par Enseignant")
        st.plotly_chart(fig4, use_container_width=True)

        # Histogramme (Histogram) - Distribution des Notes par Enseignant
        notes_distribution_query = """
        SELECT id_enseignant,
               AVG(note) AS moyenne_note,
               PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY note) AS mediane_note,
               STDDEV(note) AS ecart_type_note
        FROM note
        GROUP BY id_enseignant
        """
        notes_distribution = pd.read_sql(notes_distribution_query, conn)
        notes_distribution = notes_distribution.merge(enseignants, left_on='id_enseignant', right_on='id_enseignant')
        fig5 = px.histogram(notes_distribution, x='moyenne_note', title="Distribution des Notes par Enseignant")
        st.plotly_chart(fig5, use_container_width=True)

        # Graphique à Barres (Bar Chart) - Nombre de Classes Enseignées par Enseignant
        classes_taught_query = """
        SELECT id_enseignant, COUNT(DISTINCT id_classe) AS nombre_classes
        FROM enseigne
        GROUP BY id_enseignant
        """
        classes_taught = pd.read_sql(classes_taught_query, conn)
        classes_taught = classes_taught.merge(enseignants, left_on='id_enseignant', right_on='id_enseignant')
        fig6 = px.bar(classes_taught, x='nom', y='nombre_classes', title="Nombre de Classes Enseignées par Enseignant")
        st.plotly_chart(fig6, use_container_width=True)

    # Fermeture de la connexion à la base de données
    conn.close()
    
# Function to display a progress bar for a target goal




# Function to manage the sidebar navigation
def sidebar(data):
    st.session_state.show_analyze_classes = False  # Initialisation de la variable de session

    with st.sidebar:
        # Sidebar menu
        selected = option_menu(
            menu_title="Menu Principal",
            options=["Accueil", "Progrès", "Profil", "Enregistrement","Dash", "Déconnexion"],
            icons=["house", "bar-chart", "person", "clipboard","graph-up", "logout"],
            menu_icon="cast",
            default_index=0
        )
    if selected == "Accueil":
        app_page(data)
    elif selected == "Progrès":
        analyze_classes(data)
def analyze_classes(data):
    import psycopg2
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

# Fonction pour établir la connexion à la base de données PostgreSQL
def create_connection():
    conn = psycopg2.connect(
        dbname="PerfprofESGAE",
        user="postgres",
        password="2024",
        host="localhost",
        port="5432"
    )
    return conn

# Fonction pour récupérer les classes depuis la base de données
def get_classes():
    try:
        conn = create_connection()
        query = "SELECT id_classe, nom_classe FROM classes"
        result = pd.read_sql_query(query, conn)
        conn.close()
        
        # Vérifier si le résultat est vide
        if result.empty:
            st.warning("Aucune classe trouvée dans la base de données.")
        
        return result
    except psycopg2.DatabaseError as e:
        st.error(f"Erreur lors de la requête à la base de données PostgreSQL : {e}")
    except Exception as e:
        st.error(f"Une erreur s'est produite : {e}")
    
    return pd.DataFrame()

# Fonction pour récupérer les détails d'une classe spécifique
def get_class_details(class_id):
    try:
        conn = create_connection()
        query = f"""
        SELECT 
            m.nom_matière AS matière, 
            CONCAT(e.nom, ' ', e.prénom) AS enseignant,
            SUM(CASE WHEN et.genre = 'H' THEN 1 ELSE 0 END) AS H,
            SUM(CASE WHEN et.genre = 'F' THEN 1 ELSE 0 END) AS F,
            COUNT(et.id_étudiant) AS T,
            SUM(CASE WHEN n.note < 10 AND et.genre = 'H' THEN 1 ELSE 0 END) AS "H < 10",
            SUM(CASE WHEN n.note < 10 AND et.genre = 'F' THEN 1 ELSE 0 END) AS "F < 10",
            SUM(CASE WHEN n.note < 10 THEN 1 ELSE 0 END) AS "T < 10",
            SUM(CASE WHEN n.note >= 10 AND et.genre = 'H' THEN 1 ELSE 0 END) AS "H >= 10",
            SUM(CASE WHEN n.note >= 10 AND et.genre = 'F' THEN 1 ELSE 0 END) AS "F >= 10",
            SUM(CASE WHEN n.note >= 10 THEN 1 ELSE 0 END) AS "T >= 10",
            ROUND(100.0 * SUM(CASE WHEN n.note < 10 THEN 1 ELSE 0 END) / COUNT(n.id_note), 2) AS "Taux d'échec (%)",
            ROUND(100.0 * SUM(CASE WHEN n.note >= 10 THEN 1 ELSE 0 END) / COUNT(n.id_note), 2) AS "Taux de réussite (%)"
        FROM 
            étudiants et
            JOIN classes c ON et.id_classe = c.id_classe
            JOIN note n ON et.id_étudiant = n.id_étudiant
            JOIN enseignants e ON n.id_enseignant = e.id_enseignant
            JOIN matière m ON n.id_matière = m.id_matière
        WHERE 
            c.id_classe = {class_id}
        GROUP BY 
            m.nom_matière, e.nom, e.prénom
        """
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"Erreur lors de la requête à la base de données : {e}")
        return None

# Fonction principale pour l'analyse des classes
def analyze_classes():
    st.title("Analyse des Classes")
    
    # Récupérer les données des classes
    classes = get_classes()
    
    if classes.empty:
        st.warning("Aucune classe trouvée.")
        return
    
    # Créer un dictionnaire des noms de classes
    class_names = {row['id_classe']: row['nom_classe'] for index, row in classes.iterrows()}

    # Sélection de la classe via une select box
    selected_class_id = st.selectbox(
        "Sélectionnez la classe à analyser",
        options=class_names.keys(),
        format_func=lambda x: class_names[x],
        key='selectbox_classes'
    )

    # Afficher le nom de la classe sélectionnée
    st.header(f"Classe sélectionnée : {class_names[selected_class_id]}")

    # Afficher les détails de la classe sélectionnée
    st.subheader("Détails par Matière et Enseignant")
    class_details = get_class_details(selected_class_id)
    if class_details is None:
        st.error("Erreur: Impossible de récupérer les détails de la classe")
        return
    
    # Structurer les données avec des sous-colonnes pour le tableau
    columns = [
        ("Matière", "matière"),
        ("Enseignant", "enseignant"),
        ("Effectifs", "H"),
        ("Effectifs", "F"),
        ("Effectifs", "T"),
        ("Moyenne Générale <10", "H < 10"),
        ("Moyenne Générale <10", "F < 10"),
        ("Moyenne Générale <10", "T < 10"),
        ("Moyenne Générale >=10", "H >= 10"),
        ("Moyenne Générale >=10", "F >= 10"),
        ("Moyenne Générale >=10", "T >= 10"),
        ("Taux d'Échec (%)", "Taux d'échec (%)"),
        ("Taux de Réussite (%)", "Taux de réussite (%)"),
    ]

    # Filtrer les colonnes disponibles
    available_columns = [col[1] for col in columns if col[1] in class_details.columns]
    multi_index = pd.MultiIndex.from_tuples([col for col in columns if col[1] in available_columns])
    table_data = class_details[available_columns]
    table_data.columns = multi_index

    # Créer un tableau Plotly
    fig_table = go.Figure(data=[go.Table(
        header=dict(values=[f"{col[0]}<br>{col[1]}" for col in multi_index],
                    fill_color='paleturquoise',
                    align='center',
                    font=dict(size=12)),
        cells=dict(values=[table_data[col].tolist() for col in multi_index],
                   fill_color='lavender',
                   align='center',
                   font=dict(size=12))
    )])

    fig_table.update_layout(width=2000, height=400)
    st.plotly_chart(fig_table)

    # Afficher le taux de réussite par enseignant sous forme de histogramme
    st.subheader("Performances Enseignants")
    histogram_data = class_details[['enseignant', "Taux de réussite (%)"]].sort_values(by="Taux de réussite (%)", ascending=True)

    fig_histogram = go.Figure(data=[go.Bar(
        x=histogram_data["Taux de réussite (%)"],
        y=histogram_data["enseignant"],
        orientation='h',
        marker_color='lightskyblue'
    )])

    fig_histogram.update_layout(
        title="Taux de Réussite par Enseignant",
        xaxis_title="Taux de Réussite (%)",
        yaxis_title="Enseignant",
        width=1800,
        height=700
    )
    
    st.plotly_chart(fig_histogram)

    # Progression du nombre d'enseignants avec taux de réussite et d'échec
    st.subheader("Progression du Nombre d'Enseignants avec Taux de Réussite et d'Échec")
    query_teacher_success = """
    SELECT 
        CONCAT(e.nom, ' ', e.prénom) AS enseignant,
        ROUND(100.0 * SUM(CASE WHEN n.note >= 10 THEN 1 ELSE 0 END) / COUNT(n.id_note), 2) AS "Taux de réussite (%)",
        ROUND(100.0 * SUM(CASE WHEN n.note < 10 THEN 1 ELSE 0 END) / COUNT(n.id_note), 2) AS "Taux d'échec (%)"
    FROM 
        enseignants e
        JOIN note n ON e.id_enseignant = n.id_enseignant
    GROUP BY 
        e.nom, e.prénom
    """

    try:
        conn = create_connection()
        df_teacher_success = pd.read_sql_query(query_teacher_success, conn)
        conn.close()
    except Exception as e:
        st.error(f"Erreur lors de la requête à la base de données pour les taux de réussite des enseignants : {e}")
        return

    # Données de succès et d'échec
    success_data = df_teacher_success[['enseignant', "Taux de réussite (%)"]].sort_values(by="Taux de réussite (%)", ascending=True)
    failure_data = df_teacher_success[['enseignant', "Taux d'échec (%)"]].sort_values(by="Taux d'échec (%)", ascending=True)

    # Créer les graphiques Plotly
    fig_success = go.Figure(data=[
        go.Bar(x=success_data["Taux de réussite (%)"], y=success_data["enseignant"], orientation='h', marker_color='green')
    ])
    fig_failure = go.Figure(data=[
        go.Bar(x=failure_data["Taux d'échec (%)"], y=failure_data["enseignant"], orientation='h', marker_color='red')
    ])

    # Mise en forme des graphiques
    fig_success.update_layout(
        title="Taux de Réussite par Enseignant",
        xaxis_title="Taux de Réussite (%)",
        yaxis_title="Enseignant",
        width=1800,
        height=700
    )

    fig_failure.update_layout(
        title="Taux d'Échec par Enseignant",
        xaxis_title="Taux d'Échec (%)",
        yaxis_title="Enseignant",
        width=1800,
        height=700
    )

    # Afficher les graphiques
    st.plotly_chart(fig_success)
    st.plotly_chart(fig_failure)

# Fonction principale pour exécuter l'application Streamlit
analyze_classes()

# Function to manage the sidebar navigation
def sidebar(data):
    st.session_state.show_analyze_classes = False  # Initialisation de la variable de session

    with st.sidebar:
        # Sidebar menu
        selected = option_menu(
            menu_title="Menu Principal",
            options=["Accueil", "Progrès", "Profil", "Enregistrement","Dash", "Déconnexion"],
            icons=["house", "bar-chart", "person", "clipboard","graph-up", "logout"],
            menu_icon="cast",
            default_index=0
        )
    if selected == "Accueil":
        app_page(data)
    elif selected == "Progrès":
        analyze_classes()
    elif selected == "Profil":
        with create_connection() as conn:
            profile_page(conn)
    elif selected == "Enregistrement":
        gestion_Enregistrement()
    elif selected == "Dash":
        with create_connection() as conn:
         dashboard_page(conn)
    elif selected == "Déconnexion":
        st.session_state['logged_in'] = False
        st.success("Vous êtes déconnecté.")
    






# Appel de la fonction pour afficher la page d'analyse des classes


    # Fonction pour créer une connexion à la base de données
def create_connection():
    import psycopg2
    conn = psycopg2.connect(
        dbname="PerfprofESGAE",
        user="postgres",
        password="2024",
        host="localhost",
        port="5432"
    )
    return conn

# Fonction pour afficher le tableau de bord
def dashboard_page(conn):
    st.title("Tableau de Bord")

    # Récupération des données depuis les tables PostgreSQL
    classes = pd.read_sql("SELECT * FROM classes", conn)
    matieres = pd.read_sql("SELECT * FROM matière", conn)
    enseignants = pd.read_sql("SELECT * FROM enseignants", conn)
    etudiants = pd.read_sql("SELECT * FROM étudiants", conn)
    semestres = pd.read_sql("SELECT * FROM semestre", conn)
    programmes = pd.read_sql("SELECT * FROM programme", conn)
    inscriptions = pd.read_sql("SELECT * FROM inscription", conn)
    notes = pd.read_sql("SELECT * FROM note", conn)
    enseigne = pd.read_sql("SELECT * FROM enseigne", conn)

    # Visualisation 1: Graphique en Secteurs (Pie Chart) - Répartition des Évaluations par Enseignant
    st.subheader("Répartition des Évaluations par Enseignant")
    pie_data = notes['id_enseignant'].value_counts().reset_index()
    pie_data.columns = ['id_enseignant', 'count']
    pie_data = pie_data.merge(enseignants, left_on='id_enseignant', right_on='id_enseignant')
    fig1 = px.pie(pie_data, values='count', names='nom', title='Répartition des Évaluations par Enseignant')
    st.plotly_chart(fig1)

    # Visualisation 2: Graphique à Aires (Area Chart) - Moyenne des Notes par Matière
    st.subheader("Moyenne des Notes par Matière")
    area_data = notes.groupby('id_matière')['note'].mean().reset_index()
    area_data = area_data.merge(matieres, left_on='id_matière', right_on='id_matière')
    fig2 = px.area(area_data, x='nom_matière', y='note', title='Moyenne des Notes par Matière')
    st.plotly_chart(fig2)

    # Visualisation 3: Graphique en Nuage de Points (Scatter Plot) - Évolution des Notes par Étudiant
    st.subheader("Évolution des Notes par Étudiant")
    scatter_data = notes.merge(etudiants, on='id_étudiant')
    fig3 = px.scatter(scatter_data, x='date_évaluation', y='note', color='nom', title='Évolution des Notes par Étudiant')
    st.plotly_chart(fig3)

    # Visualisation 4: Graphique en Courbes (Line Chart) - Taux de Réussite des Étudiants par Enseignant
    st.subheader("Taux de Réussite des Étudiants par Enseignant")
    pass_rate_query = """
    SELECT id_enseignant, 
           SUM(CASE WHEN note >= 10 THEN 1 ELSE 0 END) / COUNT(*) AS taux_reussite
    FROM note
    GROUP BY id_enseignant
    """
    pass_rate = pd.read_sql(pass_rate_query, conn)
    pass_rate = pass_rate.merge(enseignants, left_on='id_enseignant', right_on='id_enseignant')
    fig4 = px.line(pass_rate, x='nom', y='taux_reussite', title="Taux de Réussite des Étudiants par Enseignant")
    st.plotly_chart(fig4)

    # Visualisation 5: Histogramme (Histogram) - Distribution des Notes par Enseignant
    st.subheader("Distribution des Notes par Enseignant")
    notes_distribution_query = """
    SELECT id_enseignant,
           AVG(note) AS moyenne_note,
           PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY note) AS mediane_note,
           STDDEV(note) AS ecart_type_note
    FROM note
    GROUP BY id_enseignant
    """
    notes_distribution = pd.read_sql(notes_distribution_query, conn)
    notes_distribution = notes_distribution.merge(enseignants, left_on='id_enseignant', right_on='id_enseignant')
    fig5 = px.histogram(notes_distribution, x='moyenne_note', title="Distribution des Notes par Enseignant")
    st.plotly_chart(fig5)

    # Visualisation 6: Graphique à Barres (Bar Chart) - Nombre de Classes Enseignées par Enseignant
    st.subheader("Nombre de Classes Enseignées par Enseignant")
    classes_taught_query = """
    SELECT id_enseignant, COUNT(DISTINCT id_classe) AS nombre_classes
    FROM enseigne
    GROUP BY id_enseignant
    """
    classes_taught = pd.read_sql(classes_taught_query, conn)
    classes_taught = classes_taught.merge(enseignants, left_on='id_enseignant', right_on='id_enseignant')
    fig6 = px.bar(classes_taught, x='nom', y='nombre_classes', title="Nombre de Classes Enseignées par Enseignant")
    st.plotly_chart(fig6)

      # Visualisation 7: Treemap (Tree Map) - Répartition des Matières par Classe
    st.subheader("Répartition des Matières par Classe")
    treemap_data = pd.DataFrame({
        'id_classe': semestres['id_classe'],
        'id_matière': semestres['id_matière'],
        'count': 1  # Valeur fictive pour le treemap, ajustez selon vos données
    })
    fig7 = px.treemap(treemap_data, path=['id_classe', 'id_matière'], values='count', title="Répartition des Matières par Classe")
    st.plotly_chart(fig7)
    
    # Visualisation 8: Graphique en Barres Empilées (Stacked Bar Chart) - Répartition des Inscriptions par Classe
    st.subheader("Répartition des Inscriptions par Classe")
    stacked_data = pd.crosstab(inscriptions['id_classe'], inscriptions['id_étudiant'])
    fig8 = px.bar(stacked_data, barmode='stack', title='Répartition des Inscriptions par Classe')
    st.plotly_chart(fig8)


# Connexion à la base de données
def connect_db():
    conn = psycopg2.connect(
        dbname='PerfprofESGAE',
        user='postgres',
        password='2024',
        host='localhost',
        port='5432'
    )
    return conn
def read_classes():
    conn = connect_db()
    cur = conn.cursor()
    try:
        cur.execute("SELECT nom_classe, année_scolaire FROM classes")
        rows = cur.fetchall()
        return rows
    except Exception as e:
        st.error(f"Erreur lors de la récupération des classes : {e}")
    finally:
        cur.close()
        conn.close()

def create_classe(nom_classe, année_scolaire):
    conn = connect_db()
    cur = conn.cursor()
    try:
        query = """
        INSERT INTO classes (nom_classe, année_scolaire)
        VALUES (%s, %s)
        """
        cur.execute(query, (nom_classe, année_scolaire))
        conn.commit()
    except Exception as e:
        st.error(f"Erreur lors de l'ajout de la classe : {e}")
    finally:
        cur.close()
        conn.close()

def update_classe(id_classe, nouveau_nom_classe, année_scolaire):
    conn = connect_db()
    cur = conn.cursor()
    try:
        query = """
        UPDATE classes
        SET nom_classe = %s, année_scolaire = %s
        WHERE nom_classe = %s
        """
        cur.execute(query, (nouveau_nom_classe, année_scolaire, id_classe))
        conn.commit()
    except Exception as e:
        st.error(f"Erreur lors de la mise à jour de la classe : {e}")
    finally:
        cur.close()
        conn.close()

def delete_classe(nom_classe):
    conn = connect_db()
    cur = conn.cursor()
    try:
        query = "DELETE FROM classes WHERE nom_classe = %s"
        cur.execute(query, (nom_classe,))
        conn.commit()
    except Exception as e:
        st.error(f"Erreur lors de la suppression de la classe : {e}")
    finally:
        cur.close()
        conn.close()
def read_matieres():
    conn = connect_db()
    cur = conn.cursor()
    try:
        cur.execute("SELECT nom_matière FROM matière")
        rows = cur.fetchall()
        return rows
    except Exception as e:
        st.error(f"Erreur lors de la récupération des matières : {e}")
    finally:
        cur.close()
        conn.close()

def create_matiere(nom_matiere):
    conn = connect_db()
    cur = conn.cursor()
    try:
        query = """
        INSERT INTO matière (nom_matière)
        VALUES (%s)
        """
        cur.execute(query, (nom_matiere,))
        conn.commit()
    except Exception as e:
        st.error(f"Erreur lors de l'ajout de la matière : {e}")
    finally:
        cur.close()
        conn.close()

def update_matiere(nom_matiere, nouveau_nom_matiere):
    conn = connect_db()
    cur = conn.cursor()
    try:
        query = """
        UPDATE matière
        SET nom_matière = %s
        WHERE nom_matière = %s
        """
        cur.execute(query, (nouveau_nom_matiere, nom_matiere))
        conn.commit()
    except Exception as e:
        st.error(f"Erreur lors de la mise à jour de la matière : {e}")
    finally:
        cur.close()
        conn.close()

def delete_matiere(nom_matiere):
    conn = connect_db()
    cur = conn.cursor()
    try:
        query = "DELETE FROM matière WHERE nom_matière = %s"
        cur.execute(query, (nom_matiere,))
        conn.commit()
    except Exception as e:
        st.error(f"Erreur lors de la suppression de la matière : {e}")
    finally:
        cur.close()
        conn.close()
def read_enseignants():
    conn = connect_db()
    cur = conn.cursor()
    try:
        cur.execute("SELECT nom, prénom, date_naissance, genre, telephone, département, email, date_embauche FROM enseignants")
        rows = cur.fetchall()
        return rows
    except Exception as e:
        st.error(f"Erreur lors de la récupération des enseignants : {e}")
    finally:
        cur.close()
        conn.close()

def create_enseignant(nom, prénom, date_naissance, genre, telephone, département, email, date_embauche):
    conn = connect_db()
    cur = conn.cursor()
    try:
        query = """
        INSERT INTO enseignants (nom, prénom, date_naissance, genre, telephone, département, email, date_embauche)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(query, (nom, prénom, date_naissance, genre, telephone, département, email, date_embauche))
        conn.commit()
    except Exception as e:
        st.error(f"Erreur lors de l'ajout de l'enseignant : {e}")
    finally:
        cur.close()
        conn.close()

def update_enseignant(nom, nouveau_nom, nouveau_prénom, nouvelle_date_naissance, nouveau_genre, nouveau_téléphone, nouveau_département, nouveau_email, nouvelle_date_embauche):
    conn = connect_db()
    cur = conn.cursor()
    try:
        query = """
        UPDATE enseignants
        SET nom = %s, prénom = %s, date_naissance = %s, genre = %s, telephone = %s, département = %s, email = %s, date_embauche = %s
        WHERE nom = %s
        """
        cur.execute(query, (nouveau_nom, nouveau_prénom, nouvelle_date_naissance, nouveau_genre, nouveau_téléphone, nouveau_département, nouveau_email, nouvelle_date_embauche, nom))
        conn.commit()
        st.success(f"Enseignant {nom} mis à jour avec succès.")
    except Exception as e:
        st.error(f"Erreur lors de la mise à jour de l'enseignant : {e}")
    finally:
        cur.close()
        conn.close()


def delete_enseignant(nom):
    conn = connect_db()
    cur = conn.cursor()
    try:
        query = "DELETE FROM enseignants WHERE nom = %s"
        cur.execute(query, (nom,))
        conn.commit()
    except Exception as e:
        st.error(f"Erreur lors de la suppression de l'enseignant : {e}")
    finally:
        cur.close()
        conn.close()
def read_etudiants():
    conn = connect_db()
    cur = conn.cursor()
    try:
        query = """
        SELECT e.nom, e.prénom, e.date_naissance, e.genre, c.nom_classe
        FROM étudiants e
        JOIN classes c ON e.id_classe = c.id_classe
        """
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    except Exception as e:
        st.error(f"Erreur lors de la récupération des étudiants : {e}")
    finally:
        cur.close()
        conn.close()


def create_etudiant(nom, prénom, date_naissance, genre, id_classe):
    conn = connect_db()
    cur = conn.cursor()
    try:
        query = """
        INSERT INTO étudiants (nom, prénom, date_naissance, genre, id_classe)
        VALUES (%s, %s, %s, %s, %s)
        """
        cur.execute(query, (nom, prénom, date_naissance, genre, id_classe))
        conn.commit()
    except Exception as e:
        st.error(f"Erreur lors de l'ajout de l'étudiant : {e}")
    finally:
        cur.close()
        conn.close()


def update_etudiant(nom, nouveau_nom, nouveau_prénom, nouvelle_date_naissance, nouveau_genre, nouveau_nom_classe):
    conn = connect_db()
    cur = conn.cursor()
    try:
        query = """
        UPDATE étudiants
        SET nom = %s, prénom = %s, date_naissance = %s, genre = %s, id_classe = %s
        WHERE nom = %s
        """
        cur.execute(query, (nouveau_nom, nouveau_prénom, nouvelle_date_naissance, nouveau_genre, nouveau_nom_classe, nom))
        conn.commit()
    except Exception as e:
        st.error(f"Erreur lors de la mise à jour de l'étudiant : {e}")
    finally:
        cur.close()
        conn.close()
def fetch_class_names():
    conn = connect_db()
    cur = conn.cursor()
    try:
        cur.execute("SELECT id_classe, nom_classe FROM classes")
        classes = cur.fetchall()
        return {classe[1]: classe[0] for classe in classes}
    except Exception as e:
        st.error(f"Erreur lors de la récupération des classes : {e}")
        return {}
    finally:
        cur.close()
        conn.close()
        
def delete_etudiant(nom):
    conn = connect_db()
    cur = conn.cursor()
    try:
        query = "DELETE FROM étudiants WHERE nom = %s"
        cur.execute(query, (nom,))
        conn.commit()
    except Exception as e:
        st.error(f"Erreur lors de la suppression de l'étudiant : {e}")
    finally:
        cur.close()
        conn.close()

        
# Fonction pour lire tous les semestres avec les noms joints des tables associées
def read_semestres():
    conn = connect_db()
    cur = conn.cursor()
    try:
        cur.execute("SELECT id_semestre, nom_semestre FROM semestre")
        rows = cur.fetchall()
        return rows
    except Exception as e:
        st.error(f"Erreur lors de la récupération des semestres : {e}")
    finally:
        cur.close()
        conn.close()

def create_semestre(nom_semestre):
    conn = connect_db()
    cur = conn.cursor()
    try:
        query = """
        INSERT INTO semestre (nom_semestre)
        VALUES (%s)
        """
        cur.execute(query, (nom_semestre,))
        conn.commit()
    except Exception as e:
        st.error(f"Erreur lors de l'ajout du semestre : {e}")
    finally:
        cur.close()
        conn.close()

def update_semestre(id_semestre, nouveau_nom_semestre):
    conn = connect_db()
    cur = conn.cursor()
    try:
        query = """
        UPDATE semestre
        SET nom_semestre = %s
        WHERE id_semestre = %s
        """
        cur.execute(query, (nouveau_nom_semestre, id_semestre))
        conn.commit()
    except Exception as e:
        st.error(f"Erreur lors de la mise à jour du semestre : {e}")
    finally:
        cur.close()
        conn.close()

def delete_semestre(id_semestre):
    conn = connect_db()
    cur = conn.cursor()
    try:
        query = "DELETE FROM semestre WHERE id_semestre = %s"
        cur.execute(query, (id_semestre,))
        conn.commit()
    except Exception as e:
        st.error(f"Erreur lors de la suppression du semestre : {e}")
    finally:
        cur.close()
        conn.close()


        
def gestion_Enregistrement():
    # Chemin absolu vers votre logo
    logo_path = os.path.join(os.getcwd(), 'img', '001.png')

    # Vérifier si le fichier existe
    if os.path.exists(logo_path):
        st.image(logo_path, width=203)
    else:
        st.error("Erreur: Impossible de trouver le fichier de logo.")
    # Menu latéral
    menu = ["Classes", "Matières", "Enseignants", "Étudiants", "Semestre", "Notes"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Classes":
        manage_classes()
    elif choice == "Matières":
        manage_matieres()
    elif choice == "Enseignants":
        manage_enseignants()
    elif choice == "Étudiants":
        manage_etudiants()
    elif choice == "Semestre":
        manage_semestres()
    elif choice == "Notes":
        manage_notes()

def manage_classes():
    st.header("Gestion des Classes")

    # Affichage des classes existantes
    st.subheader("Liste des Classes")
    classes = read_classes()
    if classes:
        classes_df = pd.DataFrame(classes, columns=[ 'Nom', 'Année Scolaire'])
        st.dataframe(classes_df)
    else:
        st.info("Aucune classe trouvée.")

    # Formulaire d'ajout de classe
    st.subheader("Ajouter une Classe")
    nom_classe = st.text_input("Nom de la Classe")
    année_scolaire = st.text_input("Année Scolaire")
    if st.button("Ajouter Classe"):
        if nom_classe and année_scolaire:
            create_classe(nom_classe, année_scolaire)
            st.success("Classe ajoutée avec succès.")
        else:
            st.warning("Veuillez remplir tous les champs.")

    # Formulaire de mise à jour de classe
    st.subheader("Mettre à jour une Classe")
    nom_classe = st.text_input("Nom de la Classe à mettre à jour")
    nouveau_nom_classe = st.text_input("Nouveau Nom de la Classe")
    année_scolaire_update = st.text_input("Nouvelle Année Scolaire")
    if st.button("Mettre à jour Classe"):
        if nom_classe and nouveau_nom_classe and année_scolaire_update:
            update_classe(nom_classe, nouveau_nom_classe, année_scolaire_update)
            st.success(f"Classe {nom_classe} mise à jour.")
        else:
            st.warning("Veuillez remplir tous les champs.")

    # Formulaire de suppression de classe
    st.subheader("Supprimer une Classe")
    nom_classe_delete = st.text_input("Nom de la Classe à supprimer")
    if st.button("Supprimer Classe"):
        if nom_classe_delete:
            delete_classe(nom_classe_delete)
            st.success(f"Classe {nom_classe_delete} supprimée.")

def manage_matieres():
    st.header("Gestion des Matières")

    # Affichage des matières existantes
    st.subheader("Liste des Matières")
    matieres = read_matieres()
    if matieres:
        matieres_df = pd.DataFrame(matieres, columns=['Nom'])
        st.dataframe(matieres_df)
    else:
        st.info("Aucune matière trouvée.")

    # Formulaire d'ajout de matière
    st.subheader("Ajouter une Matière")
    nom_matiere = st.text_input("Nom de la Matière")
    if st.button("Ajouter Matière"):
        if nom_matiere:
            create_matiere(nom_matiere)
            st.success("Matière ajoutée avec succès.")
        else:
            st.warning("Veuillez remplir le champ.")

    # Formulaire de mise à jour de matière
    st.subheader("Mettre à jour une Matière")
    nom_matiere = st.text_input("Nom de la Matière à mettre à jour")
    nouveau_nom_matiere = st.text_input("Nouveau Nom de la Matière")
    if st.button("Mettre à jour Matière"):
        if nom_matiere and nouveau_nom_matiere:
            update_matiere(nom_matiere, nouveau_nom_matiere)
            st.success(f"Matière {nom_matiere} mise à jour.")
        else:
            st.warning("Veuillez remplir tous les champs.")

    # Formulaire de suppression de matière
    st.subheader("Supprimer une Matière")
    nom_matiere_delete = st.text_input("Nom de la Matière à supprimer")
    if st.button("Supprimer Matière"):
        if nom_matiere_delete:
            delete_matiere(nom_matiere_delete)
            st.success(f"Matière {nom_matiere_delete} supprimée.")

def manage_enseignants():
    st.header("Gestion des Enseignants")

    # Affichage des enseignants existants
    st.subheader("Liste des Enseignants")
    enseignants = read_enseignants()
    if enseignants:
        enseignants_df = pd.DataFrame(enseignants, columns=['Nom', 'Prénom', 'Date Naissance', 'Genre', 'Téléphone', 'Département', 'Email', 'Date Embauche'])
        st.dataframe(enseignants_df)
    else:
        st.info("Aucun enseignant trouvé.")

    # Formulaire d'ajout d'enseignant
    st.subheader("Ajouter un Enseignant")
    nom = st.text_input("Nom de l'Enseignant")
    prénom = st.text_input("Prénom de l'Enseignant")
    date_naissance = st.date_input("Date de Naissance")
    genre = st.selectbox("Genre", ["H", "F"])
    téléphone = st.text_input("Téléphone")
    département = st.text_input("Département")
    email = st.text_input("Email")
    date_embauche = st.date_input("Date d'Embauche")
    if st.button("Ajouter Enseignant"):
        if nom and prénom and date_naissance and genre and téléphone and département and email and date_embauche:
            create_enseignant(nom, prénom, date_naissance, genre, téléphone, département, email, date_embauche)
            st.success("Enseignant ajouté avec succès.")
        else:
            st.warning("Veuillez remplir tous les champs.")

    # Formulaire de mise à jour d'enseignant
    st.subheader("Mettre à jour un Enseignant")
    nom = st.text_input("Nom de l'Enseignant à mettre à jour")
    nouveau_nom = st.text_input("Nouveau Nom de l'Enseignant")
    nouveau_prénom = st.text_input("Nouveau Prénom de l'Enseignant")
    nouvelle_date_naissance = st.date_input("Nouvelle Date de Naissance")
    nouveau_genre = st.selectbox("Nouveau Genre", ["H", "F"])
    nouveau_téléphone = st.text_input("Nouveau Téléphone")
    nouveau_département = st.text_input("Nouveau Département")
    nouveau_email = st.text_input("Nouveau Email")
    nouvelle_date_embauche = st.date_input("Nouvelle Date d'Embauche")
    if st.button("Mettre à jour Enseignant"):
        if nom and nouveau_nom and nouveau_prénom and nouvelle_date_naissance and nouveau_genre and nouveau_téléphone and nouveau_département and nouveau_email and nouvelle_date_embauche:
            update_enseignant(nom, nouveau_nom, nouveau_prénom, nouvelle_date_naissance, nouveau_genre, nouveau_téléphone, nouveau_département, nouveau_email, nouvelle_date_embauche)
            st.success(f"Enseignant {nom} mis à jour.")
        else:
            st.warning("Veuillez remplir tous les champs.")

    # Formulaire de suppression d'enseignant
    st.subheader("Supprimer un Enseignant")
    nom_enseignant_delete = st.text_input("Nom de l'Enseignant à supprimer")
    if st.button("Supprimer Enseignant"):
        if nom_enseignant_delete:
            delete_enseignant(nom_enseignant_delete)
            st.success(f"Enseignant {nom_enseignant_delete} supprimé.")

def manage_etudiants():
    st.subheader("Gestion des Étudiants")
    
    st.header("Liste des Étudiants")
    etudiants = read_etudiants()
    if etudiants:
        etudiants_df = pd.DataFrame(etudiants, columns=['Nom', 'Prénom', 'Date de Naissance', 'Genre', 'Classe'])
        st.dataframe(etudiants_df)
    else:
        st.info("Aucun étudiant trouvé.")
    st.subheader("Ajouter un Étudiant")
    nom_etudiant = st.text_input("Nom de l'Étudiant")
    prénom_etudiant = st.text_input("Prénom de l'Étudiant")
    date_naissance_etudiant = st.date_input("Date de Naissance de l'Étudiant")
    genre_etudiant = st.selectbox("Genre de l'Étudiant", ["H", "F"])

    # Récupérer les noms des classes
    classes_options = fetch_class_names()
    nom_classe_etudiant = st.selectbox("Classe de l'Étudiant", list(classes_options.keys()))

    if st.button("Ajouter Étudiant"):
        if nom_etudiant and prénom_etudiant and date_naissance_etudiant and genre_etudiant and nom_classe_etudiant:
         id_classe = classes_options[nom_classe_etudiant]  # Assurez-vous que cela renvoie l'id_classe correctement
        create_etudiant(nom_etudiant, prénom_etudiant, date_naissance_etudiant, genre_etudiant, id_classe)
        st.success("Étudiant ajouté avec succès.")
    else:
        st.warning("Veuillez remplir tous les champs.")
        
    # Formulaire de mise à jour d'étudiant
    st.subheader("Mettre à jour un Étudiant")
    nom_etudiant = st.text_input("Nom de l'Étudiant à mettre à jour")
    nouveau_nom_etudiant = st.text_input("Nouveau Nom de l'Étudiant")
    nouveau_prénom_etudiant = st.text_input("Nouveau Prénom de l'Étudiant")
    nouvelle_date_naissance_etudiant = st.date_input("Nouvelle Date de Naissance de l'Étudiant")
    nouveau_genre_etudiant = st.selectbox("Nouveau Genre de l'Étudiant", ["H", "F"])
    nouveau_nom_classe_etudiant = st.selectbox("Nouvelle Classe de l'Étudiant", list(classes_options.keys()))
    
    if st.button("Mettre à jour Étudiant"):
        if nom_etudiant and nouveau_nom_etudiant and nouveau_prénom_etudiant and nouvelle_date_naissance_etudiant and nouveau_genre_etudiant and nouveau_nom_classe_etudiant:
            update_etudiant(nom_etudiant, nouveau_nom_etudiant, nouveau_prénom_etudiant, nouvelle_date_naissance_etudiant, nouveau_genre_etudiant, classes_options[nouveau_nom_classe_etudiant])
            st.success(f"Étudiant {nom_etudiant} mis à jour.")
        else:
            st.warning("Veuillez remplir tous les champs.")


    # Formulaire de suppression d'étudiant
    st.subheader("Supprimer un Étudiant")
    nom_etudiant_supprimer = st.text_input("Nom de l'Étudiant à supprimer")
    
    if st.button("Supprimer Étudiant"):
        if nom_etudiant_supprimer:
            delete_etudiant(nom_etudiant_supprimer)
            st.success(f"Étudiant {nom_etudiant_supprimer} supprimé avec succès.")
        else:
            st.warning("Veuillez fournir le nom de l'étudiant à supprimer.")

def manage_semestres():
    st.header("Gestion des Semestres")

    # Affichage des semestres existants
    st.subheader("Liste des Semestres")
    semestres = read_semestres()
    if semestres:
        semestres_df = pd.DataFrame(semestres, columns=['ID', 'Nom'])
        st.dataframe(semestres_df)
    else:
        st.info("Aucun semestre trouvé.")

    # Formulaire d'ajout de semestre
    st.subheader("Ajouter un Semestre")
    nom_semestre = st.text_input("Nom du Semestre")
    if st.button("Ajouter Semestre"):
        if nom_semestre:
            create_semestre(nom_semestre)
            st.success("Semestre ajouté avec succès.")
        else:
            st.warning("Veuillez remplir le champ.")

    # Formulaire de mise à jour de semestre
    st.subheader("Mettre à jour un Semestre")
    id_semestre = st.number_input("ID du Semestre à mettre à jour", min_value=1)
    nouveau_nom_semestre = st.text_input("Nouveau Nom du Semestre")
    if st.button("Mettre à jour Semestre"):
        if id_semestre and nouveau_nom_semestre:
            update_semestre(id_semestre, nouveau_nom_semestre)
            st.success(f"Semestre {id_semestre} mis à jour.")
        else:
            st.warning("Veuillez remplir tous les champs.")

    # Formulaire de suppression de semestre
    st.subheader("Supprimer un Semestre")
    id_semestre_delete = st.number_input("ID du Semestre à supprimer", min_value=1)
    if st.button("Supprimer Semestre"):
        if id_semestre_delete:
            delete_semestre(id_semestre_delete)
            st.success(f"Semestre {id_semestre_delete} supprimé.")



# Fonction pour récupérer la liste des classes depuis la base de données
def read_classes():
    conn = connect_db()
    cur = conn.cursor()
    try:
        cur.execute("SELECT id_classe, nom_classe FROM classes")
        rows = cur.fetchall()
        return rows
    except Exception as e:
        st.error(f"Erreur lors de la récupération des classes : {e}")
    finally:
        cur.close()
        conn.close()

# Fonction pour récupérer les matières par classe depuis la base de données
def read_matieres_par_classe(id_classe):
    conn = connect_db()
    cur = conn.cursor()
    try:
        cur.execute("""
            SELECT m.id_matiere, m.nom_matiere
            FROM matieres m
            INNER JOIN classes c ON m.id_classe = c.id_classe
            WHERE c.id_classe = %s
        """, (id_classe,))
        rows = cur.fetchall()
        return rows
    except Exception as e:
        st.error(f"Erreur lors de la récupération des matières : {e}")
    finally:
        cur.close()
        conn.close()

# Fonction pour récupérer les enseignants par classe et matière depuis la base de données
def read_enseignants_par_classe_matiere(id_classe, id_matière):
    conn = connect_db()
    cur = conn.cursor()
    try:
        cur.execute("""
            SELECT e.id_enseignant, e.nom, e.prénom
            FROM enseignants e
            INNER JOIN enseigne en ON e.id_enseignant = en.id_enseignant
            WHERE en.id_classe = %s AND en.id_matière = %s
        """, (id_classe, id_matière))
        rows = cur.fetchall()
        return rows
    except Exception as e:
        st.error(f"Erreur lors de la récupération des enseignants : {e}")
    finally:
        cur.close()
        conn.close()

# Fonction pour récupérer les notes par étudiant et matière depuis la base de données
def read_notes_par_etudiant_matiere(id_etudiant, id_matiere):
    conn = connect_db()
    cur = conn.cursor()
    try:
        cur.execute("""
            SELECT
                n.id_note,
                e.nom AS nom_etudiant,
                e.prenom AS prenom_etudiant,
                ens.nom AS nom_enseignant,
                m.nom_matiere AS nom_matiere,
                n.note,
                n.commentaire,
                n.date_evaluation
            FROM notes n
            INNER JOIN etudiants e ON n.id_etudiant = e.id_etudiant
            INNER JOIN enseignants ens ON n.id_enseignant = ens.id_enseignant
            INNER JOIN matieres m ON n.id_matiere = m.id_matiere
            WHERE n.id_etudiant = %s AND n.id_matiere = %s
        """, (id_etudiant, id_matiere))
        rows = cur.fetchall()
        return rows
    except Exception as e:
        st.error(f"Erreur lors de la récupération des notes : {e}")
    finally:
        cur.close()
        conn.close()

# Fonction pour ajouter une note dans la base de données
def create_note(valeur, id_etudiant, id_matiere):
    conn = connect_db()
    cur = conn.cursor()
    try:
        cur.execute("""
            INSERT INTO notes (note, id_etudiant, id_matiere)
            VALUES (%s, %s, %s)
        """, (valeur, id_etudiant, id_matiere))
        conn.commit()
    except Exception as e:
        st.error(f"Erreur lors de l'ajout de la note : {e}")
    finally:
        cur.close()
        conn.close()

# Fonction pour mettre à jour une note dans la base de données
def update_note(id_note, nouvelle_valeur):
    conn = connect_db()
    cur = conn.cursor()
    try:
        cur.execute("""
            UPDATE note
            SET note = %s
            WHERE id_note = %s
        """, (nouvelle_valeur, id_note))
        conn.commit()
    except Exception as e:
        st.error(f"Erreur lors de la mise à jour de la note : {e}")
    finally:
        cur.close()
        conn.close()

# Fonction pour supprimer une note dans la base de données
def delete_note(id_note):
    conn = connect_db()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM note WHERE id_note = %s", (id_note,))
        conn.commit()
    except Exception as e:
        st.error(f"Erreur lors de la suppression de la note : {e}")
    finally:
        cur.close()
        conn.close()

# Fonction pour récupérer une note par étudiant et matière
# Fonction pour récupérer une note par étudiant et matière
def get_note_by_etudiant_matiere(nom_etudiant, nom_matiere):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM notes WHERE nom_étudiant = %s AND nom_matière = %s", (nom_etudiant, nom_matiere))
        note = cur.fetchone()
        return note  # Retourne le tuple entier de la note
    except Exception as e:
        st.error(f"Erreur lors de la récupération de la note : {e}")
        return None
    finally:
        cur.close()
        conn.close()
# Fonction pour récupérer les étudiants par classe et matière
def read_etudiants_par_classe_matiere(id_classe, id_matiere):
    conn = connect_db()
    cur = conn.cursor()
    try:
        cur.execute("""
            SELECT id_etudiant, nom, prenom
            FROM etudiants
            WHERE id_classe = %s
                AND id_matiere = %s
        """, (id_classe, id_matiere))
        rows = cur.fetchall()
        return rows
    except Exception as e:
        st.error(f"Erreur lors de la récupération des étudiants : {e}")
    finally:
        cur.close()
        conn.close()

# Fonction pour se connecter à la base de données
# Fonction pour gérer les notes dans l'interface Streamlit
import streamlit as st
import psycopg2
import pandas as pd

# Connexion à la base de données PostgreSQL
def get_db_connection():
    return psycopg2.connect(
        dbname="PerfprofESGAE",
        user="postgres",
        password="2024",
        host="localhost",
        port="5432"
    )

# Fonction pour lire les classes
def read_classes():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id_classe, nom_classe FROM classes")
    classes = cur.fetchall()
    cur.close()
    conn.close()
    return classes

# Fonction pour lire les matières par classe
def read_matieres_par_classe(id_classe):
    conn = get_db_connection()
    cur = conn.cursor()
    query = """
        SELECT m.id_matière, m.nom_matière
        FROM matière m
        JOIN enseigne e ON m.id_matière = e.id_matière
        WHERE e.id_classe = %s
    """
    cur.execute(query, (id_classe,))
    matieres = cur.fetchall()
    cur.close()
    conn.close()
    return matieres

# Fonction pour lire les étudiants par classe
def read_etudiants_par_classe(id_classe):
    conn = get_db_connection()
    cur = conn.cursor()
    query = "SELECT id_étudiant, nom, prénom FROM étudiants WHERE id_classe = %s"
    cur.execute(query, (id_classe,))
    etudiants = cur.fetchall()
    cur.close()
    conn.close()
    return etudiants

# Fonction pour lire les notes par étudiant et matière
def read_notes_par_etudiant_matiere(id_etudiant, id_matiere):
    conn = get_db_connection()
    cur = conn.cursor()
    query = """
        SELECT n.id_note, e.nom, e.prénom, en.nom, m.nom_matière, n.note, n.commentaire, n.date_évaluation
        FROM note n
        JOIN étudiants e ON n.id_étudiant = e.id_étudiant
        JOIN enseignants en ON n.id_enseignant = en.id_enseignant
        JOIN matière m ON n.id_matière = m.id_matière
        WHERE n.id_étudiant = %s AND n.id_matière = %s
    """
    cur.execute(query, (id_etudiant, id_matiere))
    notes = cur.fetchall()
    cur.close()
    conn.close()
    return notes

# Fonction pour créer une note
def create_note(note, id_etudiant, id_matiere, id_enseignant, commentaire, date_evaluation):
    conn = get_db_connection()
    cur = conn.cursor()
    query = """
        INSERT INTO note (note, id_étudiant, id_matière, id_enseignant, commentaire, date_évaluation)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cur.execute(query, (note, id_etudiant, id_matiere, id_enseignant, commentaire, date_evaluation))
    conn.commit()
    cur.close()
    conn.close()
# Récupérer la liste des classes
def get_classes():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id_classe, nom_classe FROM classes")
    classes = cur.fetchall()
    cur.close()
    conn.close()
    return classes

# Récupérer la liste des étudiants par classe
def get_etudiants_by_classe(id_classe):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id_étudiant, nom FROM étudiants WHERE id_classe = %s", (id_classe,))
    etudiants = cur.fetchall()
    cur.close()
    conn.close()
    return etudiants

# Récupérer la liste des matières enseignées dans une classe
def get_matieres_by_classe(id_classe):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT DISTINCT m.id_matière, m.nom_matière
        FROM matière m
        JOIN enseigne e ON m.id_matière = e.id_matière
        WHERE e.id_classe = %s
    """, (id_classe,))
    matieres = cur.fetchall()
    cur.close()
    conn.close()
    return matieres

# Récupérer l'enseignant par matière et classe
def get_enseignant_by_matiere_classe(id_classe, id_matiere):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT e.nom, e.prénom
        FROM enseignants e
        JOIN enseigne en ON e.id_enseignant = en.id_enseignant
        WHERE en.id_matière = %s AND en.id_classe = %s
    """, (id_matiere, id_classe))
    enseignant = cur.fetchone()
    cur.close()
    conn.close()
    return enseignant

# Récupérer la note d'un étudiant pour une matière donnée
def get_note_by_etudiant_matiere(id_etudiant, id_matiere):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT note, commentaire FROM note WHERE id_étudiant = %s AND id_matière = %s", (id_etudiant, id_matiere))
    note = cur.fetchone()
    cur.close()
    conn.close()
    return note

# Mettre à jour une note
def update_note(id_etudiant, id_matiere, nouvelle_note, commentaire):
    if commentaire.strip():  # Vérifier si le commentaire n'est pas vide
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("UPDATE note SET note = %s, commentaire = %s WHERE id_étudiant = %s AND id_matière = %s", (nouvelle_note, commentaire, id_etudiant, id_matiere))
        conn.commit()
        cur.close()
        conn.close()
        return True  # Indiquer que la mise à jour s'est effectuée avec succès
    else:
        return False  # Indiquer que le commentaire est obligatoire

# Supprimer une note
def delete_note(id_etudiant, id_matiere):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM note WHERE id_étudiant = %s AND id_matière = %s", (id_etudiant, id_matiere))
    conn.commit()
    cur.close()
    conn.close()



# Code principal pour gérer les notes
def manage_notes():
    st.header("Gestion des Notes")

    # Sélection de la Classe
    classes = read_classes()
    classes_options = {row[1]: row[0] for row in classes} if classes else {}
    nom_classe = st.selectbox("Classe", list(classes_options.keys()), key="select_classe")

    # Sélection de la Matière
    matieres = read_matieres_par_classe(classes_options[nom_classe])
    matieres_options = {row[1]: row[0] for row in matieres} if matieres else {}
    nom_matiere = st.selectbox("Matière", list(matieres_options.keys()), key="select_matiere")

    # Sélection de l'Étudiant
    etudiants = read_etudiants_par_classe(classes_options[nom_classe])
    etudiants_options = {f"{row[1]} {row[2]}": row[0] for row in etudiants} if etudiants else {}
    nom_etudiant = st.selectbox("Étudiant", list(etudiants_options.keys()), key="select_etudiant")

    # Affichage des notes existantes
    st.subheader("Liste des Notes")
    notes = read_notes_par_etudiant_matiere(etudiants_options[nom_etudiant], matieres_options[nom_matiere])
    if notes:
        notes_df = pd.DataFrame(notes, columns=["ID de la Note", "Nom de l'Étudiant", "Prénom de l'Étudiant", "Nom de l'Enseignant", "Nom de la Matière", "Note", "Commentaire", "Date d'Évaluation"])
        st.dataframe(notes_df.drop(columns=['ID de la Note']))  # Ne pas afficher l'ID de la note dans l'interface
    else:
        st.info("Aucune note trouvée.")

    # Formulaire d'ajout de note
    st.subheader("Ajouter une Note")
    enseignants = read_enseignants_par_classe_matiere(classes_options[nom_classe], matieres_options[nom_matiere])
    enseignants_options = {f"{row[1]} {row[2]}": row[0] for row in enseignants} if enseignants else {}
    nom_enseignant = st.selectbox("Enseignant", list(enseignants_options.keys()), key="select_enseignant_ajout")

    valeur_note_ajout = st.text_input("Valeur de la Note", key="number_note_ajout")
    commentaire_ajout = st.text_area("Commentaire", key="commentaire_ajout")
    date_evaluation_ajout = st.date_input("Date d'Évaluation", key="date_evaluation_ajout")
    if st.button("Ajouter Note") and nom_enseignant and valeur_note_ajout:
        create_note(valeur_note_ajout, etudiants_options[nom_etudiant], matieres_options[nom_matiere], enseignants_options[nom_enseignant], commentaire_ajout, date_evaluation_ajout)
        st.success("Note ajoutée avec succès.")

    st.subheader("Mise à jour")
    classes_options = get_classes()
    nom_classe = st.selectbox("Sélectionner la classe", options=[nom for _, nom in classes_options])

    if nom_classe:
        id_classe = [id for id, nom in classes_options if nom == nom_classe][0]
    # Sélection de l'étudiant
    etudiants_options = get_etudiants_by_classe(id_classe)
    nom_etudiant = st.selectbox("Sélectionner l'étudiant", options=[nom for _, nom in etudiants_options])

    if nom_etudiant:
        id_etudiant = [id for id, nom in etudiants_options if nom == nom_etudiant][0]
        # Sélection de la matière
        matieres_options = get_matieres_by_classe(id_classe)
        nom_matiere = st.selectbox("Sélectionner la matière", options=[nom for _, nom in matieres_options])

        if nom_matiere:
            id_matiere = [id for id, nom in matieres_options if nom == nom_matiere][0]
            # Récupérer l'enseignant de la matière sélectionnée
            enseignant = get_enseignant_by_matiere_classe(id_classe, id_matiere)
            if enseignant:
                st.write(f"Enseignant: {enseignant[0]} {enseignant[1]}")
            else:
                st.write("Aucun enseignant trouvé pour cette combinaison de classe et de matière.")

            # Afficher la note actuelle et permettre la mise à jour avec commentaire
            existing_note = get_note_by_etudiant_matiere(id_etudiant, id_matiere)
            if existing_note:
                st.write(f"Note actuelle: {existing_note[0]}")
                if st.button("Mettre à jour Note"):
                    nouvelle_valeur_note = st.slider("Nouvelle Valeur de la Note", min_value=0.0, max_value=20.0, value=float(existing_note[0]), step=0.1)
                    commentaire = st.text_input("Commentaire (obligatoire)", value=existing_note[1] if existing_note[1] else "")
                    if st.button("Valider"):
                        if update_note(id_etudiant, id_matiere, nouvelle_valeur_note, commentaire):
                            st.success("Note mise à jour avec succès.")
                        else:
                            st.warning("Veuillez fournir un commentaire pour mettre à jour la note.")
            else:
                st.error("Aucune note existante à mettre à jour.")

            # Supprimer la note
            if st.button("Supprimer Note"):
                existing_note = get_note_by_etudiant_matiere(id_etudiant, id_matiere)
                if existing_note:
                    delete_note(id_etudiant, id_matiere)
                    st.success("Note supprimée avec succès.")
                else:
                    st.error("Aucune note existante à supprimer.")

     
# Function to display the user profile page
def profile_page(conn):
    st.title("Profil Utilisateur")

    email = st.session_state['user_email']
    query = "SELECT * FROM utilisateurs WHERE adresse_mail = %s"
    df = pd.read_sql(query, conn, params=(email,))
    
    if not df.empty:
        user_info = df.iloc[0]
        st.write("### Vos Informations :")
        st.write(f"**Nom Complet**: {user_info['nom_complet']}")
        st.write(f"**Email**: {user_info['adresse_mail']}")
        st.write(f"**Téléphone**: {user_info['telephone']}")
    else:
        st.error("Impossible de charger les informations du profil.")

# Function to check if required modules are installed
def check_imports():
    required_modules = ["pandas", "streamlit", "plotly", "psycopg2", "numerize", "streamlit_extras", "streamlit_option_menu"]
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            st.markdown(f"<span style='color: yellow;'>Impossible de résoudre l'importation: {module}</span>", unsafe_allow_html=True)

# Check the session state for login status
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Display the main application or the login/register page based on the session state
if st.session_state['logged_in']:
    with create_connection() as conn:
        data = load_data(conn)
        sidebar(data)
else:
    login_register_page()

# Check for required imports
check_imports()
# Main function to run the application


