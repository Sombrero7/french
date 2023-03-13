from django.shortcuts import render
from json import dumps

# Create your views here.
def opposites(request):
    # create data dictionary
    data = [
        ["Laugh", "Cry"],
        ["Even", "Odd"],
        ["Hot", "Cold"],
        ["Light", "Dark"],
        ["Opposite", "Same"],
        ["Far", "Near"],
        ["Give", "Take"],
        ["Night", "Day"],
        ["Import", "Export"],
        ["Hard", "Easy"],
        ["Never", "Always"],
        ["Late", "Early"],
        ["Less", "More"],
        ["Male", "Female"],
        ["Happiness", "Sadness"],
        ["Fast", "Slow"],
        ["Old", "Young"],
        ["Boy", "Girl"],
        ["Up", "Down"],
        ["Left", "Right"],
        ["Rich", "Poor"],
        ["Love", "Hate"],
        ["Inside", "Outside"],
        ["Bad", "Good"],
        ["Short", "Tall"],
    ]
    data = dumps(data)
    return render(request, "game/opposites.html", {"data": data})


# Create your views here.
def selection(request):
    # create data dictionary
    data = [
        ["aller", "to go"],
        ["avoir", "to have"],
        ["aimer", "to like"],
        ["arrêter", "to stop"],
        ["donner", "to give"],
        ["boire", "to drink"],
        ["dire", "to say"],
        ["être", "to be"],
        ["faire", "to do"],
        ["garder", "to keep"],
        ["mélanger", "to mix"],
        ["manger", "to eat"],
        ["ranger", "to clean"],
        ["organiser", "to organize"],
        ["cuper", "to cut"],
        ["tomber", "to fall"],
        ["laisser", "to let"],
        ["passer", "to pass"],
        ["relentir", "to slow down"],
        ["s'éclipser", "to disappear"],
        ["prendre", "to take"],
        ["perdre", "to lose"],
        ["pouvoir", "to be able to"],
        ["vouloir", "to want"],
        ["voir", "to see"],
    ]
    
    data = dumps(data)
    return render(request, "game/data_selection.html", {"data": data})