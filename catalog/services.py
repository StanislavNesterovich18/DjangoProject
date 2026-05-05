from catalog.models import Product


def products_category_view(category):
    return Product.objects.filter(category=category)
