  
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config
import db

def getMenu():
    menuList=[]
    cur = db.getConnection()
    query = cur.execute("SELECT `menu_title`,`page_name` FROM `page`")    
    results = cur.fetchall()
    db.closeConn(cur)   
    for result in results:
        menuList.append(result) 
    return menuList 
 
def getPage(pageKey):
    page ={"menu_title":[], "page_title":[], "pageId":[], "page_name":[], "content":[],}
    cur = db.getConnection()
    query = cur.execute("SELECT * FROM `page` WHERE `page_name`=%s", (pageKey,))    
    #query = cur.execute("SELECT `title`,`content`,`pageId` FROM `page` WHERE `pageKey`=%s", (pageId,))  
    results = cur.fetchall()
    db.closeConn(cur) 
    
    for result in results:
        page["menu_title"].append(result[1])
        page["page_title"].append(result[2])
        page["pageId"].append(result[0])
        page["page_name"].append(result[3])
        page["content"].append(result[4])
    return page

def getImages():
    productList=[]
    cur = db.getConnection()
    query = cur.execute("SELECT `file`,`description`,`price` FROM `gallery`")
    results = cur.fetchall()
    db.closeConn(cur)
    for result in results:
        # page["file"].append(result[0])
        # page["description"].append(result[1])
        # page["price"].append(result[2])
        productList.append(result)
    return productList

@view_config(
    route_name='home',
    renderer="templates/home.jinja2"
) 
def home(request):
    items=getMenu()
    page = getPage("home")
    menuTitle = page.get("menu_title")[0]
    pageTitle = page.get("page_title")[0]
    pageId = page.get("pageId")[0]
    pageName = page.get("page_name")[0]
    content = page.get("content")[0]
    return{"items":items,"pageTitle":pageTitle, "content":content, "pageId":pageId, "menuTitle":menuTitle, pageName:"pageName"}
    # return{page}

@view_config(
    route_name='b1',
    renderer="templates/home.jinja2"
) 
def b1(request):
    items=getMenu()
    page = getPage("b1")
    menuTitle = page.get("menu_title")[0]
    pageTitle = page.get("page_title")[0]
    pageId = page.get("pageId")[0]
    pageName = page.get("page_name")[0]
    content = page.get("content")[0]
    return{"items":items,"pageTitle":pageTitle, "content":content, "pageId":pageId, "menuTitle":menuTitle, pageName:"pageName"}
    # return{page}
    
@view_config(
    route_name='b2',
    renderer="templates/home.jinja2"
) 
def b2(request):
    items=getMenu()
    page = getPage("b2")
    menuTitle = page.get("menu_title")[0]
    pageTitle = page.get("page_title")[0]
    pageId = page.get("pageId")[0]
    pageName = page.get("page_name")[0]
    content = page.get("content")[0]
    return{"items":items,"pageTitle":pageTitle, "content":content, "pageId":pageId, "menuTitle":menuTitle, pageName:"pageName"}
    # return{page}

@view_config(
    route_name='b3',
    renderer="templates/home.jinja2"
) 
def b3(request):
    items=getMenu()
    page = getPage("b3")
    menuTitle = page.get("menu_title")[0]
    pageTitle = page.get("page_title")[0]
    pageId = page.get("pageId")[0]
    pageName = page.get("page_name")[0]
    content = page.get("content")[0]
    return{"items":items,"pageTitle":pageTitle, "content":content, "pageId":pageId, "menuTitle":menuTitle, pageName:"pageName"}

@view_config(
    route_name='b4',
    renderer="templates/home.jinja2"
) 
def b4(request):
    items=getMenu()
    page = getPage("b4")
    menuTitle = page.get("menu_title")[0]
    pageTitle = page.get("page_title")[0]
    pageId = page.get("pageId")[0]
    pageName = page.get("page_name")[0]
    content = page.get("content")[0]
    return{"items":items,"pageTitle":pageTitle, "content":content, "pageId":pageId, "menuTitle":menuTitle, pageName:"pageName"}

@view_config(
    route_name='b5',
    renderer="templates/home.jinja2"
) 
def b5(request): 
    items=getMenu()
    page = getPage("b5")
    menuTitle = page.get("menu_title")[0]
    pageTitle = page.get("page_title")[0]
    pageId = page.get("pageId")[0]
    pageName = page.get("page_name")[0]
    content = page.get("content")[0]
    return{"items":items,"pageTitle":pageTitle, "content":content, "pageId":pageId, "menuTitle":menuTitle, pageName:"pageName"}

@view_config(
    route_name='products',
    renderer="templates/products.jinja2"
) 
def products(request):
    items=getMenu()
    products=getImages()
    # page = getImages("products")
    # file = page.get("file")[0]
    # description = page.get("description")[0]
    # price = page.get("price")[0]
    # return{"items":items,"file":file, "description":description, "price":price}
    # return{page}
    return{"items":items,"products":products}
 
if __name__ == '__main__':
    
    with Configurator() as config:
        config.include('pyramid_jinja2')
        #config.include('pyramid_debugtoolbar')
        config.add_static_view(name='static',
            path='static')
        config.add_static_view(name='img',
            path='img')
        config.add_static_view(name='gal',
            path='img/gallery')

        config.add_route('home', '/home')
        config.add_route('b1', '/b1')
        config.add_route('b2', '/b2')
        config.add_route('b3', '/b3')
        config.add_route('b4', '/b4')
        config.add_route('b5', '/b5')
        config.add_route('products', '/products')
        # config.add_route('destination', '/Destination')

        config.scan()

        app = config.make_wsgi_app()

    server = make_server('0.0.0.0', 6540, app)

    server.serve_forever()