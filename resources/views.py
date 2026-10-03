from django.shortcuts import render, get_object_or_404
from .models import StudyResource
from units.models import Unit
import cloudinary


def resource_list(request):
    resources = StudyResource.objects.filter(
        status='published'
    ).select_related('unit').order_by(
        'unit__code',
        'title'
    )

    context = {
        'resources': resources
    }

    return render(
        request,
        'resources/resource_list.html',
        context
    )


def unit_list(request):
    units = Unit.objects.all().order_by('code')

    context = {
        'units': units
    }

    return render(
        request,
        'resources/unit_list.html',
        context
    )


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

    for resource in resources:

        if resource.file:
            filename = str(resource.file).lower()

            if '.pdf' in filename:
                resource.file_type = 'PDF'

            elif '.docx' in filename:
                resource.file_type = 'DOCX'

            elif '.pptx' in filename:
                resource.file_type = 'PPTX'

            elif any(
                extension in filename
                for extension in [
                    '.jpg',
                    '.jpeg',
                    '.png',
                    '.gif',
                    '.webp'
                ]
            ):
                resource.file_type = 'Image'

            else:
                resource.file_type = 'File'

            resource.download_url = cloudinary.utils.cloudinary_url(
                resource.file.public_id,
                resource_type='raw',
                type='upload',
                flags='attachment'
            )[0]

        else:
            resource.file_type = 'File'
            resource.download_url = None

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