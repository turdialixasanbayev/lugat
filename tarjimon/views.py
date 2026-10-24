from django.shortcuts import render

from .models import Dictionary


def search_view(request):
    query = request.GET.get('q', '').strip()
    direction = request.GET.get('direction', 'en_uz')

    translation = None

    if query:
        if direction == 'en_uz':
            word_obj = Dictionary.objects.filter(english__iexact=query).first()

            if word_obj:
                translation = word_obj.uzbek
        else:
            word_obj = Dictionary.objects.filter(uzbek__iexact=query).first()

            if word_obj:
                translation = word_obj.english

    context = {
        'searched_word': query,
        'translation': translation,
        'direction': direction,
    }

    return render(request, 'index.html', context)
