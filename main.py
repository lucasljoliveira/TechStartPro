import sqlite3
import csv
import easygui #abrir arquivo


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
            #print(c.fetchall())
            # EXCLUIR TABELAS - TESTE!
            #c.execute("DROP TABLE PRODUCTCATEGORY")
            #c.execute("DROP TABLE PRODUCT")
            #c.execute("DROP TABLE CATEGORY")

            # Criar tabelas / verificar se já existem
            c.execute("""CREATE TABLE IF NOT EXISTS CATEGORY 
                (idcategory INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL UNIQUE)""")
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

    def selectCategory(self, search, searchType):
        categories = []
        try:
            conn = sqlite3.connect('product.db')
            c = conn.cursor()
            # ID
            if searchType == 1:
                query = "SELECT * FROM CATEGORY WHERE IDCATEGORY = :c_search"
                c.execute(query, 
                    {
                        'c_search': search
                    }
                )
            # ALL
            elif searchType == 0:
                query = "SELECT * FROM CATEGORY"
                c.execute(query)

            records = c.fetchall()

            for i in records:
                c1 = category(i[0], i[1])
                categories.append(c1)
            
        except Exception as err:
            print('Query Failed: %s\nError: %s' % (query, str(err)))
        finally:
            conn.close()

        return categories

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
            query = "DELETE FROM CATEGORY WHERE ID = :c_id AND NOT EXISTS (SELECT NULL FROM PRODUCTCATEGORY WHERE PRODUCTCATEGORY.IDCATEGORY = CATEGORY.IDCATEGORY)"
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
    def selectProduct(self, search, searchType):
        products = []
        try:
            conn = sqlite3.connect('product.db')
            c = conn.cursor()
            if   searchType == 1:
                query = "SELECT * FROM PRODUCT WHERE NAME LIKE '%' || :p_stype || '%'"
            elif searchType == 2:
                query = "SELECT * FROM PRODUCT WHERE DESCRIPTION LIKE '%' || :p_stype || '%'"
            elif searchType == 3:
                query = "SELECT * FROM PRODUCT WHERE PRICE = :p_stype"
            elif searchType == 4:
                query = "SELECT PRODUCT.* FROM PRODUCTCATEGORY INNER JOIN PRODUCT ON PRODUCTCATEGORY.IDPRODUCT = PRODUCT.IDPRODUCT WHERE PRODUCTCATEGORY.IDCATEGORY = :p_stype"
            if   searchType == 5:
                query = "SELECT * FROM PRODUCT WHERE IDPRODUCT = :p_stype"
            elif searchType == 0:
                query = "SELECT * FROM PRODUCT"
            
            c.execute(query, 
                    {
                        'p_stype': search
                    }
                )
            
            records = c.fetchall()


            for i in records:
                query = "SELECT PRODUCTCATEGORY.IDCATEGORY FROM PRODUCTCATEGORY INNER JOIN CATEGORY ON PRODUCTCATEGORY.IDCATEGORY = CATEGORY.IDCATEGORY WHERE PRODUCTCATEGORY.IDPRODUCT = :p_id"
                c.execute(query, 
                    {
                        'p_id': i[0]
                    }
                )
                records_pd = c.fetchall()

                if records_pd != []:
                    productcategory = []
                    for pd in records_pd:
                        productcategory.append(pd[0])
                
                p1 = product(i[0], i[1], i[2], i[3], productcategory)
                products.append(p1)

        except Exception as err:
            print('Query Failed: %s\nError: %s' % (query, str(err)))
        finally:
            conn.close()

        return products

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
            # ALTERANDO PRODUTO
            query = "UPDATE PRODUCT SET NAME = :p_name, description = :p_description, price = :p_price WHERE IDPRODUCT = :p_id"
            c.execute(query, 
                {
                    'p_name': product.name,
                    'p_description': product.description,
                    'p_price': product.price,
                    'p_id': product.id
                }
            )
            # DELETE PRODUCT CATEGORIES
            query_c = "DELETE FROM PRODUCTCATEGORY WHERE IDPRODUCT = :p_id"
            c.execute(query_c, 
                {
                    'p_id': product.id
                }
            )
            # INSER NEW CATEGORIES
            pc_query = "INSERT INTO PRODUCTCATEGORY (IDPRODUCT, IDCATEGORY) VALUES (:pc_idproduct, :pc_idcategory)"
            for category in product.categories:
                c.execute(pc_query,
                    {
                        'pc_idproduct': product.id,
                        'pc_idcategory': category
                    }
                )

            conn.commit()
        except Exception as err:
            print('Query Update Product Failed. Error: %s' % (str(err)))
        finally:
            conn.close()

    def deleteProduct(self, product):
        try:
            conn = sqlite3.connect('product.db')
            c = conn.cursor()
            query = "DELETE FROM PRODUCT WHERE IDPRODUCT = :p_id"
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

    def selectProdCategory(self, product):

        productcategory = []
        try:
            conn = sqlite3.connect('product.db')
            c = conn.cursor()
            query = query = "SELECT PRODUCT.* FROM PRODUCTCATEGORY INNER JOIN CATEGORY ON PRODUCTCATEGORY.IDCATEGORY = CATEGORY.IDCATEGORY WHERE PRODUCTCATEGORY.IDPRODUCT = :p_id"
            c.execute(query, 
                {
                    'p_id': product.id
                }
            )
            records = c.fetchall()


            for i in records:
                productcategory.append(i[0])

        except Exception as err:
            print('Query Failed: %s\nError: %s' % (query, str(err)))
        finally:
            conn.close()

        return productcategory

    def updateProdCategory(self, product, category_old, category_new):
        try:
            conn = sqlite3.connect('product.db')
            c = conn.cursor()
            query = "UPDATE PRODUCTCATEGORY SET IDCATEGORY = :newc_id WHERE IDPRODUCT = :p_id AND IDCATEGORY = :oldc_id"
            c.execute(query, 
                {
                    'p_id': product.idcategory,
                    'oldc_id': category_old.idcategory,
                    'newc_id': category_new.idcategory
                }
            )
            conn.commit()
        except Exception as err:
            print('Query Failed: %s\nError: %s' % (query, str(err)))
        finally:
            conn.close()

            
class services:
    def readCategoryCSV(self):
        categories = []
        #filename = filedialog.askopenfilename(initialdir="c:/", title="Select a file", filetype=(("CSV files", "*.csv"), ("All files", "*.*")))
        try:
            filename = easygui.fileopenbox(msg='Open CSV File', title='Import categories', default='*.csv', filetypes=["*.csv"], multiple=False)
            print(filename)
            with open(filename, newline='\n', encoding='utf-8') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                reader = csv.reader(csvfile)
                for row in reader:
                    c = category('', row[0])
                    categories.append(c)

        except Exception as err:
            print('Load CSV Failed.\nError: %s' % (str(err)))
        
        return categories
       

class main:
    db = database()
    s = services()

    while (True):
        app = 
        print('1. Create category\n2. Show categories\n3. Create Product\n4. Show Product\n5. Update Product\n6. Delete Product\n0. Exit')
        option = int(input('Insert a option: '))

        # CREATE CATEGORY
        if option == 1:
            print('1. Manually\n2. Import CSV')
            option = int(input('Insert a option: '))
            if option == 1:
                category = category('', input('Insert a name: '))
                db.createCategory(category)
            elif option == 2:
                categories = s.readCategoryCSV()
                if categories != []:
                    print('Categories found:')
                    for category in categories:
                        print('  ' + category.name)
                    if input('Create these categories? (YES/NO): ').upper() == 'YES':
                        for category in categories:
                            db.createCategory(category)
                        print('*** Categories successfully created. ***')
                    else:
                        print('*** Categories creation cancelled. ***')
                else:
                    print('*** No categories found. ***')
        # READ CATEGORY
        elif option == 2:
            categories = db.selectCategory('', 0)
            print('Categories')
            if categories == []:
                print('*** No categories were inserted. ***')
            else:
                for i in categories:
                    print('    ' + str(i.id) + '. ' + i.name)
        # CREATE
        elif option == 3:
            p = product('', input('Insert a name: '), input('Insert a description: '), float(input('Insert a price: ')), [])
            chooseCategory = True
            c = []
            while chooseCategory:
                print('Categories')
                categories = db.selectCategory('', 0)
                for i in categories:
                    print('    ' + str(i.id) + '. ' + i.name)
                c.append(int(input('Insert a category ID: ')))
                if input('Add another category? (YES/NO): ') == 'NO':
                    chooseCategory = False

            p.categories = c
            db.createProduct(p)
        # READ PRODUCT
        elif option == 4:
            print('Search by\n    1. Name\n    2. Description\n    3. Price\n    4. Category\n    0. Show all')
            option = int(input('Insert a option: '))
            # NAME
            if option == 1:
                products = db.selectProduct(input('Insert a name: '), 1)
                for i in products:
                    print('    ' + str(i.id) + '. ' + i.name + ' (' + i.description + ') R$ ' + str(i.price))
            #DESCRIPTION
            if option == 2:
                products = db.selectProduct(input('Insert a description: '), 2)
                for i in products:
                    print('    ' + str(i.id) + '. ' + i.name + ' (' + i.description + ') R$ ' + str(i.price))
            #PRICE
            if option == 3:
                products = db.selectProduct(float(input('Insert a price: ')), 3)
                for i in products:
                    print('    ' + str(i.id) + '. ' + i.name + ' (' + i.description + ') R$ ' + str(i.price))
            #CATEGORIES
            if option == 4:
                print('Categories')
                categories = db.selectCategory('', 0)
                for i in categories:
                    print('    ' + str(i.id) + '. ' + i.name)
                products = db.selectProduct(int(input('Insert a category ID: ')), 4)
                for i in products:
                    print('    ' + str(i.id) + '. ' + i.name + ' (' + i.description + ') R$ ' + str(i.price))
            #ALL
            if option == 0:
                products = db.selectProduct('', 0)
                for i in products:
                    print('    ' + str(i.id) + '. ' + i.name + ' (' + i.description + ') R$ ' + str(i.price))
        # UPDATE
        elif option == 5:
            #PRODUCT
            products = db.selectProduct('', 0)
            for i in products:
                print('    ' + str(i.id) + '. ' + i.name + ' (' + i.description + ') R$ ' + str(i.price))
            try:
                option = int(input('  Insert a product ID: '))
            except Exception as err:
                print('*** Interger values only. Error: %s ***' % (str(err)))
            product = db.selectProduct(option, 5)
            if product != []:
                product = product[0]
                if input('  Change name? (YES/NO): ').upper() == 'YES':
                    while(True):
                        aux = input('    Insert a new name(' + product.name + '): ')
                        if aux != '':
                            product.name = aux
                            break
                if input('  Change description? (YES/NO): ').upper() == 'YES':
                    while(True):
                        aux = input('    Insert a new description(' + product.description + '): ')
                        if aux != '':
                            product.description = aux
                            break
                if input('  Change price? (YES/NO): ').upper() == 'YES':
                    while(True):
                        try:
                            aux = float(input(    'Insert a new price(' + str(product.price) + '): '))
                            if aux >= 0:
                                product.price = float(aux)
                                break
                            else:
                                print('*** Negative values are not accepted. ***')
                        except Exception as err:
                            print('*** Text are not accepted. Error: %s ***' % (str(err)))

                #UPDATE CATEGORIES
                while(True):
                    print('    1. Change category\n    2. Create category\n    3. Delete Category\n    0. Save changes')
                    try:
                        option = int(input('Insert a option: '))
                    except Exception as err:
                        print('*** Interger values only. Error: %s ***' % (str(err)))
                    print('Available categories')
                    c = []
                    for i in product.categories:
                        cat = db.selectCategory(i, 1) 
                        cat = cat[0]
                        c.append(cat)
                        print('    ' + str(cat.id) + '. ' + cat.name)
                
                    # CHANGE PRODUCT CATEGORY
                    if option == 1:
                        while(True):
                            try:
                                old_c = int(input('Insert a category ID: '))
                                break
                            except Exception as err:
                                print('*** Interger values only. Error: %s ***' % (str(err)))
                    
                        print('New available categories')
                        categories = db.selectCategory('', 0)
                        for i in categories:
                            print('    ' + str(i.id) + '. ' + i.name)
                        try:
                            new_c = int(input('Insert a category ID: '))
                        except Exception as err:
                            print('*** Interger values only. Error: %s ***' % (str(err)))
                        if new_c in product.categories:
                            print('*** Category already exists. ***')
                        else:
                            if db.selectCategory(new_c, 1) != []:
                                product.categories.remove(old_c)
                                product.categories.append(new_c)     
                            else:
                                print('*** Category not exists. ***')

                    # CREATE PRODUCT CATEGORY
                    if option == 2:
                        print('Categories')
                        categories = db.selectCategory('', 0)
                        for i in categories:
                            print('    ' + str(i.id) + '. ' + i.name)
                        try:
                            new_c = int(input('Insert a category ID: '))
                        except Exception as err:
                            print('*** Interger values only. Error: %s ***' % (str(err)))
                        if new_c in product.categories:
                            print('*** Category already exists. ***')
                        else:
                            if db.selectCategory(new_c, 1) != []:
                                product.categories.append(new_c)  
                            else:
                                print('*** Category not exists. ***')

                    # DELETE PRODUCT CATEGORY
                    if option == 3:
                        try:
                            old_c = int(input('Insert a category ID: '))
                        except Exception as err:
                            print('*** Interger values only. Error: %s ***' % (str(err)))
                        if old_c in product.categories:
                            product.categories.remove(old_c) 
                        else:
                            print('*** Category not exists. ***')

                    if option == 0:
                        db.updateProduct(product)
                        break

        # DELETE PRODUCT
        elif option == 6:
            products = db.selectProduct('', 0)
            for i in products:
                print('    ' + str(i.id) + '. ' + i.name + ' (' + i.description + ') R$ ' + str(i.price))
            try:
                p = int(input('Insert a product ID: '))
            except Exception as err:
                print('*** Interger values only. Error: %s ***' % (str(err)))

            product = db.selectProduct(p, 5)

            if product != []:
                product = product[0]
                db.deleteProduct(product)
            else:
                print('*** Product not exists. ***')
        elif option == 0:
            break



    #p1 = product(1, 'MESA', 'QUADRADA', 150, [1,2])
    #c1 = category('', 'MÓVEIS')

    #db.createCategory(c1)
    #db.createProduct(p1)
    
    #print (db.selectProdCategory(''))
    #print(db.selectProduct(''))
    #print(db.selectCategory(''))

    #csvData = s.readCategoryCSV()
   
