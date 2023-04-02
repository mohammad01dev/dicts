country = { "iran": ["Tehran","Karaj","Mashad","Tabriz","Urumie","Ardebil"], "Turkey":["Ankara","Istanbul","Izmir","Qahraman Baras"] }

userNational = input("Please Enter The Your National: ")

cityId = 0

cityIndex = int(input("Please Enter The cityId: "))
for i in range(0, len(country.get(userNational))) :
    print(i, country.get(userNational))
    if (cityIndex == i):
        print(country.get(userNational)[cityIndex])
