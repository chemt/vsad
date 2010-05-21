import datetime
import models

CART_ID = 'CART-ID'

class ItemAlreadyExists(Exception):
    pass

class ItemDoesNotExist(Exception):
    pass

class Cart:
    def __init__(self, request):
        cart_id = request.session.get(CART_ID)
        if cart_id:
            try:
                cart = models.Cart.objects.get(id=cart_id, checked_out=False)
            except models.Cart.DoesNotExist:
                cart = self.new(request)
        else:
            cart = self.new(request)
        self.cart = cart

    def __iter__(self):
        for item in self.cart.item_set.all():
            yield item

    def checkout(self):
        self.cart.checked_out = True
        self.cart.save()


    def new(self, request):
        cart = models.Cart(creation_date=datetime.datetime.now())
        cart.save()
        request.session[CART_ID] = cart.id
        return cart

    def add(self, product, unit_price, quantity=1):
        try:
            item = models.Item.objects.get(cart=self.cart, product=product,)
        except models.Item.DoesNotExist:
            item = models.Item()
            item.cart = self.cart
            item.product = product
            item.unit_price = unit_price
            item.quantity = quantity
            item.save()
        else:
            item.unit_price = unit_price
            item.quantity += int(quantity)
            item.save()

    def inc(self, id):
        try:
            item = models.Item.objects.get(cart=self.cart, id=id,)
        except models.Item.DoesNotExist:
            pass
        else:
            item.quantity += 1
            item.save()

    def dec(self, id):
        try:
            item = models.Item.objects.get(cart=self.cart, id=id,)
        except models.Item.DoesNotExist:
            pass
        else:
            item.quantity -= 1
            if item.quantity: 
                item.save()
            else:
                item.delete()
    
    def delete(self, id):        
        try:
            item = models.Item.objects.get(cart=self.cart, id=id,)
        except models.Item.DoesNotExist:
            pass
        else:
            item.delete()

    def remove(self, product):
        try:
            item = models.Item.objects.get(
                cart=self.cart,
                product=product,
            )
        except models.Item.DoesNotExist:
            raise ItemDoesNotExist
        else:
            item.delete()

    def update(self, product, unit_price, quantity):
        try:
            item = models.Item.objects.get(
                cart=self.cart,
                product=product,
            )
            item.cart = self.cart
            item.product = product
            item.unit_price = unit_price
            item.quantity = quantity
            item.save(force_update = True)
        except models.Item.DoesNotExist:
            raise ItemDoesNotExist

    def clear(self):
        for item in models.Item.objects.filter(cart=self.cart):
            item.delete()

    # There's all sort of info you might want to easily get from your cart
    
    def get_total(self):
        total = 0.0
        for item in models.Item.objects.filter(cart=self.cart):
            total += item.total_price()
        assert False, total
        return total
    
    
    def getQuantity(self, product):
        try: 
            item = models.Item.objects.get(cart = self.cart, product = product)
            return item.quantity
            
        except models.Item.DoesNotExist:
            raise ItemDoesNotExist