import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
url = "https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv"
df = pd.read_csv(url)
print("Dataset Preview:")
print(df.head())
top_countries = ['India', 'United States', 'Brazil', 'Russia', 'United Kingdom']
df_top = df[df['Country'].isin(top_countries)]
sns.set(style="whitegrid")
plt.figure(figsize=(12,6))
for country in top_countries:
    country_data = df_top[df_top['Country'] == country]
    plt.plot(country_data['Date'], country_data['Confirmed'], label=country)
plt.title('COVID-19 Confirmed Cases Over Time (Top 5 Countries)')
plt.xlabel('Date')
plt.ylabel('Confirmed Cases')
plt.legend()
plt.tight_layout()
plt.show()
total_deaths = df_top.groupby('Country')['Deaths'].max().sort_values(ascending=False)
plt.figure(figsize=(8,5))
sns.barplot(
    x=total_deaths.index,
    y=total_deaths.values,
    hue=total_deaths.index,  
    dodge=False,              
    palette='coolwarm',
    legend=False              
)

plt.title('Total COVID-19 Deaths by Country')
plt.xlabel('Country')
plt.ylabel('Deaths')
plt.tight_layout()
plt.show()


plt.figure(figsize=(8,6))
sns.scatterplot(x='Confirmed', y='Deaths', hue='Country', data=df_top)
plt.title('Confirmed Cases vs Deaths')
plt.xlabel('Confirmed Cases')
plt.ylabel('Deaths')
plt.tight_layout()
plt.show()


corr = df_top[['Confirmed', 'Deaths', 'Recovered']].corr()
plt.figure(figsize=(5,4))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()

print("✅ Visualization Completed Successfully!")
