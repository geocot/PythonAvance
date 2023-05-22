def TourHanoi(n, source, destination, auxiliaire):
    if n == 1:
        print("Déplacer le disque 1 de la source", source, "vers la destination", destination)
        return
    TourHanoi(n - 1, source, auxiliaire, destination)
    print("Déplacer le disque", n, "de la source", source, "vers la destination", destination)
    TourHanoi(n - 1, auxiliaire, destination, source)


# Départ
n = 3
TourHanoi(n, 'A', 'B', 'C')

