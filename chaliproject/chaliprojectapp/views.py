from django.shortcuts import render, redirect
from .forms import UserForm

def user_input(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Create a success page or redirect as needed
    else:
        form = UserForm()
    return render(request, 'user_input.html', {'form': form})

