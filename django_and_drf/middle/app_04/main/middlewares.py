from main.models import SubRubric

def app_context_processor(request: str) -> dict:
    """Context processor for temlates for subrubric"""

    context = {}
    context['rubrics'] = SubRubric.objects.all()
    return context