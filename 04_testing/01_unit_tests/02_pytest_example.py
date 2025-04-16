"""
pytest를 사용한 단위 테스트 예제
이 파일은 pytest를 사용하여 단위 테스트를 작성하는 방법을 보여줍니다.
"""

import pytest
from datetime import datetime
from typing import List, Optional

class Product:
    """상품 정보를 관리하는 클래스"""
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock
        self.created_at = datetime.now()
        self.is_available = stock > 0

    def update_stock(self, new_stock: int) -> None:
        """상품의 재고를 업데이트합니다."""
        self.stock = new_stock
        self.is_available = new_stock > 0

    def apply_discount(self, discount_rate: float) -> None:
        """상품에 할인을 적용합니다."""
        if 0 <= discount_rate <= 1:
            self.price *= (1 - discount_rate)

class ProductRepository:
    """상품 데이터를 관리하는 저장소 클래스"""
    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, product: Product) -> None:
        """새로운 상품을 추가합니다."""
        self.products.append(product)

    def get_product(self, name: str) -> Optional[Product]:
        """상품명으로 상품을 조회합니다."""
        for product in self.products:
            if product.name == name:
                return product
        return None

    def get_available_products(self) -> List[Product]:
        """재고가 있는 상품 목록을 반환합니다."""
        return [p for p in self.products if p.is_available]

# pytest 픽스처 정의
@pytest.fixture
def sample_product():
    """테스트용 샘플 상품을 생성합니다."""
    return Product("Test Product", 10000, 10)

@pytest.fixture
def product_repository(sample_product):
    """테스트용 상품 저장소를 생성합니다."""
    repository = ProductRepository()
    repository.add_product(sample_product)
    return repository

# 테스트 케이스
def test_product_creation(sample_product):
    """상품 생성 테스트"""
    assert sample_product.name == "Test Product"
    assert sample_product.price == 10000
    assert sample_product.stock == 10
    assert sample_product.is_available is True
    assert isinstance(sample_product.created_at, datetime)

def test_product_stock_update(sample_product):
    """상품 재고 업데이트 테스트"""
    sample_product.update_stock(0)
    assert sample_product.stock == 0
    assert sample_product.is_available is False

def test_product_discount(sample_product):
    """상품 할인 테스트"""
    sample_product.apply_discount(0.1)  # 10% 할인
    assert sample_product.price == 9000

def test_product_repository_add(product_repository, sample_product):
    """상품 저장소 추가 테스트"""
    assert len(product_repository.products) == 1
    assert product_repository.products[0] == sample_product

def test_product_repository_get(product_repository):
    """상품 저장소 조회 테스트"""
    found_product = product_repository.get_product("Test Product")
    assert found_product is not None
    assert found_product.name == "Test Product"
    
    not_found_product = product_repository.get_product("Nonexistent")
    assert not_found_product is None

def test_product_repository_available_products(product_repository):
    """재고가 있는 상품 조회 테스트"""
    available_products = product_repository.get_available_products()
    assert len(available_products) == 1
    
    # 재고를 0으로 설정하고 다시 테스트
    product_repository.products[0].update_stock(0)
    available_products = product_repository.get_available_products()
    assert len(available_products) == 0

# 파라미터화된 테스트
@pytest.mark.parametrize("stock,expected_available", [
    (10, True),
    (1, True),
    (0, False),
    (-1, False)
])
def test_product_availability(sample_product, stock, expected_available):
    """상품 가용성 테스트 (파라미터화)"""
    sample_product.update_stock(stock)
    assert sample_product.is_available == expected_available

@pytest.mark.parametrize("discount_rate,expected_price", [
    (0.1, 9000),
    (0.2, 8000),
    (0.5, 5000),
    (1.0, 0)
])
def test_product_discount_rates(sample_product, discount_rate, expected_price):
    """상품 할인율 테스트 (파라미터화)"""
    sample_product.apply_discount(discount_rate)
    assert sample_product.price == expected_price

# 예외 테스트
def test_invalid_discount_rate(sample_product):
    """잘못된 할인율 테스트"""
    with pytest.raises(AssertionError):
        sample_product.apply_discount(1.1)  # 110% 할인은 불가능 