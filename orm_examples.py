from main_app.models import Cat

Cat.objects.all()

c = Cat(name='Biscuit', breed='Sphinx', description='Cuddle monster. Hairless.', age=2)
c.save()
print(c.id)

Cat.objects.all()

c = Cat(name='Whiskers', breed='Persian', description='Fluffy and friendly', age=3)
c.save()
Cat.objects.all()

c = Cat.objects.first()
print(c)
c.name = 'Rubber Biscuit'
c.save()

c = Cat(name='Pebbles', breed='alley cat', description='smells like old socks', age=7)
c.save()
Cat.objects.all()
c.delete()
Cat.objects.all()

Cat.objects.get(id=1)

try:
    cat = Cat.objects.get(id=1)
    print(f"Found cat: {cat}")
except Cat.DoesNotExist:
    print("This cat does not exist!")

Cat.objects.filter(name='Rubber Biscuit')
Cat.objects.filter(name__contains='Bis')
Cat.objects.filter(age__lte=3)
Cat.objects.filter(age__gt=2)
Cat.objects.exclude(name='Pebbles')

Cat.objects.order_by('name')
Cat.objects.order_by('-age')
oldest_cat = Cat.objects.order_by('-age')[0]
youngest_cat = Cat.objects.order_by('age')[0]

young_cats = Cat.objects.filter(age__lte=3).order_by('name')
total_cats = Cat.objects.count()
young_cats_count = Cat.objects.filter(age__lte=3).count()

first_cat = Cat.objects.first()
last_cat = Cat.objects.last()
cats_by_age = Cat.objects.order_by('age')
second_youngest = cats_by_age[1]

Cat.objects.filter(age__exact=3)
Cat.objects.filter(age__gt=2)
Cat.objects.filter(age__gte=3)
Cat.objects.filter(age__lt=5)
Cat.objects.filter(age__lte=3)
Cat.objects.filter(name__contains='Bis')
Cat.objects.filter(name__icontains='bis')
Cat.objects.filter(name__startswith='B')
Cat.objects.filter(breed__endswith='cat')
Cat.objects.filter(age__in=[1, 2, 3])
Cat.objects.filter(age__range=(1, 5))

Cat.objects.bulk_create([
    Cat(name='Fluffy', breed='Maine Coon', description='Very fluffy', age=4),
    Cat(name='Shadow', breed='Black Cat', description='Mysterious', age=2),
    Cat(name='Ginger', breed='Orange Tabby', description='Loves to play', age=1)
])

Cat.objects.filter(age__lt=2).update(description='Young cat')
Cat.objects.filter(name__contains='test').delete()
