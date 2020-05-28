# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 15:09:28 2020

@author: jeevan
"""
import pandas as pd
import en_core_web_lg
def extract_skills(extracted_skills,df2,training_range):
        df_languages=pd.read_csv('E:\Thesis\languages.csv')
        df_frameworks=pd.read_csv("E:\Thesis\\framework.csv")
        df_database=pd.read_csv("E:\Thesis\\database.csv")
        df_os=pd.read_csv("E:\Thesis\\operating_systems.csv")
        df_plat=pd.read_csv("E:\Thesis\\platforms.csv")
        frameworks=df_frameworks.iloc[:,1].tolist()
        frameworks=[x.lower().strip() for x in frameworks]
        #frameworks=[str(x).split(",")[0] for x in df_frameworks.iloc[:,1]]
        languages=list(df_languages.iloc[:,1])
        languages=[x.lower().strip() for x in languages]
        #frameworks=[x.lower().strip().split('\t')[0] for x in frameworks]
        databases=df_database.iloc[:,1].tolist()
        databases=[x.lower().strip() for x in databases]
        op_systems=df_os.iloc[:,1].tolist()
        op_systems=[x.lower().strip() for x in op_systems]
        platforms=df_plat.iloc[:,1].tolist()
        #print(platforms)
        platforms=[x.lower().strip() for x in platforms]
        #print(frameworks)
        new_extracted=dict()
        nlp=en_core_web_lg.load()
        for ele in extracted_skills.keys():
            final_lang=''
            final_frame=''
            final_others=''
            final_database=''
            final_plat=''
            final_os=''
            #print(extracted_skills[ele])
            for skill in extracted_skills[ele]:
                skill_base=skill.lower().strip()
                #print(skill_base)
                if(skill_base in languages):
                    if(final_lang==''):
                        final_lang=skill_base
                    else:
                        final_lang=final_lang+","+skill_base
                elif(skill_base in frameworks):
                    if(final_frame==''):
                        final_frame=skill_base
                    else:
                        final_frame=final_frame+","+skill_base
                elif(skill_base in databases):
                    if(final_database==''):
                        final_database=skill_base
                    else:
                        final_database=final_database+","+skill_base
                elif(skill_base in op_systems):
                    if(final_os==''):
                        final_os=skill_base
                    else:
                        final_os=final_os+","+skill_base
                elif(skill_base in platforms):
                    if(final_plat==''):
                        final_plat=skill_base
                    else:
                        final_plat=final_plat+","+skill_base
                else:
                    if(final_others==''):
                        final_others=skill_base
                    else:
                        final_others=final_others+","+skill_base
            new_extracted[ele]=[final_lang,final_frame,final_database,final_os,final_plat,final_others]
        print((list(new_extracted.items()))[:100])
        # for ele,describe in list(zip(df2.loc[:,'Job_Id'],df2.loc[:,'jobdescription'].tolist()))[:training_range]:
        #     doc=nlp(describe)
        #     final_lang=''
        #     final_frame=''
        #     final_others=''
        #     final_database=''
        #     final_plat=''
        #     final_os=''
        #     for ent in doc.ents:
        #         word=ent.text
        #         word=word.lower().strip()
        #         try:
        #             if(word in languages and word not in final_lang and word not in new_extracted[ele][0].split(",")):
        #                 if(final_lang==''):
        #                     final_lang=word
        #                 else:
        #                     final_lang=final_lang+","+word
        #             elif(word in frameworks and word not in final_frame and word not in new_extracted[ele][1].split(",")):
        #                 if(final_frame==''):
        #                     final_frame=word
        #                 else:
        #                     final_frame=final_frame+","+word
        #             elif(word in databases and word not in final_database and word not in new_extracted[ele][2].split(",")):
        #                 if(final_database==''):
        #                     final_database=word
        #                 else:
        #                     final_database=final_database+","+word
        #             elif(word in op_systems and word not in final_os and word not in new_extracted[ele][3].split(",")):
        #                 if(final_os==''):
        #                     final_os=word
        #                 else:
        #                     final_os=final_os+","+word
        #             elif(word in platforms and word not in final_plat and word not in new_extracted[ele][4].split(",")):
        #                 if(final_plat==''):
        #                     final_plat=word
        #                 else:
        #                     final_plat=final_plat+","+word
        #             else:
        #                 if(final_others==''):
        #                     final_others=word
        #                 else:
        #                     final_others=final_others+","+word
        #         except KeyError:
        #             print("")
        #     try:
        #         if(final_lang!=''):
        #             new_extracted[ele][0]+=","+final_lang
        #         if(final_frame!=''):
        #             new_extracted[ele][1]+=","+final_frame
        #         if(final_database!=''):
        #             new_extracted[ele][2]+=","+final_database
        #         if(final_os!=''):
        #             new_extracted[ele][3]+=","+final_os
        #         if(final_plat!=''):
        #             new_extracted[ele][4]+=","+final_plat
        #         if(final_others!=''):
        #             new_extracted[ele][5]+=","+final_others
        #     except KeyError:
        #         print("")
        #     #new_extracted[ele]=[final_lang,final_frame,final_database,final_os,final_plat,final_others]
        extracted_skills_df=pd.DataFrame.from_dict(new_extracted,orient='index',columns=['Language','Framework','Database','OS','Platform','Others'])
        return extracted_skills_df


#removed for loop which adds JD's keyword to skilldf 
#extracted_skills_df_withoutjd.to_csv("\newthing\extracted_skills_df_withoutjd.csv")