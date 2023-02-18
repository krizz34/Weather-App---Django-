from django.shortcuts import render

def home(request):
    import json
    import requests
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=CC312069-BD64-4B34-AE10-54F9D3564001")
    try:
        api=json.loads(api_request.content)

    except Exception as e:
        api="Error!!!"
    return render(request,'home.html',{'api':api})

def about(request):
    return render(request,'about.html',{})
