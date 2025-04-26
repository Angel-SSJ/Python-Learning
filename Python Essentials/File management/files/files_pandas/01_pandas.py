import pandas as pd


csv = pd.read_csv('analisisVentas.csv')

print(csv.head())
InformacionMayor = csv.loc[csv['Ventas'].idxmax()]

print(f'La mayor venta es de: {str(InformacionMayor['Ventas'])} y el vendedor es: {str(InformacionMayor['Vendedor'])}')
print(f'La mayor venta ocurrio en: {str(InformacionMayor['Mes'])}')
print(f'La mayor venta la realizo:{str(InformacionMayor['Vendedor'])}')


InformacionMenor = csv.loc[csv['Ventas'].idxmax()]

print(f'La menor venta es de: {str(InformacionMenor['Ventas'])} y el vendedor es: {str(InformacionMayor['Vendedor'])}')
print(f'La menor venta ocurrio en: {str(InformacionMenor['Mes'])}')
print(f'La menor venta la realizo:{str(InformacionMenor['Vendedor'])}')



cs