from django.shortcuts import render, redirect
from django.contrib import messages
from incidentdown.models import IncidentDown


# Create your views here.
def index(request):
    return render(request, 'incidentdown/index.html')

def submitincident(request):
    if request.method == 'POST':
        caller_id = request.POST['caller_id']
        emailAdress = request.POST['emailAdress']
        description = request.POST['description']
        comments = request.POST['comments']
        impact = request.POST['impact']
        urgency = request.POST['urgency']
        worknotes = request.POST['worknotes']
        assignment_group = request.POST['assignment_group']
        state = request.POST['state']

    incidents = IncidentDown(
        caller_id=caller_id,
        emailAdress=emailAdress,
        description=description,
        comments=comments,
        impact=impact,
        urgency=urgency,
        worknotes=worknotes,
        assignment_group=assignment_group,
        state=state,

    )

    incidents.save()
    messages.success(request, 'Incident submitted successfully')
    return redirect('index')