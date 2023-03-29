from flask import Flask, render_template, request, url_for, redirect
import pandas as pd
import numpy as np
import os 
import sys
import re 

app = Flask(__name__)

option = {"author": "Author", "code": "Code", "data": "Data", "previous_url": "Previous URL", "response_pdf": "Response PDF", "previous_pdf": "Previous PDF"}
months = ["Select", "All", "January", "Feburary", "March", "April", "May", "June", "July", "August", "September","October", "November","December",]
years = ["Select","2021", "2022"]


teamnames = {'T1 臺南台鋼獵鷹' : 'ghosthawks',
              'PLG 桃園璞園領航猿': 'pilots', 
              'CBA 江蘇肯蒂亞': '', 
              'SBL 臺灣銀行': 'trust', 
              'CBA 上海久事': '', 
              'SBL 裕隆納智捷': 'dinos', 
              'SBL 台灣啤酒': 'bears', 
              'T1 台灣啤酒英熊': 'herobears', 
              'PLG 臺北富邦勇士': 'braves', 
              'T1 新北中信特攻': 'dea', 
              'T1 桃園永豐雲豹': 'leopards', 
              'PLG 台新夢想家' : 'dreamers', 
              'SBL 彰化柏力力': 'eagles', 
              'T1 臺中太陽' : 'suns', 
              '日本 B3 豐田合成蠍子' : '', 
              'CBA 天津榮鋼' : '', 
              'PLG 高雄17直播鋼鐵人': 'steelers',
              'CBA 廣州龍獅': '', 
              'PLG 新竹街口攻城獅' : 'lioneers', 
              'PLG 新北國王': 'kings', 
              'T1 高雄全家海神': 'aquas',
              '': ''}




@app.route('/')
def home():
    return render_template("index.html")
    
@app.route('/players') 
def players(): 
    df = pd.read_csv('players.csv') 


    df['plgDraftYear'].fillna(0, inplace=True) 
    df['plgDraftYear']= df['plgDraftYear'].astype('int')
    rookies = [ str(i)+'Rookie' for i in df['plgDraftYear'] if type(i)==int]
    df['plgDraftYear'].replace(0, '', inplace=True)

    df.fillna('', inplace=True)
    # print(df)
    df.drop(columns='id', inplace=True)
    # print(set(df['2022_2023Team']))

    teams=[]
    for team in df['2022_2023Team']: 
        teams.append(teamnames[team])
 

    # print(df['league'])

    # print(df.dtypes)
    leagues = df['league'].tolist()





    view = ['name', 'identity', 'age', 'height', 'birthday', 'plgDraftYear', 'plgDraftPick', '2022_2023Team']
    df = df[view]

    return render_template("players.html", head=df.columns, data=df,teams=teams, nums = len(teams), rookies=rookies, league=leagues)


@app.route('/contract') 
def contract(): 

    return render_template("contract.html")

@app.route('/draft')
def draft(): 
    return render_template("draft.html") 

@app.route('/trade')
def trade(): 
    return render_template("trade.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
