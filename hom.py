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

    id_patient1=st.text_input("Enter erythema ")
    id_patient2=st.text_input("Enter scaling")
    id_patient3=st.text_input("Enter definite_borders")
    id_patient4=st.text_input("Enter itching")
    id_patient5=st.text_input("Enter koebner_phenomenon")
    id_patient6=st.text_input("Enter polygonal_papules")
    id_patient7=st.text_input("Enter follicular_papules")
    id_patient8=st.text_input("Enter oral_mucosal_involvement")
    id_patient9=st.text_input("Enter knee_and_elbow_involvement")
    id_patient10=st.text_input("Enter scalp_involvement")
    id_patient11=st.text_input("Enter family_history")
    id_patient12=st.text_input("Enter melanin_incontinence")
    id_patient13=st.text_input("Enter eosinophils_in_the_infiltrate")
    id_patient14=st.text_input("Enter PNL_infiltrate")
    id_patient15=st.text_input("Enter fibrosis_of_the_papillary_dermis")
    id_patient16=st.text_input("Enter exocytosis")
    id_patient17=st.text_input("Enter acanthosis")
    id_patient18=st.text_input("Enter hyperkeratosis")
    id_patient19=st.text_input("Enter parakeratosis")
    id_patient20=st.text_input("Enter clubbing_of_the_rete_ridges")
    id_patient21=st.text_input("Enter elongation_of_the_rete_ridges")
    id_patient22=st.text_input("Enter thinning_of_the_suprapapillary_epidermis")
    id_patient23=st.text_input("Enter spongiform_pustule")
    id_patient24=st.text_input("Enter munro_microabcess")
    id_patient25=st.text_input("Enter focal_hypergranulosis")
    id_patient26=st.text_input("Enter disappearance_of_the_granular_layer")
    id_patient27=st.text_input("Enter vacuolisation_and_damage_of_basal_layer")
    id_patient28=st.text_input("Enter spongiosis")
    id_patient29=st.text_input("Enter saw-tooth_appearance_of_retes")
    id_patient30=st.text_input("Enter follicular_horn_plug")
    id_patient31=st.text_input("Enter perifollicular_parakeratosis")
    id_patient32=st.text_input("Enter inflammatory_monoluclear_inflitrate")
    id_patient33=st.text_input("Enter band-like_infiltrate")
    id_patient34=st.text_input("Enter Age")

   
    

    if st.button("save"):
            
        insert = "INSERT INTO patient (érythème ,desquamation,limites_définies,démangeaisons,phénomène_de_Koebner,papules_polygonales,papules_folliculaires,atteinte_des_muqueuses_buccales,atteinte_des_genoux_et_des_coudes,atteinte_du_cuir_chevelu,antécédents_familiaux, incontinence_de_mélanine,éosinophiles_dans_infiltrat,infiltrat_de_la_PNL,fibrose_du_derme_papillaire,exocytose,acanthose,hyperkératose,parakératose,hernie_des_crêtes_de_rete,allongement_des_crêtes_de_rete,amincissement_de_épiderme_suprapapillaire,pustule_spongiforme,Micro_abcès_de_Munro,hypergranulie_focale,disparition_de_la_couche_granuleuse,vacuolisation_et_atteinte_de_la_couche_basale,spongiose,aspect_en_dents_de_scie_des_rets,bouchon_de_corne_folliculaire,parakératose_périfolliculaire,infiltrat_monolucléaire_inflammatoire,infiltrat_en_forme_de_bande,Âge ) VALUES({0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16},{17},{18},{19},{20},{21},{22},{23},{24},{25},{26},{27},{28},{29},{30},{31},{32},{33});".format(id_patient1,id_patient2,id_patient3,id_patient4,id_patient5,id_patient6,id_patient7,id_patient8,id_patient9,id_patient10,id_patient11,id_patient12,id_patient13,id_patient14,id_patient15,id_patient16,id_patient17,id_patient18,id_patient19,id_patient20,id_patient21,id_patient22,id_patient23,id_patient24,id_patient25,id_patient26,id_patient27,id_patient28,id_patient29,id_patient30,id_patient31,id_patient32,id_patient33,id_patient34)
        print(" ==insert==>   ",insert)
                    
        mycursor.execute(insert)
                    
        # print(" ==insert==>   ",mycursor.execute(insert))
        mysql.commit()

        # print(" ==insert==>   ",mysql.commit())
        mycursor.close()
        # print(" ==insert==>   ",mycursor.close())
        mysql.close()
        # print(" ==insert==>   ",mysql.close())
            
            
        
        
    
