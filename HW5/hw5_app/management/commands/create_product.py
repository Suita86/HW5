class Command(BaseCommand):
    help = 'Add a product to the database'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Product name')
        parser.add_argument('description', type=str, help='Product description')
        parser.add_argument('price', type=str, help='Product price')
        parser.add_argument('quantity', type=str, help='Product quantity')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        description = kwargs.get('description')
        price = kwargs.get('price')
        quantity = kwargs.get('quantity')

        # Call the create_client function to add a client to the database
        product = Product(name=name, description=description, price=price, quantity=quantity)
        product.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully added product: {name}'))


'''
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    date_added = models.DateField(auto_now_add=True)
'''
