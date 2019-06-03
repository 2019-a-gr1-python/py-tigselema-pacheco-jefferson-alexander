#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:07:32 2019

@author: dev-08
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

directorio = "pokemon.csv"
pokemons = pd.read_csv(directorio, index_col= 0)

tiposPokemon = pokemons['Type 1'].unique()
cantidadPokemonsXTipo = np.zeros(tiposPokemon.size);
for idx, tipo in enumerate(tiposPokemon):
    cantidadPokemonsXTipo[idx] = pokemons[pokemons['Type 1'] == tipo].Name.count()

plt.figure(1)
plt.bar(tiposPokemon, cantidadPokemonsXTipo)
plt.xticks(rotation=90)
plt.xlabel('Tipo')
plt.ylabel('Cantidad')
plt.title('Pokemon por Tipos')

generacionesPokemon = pokemons['Generation'].unique()
cantidadPokemonsXGeneracion = np.zeros(generacionesPokemon.size);
for idx, generacion in enumerate(generacionesPokemon):
    cantidadPokemonsXGeneracion[idx] = pokemons[pokemons['Generation'] == generacion].Name.count()

plt.figure(2)
plt.bar(generacionesPokemon, cantidadPokemonsXGeneracion)
plt.xticks(rotation=90)
plt.xlabel('Generacion')
plt.ylabel('Cantidad')
plt.title('Pokemon por Generacion')


pokemonDescendenteTotal = pokemons.sort_values(ascending = False, by = 'Total')

print('Pokemons màs poderosos')
print(pokemonDescendenteTotal.loc[:,['Name','Total','Type 1','Generation','Attack', 'Defense']].head(5))
print('Pokemons más debiles')
print(pokemonDescendenteTotal.loc[:,['Name','Total','Type 1','Generation','Attack', 'Defense']].tail(5))

pokemonDescendenteDefense = pokemons.sort_values(ascending = False, by = 'Defense')

print('Pokemons con más defensa')
print(pokemonDescendenteDefense.loc[:,['Name','Type 1', 'Defense','Generation']].head(5))
print('Pokemons con menos defensa')
print(pokemonDescendenteDefense.loc[:,['Name','Type 1', 'Defense','Generation']].tail(5))

pokemonDescendenteSpeedAtk = pokemons.sort_values(ascending = False, by = 'Sp. Atk')

print('Pokemons con más velocidad de ataque')
print(pokemonDescendenteSpeedAtk.loc[:,['Name','Type 1','Sp. Atk','Generation']].head(5))
print('Pokemons con menos velocidad de ataque')
print(pokemonDescendenteSpeedAtk.loc[:,['Name','Type 1','Sp. Atk','Generation']].tail(5))