from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from models import db, User, Product, Category, Order, OrderItem, Review
import os

# Flask 확장 초기화
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
mail = Mail()
bcrypt = Bcrypt()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def init_app(app):
    # 데이터베이스 설정
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Flask 확장 초기화
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    mail.init_app(app)
    bcrypt.init_app(app)
    
    # 로그인 설정
    login_manager.login_view = 'auth.login'
    login_manager.login_message = '로그인이 필요합니다.'
    login_manager.login_message_category = 'info'
    
    # 데이터베이스 생성
    with app.app_context():
        db.create_all()
        
        # 기본 관리자 계정 생성
        if not User.query.filter_by(username='admin').first():
            admin = User(
                username='admin',
                email='admin@example.com',
                is_admin=True
            )
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
            
        # 기본 카테고리 생성
        if not Category.query.first():
            categories = [
                Category(name='전자제품', description='스마트폰, 노트북 등 전자제품'),
                Category(name='의류', description='남성, 여성 의류'),
                Category(name='가구', description='가정용 가구'),
                Category(name='식품', description='신선식품, 가공식품')
            ]
            db.session.add_all(categories)
            db.session.commit()

def get_all_products():
    return Product.query.all()

def get_product_by_id(product_id):
    return Product.query.get(product_id)

def get_products_by_category(category_id):
    return Product.query.filter_by(category_id=category_id).all()

def get_all_categories():
    return Category.query.all()

def get_category_by_id(category_id):
    return Category.query.get(category_id)

def create_order(user_id, items, shipping_address):
    total_amount = sum(item['price'] * item['quantity'] for item in items)
    
    order = Order(
        user_id=user_id,
        total_amount=total_amount,
        shipping_address=shipping_address
    )
    db.session.add(order)
    db.session.flush()
    
    for item in items:
        order_item = OrderItem(
            order_id=order.id,
            product_id=item['product_id'],
            quantity=item['quantity'],
            price=item['price']
        )
        db.session.add(order_item)
        
        # 재고 감소
        product = Product.query.get(item['product_id'])
        product.stock -= item['quantity']
    
    db.session.commit()
    return order

def get_user_orders(user_id):
    return Order.query.filter_by(user_id=user_id).all()

def get_order_by_id(order_id):
    return Order.query.get(order_id)

def create_review(user_id, product_id, rating, comment):
    review = Review(
        user_id=user_id,
        product_id=product_id,
        rating=rating,
        comment=comment
    )
    db.session.add(review)
    db.session.commit()
    return review

def get_product_reviews(product_id):
    return Review.query.filter_by(product_id=product_id).all()

def get_user_reviews(user_id):
    return Review.query.filter_by(user_id=user_id).all()

def update_product_stock(product_id, quantity):
    product = Product.query.get(product_id)
    if product:
        product.stock += quantity
        db.session.commit()
        return True
    return False

def search_products(query):
    return Product.query.filter(
        (Product.name.ilike(f'%{query}%')) |
        (Product.description.ilike(f'%{query}%'))
    ).all() 