import os 
from os import listdir
from os.path import isfile, join
import pandas as pd 

years =  ["2021","2022"]

mypath = '/Users/winson/Developer/webScrape/ACLToolBox/database/'
master = pd.DataFrame()
url = 'https://openreview.net/forum?id='
pdf = 'https://openreview.net'


for year in years:
	path = mypath+year
	print(path)
	if not os.path.isdir(path):
		print('no', year)
		continue
	onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]


	for file in onlyfiles: 
		df = pd.read_csv(path +'/'+ file)
		print(df.columns)


		if not 'Abstract' in df.columns:
			try: 
				df['Abstract'] = df['abstract']
				df = df.drop(columns=['abstract'])
			except: 
				pass 
		
		if not 'author' in df.columns: 
			try:
				df['author'] = df['authors']
				df = df.drop(columns=['authors'])
			except: 
				pass 

		if 'pdf' in df.columns: 
			df['PDF'] =  df['pdf'].apply(lambda x: '<a href="{}">{}</a>'.format(pdf+str(x), 'pdf') if not pd.isnull(x) else x)
			df = df.drop(columns=['pdf'])

		if 'authorids' in df.columns:
			df = df.drop(columns=['authorids'])

		
		

		if not 'Code' in df.columns: 
			try:
				if not 'Software' in df.columns:
					df['Code'] = df['software']
					df = df.drop(columns=['software'])
				else: 
					df['Code'] = df['Software']
					df = df.drop(columns=['Software'])
					
			except: 
				pass 

		if not 'Data' in df.columns:
			try: 
				df['Data'] = df['data']
				df = df.drop(columns=['data'])		
			except: 
				pass 				

		if not 'Previous URL' in df.columns: 
			try:
				df['Previous URL'] = df['previous_URL']
				df = df.drop(columns=['previous_URL'])
				
			except: 
				pass 		

		if not 'Previous PDF' in df.columns: 
			try:
				df['Previous PDF'] = df['previous_PDF']
				df = df.drop(columns=['previous_PDF'])
				
			except: 
				pass 
		
		if not 'Response PDF' in df.columns: 
			try: 
				df['Response PDF'] = df['response_PDF']
				df = df.drop(columns=['response_PDF'])
				
			except: 
				pass 

		
		df['Month'] = [file[:-4] if file[:-4] != 'Jun' else 'June' for i in range(len(df.index))]
		df['Year'] = [year for i in range(len(df.index))]
		master = master.append(df, ignore_index=True)

for ind in master.index: 
	master['title'][ind] = '<a href="{}">{}</a>'.format(url+master['id'][ind], master['title'][ind])
	if not pd.isnull(master['Data'][ind]):
		master['Data'][ind] = '<a href="{}">{}</a>'.format(pdf+'/attachment?id='+ master['id'][ind]+'&name=data', "Data")
	if not pd.isnull(master['Code'][ind]):
		master['Code'][ind] = '<a href="{}">{}</a>'.format(pdf+'/attachment?id='+ master['id'][ind]+'&name=software', "Code")
	if not pd.isnull(master['Previous URL'][ind]):
		if pdf in master['Previous URL'][ind]: 
			master['Previous URL'][ind] = '<a href="{}">{}</a>'.format(str(master['Previous URL'][ind]), 'Previous URL')
		else: 
			master['Previous URL'][ind] = '<a href="{}">{}</a>'.format(pdf+str(master['Previous URL'][ind]), 'Previous URL')
	if not pd.isnull(master['Previous PDF'][ind]): 
		if pdf in master['Previous PDF'][ind]: 
			master['Previous PDF'][ind] = '<a href="{}">{}</a>'.format(str(master['Previous PDF'][ind]), 'Previous PDF')
		else: 
			master['Previous PDF'][ind] = '<a href="{}">{}</a>'.format(pdf+str(master['Previous PDF'][ind]), 'Previous PDF')
	if not pd.isnull(master['Response PDF'][ind]):  
		if pdf in master['Response PDF'][ind]: 
			master['Response PDF'][ind] = '<a href="{}">{}</a>'.format(str(master['Response PDF'][ind]), 'Response PDF')
		else: 
			master['Response PDF'][ind] = '<a href="{}">{}</a>'.format(pdf+str(master['Response PDF'][ind]), 'Response PDF')




master = master.rename(columns={i: " ".join(i.split()) for i in master.columns})
master = master.drop(columns=['Unnamed: 0', 'id', 'TL;DR', 'preprint', 'consent', 'paperhash', 'existing_preprints', '_bibtex', 'forum'])
master = master.dropna(axis=1, how='all')
master = master.dropna(subset=['title', 'Abstract'])
master = master.rename(columns={'title': 'Title', 'author': 'Author'})


# master['id']= master['id'].apply(lambda x: '<a href="{}">{}</a>'.format(url+x, x)) 
# master['Code'] =  master['Code'].apply(lambda x: '<a href="{}">{}</a>'.format(pdf+str(x), 'Code') if not pd.isnull(x) else x)
# master['Data'] =  master['Data'].apply(lambda x: '<a href="{}">{}</a>'.format(pdf+str(x), 'Data') if not pd.isnull(x) else x)
# master['Previous URL'] = master['Previous URL'].apply(lambda x: '<a href="{}">{}</a>'.format(pdf+str(x), 'Previous URL') if not pd.isnull(x) else x)
# master['Previous PDF'] = master['Previous PDF'].apply(lambda x: '<a href="{}">{}</a>'.format(pdf+str(x), 'Previous PDF') if not pd.isnull(x) else x)
# master['Response PDF'] = master['Response PDF'].apply(lambda x: '<a href="{}">{}</a>'.format(pdf+str(x), 'Response PDF') if not pd.isnull(x) else x)

master = master.where(pd.notnull(master), "None")

for column in master.columns: 
	print(column)

# df1 = master[master['Month'] == 'November']
# df2 = master[master['Month'] == 'May']
# print(df2['Data'])
# print(df1['Data'])
print(master)
master.to_csv('master.csv')

# print(onlyfiles)
