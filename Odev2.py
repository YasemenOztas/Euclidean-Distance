def euclideanDistance(points):
    distances = []

    for i in range(0, len(points)):
        for j in range(i + 1, len(points)):
            (x1, y1) = points[i]
            (x2, y2) = points[j]
            distance = round(( (x1 - x2) ** 2 + (y1 - y2) ** 2 ) ** 0.5 , 4) # Virgülden sonra 4 basamak yazar
            distances.append(distance)
    
    s = distances[0] # Her hangi bir değer aldım
    for i in distances:
        if s > i:
            s = i

#    print("Distances:", distances)
    print("Min Distance:", s)


"""
İlk for döngüsünde tuttuğum tüm noktaları, kendisinden sonra gelen noktalar ile arasındaki mesafelerini hesapladım
Bu şekilde iki nokta arasındaki mesafeyi ikişer kez yazdırmadım (nokta1-nokta2 ile nokta2-nokta1 gibi)
Her iki noktanın x ve y değerlerini alıp pisagor teoremiyle aralarındaki mesafeyi hesapladım
Bu mesafeleri bir diziye aktarıp en küçük olan mesafeyi yazdırdım
(Diziyi sorted ile sıralayıp ilk değeri de alabilirdim veya min(distances) kullanabilirdim)
"""


points = ((1, 8), (4, 4), (-2, 3), (7, -5), (3, 5))

euclideanDistance(points)
