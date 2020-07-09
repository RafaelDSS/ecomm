"""
    Modelos do app de produtos.
"""
from django.db import models
from django.db.models import Q, QuerySet


# Create your models here.

class ProductManager(models.Manager):
    def with_text(self, text: str) -> QuerySet:
        """
            Realiza a pesquisa  nos produtos cujo nome contenha **text**.

            :param text: Texto que será usado na pesquisa

            :return: QuerySet com o filtro aplicado
        """
        return self.get_queryset().filter(name__contains=text)

    def expensive_products(self) -> QuerySet:
        """
            realiza o filtro dos produtos cujo preço seja maior que R$ 500,00.

            :return: QuerySet com filtro aplicado
        """
        return self.get_queryset().filter(price__gte=500)

    def cheap_toys(self) -> QuerySet:
        """
            Retorna a lista com os brinquedos mais baratos.

            :return: QuerySet com filtro aplicado
        """
        # Executa a queryset com o filtro maior ou igual a 500
        return self.get_queryset().filter(category__name="Brinquedos", price__lte=100)

    def toys_or_expensive_items(self) -> QuerySet:
        """
            Retorna a lista com os brinquedos mais caros.

            :return: QuerySet com filtro aplicado
        """
        query_filter = Q(category__name="Brinquedos") | Q(price__gte=500)
        return self.get_queryset().filter(query_filter)


class Category(models.Model):
    """
        Model contendo todos os campos nescessários para cadastrar categorias no ecomm.
    """
    name = models.CharField("Nome", max_length=50)
    description = models.TextField("Descrição")

    class Meta:
        verbose_name_plural = "Categorias"

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    """
        Model contendo todos os campos nescessários para cadastrar produtos no ecomm.
    """
    objects = ProductManager()
    name = models.CharField("Nome", max_length=100)
    description = models.TextField("Descrição")
    price = models.DecimalField("Preço", max_digits=8, decimal_places=2)
    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        related_name="products",
        verbose_name="Categoria",
    )

    class Meta:
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.name


class Order(models.Model):
    """
        Model contendo todos os campos nescessários para cadastrar ordens no ecomm.
    """
    name = models.CharField("Nome do cliente", max_length=100)
    payment = models.CharField("Meio Pagamento", max_length=50)
    products = models.ManyToManyField(Product)

    @property
    def total_amount(self):
        return sum([product.price for product in self.products.all()])

    def __str__(self):
        return f"{self.name} - {self.total_amount}"
