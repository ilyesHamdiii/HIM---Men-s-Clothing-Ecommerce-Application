import json
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from store.models import Product, Category


def generate_unique_slug(model, base_slug):
    """Génère un slug unique basé sur un modèle et un slug de base"""
    slug = base_slug
    counter = 1
    while model.objects.filter(slug=slug).exists():
        slug = f"{base_slug}-{counter}"
        counter += 1
    return slug


class Command(BaseCommand):
    help = 'Import products from JSON file'

    def handle(self, *args, **kwargs):
        try:
            with open('store/fixtures/x.json', 'r', encoding='utf-8-sig') as f:
                data = json.load(f)
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR("❌ 'fixture.json' not found."))
            return

        for item in data:
            category_name = item.get('category', 'Uncategorized')
            slug = slugify(category_name)

            # Crée ou récupère la catégorie
            category_obj, _ = Category.objects.get_or_create(
                name=category_name,
                defaults={'slug': generate_unique_slug(Category, slug)}
            )

            # Crée ou met à jour le produit
            product, created = Product.objects.update_or_create(
                id=item['id'],
                defaults={
                    'name': item['name'],
                    'category': category_obj,
                    'material': item.get('material', ''),
                    'description': item.get('description', ''),
                    'price': item.get('price', 0.0),
                    'image_url': item.get('image_url', '')
                }
            )

            msg = f"{'🆕 Created' if created else '♻️ Updated'}: {product.name}"
            self.stdout.write(self.style.SUCCESS(msg))
