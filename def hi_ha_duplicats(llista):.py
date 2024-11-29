def hi_ha_duplicats(llista):
    """Comprova si hi ha elements duplicats en la llista."""
    return len(llista) != len(set(llista))

# Proves de la funció
print(hi_ha_duplicats([1, 2, 3, 4, 5]))  # Retorna False (no hi ha duplicats)
print(hi_ha_duplicats([1, 2, 3, 2, 5]))  # Retorna True (hi ha duplicats)
print(hi_ha_duplicats(['a', 'b', 'c', 'a']))  # Retorna True (hi ha duplicats)
print(hi_ha_duplicats(['x', 'y', 'z']))  # Retorna False (no hi ha duplicats)
print(hi_ha_duplicats([]))  # Retorna False (una llista buida no té duplicats)
