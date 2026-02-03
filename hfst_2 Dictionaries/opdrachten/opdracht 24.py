sport_uitslagen = {
    'emma': [2,3,1,4,2],
    'liam': [1,2,1,3,0],
    'noah': [0,1,2,1,3],
    'sarah': [3,3,4,2,1],
    'kiana': [1,0,2,1,2],
    'lucas': [2,1,3,1,0]
}
meest = 0
minst = 10
meest_naam = ''
minst_naam =''
for naam, uitslagen in sport_uitslagen.items():
    gemiddeld = sum(uitslagen)/5
    if gemiddeld > meest:
        meest = gemiddeld
        meest_naam = naam
    elif gemiddeld < minst:
        minst = gemiddeld
        minst_naam = naam
print(f'{meest_naam} scoorde het meeste met gemiddeld {meest} doelpunten.')
print(f'{minst_naam} scoord het minste met gemiddeld {minst} doelpunten.')
    