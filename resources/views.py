from django.shortcuts import render, get_object_or_404
from .models import StudyResource
from units.models import Unit

# Create your views here.

def resource_list(request):
    resources = StudyResource.objects.filter( status='published').select_related('unit').order_by('unit__code', 'title')

    context = {'resources': resources ,
    }

    return render(request, 'resources/resource_list.html', context)

def unit_list(request):
    units = Unit.objects.all().order_by('code')

    context = {
        'units': units
    }

    return render(request, 'resources/unit_list.html', context)

def unit_resource_categories(request, unit_id):
    unit = get_object_or_404(Unit, id=unit_id)

    context = {
        'unit': unit
    }

    return render(
        request,
        'resources/unit_resource_categories.html',
        context
    )
def resource_list_by_category(request, unit_id, category):
    unit = get_object_or_404(Unit, id=unit_id)

    resources = StudyResource.objects.filter(
        unit=unit,
        category=category,
        status='published'
    ).order_by('title')

    category_name = dict(
        StudyResource.CATEGORY_CHOICES
    ).get(category, category)

    context = {
        'unit': unit,
        'category': category_name,
        'resources': resources
    }

    return render(
        request,
        'resources/resource_list_by_category.html',
        context
    )