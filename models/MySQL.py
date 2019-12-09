import mysql.connector
class MySQL :
    """
        Cette classe me permettra d'éffectuer des requettes 
        vers ma base des données MySQL
    """
    def __init__(self) :
        self.host = "localhost"
        self.database = "trade"
        self.user = "root"
        self.password = ""

    def select(self, table_name="trade", where_clause = {}, mode="="):
        mydb = mysql.connector.connect(host=self.host,user=self.user,passwd=self.password,database=self.database)
        #print(table_name)
        wc_str = ""
        for i in where_clause.keys():
            if(wc_str != ""):
                wc_str += " and "
            if(mode=="="):
                wc_str += i+" = \""+str(where_clause.get(i))+"\""
            if(mode=="like"):
                wc_str += i+" LIKE '%"+str(where_clause.get(i))+"%'"    
        wc_str = "SELECT * FROM "+table_name+" WHERE "+wc_str
        #print(wc_str)
        mycursor = mydb.cursor()
        mycursor.execute(wc_str)
        myresult = mycursor.fetchall()
        return myresult