# N-1
# class Book:
#     def __init__(self, id, title, year, price):
#         self.id=int(id)
#         self.title=title
#         self.year=year
#         self.price=price
#     def __str__(self):
#         return f'''
#     Title: {self.title}
#     Year: {self.title}
#     Year: {self.year}
#     Price: {self.price}'''

# class BookManager:
#     def __init__(self):
#         self.next_id=1
#         self.books=[]
#     def create(self, title, year, price):
#         b=Book(self.next_id,title,year,price)
#         self.books.append(b)
#         self.next_id+=1
#     def show_all(self):
#         for i in self.books:
#             print(i)
#     def get_by_id(self, id):
#         for i in self.books:
#             if i.id==id:
#                 print(i)
#     def update(self,id, new_title,new_year,new_price):
#         for i in self.books:
#             if i.id==id:
#                 i.title=new_title
#                 i.price=new_price
#                 i.year=new_year
#     def delete(self, id):
#         for i in self.books:
#             if i.id==id:
#                 self.books.remove(i)

# bm=BookManager()
# while True:
#     print (f'''
#     1.create book
#     2.show all books
#     3.get book by id
#     4.update by id1
#     5.delete book
#     6. exit''')

#     n=int(input('Enter a number: '))

#     if n==1:
#         title=input('Enter a book title: ')
#         year=input('Enter a book year: ')
#         price=input('Enter a book price: ')
#         bm.create(title,year,price)
#     if n==2:
#         bm.show_all()
#     if n==3:
#         num=int(input('Enter book id: '))
#         bm.get_by_id(num)
#     if n==4:
#         num=int(input('Enter book id: '))
#         new_title=input('Enter new title: ')
#         new_year=input('Enter new year: ')
#         new_price=input('Enter new price: ')
#         bm.update(num)
#     if n==5:
#         num=int(input('Enter book id: '))
#         bm.delete(num)
#     if n==6:
#         break





# N-2
# class Author:
#     def __init__(self, id, full_name, birth_year, country):
#         self.id=int(id)
#         self.full_name=full_name
#         self.birth_year=birth_year
#         self.country=country
#     def __str__(self):
#         return f'''
#     id: {self.id}
#     full_name: {self.full_name}
#     birth_year: {self.birth_year}
#     country: {self.country}'''
# class AuthorManager:
#     def __init__(self):
#         self.next_id=1
#         self.authors=[]
#     def create(self, full_name, birth_year, country):
#         a=Author(self.next_id,full_name, birth_year,country)
#         self.authors.append(a)
#         self.next_id+=1
#     def show_all(self):
#         for i in self.authors:
#             print(i)
#     def get_by_id(self, id):
#         for i in self.authors:
#             if i.id==id:
#                 print(i)
#     def update(self,id, new_name,new_year,new_country):
#         for i in self.authors:
#             if i.id==id:
#                 i.full_name=new_name
#                 i.birth_year=new_year
#                 i.country=new_country
#     def delete(self, id):
#         for i in self.authors:
#             if i.id==id:
#                 self.authors.remove(i)
# am=AuthorManager()

# while True:
#     print(f'''
#     1. Create an author
#     2. Show all authors
#     3. Get author by id
#     4. Change author by id
#     5. Delete
#     6. Exit''')

#     n=int(input('Enter your choice: '))
#     if n==1:
#         full_name=input('Enter an author: ')
#         birth_year=input('Enter an authors birth year: ')
#         country=input('Enter an authors mother-land: ')
#         am.create(full_name,birth_year,country)
#     if n==2:
#         am.show_all()
#     if n==3:
#         num=int(input('Enter an id: '))
#         am.get_by_id(num)
#     if n==4:
#         num=int(input('Enter an id: '))
#         new_name=input('Enter an authors new name: ')
#         new_year=input('Enter an authors new birth year: ')
#         new_country=input('Enter an authors new mother-land: ')
#         am.update(num,new_name, new_year, new_country)
#     if n==5:
#         num=int(input('Enter an id: '))
#         am.delete(num)
#     if n==6:
#         break
#     else:
#         print("Invalid choice. Please choose between 1 and 6.")




# N-3
# from datetime import datetime

# class Note:
#     def __init__(self, note_id, title, description):
#         self.id = note_id  
#         self.title = title
#         self.description = description
#         self.created_at = datetime.now()
#         self.is_complete=False
#     def __str__(self):
#         return f'''
#         ID: {self.id}
#         Title: {self.title}
#         Description: {self.description}
#         Status: {self.is_complete}
#         Created at: {self.created_at.strftime('%d %B %Y %H:%M')}
#         '''

# class NoteManager:
#     def __init__(self):
#         self.notelist = []
#         self.next_id = 1

#     def create(self, title, description):
#         n = Note(self.next_id, title, description)
#         self.notelist.append(n)
#         self.next_id += 1
#         print("Заметка успешно создана!")

#     def show_all(self):
#         if not Note in self.notelist:
#             print('Empty note list')
#         for i in self.notelist:
#             print(i)

#     def update(self, note_id, new_title, new_description):
#         for i in self.notelist:
#             if i.id == note_id:
#                 i.title = new_title
#                 i.description = new_description
#                 print("Updated")
#                 return
#         print('Id not found') 

#     def get_by_id(self, note_id):
#         for i in self.notelist:
#             if i.id == note_id:
#                 print(i)
#                 return
#         print('Id not found')
#     def get_by_title(self, title):
#         for i in self.notelist:
#             if i.title==title:
#                 print(i)
#                 return
#         print('Invalid title')
#     def count_note(self):
#         count=0
#         for i in self.notelist:
#             count+=1
#         print('Notes: ', count)
#     def complete(self, node_id, complete=True):
#         for i in self.notelist:
#             if i.id==node_id:
#                 i.is_complete=complete
#                 print(i,'Completed ✅')
#                 return
#         print('Id not found')
#     def delete(self, note_id):
#         for i in self.notelist:
#             if i.id == note_id:
#                 self.notelist.remove(i)
#                 print("Deleted")
#                 return
#         print('Id not found')
#     def delete_all(self):
#         for i in self.notelist:
#             self.notelist.remove(i)
#             print('All notes are deleted')

# nm = NoteManager()

# while True:
#     print('''
# 1. Create a note
# 2. Show all notes
# 3. Update a note
# 4. Get by id
# 5. Get by title
# 6. Count notes
# 7. Note Status
# 8. Delete note
# 9. Delete all
# 10. Exit''')


#     num = int(input('Enter your choice: '))
  

#     if num == 1:
#         title = input('Enter a note title: ')
#         description = input('Enter a note description: ')
#         nm.create(title, description)
#     elif num == 2:
#         nm.show_all()
#     elif num == 3:
#         note_id = int(input('Enter a note id: '))
#         new_title = input('New title: ')
#         new_description = input('New description: ')
#         nm.update(note_id, new_title, new_description)
#     elif num == 4:
#         note_id = int(input('Enter a note id: '))
#         nm.get_by_id(note_id)
#     elif num==5:
#         title=input('Enter a note title: ')
#         nm.get_by_title(title)
#     elif num==6:
#         nm.count_note()
#     elif num==7:
#         note_id = int(input('Enter a note id: '))
#         nm.complete(note_id)
#     elif num == 8:
#         note_id = int(input('Enter a note id: '))
#         nm.delete(note_id) 
#     elif num==9:
#         nm.delete_all()
#     elif num == 10:
#         print("Выход из программы.")
#         break
#     else:
#         print("Неверный выбор. Попробуйте снова.")






# N-4
# class Category:
#     def __init__(self, id, name):
#         self.id=int(id)
#         self.name=name
#     def __str__(self):
#         return f'category id: {self.id} | Name: {self.name}'
# class Product:
#     def __init__(self, id, name, price, category_id):
#         self.id=int(id)
#         self.name=name
#         self.price=float(price)
#         self.category_id=int(category_id)
#     def __str__(self):
#         return f'''
#         Product ID: {self.id} 
#         Name: {self.name} 
#         Price: ${self.price:.2f} "
#         Category ID: {self.category_id}"
#         '''
# class CategoryManager:
#     def __init__(self):
#         self.next_id=1
#         self.categories=[]
#     def create(self,name):
#         c=Category(self.next_id, name)
#         self.categories.append(c)
#         self.next_id+=1
#     def show_all(self):
#         for i in self.categories:
#             print(i)
#     def get_by_id(self, id):
#         for i in self.categories:
#             if i.id==id:
#                 print(i)
#     def update(self, new_name,new_price,new_category_id):
#         for i in self.categories:
#             if i.id==id:
#                 i.name=new_name
#                 i.price=new_price
#                 i.category_id=new_category_id
#     def delete(self, id):
#         for i in self.categories:
#             if i.id==id:
#                 self.categories.remove(i)


# class ProductManager:
#     def __init__(self):
#         self.next_id = 1
#         self.products = []

#     def create(self, name, price, category_id, category_manager):
#         p = Product(self.next_id, name, price, category_id)
#         self.products.append(p)
#         self.next_id += 1

#     def show_all(self):
#         for p in self.products:
#             print(p)

#     def get_by_id(self, id):
#         for p in self.products:
#             if p.id == id:
#                 print(p)
#                 return p
#     def show_by_category(self, category_id, category_manager):
#         if not category_manager.get_by_id(category_id):
#             return
            
#         filtered_products = [p for p in self.products if p.category_id == category_id]
#         if not filtered_products:
#             print(f"No products found in Category ID {category_id}.")
#             return
            
#         print(f"Products in Category ID {category_id} ")
#         for p in filtered_products:
#             print(p)

#     def update(self, id, new_name, new_price, new_category_id, category_manager):
#         if not category_manager.get_by_id(new_category_id):
#             print(f"Cannot update product. Category with ID {new_category_id} does not exist.")
#             return
            
#         for p in self.products:
#             if p.id == id:
#                 p.name = new_name
#                 p.price = float(new_price)
#                 p.category_id = int(new_category_id)

#     def delete(self, id):
#         for i in self.products:
#             if i.id==id:
#                 self.products.remove(i)
        

# cm=CategoryManager()
# pm=ProductManager()

# while True:
#     print('''
# --- MAIN MENU ---
# [Category Management]
# 1. Create a category
# 2. Show all categories
# 3. Get category by ID
# 4. Update category by ID
# 5. Delete category by ID

# [Product Management]
# 6. Create a product
# 7. Show all products
# 8. Get product by ID
# 9. Show products by category ID  <-- NEW!
# 10. Update product by ID
# 11. Delete product by ID
# 12. Exit
# ''')

#     choice=int(input('Enter your choice: '))
#     if choice == 1:
#         name = input('Enter category name: ')
#         cm.create(name)
        
#     if choice == 2:
#         cm.show_all()
        
#     if choice == 3:
#         num = int(input('Enter category ID: '))
#         cm.get_by_id(num)
        
#     if choice == 4:
#         num = int(input('Enter category ID to update: '))
#         new_name = input('Enter new category name: ')
#         cm.update(num, new_name)
        
#     if choice == 5:
#         num = int(input('Enter category ID to delete: '))
#         cm.delete(num)
        
    # if choice == 6:
    #     name = input('Enter product name: ')
    #     price = input('Enter product price: ')
    #     category_id = int(input('Enter category ID for this product: '))
    #     pm.create(name, price, category_id, cm)
        
    # if choice == 7:
    #     pm.show_all()
        
    # if choice == 8:
    #     num = int(input('Enter product ID: '))
    #     pm.get_by_id(num)
        
    # if choice == 9:
    #     num = int(input('Enter category ID to view its products: '))
    #     pm.show_by_category(num, cm)
        
    # if choice == 10:
    #     num = int(input('Enter product ID to update: '))
    #     new_name = input('Enter new product name: ')
    #     new_price = input('Enter new product price: ')
    #     new_category_id = int(input('Enter new category ID: '))
    #     pm.update(num, new_name, new_price, new_category_id, cm)
        
    # if choice == 11:
    #     num = int(input('Enter product ID to delete: '))
    #     pm.delete(num)
        
    # if choice == 12:
    #     break
    # else:
    #     print("Invalid choice. Please choose a number between 1 and 12.")
        