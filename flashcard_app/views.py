from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from flashcard_app.models import Flashcard, FlashcardDeck, Course


def home(request):
  if request.user.is_anonymous:
    return render(request, 'flashcard_app/home.html')
  
  context = {
    'flashcard_decks': FlashcardDeck.objects.filter(author=request.user)
  }
  return render(request, 'flashcard_app/home.html', context)


@login_required
def create_deck(request):
  if request.method == 'POST':
    deck = FlashcardDeck() # new flashcard deck object

    # process form data
    deck.name = request.POST.get('name')
    deck.description = request.POST.get('description')
    course_id = request.POST.get('course')
    deck.course = Course.objects.get(id=course_id)
    deck.author = request.user
  
    deck.save() # save to database
    # messages.success(request, f'Succesfully created deck: {deck.name}!')
    return redirect(f'/edit-deck/{deck.id}')

  context = {
    'courses': Course.objects.filter(author=request.user)
  }

  return render(request, 'flashcard_app/create-deck.html', context)


@login_required
def edit_deck(request, deck_id):
  if request.method == 'POST':
    flashcard = Flashcard() # new course object

    # process form data
    flashcard.front = request.POST.get('front')
    flashcard.back = request.POST.get('back')
    flashcard.flashcard_deck = FlashcardDeck.objects.get(id=deck_id)
  
    flashcard.save() # save to database

  context = {
    'deck' : FlashcardDeck.objects.prefetch_related('flashcard_set').get(id=deck_id)
  }

  return render(request, 'flashcard_app/edit-deck.html', context)


@login_required
def delete_deck(request, deck_id):
  deck = FlashcardDeck.objects.get(id=deck_id)
  FlashcardDeck.objects.filter(id=deck_id).delete()
  messages.success(request, f'Succesfully deleted deck: {deck.name}')
  return redirect('/')


@login_required
def delete_flashcard(request, flashcard_id):
  card = Flashcard.objects.get(id=flashcard_id)
  deck_id = card.flashcard_deck.id
  Flashcard.objects.filter(id=flashcard_id).delete()
  return redirect(f'/edit-deck/{deck_id}')


@login_required
def study(request, study_id):
  context = {
    'flashcard_deck': FlashcardDeck.objects.prefetch_related('flashcard_set').get(id=study_id)
  }
  return render(request, 'flashcard_app/study.html', context)


@login_required
def courses(request):
  if request.method == 'POST':
    course = Course() # new course object

    # process form data
    course.name = request.POST.get('course_name')
    course.section_num = request.POST.get('course_section_num')
    course.semester = request.POST.get('course_semester')
    course.year = request.POST.get('course_year')
    course.author = request.user
  
    course.save() # save to database
    messages.success(request, f'Succesfully created course: {course.name}!')

  context = {
    'courses': Course.objects.filter(author=request.user)
  }
  return render(request, 'flashcard_app/courses.html', context)


@login_required
def delete_course(request, course_id):
  Course.objects.filter(id=course_id).delete()
  messages.success(request, f'Your course and all associated flashcard decks have been deleted')
  return redirect('/courses/')

# need at least one join
