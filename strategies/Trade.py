from models.Rate import Rate

rates_M5 = []
rates_M15 = []
rates_M30 = []
rates_H1 = []
rates_H4 = []
rates_D = []
rates_W = []
rates_M = []

def refresh_rates():
        rates_M5 = Rate.load_rate(period=5)
        rates_M15 = Rate.load_rate(period=15)
        rates_M30 = Rate.load_rate(period=30)
        rates_H1 = Rate.load_rate(period=60)
        rates_H4 = Rate.load_rate(period=(60*4))
        rates_D = Rate.load_rate(period=(60*24))
        rates_W = Rate.load_rate(period=(10080))
        rates_M = Rate.load_rate(period=(43200))



#Yvon
def moving_average(count=8, period = "M5"):
    """
        Ceci est une fonction pour étudier et etablire des 
        stratégies de trade en se basant sur les moyennes
        mobiles
    """
    rate_list = []
    if(period=="M5"):
        rate_list = rates_M5
    elif(period=="M15"):
        rate_list = rates_M15
    elif(period=="M30"):
        rate_list = rates_M30
    elif(period=="H1"):
        rate_list = rates_H1
    elif(period=="H4"):
        rate_list = rates_H4
    elif(period=="D"):
        rate_list = rates_D
    elif(period=="W"):
        rate_list = rates_W
    elif(period=="M"):
        rate_list = rates_M

    for i in range(0, len(rate_list)):
        tmp_sum = rate_list[i]._get_open()
        for j in range(1, count):
            if( (i-j) < 0):
                break
            tmp_sum += rate_list[i-j]._get_open()
        tmp_average = tmp_sum / count
        (rate_list[i].moving_average).open = tmp_average
        tendance = "neutre"    
        regard = 1;    
        if((i-regard) >= 0 and rate_list[i].moving_average.open > rate_list[i-regard].moving_average.open):   
            rate_list[i].tendance = "up"
        elif((i-regard) >= 0 and rate_list[i].moving_average.open < rate_list[i-regard].moving_average.open):      
            rate_list[i].tendance = "down"
        #print(rate_list[i]._get_id()+" -> "+str(rate_list[i].moving_average.open)+" -> "+rate_list[i].tendance)
    return rate_list

#Yvon : Determiner la tendance pour une unité de temps données 
def determiner_tendance(ut="M5", position=0):
    """
        Determine la tendance pour une unité de temps donnée, 
        en se basant sur l'analyse des courbes de 4 moyennes mobiles.
        Paramètres :
        - ut : Unité de temps
               Valeur par défaut : 5 Minutes
        - position : Détermine la date exacte pour laquelle on souhaite connaitre la tendance.
                     Valeur par défaut : 0, cela donne la tendance à la date de la dernière bougie connue
    """
    rates_8 = moving_average(count=8, period=ut)
    rates_20 = moving_average(count=20, period=ut)
    rates_40 = moving_average(count=40,period=ut)
    rates_80 = moving_average(count=80, period=ut)

    down = 0
    up = 0
    if(position == 0):
        #print(rates_8[len(rates_8)-1].to_string())
        #print(rates_20[len(rates_20)-1].to_string())
        #print(rates_40[len(rates_40)-1].to_string())
        #print(rates_80[len(rates_80)-1].to_string())
        if(rates_8[len(rates_8)-1].tendance == "down"):
            down +=1
        elif (rates_8[len(rates_8)-1].tendance == "up"):
            up +=1
        if(rates_20[len(rates_20)-1].tendance == "down"):
            down +=1
        elif (rates_20[len(rates_20)-1].tendance == "up"):
            up +=1
        if(rates_40[len(rates_40)-1].tendance == "down"):
            down +=1
        elif (rates_40[len(rates_40)-1].tendance == "up"):
            up +=1
        if(rates_80[len(rates_80)-1].tendance == "down"):
            down +=1
        elif (rates_80[len(rates_80)-1].tendance == "up"):
            up +=1
    else:
        rate_8 = Rate()
        for i in rates_8:
            id_tab = (i._get_id()).split(" ")
            #print("Teste pour ", i.to_string())
            if(position.split(" ")[0]==id_tab[0]):
                #print("Date capturée : ", i.to_string())
                heure_tab = id_tab[1].split(":")
                if((heure_tab[0] == (((position.split(" "))[1]).split(":"))[0]) and (heure_tab[1] == (((position.split(" "))[1]).split(":"))[1]) and (heure_tab[2] == (((position.split(" "))[1]).split(":"))[2])):
                    if(i.tendance == "down"):
                        down +=1
                    elif(i.tendance == "up"):
                        up += 1
                    pass
            pass
        pass

    if(down > up):
        return -1
    elif(down < up):
        return 1
    
#Yvon
def moving_average_strategie():
    refresh_rates()
    periods = [1, 5, 15, 30, 60, (60*4), (60*24), (10080), (43200)]
    print("Tendance sur 5M : ", determiner_tendance(ut="M5", position="2019.11.07 16:00:00"))
    """print("Tendance sur 15M : ", determiner_tendance(ut="M15", position="2019.11.07 16:00:00"))
    print("Tendance sur 30M : ", determiner_tendance(ut="M30", position="2019.11.07 16:00:00"))
    print("Tendance sur H1 : ", determiner_tendance(ut="H1", position="2019.11.07 16:00:00"))
    print("Tendance sur H4 : ", determiner_tendance(ut="H4", position="2019.11.07 16:00:00"))
    print("Tendance sur D : ", determiner_tendance(ut="D", position="2019.11.07 16:00:00"))
    print("Tendance sur W : ", determiner_tendance(ut="W", position="2019.11.07 16:00:00"))
    print("Tendance sur M : ", determiner_tendance(ut="M", position="2019.11.07 16:00:00"))
    tendance = determiner_tendance(ut=5, position="2019.11.07 16:00:00") + determiner_tendance(ut=15, position="2019.11.07 16:00:00") + determiner_tendance(ut=30, position="2019.11.07 16:00:00") + determiner_tendance(ut=60, position="2019.11.07 16:00:00")
    print("Valeur de la tendance connue : ", tendance)
    if(tendance == 0):
        print("Tendance non pertinante")
    elif(tendance >= 1):
        print("La tendance dit qu'il faut acheter")
    elif(tendance <= -1):
        print("La tendance dit qu'il faut vendre")
    pass
    """

#Michelle
def hause(point_retour=10, period=5):
    """
        Fonction pour determiner quand une serie bougie est en hausse ou en baisse
    """
    rates = Rate.load_rate(period=period)
    for i in range(0, len(rates)):
        if((i-point_retour)<0):
            continue
        tmp_tendance = "neutrale"
        if(float(rates[i]._get_open()) > float(rates[i-point_retour]._get_open())):
            rates[i].tendance = "up"
        elif(float(rates[i]._get_open()) < float(rates[i-point_retour]._get_open())):
            rates[i].tendance = "down"
        else:
            if((i-1) < 0):
                break
            rates[i].tendance = rates[i-1].tendance
    return rates