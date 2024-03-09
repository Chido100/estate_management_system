from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import IncidentReporting
from .forms import IncidentReportingForm




# View Incident Report details
@login_required
def incident_report_details(request, pk):
    incident_report = get_object_or_404(IncidentReporting, pk=pk)

    report = User.objects.get(username=access_request.reporter)
    report_per_user = report.reporter.all()
    context = {'incident_report': incident_report, 'report_per_user': report_per_user}
    
    return render(request, 'incident_reporting/incident_report_details.html', context)



""" For Resident """

# Create incident report
@login_required
def new_incident(request):
    if request.method == 'POST':
        form = IncidentReportingForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.reporter = request.user
            report.incident_status = 'Pending'
            report.save()
            messages.info(request, "Your report has been submitted successfully.")
            return redirect('dashboard')
        else:
            messages.warning(request, "Something went wrong. Please check details.")
            return redirect('new-incident')
    else:
        form = IncidentReportingForm()
    return render(request, 'incident_reporting/new_incident.html', {'form': form})


# Update incident report
@login_required
def update_incident(request, pk):
    incident_report = get_object_or_404(IncidentReporting, pk=pk)
    if not incident_report.is_resolved:

        if request.method == 'POST':
            form = IncidentReportingForm(request.POST, instance=incident_report)
            if form.is_valid():
                form.save()
                messages.info(request, "Your report has been updated and all changes are saved.")
                return redirect('dashboard')
            else:
                messages.warning(request, "Something went wrong. Please check details.")
        else:
            form = IncidentReportingForm(instance=incident_report)
            return render(request, 'incident_reporting/update_incident.html', {'form': form})

    else:
        messages.warning(request, "You cannot make any changes!")
        return redirect('dashboard')




""" For Management Team """


# View reports in queue
@login_required
def report_queue(request):
    incident_report = IncidentReporting.objects.filter(request_status='Pending').order_by('-date_created')
    return render(request, 'incident_reporting/report_queue.html', {'incident_report': incident_report})


# Accept a report from queue
@login_required
def accept_incident_report(request, pk):
    incident_report = IncidentReporting.objects.get(pk=pk)
    incident_report.assignee = request.user
    incident_report.request_status = 'In-Progress'
    incident_report.date_accepted = datetime.datetime.now()
    incident_report.save()
    messages.info(request, 'Incident Report has been accepted, Please resolve as soon as possible.')
    return redirect('report-in-progress')


# Close a report
@login_required
def close_incident_report(request, pk):
    incident_report = IncidentReporting.objects.get(pk=pk)
    incident_report.request_status = 'Completed'
    incident_report.is_resolved = True
    incident_report.closed_date = datetime.datetime.now()
    incident_report.save()
    messages.info(request, 'Incident Report has been resolved')
    return redirect('report-queue')


# Incident report in progress
@login_required
def report_in_progress(request):
    incident_reports = IncidentReporting.objects.filter(assignee=request.user, is_resolved=False)
    return render(request, 'incident_reporting/report_in_progress.html', {'incident_report': incident_reports})



# All resolved incidents
@login_required
def all_resolved_reports(request):
    incident_reports = IncidentReporting.objects.filter(assignee=request.user, is_resolved=True)
    return render(request, 'incident_reporting/all_resolved_reports.html', {'incident_reports': incident_reports})