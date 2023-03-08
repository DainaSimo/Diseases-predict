import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split # va permettre de separer le jeu de donnees en jeu de test et d'entrainnement 
from sklearn.metrics import accuracy_score ,confusion_matrix # va permettre d'afficher la performance de notre modele
import pickle
import streamlit as st
#from ConnectDB import search
import base64

import mysql.connector

mysql = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database = "derma_predict"
    )

def app():
    
    ###################################### DEBUT CONNEXION BD ##################
   

    print("==mysql==> ",mysql)

    mycursor = mysql.cursor()

    print("==mycursor==> ",mycursor)

    def search(id_patient):
        
        query = 'SELECT * FROM patient WHERE id_patient="{}"'.format(id_patient)
        print("==query===> ",query)
        mycursor.execute(query)
        data = mycursor.fetchall()
        for row in data:
            print("==row===> ",row)
        return data 
    ############################################ FIN CONNECTION BD #######################



    def set_bg_hack_url():
        '''
        A function to unpack an image from url and set as bg.
        Returns
        -------
        The background.
        '''
            
        st.markdown(
             f"""
             <style>
             .stApp {{
                 background: url("https://cdn.pixabay.com/photo/2020/06/19/22/33/wormhole-5319067_960_720.jpg");
                 background-size: cover
             }}
             </style>
             """,
             unsafe_allow_html=True
         )

    set_bg_hack_url()

    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    def set_png_as_page_bg(png_file):
        bin_str = get_base64_of_bin_file(png_file)
        page_bg_img = '''
        <style>
        body {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        }
        </style>
        ''' % bin_str
        
        st.markdown(page_bg_img, unsafe_allow_html=True)
        return

    set_png_as_page_bg('Mon_projet.png')

    st.title("Diseases Predict")
    patient=st.text_input("Enter patient_id")
    data_return = search(patient)
    if data_return:

        date = list(data_return)
        
        frame = pd.DataFrame(date,columns=["id_patient","erythema",'scaling',"definite_borders","itching","koebner_phenomenon","polygonal_papules","follicular_papules","oral_mucosal_involvement","knee_and_elbow_involvement","scalp_involvement","family_history","melanin_incontinence","eosinophils_in_the_infiltrate","PNL_infiltrate","fibrosis_of_the_papillary_dermis","exocytosis","acanthosis","hyperkeratosis","parakeratosis","clubbing_of_the_rete_ridges","elongation_of_the_rete_ridges","thinning_of_the_suprapapillary_epidermis","spongiform_pustule","munro_microabcess",'focal_hypergranulosis',"disappearance_of_the_granular_layer","vacuolisation_and_damage_of_basal_layer","spongiosis","saw-tooth_appearance_of_retes","follicular_horn_plug","perifollicular_parakeratosis","inflammatory_monoluclear_inflitrate","band-like_infiltrate","Age"])
        Dataframe = frame.iloc[:, 1:35]
        st.write(frame)
        


    

                                    



    def valeur_manquante(donnees):
         
       
        donnees.fillna(donnees.mean().round(1),inplace=True)
        return donnees
        
        

            

    model=pickle.load(open('model.pkl','rb'))

    if st.button('Predict'):
            
        resultat=model.predict(Dataframe)
        if resultat==1:
            st.header("Psoriasis")

        elif resultat==2:
            st.header("Dermatite Séborrhéique")

        elif resultat==3:
            st.header("Lichen Plan")


        elif resultat==4:
            st.header("Pityriasis Rosea")

        elif resultat==5:
            st.header("Dermatite Chronique")

        else:
            st.header("Pityriasis Rubra Pilaris")



        st.header(" f1_score:95.45%")

        
                

	

	







