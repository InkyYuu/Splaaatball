import pstats

# Charger les statistiques
# analyses/ le  .stats
p = pstats.Stats('analyses/profiling_results.stats') 

# Nettoyage des chemins pour plus de visibilité
p.strip_dirs()

# Les fonctions les plus coûteuses en temps cumulé
print("Top 10 des fonctions les plus coûteuses (temps cumulé) :")
p.sort_stats("cumulative").print_stats(20)

# Les fonctions les plus coûteuses au total
print("\nTop 10 des fonctions les plus coûteuses (temps total) :")
p.sort_stats("time").print_stats(20)

# Les fonctions les plus appelées
print("\nTop 10 des fonctions les plus appelées :")
p.sort_stats("ncalls").print_stats(20)

with open("analyses/rapport_stats_APRES.txt", "w") as f:
    # Rediriger la sortie vers le fichier
    p.stream = f
    
    # Les fonctions les plus coûteuses en temps cumulé
    f.write("Top 10 des fonctions les plus couteuses (temps cumule) :\n")
    p.sort_stats("cumulative").print_stats(20)

    # Les fonctions les plus coûteuses au total
    f.write("\nTop 10 des fonctions les plus couteuses (temps total) :\n")
    p.sort_stats("time").print_stats(20)

    # Les fonctions les plus appelées
    f.write("\nTop 10 des fonctions les plus appelees :\n")
    p.sort_stats("ncalls").print_stats(20)

# Nom du rapport à generer
print("Rapport complet genere dans 'rapport_stats_APRES.txt'.")