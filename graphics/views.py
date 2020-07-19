from django.shortcuts import render
from graphics.models import (
    Graphics_Portfolio, Graphics_Archive, 
    Graphics_Stack, FinalDesigns, Tag, Mocks, 
    ArchiveFinalDesigns, AchieveMocks
)
from django.shortcuts import render, get_object_or_404

def graphics(request):
  template = "graphics/graphic.html"
  title = "Pius Lucky"
  stack = Graphics_Stack.objects.all()
  portfolio = Graphics_Portfolio.objects.prefetch_related("tag").all()
  archive = Graphics_Archive.objects.prefetch_related("tag").all()
  final_d = FinalDesigns.objects.all()
  a_final_d = ArchiveFinalDesigns.objects.all()
  mocks = Mocks.objects.all()
  a_mocks = AchieveMocks.objects.all()
  oth_archive = Graphics_Archive.objects.filter(position="others")
  context = {
    "title":title,
    "stack":stack,
    "portfolio":portfolio,
    "archive":archive,
    "finald":final_d,
    "a_finald":a_final_d,
    "mocks":mocks,
    "a_mocks":a_mocks,
    "oth_archive":oth_archive
  }
  return render(request, template, context)


def archive_detail(request, slug):
  archive_post = get_object_or_404(Graphics_Archive, slug=slug)
  archive_fd = ArchiveFinalDesigns.objects.filter(portfolio__slug = slug)
  archive_mk = AchieveMocks.objects.filter(portfolio__slug = slug)
  title = "Detail"
  template = "graphics/detail.html"
  context = {
    "archive_post":archive_post,
    "title":title,
    "archive_post":archive_post,
    "archive_fd":archive_fd,
    "archive_mk":archive_mk
  }
  return render(request, template, context)
