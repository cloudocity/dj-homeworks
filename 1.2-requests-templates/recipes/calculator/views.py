from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def recipes(request, blud):
    servings = int(request.GET.get("servings", 1))
    print(servings)
    context = {
        'recipe': {
        }
    }
    for ingredient, amount in DATA.items():
        print(amount)
        if blud == ingredient:
            for items in amount:
                context['recipe'][items] = amount[items] * servings
                print(amount[items])
    return render(request, 'calculator/index.html', context)
