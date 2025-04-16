from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
from datetime import datetime
import os
from models import User, Product, Category, Order, OrderItem, Review
from database import init_app, get_all_products, get_product_by_id, get_products_by_category, \
    get_all_categories, get_category_by_id, create_order, get_user_orders, get_order_by_id, \
    create_review, get_product_reviews, get_user_reviews, update_product_stock, search_products

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # 실제 운영 환경에서는 안전한 키 사용

# 애플리케이션 초기화
init_app(app)

# 파일 업로드 설정
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    products = get_all_products()
    categories = get_all_categories()
    return render_template('index.html', products=products, categories=categories)

@app.route('/products/<int:product_id>')
def product_detail(product_id):
    product = get_product_by_id(product_id)
    if not product:
        flash('상품을 찾을 수 없습니다.', 'error')
        return redirect(url_for('index'))
    
    reviews = get_product_reviews(product_id)
    return render_template('product_detail.html', product=product, reviews=reviews)

@app.route('/category/<int:category_id>')
def category_products(category_id):
    category = get_category_by_id(category_id)
    if not category:
        flash('카테고리를 찾을 수 없습니다.', 'error')
        return redirect(url_for('index'))
    
    products = get_products_by_category(category_id)
    return render_template('category.html', category=category, products=products)

@app.route('/search')
def search():
    query = request.args.get('q', '')
    if query:
        products = search_products(query)
    else:
        products = get_all_products()
    return render_template('search.html', products=products, query=query)

@app.route('/cart')
@login_required
def cart():
    return render_template('cart.html')

@app.route('/cart/add', methods=['POST'])
@login_required
def add_to_cart():
    product_id = request.form.get('product_id')
    quantity = int(request.form.get('quantity', 1))
    
    product = get_product_by_id(product_id)
    if not product or product.stock < quantity:
        flash('상품을 추가할 수 없습니다.', 'error')
        return redirect(url_for('product_detail', product_id=product_id))
    
    cart = session.get('cart', {})
    cart[product_id] = cart.get(product_id, 0) + quantity
    session['cart'] = cart
    
    flash('상품이 장바구니에 추가되었습니다.', 'success')
    return redirect(url_for('cart'))

@app.route('/cart/remove/<int:product_id>')
@login_required
def remove_from_cart(product_id):
    cart = session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        session['cart'] = cart
        flash('상품이 장바구니에서 제거되었습니다.', 'success')
    return redirect(url_for('cart'))

@app.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    if request.method == 'POST':
        cart = session.get('cart', {})
        if not cart:
            flash('장바구니가 비어있습니다.', 'error')
            return redirect(url_for('cart'))
        
        items = []
        for product_id, quantity in cart.items():
            product = get_product_by_id(product_id)
            if product and product.stock >= quantity:
                items.append({
                    'product_id': product_id,
                    'quantity': quantity,
                    'price': product.price
                })
        
        if not items:
            flash('주문할 수 있는 상품이 없습니다.', 'error')
            return redirect(url_for('cart'))
        
        shipping_address = request.form.get('shipping_address')
        if not shipping_address:
            flash('배송 주소를 입력해주세요.', 'error')
            return render_template('checkout.html', items=items)
        
        order = create_order(current_user.id, items, shipping_address)
        session['cart'] = {}
        
        flash('주문이 완료되었습니다.', 'success')
        return redirect(url_for('order_detail', order_id=order.id))
    
    cart = session.get('cart', {})
    items = []
    for product_id, quantity in cart.items():
        product = get_product_by_id(product_id)
        if product:
            items.append({
                'product': product,
                'quantity': quantity,
                'total': product.price * quantity
            })
    
    return render_template('checkout.html', items=items)

@app.route('/orders')
@login_required
def orders():
    user_orders = get_user_orders(current_user.id)
    return render_template('orders.html', orders=user_orders)

@app.route('/orders/<int:order_id>')
@login_required
def order_detail(order_id):
    order = get_order_by_id(order_id)
    if not order or order.user_id != current_user.id:
        flash('주문을 찾을 수 없습니다.', 'error')
        return redirect(url_for('orders'))
    
    return render_template('order_detail.html', order=order)

@app.route('/review/<int:product_id>', methods=['POST'])
@login_required
def add_review(product_id):
    rating = int(request.form.get('rating'))
    comment = request.form.get('comment')
    
    if not rating or not comment:
        flash('평점과 리뷰 내용을 입력해주세요.', 'error')
        return redirect(url_for('product_detail', product_id=product_id))
    
    create_review(current_user.id, product_id, rating, comment)
    flash('리뷰가 등록되었습니다.', 'success')
    return redirect(url_for('product_detail', product_id=product_id))

@app.route('/admin')
@login_required
def admin():
    if not current_user.is_admin:
        flash('관리자 권한이 필요합니다.', 'error')
        return redirect(url_for('index'))
    
    products = get_all_products()
    categories = get_all_categories()
    return render_template('admin.html', products=products, categories=categories)

@app.route('/admin/product/new', methods=['GET', 'POST'])
@login_required
def new_product():
    if not current_user.is_admin:
        flash('관리자 권한이 필요합니다.', 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        price = float(request.form.get('price'))
        stock = int(request.form.get('stock'))
        category_id = int(request.form.get('category_id'))
        
        image = request.files.get('image')
        image_url = None
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            image_url = f'/static/uploads/{filename}'
        
        product = Product(
            name=name,
            description=description,
            price=price,
            stock=stock,
            category_id=category_id,
            image_url=image_url
        )
        db.session.add(product)
        db.session.commit()
        
        flash('상품이 등록되었습니다.', 'success')
        return redirect(url_for('admin'))
    
    categories = get_all_categories()
    return render_template('product_form.html', categories=categories)

@app.route('/admin/product/<int:product_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_product(product_id):
    if not current_user.is_admin:
        flash('관리자 권한이 필요합니다.', 'error')
        return redirect(url_for('index'))
    
    product = get_product_by_id(product_id)
    if not product:
        flash('상품을 찾을 수 없습니다.', 'error')
        return redirect(url_for('admin'))
    
    if request.method == 'POST':
        product.name = request.form.get('name')
        product.description = request.form.get('description')
        product.price = float(request.form.get('price'))
        product.stock = int(request.form.get('stock'))
        product.category_id = int(request.form.get('category_id'))
        
        image = request.files.get('image')
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            product.image_url = f'/static/uploads/{filename}'
        
        db.session.commit()
        flash('상품이 수정되었습니다.', 'success')
        return redirect(url_for('admin'))
    
    categories = get_all_categories()
    return render_template('product_form.html', product=product, categories=categories)

@app.route('/admin/product/<int:product_id>/delete')
@login_required
def delete_product(product_id):
    if not current_user.is_admin:
        flash('관리자 권한이 필요합니다.', 'error')
        return redirect(url_for('index'))
    
    product = get_product_by_id(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        flash('상품이 삭제되었습니다.', 'success')
    else:
        flash('상품을 찾을 수 없습니다.', 'error')
    
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True) 