from django.contrib import messages
from django.shortcuts import render, redirect


from CV.forms import CvForm


def cv(request):
    return render(request, 'home.html')


def add(request):
    """
    Save the form data
    """
    if request.method == "POST":
        form = CvForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "your Cv details added to database")
            return redirect('cv')
    else:
        form = CvForm()
    return render(request, 'Add.html', {'form': form})
