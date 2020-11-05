import sqlite3
import csv
import os #manupular arquivos
import easygui #abrir arquivo
import shutil #copiar arquivo de uma pasta para outra

class category:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class product:
    def __init__(self, id, name, description, price, categories):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.categories = categories

class database:
    def __init__(self):
        try:
            conn = sqlite3.connect('product.db')
            c = conn.cursor()
            c.execute("PRAGMA foreign_keys= 1")
            c.execute("PRAGMA table_info(PRODUCTCATEGORY)")
            print(c.fetchall())
            # EXCLUIR TABELAS - TESTE!
            c.execute("DROP TABLE PRODUCTCATEGORY")
            c.execute("DROP TABLE PRODUCT")
            c.execute("DROP TABLE CATEGORY")

            # Criar tabelas / verificar se já existem
            c.execute("""CREATE TABLE IF NOT EXISTS CATEGORY 
                (idcategory INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL)""")
            c.execute("""CREATE TABLE IF NOT EXISTS PRODUCT 
                (idproduct INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, description TEXT, price INTEGER)""")
            c.execute("""CREATE TABLE IF NOT EXISTS PRODUCTCATEGORY 
                (idproduct INTEGER NOT NULL, idcategory INTEGER NOT NULL, CONSTRAINT fk_product FOREIGN KEY (idproduct) REFERENCES product(idproduct) ON DELETE CASCADE ON UPDATE NO ACTION, CONSTRAINT fk_category FOREIGN KEY (idcategory) REFERENCES category(idcategory) ON DELETE NO ACTION ON UPDATE NO ACTION)""")
            
            # ZERAR TABELAS - TESTE!
            #c.execute("DELETE FROM CATEGORY")
            #c.execute("DELETE FROM PRODUCT")
            #c.execute("DELETE FROM CATEGORY")

        except Exception as err:
            print('Create Database Error.\nError: %s' % (str(err)))
        finally:
            print('Database loaded.')
            conn.commit()
            conn.close()

# CATEGORIAS!
    def createCategory(self, category):
        try:
            conn = sqlite3.connect('product.db')
            c = conn.cursor()
            query = "INSERT INTO CATEGORY (NAME) VALUES (:c_name)"
            c.execute(query,
                {
                    'c_name': category.name
                }
            )
            conn.commit()
        except Exception as err:
            print('Query Failed: %s\nError: %s' % (query, str(err)))
        finally:
            conn.close()

    def selectCategory(self, category):
        records = []
        try:
            conn = sqlite3.connect('product.db')
            c = conn.cursor()
            query = "SELECT * FROM CATEGORY"
            c.execute(query)
            records = c.fetchall()
        except Exception as err:
            print('Query Failed: %s\nError: %s' % (query, str(err)))
        finally:
            conn.close()

        return records

    def updateCategory(self, category):
        try:
            conn = sqlite3.connect('product.db')
            c = conn.cursor()
            query = "UPDATE CATEGORY SET NAME = :c_name WHERE ID = :c_id"
            c.execute(query, 
                {
                    'c_id': category.id,
                    'c_name': category.name
                }
            )
            conn.commit()
        except Exception as err:
            print('Query Failed: %s\nError: %s' % (query, str(err)))
        finally:
            conn.close()

    def deleteCategory(self, category):
        try:
            conn = sqlite3.connect('product.db')
            c = conn.cursor()
            query = "DELETE FROM CATEGORY WHERE ID = :c_id"
            c.execute(query, 
                {
                    'p_id': category.id
                }
            )
            conn.commit()
        except Exception as err:
            print('Query Failed: %s\nError: %s' % (query, str(err)))
        finally:
            conn.close()

# PRODUTOS
    def selectProduct(self, product):
        records = []
        try:
            conn = sqlite3.connect('product.db')
            c = conn.cursor()
            all_query = "SELECT * FROM PRODUCT"
            one_query = "SELECT * FROM PRODUCT WHERE IDPRODUCT = :p_id"

            if product != '':
                if product.id != '':
                    c.execute(one_query, 
                        {
                            'p_id': product.id
                        }
                    )
                else:
                    print('Blank product ID.')
                    return []
            else:
                c.execute(all_query)
            
            records = c.fetchall()
        except Exception as err:
            print('Query Failed: %s\nError: %s' % (all_query, str(err)))
        finally:
            conn.close()
        
        return records

    def createProduct(self, product):
        conn = sqlite3.connect('product.db')
        c = conn.cursor()
        query = "SELECT * FROM CATEGORY"
        c.execute(query)
        all_category = c.fetchall()
        if len(all_category) == 0:
            print('No categories were created')
        else:
            try:
                conn = sqlite3.connect('product.db')
                c = conn.cursor()
                p_query = "INSERT INTO PRODUCT (NAME, DESCRIPTION, price) VALUES (:p_name, :p_description, :p_price)"
                pc_query = "INSERT INTO PRODUCTCATEGORY (IDPRODUCT, IDCATEGORY) VALUES (:pc_idproduct, :pc_idcategory)"
                c.execute(p_query,
                    {
                        'p_name': product.name,
                        'p_description': product.description,
                        'p_price': product.price
                    }
                )
                product_id = c.lastrowid
                try:
                    for category in product.categories:
                        c.execute(pc_query,
                            {
                                'pc_idproduct': product_id,
                                'pc_idcategory': category
                            }
                        )
                except Exception as err:
                    print('Query Failed: %s\nError: %s' % (pc_query, str(err)))
                finally:
                    conn.commit()
            except Exception as err:
                print('Query Failed: %s\nError: %s' % (p_query, str(err)))
            finally:
                conn.close()

    def updateProduct(self, product):
        try:
            conn = sqlite3.connect('product.db')
            c = conn.cursor()
            query = "UPDATE PRODUCT SET NAME = :p_name, description = :p_description, price = :p_price WHERE ID = :p_id"
            c.execute(query, 
                {
                    'p_name': product.name,
                    'p_description': product.description,
                    'p_price': product.price,
                    'p_id': product.id
                }
            )
            conn.commit()
        except Exception as err:
            print('Query Failed: %s\nError: %s' % (query, str(err)))
        finally:
            conn.close()

    def deleteProduct(self, product):
        try:
            conn = sqlite3.connect('product.db')
            c = conn.cursor()
            query = "DELETE FROM PRODUCT WHERE ID = :p_id"
            c.execute(query, 
                {
                    'p_id': product.id
                }
            )
            conn.commit()
        except Exception as err:
            print('Query Failed: %s\nError: %s' % (query, str(err)))
        finally:
            conn.close()

    def selectProdCategory(self, category):

        records = []
        try:
            conn = sqlite3.connect('product.db')
            c = conn.cursor()
            query = "SELECT * FROM PRODUCTCATEGORY"
            c.execute(query)
            records = c.fetchall()

            # CRIAR FOR PARA BUCAR APENAS OS PRODUTOS FILTRADOS

        except Exception as err:
            print('Query Failed: %s\nError: %s' % (query, str(err)))
        finally:
            conn.close()

        return records

class services():
    def importCategoryCSV(self):
        filename = ''
        #filename = filedialog.askopenfilename(initialdir="c:/", title="Select a file", filetype=(("Python files", "*.csv"), ("All files", "*.*")))
        try:
            filename = easygui.fileopenbox()

            with open(filename, newline='\n', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                
                for row in reader:
                    print(row)
        except Exception as err:
            print('Load CSV Failed.\nError: %s' % (str(err)))

class main():

    db = database()
    s = services()

    p1 = product('1', 'MESA', 'QUADRADA', 150, [1,2])
    c1 = category('', 'MÓVEIS')

    db.createCategory(c1)
    db.createProduct(p1)
    
    print (db.selectProdCategory(''))
    print(db.selectProduct(''))
    print(db.selectCategory(''))

    #s.importCategoryCSV()
   


#    def __init__(self):
#        conn = sqlite3.connect('product.db')
#        c = conn.cursor()

#        category_max = c.execute("SELECT MAX(IDCATEGORY) + 1 FROM CATEGORY")
#        product_max = c.execute("SELECT MAX(IDPRODUCT) + 1 FROM PRODUCT")

#        conn.close()