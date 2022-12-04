import pandas as pd

class Consomation:

    def __init__(self, df, departement_data):
        self.df = df 
        self.departement_data = departement_data 


    def data_per_depart(self):
        cons = {}
        for year in range(2018, 2022):
            data_year = self.df_departement(self.df, self.departement_data, year)
            cons[str(
                year)] = data_year["Consommation annuelle moyenne de la commune (MWh)"].values
        df_cons_per_depart = pd.DataFrame(cons)
        df_cons_per_depart.rename(columns={
                                'Consommation annuelle moyenne de la commune (MWh)': 'Consommation annuelle moyenne du departement (MWh)'}, inplace=True)
        df_cons_per_depart["nom_departement"] = data_year.index.values
        df_cons_per_depart['Consommation annuelle moyenne du departement (MWh)'] = df_cons_per_depart.mean(
            axis=1)
        df_cons_per_depart = df_cons_per_depart[[
            'nom_departement', '2018', '2019', '2020', '2021', 'Consommation annuelle moyenne du departement (MWh)']]


        return df_cons_per_depart


    def df_departement(df, departement_data, year):
        df_elec = df.loc[df['Année'] == year]
        df_elec.dropna(subset=['Code INSEE de la commune',
                    'Consommation annuelle moyenne de la commune (MWh)', 'Nom de la commune'])

        df_elec = df_elec.rename(
            columns={'Code INSEE de la commune': 'code_commune_INSEE'})

        df_elec['code_commune_INSEE'] = df_elec['code_commune_INSEE'].astype(str)
        INSEE_codes = set(df_elec['code_commune_INSEE'])
        departement_data = departement_data.loc[departement_data['code_commune_INSEE'].isin(
            INSEE_codes)]
        departement_data['code_commune_INSEE'] = departement_data['code_commune_INSEE'].astype(
            int)
        df_elec['code_commune_INSEE'] = df_elec['code_commune_INSEE'].astype(int)
        new_elec = pd.merge(departement_data, df_elec,
                            how='inner', on='code_commune_INSEE')
        new_elec.drop_duplicates(
            subset=['Consommation annuelle moyenne de la commune (MWh)', 'Nom de la commune'])
        new_elec.dropna(subset=['Nom de la commune'])
        new_elec = new_elec[[
            'nom_departement', 'Consommation annuelle moyenne de la commune (MWh)', 'Nom de la commune']]
        new_elec = new_elec.groupby(['nom_departement']).sum()

        return new_elec