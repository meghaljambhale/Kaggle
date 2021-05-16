dfNew = pd.DataFrame(zip(names, prices ,links), columns=['ItemName','Price','Href'])
dfNew.drop_duplicates(inplace = True) #this will drop duplicates 
dfNew.to_csv('out.csv', index=False)
dfNew #displays the dataframe
