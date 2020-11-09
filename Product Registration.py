import sqlite3
import csv
import easygui #OPEN ARCHIVE
import sys
import os 
from mainWindow import *
from newProductWindow import *
from categoriesFound import *

class category():
    def __init__(self, id, name):
        self.id = id
        self.name = name

class product():
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
            print(os.getcwd())
            c = conn.cursor()
            c.execute("PRAGMA foreign_keys= 1")
            c.execute("PRAGMA table_info(PRODUCTCATEGORY)")

            # DELETE TABLES - TEST!
            #c.execute("DROP TABLE PRODUCTCATEGORY")
            #c.execute("DROP TABLE PRODUCT")
            #c.execute("DROP TABLE CATEGORY")

            # CREATE TABLE IF NOT EXISTS
            c.execute("""CREATE TABLE IF NOT EXISTS CATEGORY 
                (idcategory INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL UNIQUE)""")
            c.execute("""CREATE TABLE IF NOT EXISTS PRODUCT 
                (idproduct INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, description TEXT, price INTEGER)""")
            c.execute("""CREATE TABLE IF NOT EXISTS PRODUCTCATEGORY 
                (idproduct INTEGER NOT NULL, idcategory INTEGER NOT NULL, CONSTRAINT fk_product FOREIGN KEY (idproduct) REFERENCES product(idproduct) ON DELETE CASCADE ON UPDATE NO ACTION, CONSTRAINT fk_category FOREIGN KEY (idcategory) REFERENCES category(idcategory) ON DELETE NO ACTION ON UPDATE NO ACTION)""")
            
            # DELETE ROWS FROM ALL TABLES
            #c.execute("DELETE FROM PRODUCTCATEGORY")
            #c.execute("DELETE FROM PRODUCT")
            #c.execute("DELETE FROM CATEGORY")

        except Exception as err:
            print('Create Database Error.\nError: %s' % (str(err)))
        finally:
            conn.commit()
            conn.close()

# CATEGORIES!
    def createCategory(self, category):
        try:
            conn = sqlite3.connect('product.db')
            c = conn.cursor()
            query = "INSERT INTO CATEGORY (NAME) VALUES (:c_name)"
            category_exists = self.selectCategory(category.name, 1)
            if category_exists == []:    
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
        try:
            categories = []
            conn = sqlite3.connect('product.db')
            c = conn.cursor()

            # NAME
            if searchType == 1:
                query = "SELECT * FROM CATEGORY WHERE NAME = :c_search"
                c.execute(query, 
                    {
                        'c_search': search
                    }
                )
            # ID
            if searchType == 2:
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

    # PRODUCTS
    def selectProduct(self, search, searchType):
        try:
            products = []
            conn = sqlite3.connect('product.db')
            c = conn.cursor()
            if searchType == 2:
                query = """SELECT PRODUCT.* FROM PRODUCT"""
                c.execute(query)
            if searchType == 1:
                query = """SELECT PRODUCT.* FROM PRODUCT 
                                LEFT JOIN PRODUCTCATEGORY ON PRODUCTCATEGORY.IDPRODUCT = PRODUCT.IDPRODUCT 
                                LEFT JOIN CATEGORY ON PRODUCTCATEGORY.IDCATEGORY = CATEGORY.IDCATEGORY 
                                WHERE (PRODUCT.NAME LIKE :p_name OR :p_name = '')
                                    AND (PRODUCT.DESCRIPTION LIKE :p_description OR :p_description = '')
                                    AND (PRODUCT.PRICE LIKE :p_price OR :p_price = '')
                                    AND (CATEGORY.NAME LIKE :p_category OR :p_category = '')
                        """
                c.execute(query, 
                    {
                        'p_name': search[0],
                        'p_description': search[1],
                        'p_price': search[2],
                        'p_category': search[3]
                    }
                )
            if searchType == 0:
                query = "SELECT * FROM PRODUCT WHERE IDPRODUCT = :p_id"
                c.execute(query, 
                        {
                            'p_id': search
                        }
                    )
            
            records = c.fetchall()
            for i in records:
                query = """SELECT PRODUCTCATEGORY.IDCATEGORY 
                                FROM PRODUCTCATEGORY 
                                INNER JOIN CATEGORY ON PRODUCTCATEGORY.IDCATEGORY = CATEGORY.IDCATEGORY 
                            WHERE PRODUCTCATEGORY.IDPRODUCT = :p_id
                        """
                c.execute(query, 
                    {
                        'p_id': i[0]
                    }
                )
                records_pd = c.fetchall()
                productcategory = []
                if records_pd != []:
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
            conn.commit()
        except Exception as err:
            print('Query Failed: %s\nError: %s' % (pc_query, str(err)))
        finally:
            
            conn.close()

    def updateProduct(self, product):
        try:
            conn = sqlite3.connect('product.db')
            c = conn.cursor()
            # CHANGE PRODUCT
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

            # INSERT NEW CATEGORIES
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

            
class services:
    def readCategoryCSV(self):
        categories = []
        filename = ''
        filename = easygui.fileopenbox(msg='Open CSV File', title='Import categories', default='*.csv', filetypes=["*.csv"], multiple=False)

        if filename is not None:
            with open(filename, newline='\n', encoding='utf-8') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                reader = csv.reader(csvfile)
                for row in reader:
                    c = category('', row[0])
                    categories.append(c)
        else:
            categories = ''
        return categories
       

def main(ui):
    db = database()
    s = services()

    # MAIN WINDOW
    def updateProduct():
        if ui.tableWidget_products.selectionModel().hasSelection():
            p = db.selectProduct(ui.tableWidget_products.item(ui.tableWidget_products.selectionModel().currentIndex().row(), 0).text(), 0)[0]
            createEditProduct(p)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setWindowTitle('Product blank')
            msg.setText('No product selected.')
            msg.setStandardButtons(QMessageBox.Ok)
            option = msg.exec_()
    
    def deleteProduct():
        if ui.tableWidget_products.selectionModel().hasSelection():
            p = db.selectProduct(ui.tableWidget_products.item(ui.tableWidget_products.selectionModel().currentIndex().row(), 0).text(), 0)[0]
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Question)
            msg.setWindowTitle('Delete Product')
            msg.setText('Really want to delete this product?\nID: {}\nName: {}'.format(p.id, p.name))
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            option = msg.exec_()
            if option == QMessageBox.Yes:
                if ui.tableWidget_products.selectionModel().hasSelection():
                    p = db.deleteProduct(p)
                    ui.tableWidget_products.setRowCount(0)
                    searchProduct()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setWindowTitle('Product blank')
            msg.setText('No product selected.')
            msg.setStandardButtons(QMessageBox.Ok)
            option = msg.exec_()


    def searchProduct():
        products = db.selectProduct([ui.lineEdit_Name.text(), ui.lineEdit_Description.text(), ui.lineEdit_Price.text(), ui.lineEdit_Category.text()], 1)
        if products != []:
            ui.tableWidget_products.setRowCount(len(products))
            i = 0
            items = []
            for product in products:
                item = QTableWidgetItem()
                item.setFlags(Qt.ItemFlags(1))
                item.setText(str(product.id))
                items.append(item)
                ui.tableWidget_products.setItem(i, 0, items[-1])
                item1 = QTableWidgetItem()
                item1.setText(product.name)
                items.append(item1)
                ui.tableWidget_products.setItem(i, 1, items[-1])
                item2 = QTableWidgetItem()
                item2.setText(product.description)
                items.append(item2)
                ui.tableWidget_products.setItem(i, 2, items[-1])
                item3 = QTableWidgetItem()
                item3.setText("{:.2f}".format(float(product.price)))
                items.append(item3)
                ui.tableWidget_products.setItem(i, 3, items[-1])
                # CATEGORIES
                categories = ''
                for cat in product.categories:
                    if product.categories[-1] == cat:
                        categories = categories + db.selectCategory(cat, 2)[0].name
                    else:
                        categories = categories + db.selectCategory(cat, 2)[0].name + '; '
                item4 = QTableWidgetItem()
                item4.setText(categories)
                items.append(item4)
                ui.tableWidget_products.setItem(i, 4, items[-1])
                i+=1    
        else:
            if db.selectProduct(['', '', '', ''], 1) != []:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Information)
                msg.setWindowTitle('No Product')
                msg.setText('No products registered with these filters.')
                msg.setStandardButtons(QMessageBox.Ok)
                option = msg.exec_()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Information)
                msg.setWindowTitle('No Product')
                msg.setText('No products registered.')
                msg.setStandardButtons(QMessageBox.Ok)
                option = msg.exec_()


    # NEW CATEGORIES FUNCTIONS
    def importCatetoriesWindow():
        ui_c.listWidget_CategoriesFound.clear()
        categories = s.readCategoryCSV()
        if categories != [] and categories != '':
            for category in categories:
                ui_c.listWidget_CategoriesFound.addItem(category.name)
            newCategoriesWindow.show()
            mainWindow.close()
        elif categories == '':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setWindowTitle('No file selected')
            msg.setText('No file selected, try again.')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setWindowTitle('Blank file')
            msg.setText('No categories found in the file.')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        
    def closeCategoriesFound():
        newCategoriesWindow.close()
        mainWindow.show()
    
    def removeCategoriesFound():
        itens = ui_c.listWidget_CategoriesFound.selectedItems()
        for item in itens:
            ui_c.listWidget_CategoriesFound.takeItem(ui_c.listWidget_CategoriesFound.row(item))

    def saveCategoriesFound():
        if ui_c.listWidget_CategoriesFound.count() > 0:
            for i in range(0, ui_c.listWidget_CategoriesFound.count()):
                c = category('', ui_c.listWidget_CategoriesFound.item(i).text())
                db.createCategory(c)
                newCategoriesWindow.close()
                mainWindow.show()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setWindowTitle('Blank categories')
            msg.setText('No categories found.')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            newCategoriesWindow.close()
            mainWindow.show()


    # NEW PRODUCT FUNCTIONS
    def createEditProduct(product):
        if product is not False:
            ui_p.label_NewID.setText(str(product.id))
            ui_p.lineEdit_Name.setText(product.name)
            ui_p.lineEdit_Description.setText(product.description)
            ui_p.lineEdit_Price.setText(str(product.price))
            ui_p.listWidget_CategoriesAdded.clear()
            if product.categories is not None:
                for category in product.categories:
                    c = db.selectCategory(category, 2)[0]
                    ui_p.listWidget_CategoriesAdded.addItem(c.name)
        else:
            ui_p.label_NewID.setText('(New)')
            ui_p.lineEdit_Name.setText('')
            ui_p.lineEdit_Description.setText('')
            ui_p.lineEdit_Price.setText('')
            ui_p.listWidget_CategoriesAdded.clear()
        categories = db.selectCategory('',0)
        ui_p.comboBox_CategoriesList.clear()
        for category in categories:
            ui_p.comboBox_CategoriesList.addItem(category.name)
        newProductWindow.show()
        mainWindow.close()

    def newProductWindowAddCategory():
        if (ui_p.comboBox_CategoriesList.currentText() != ''):
            itens = ui_p.listWidget_CategoriesAdded.findItems(ui_p.comboBox_CategoriesList.currentText(), Qt.MatchExactly)
            if len(itens) == 0:
                ui_p.listWidget_CategoriesAdded.addItem(ui_p.comboBox_CategoriesList.currentText())
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setWindowTitle('Categories blank')
            msg.setText('No categories registered.')
            msg.setStandardButtons(QMessageBox.Ok)
            option = msg.exec_()

    def newProductWindowRemoveCategory():
        itens = ui_p.listWidget_CategoriesAdded.selectedItems()
        for item in itens:
            ui_p.listWidget_CategoriesAdded.takeItem(ui_p.listWidget_CategoriesAdded.row(item))
        
    def newProductWindowSaveProduct():
        if ui_p.lineEdit_Name.text() or ui_p.lineEdit_Description.text() or ui_p.lineEdit_Price.text() != '':
            price_digit = False
            for i in ui_p.lineEdit_Price.text():
                if (i != '.'):
                    if i.isdigit() == False:
                        price_digit = True
                        break
            if price_digit is False:
                if ui_p.listWidget_CategoriesAdded.count() > 0:
                    option = ''
                    categories = []
                    for i in range (ui_p.listWidget_CategoriesAdded.count()):
                        categories.append(db.selectCategory(ui_p.listWidget_CategoriesAdded.item(i).text(), 1)[0].id)
                    if ui_p.label_NewID.text() == '(New)':
                        p = product('', ui_p.lineEdit_Name.text(), ui_p.lineEdit_Description.text(), float(ui_p.lineEdit_Price.text()), categories)
                        db.createProduct(p)
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Icon.Question)
                        msg.setWindowTitle('New Product')
                        msg.setText('Want to create another product?')
                        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                        option = msg.exec_()
                    else:
                        p = product(ui_p.label_NewID.text(), ui_p.lineEdit_Name.text(), ui_p.lineEdit_Description.text(), ui_p.lineEdit_Price.text(), categories)
                        db.updateProduct(p)
                    if option == QMessageBox.Yes:
                        createEditProduct(False)
                    else:
                        newProductWindow.close()
                        mainWindow.show()
                        searchProduct()
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Icon.Information)
                    msg.setWindowTitle('Blank categories')
                    msg.setText('Please enter at least one category.')
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()       
            else: 
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Information)
                msg.setWindowTitle('Wrong field')
                msg.setText('Price must be a number.')
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setWindowTitle('Blank field')
            msg.setText('Some field is blank, please fill then in before saving.')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def newProductWindowClose():
        newProductWindow.close()
        mainWindow.show()

    def exitAll():
        mainWindow.close()

    # MAIN WINDOW
    ui.pushButton_CreateProduct.clicked.connect(createEditProduct)
    ui.pushButton_Search.clicked.connect(searchProduct)
    ui.pushButton_ImportCategories.clicked.connect(importCatetoriesWindow)
    ui.pushButton_UpdateProduct.clicked.connect(updateProduct)
    ui.pushButton_RemoveProduct.clicked.connect(deleteProduct)
    ui.pushButton_Exit.clicked.connect(exitAll)
    ui.tableWidget_products.setSelectionMode(QAbstractItemView.SingleSelection)


    # NEW CATEGORIES WINDOW
    newCategoriesWindow = QDialog()
    ui_c = Ui_Form_CategoriesFound()
    ui_c.setupUi(newCategoriesWindow)
    ui_c.pushButton_CloseCategoriesFound.clicked.connect(closeCategoriesFound)
    ui_c.pushButton_RemoveCategory.clicked.connect(removeCategoriesFound)
    ui_c.pushButton_SaveCategoriesFound.clicked.connect(saveCategoriesFound)


    # NEW PRODUCT WINDOW
    newProductWindow = QDialog()
    ui_p = Ui_Form_NewProduct()
    ui_p.setupUi(newProductWindow)
    ui_p.pushButton_AddCategory.clicked.connect(newProductWindowAddCategory)
    ui_p.pushButton_RemoveCategory.clicked.connect(newProductWindowRemoveCategory)
    ui_p.pushButton_SaveProduct.clicked.connect(newProductWindowSaveProduct)
    ui_p.pushButton_CloseProduct.clicked.connect(newProductWindowClose)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()

    ui.setupUi(mainWindow)

    mainWindow.show()
    main(ui)
    sys.exit(app.exec_())