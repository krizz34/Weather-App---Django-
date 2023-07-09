from django.shortcuts import render

def home(request):
    import json
    import requests

    if request.method =="POST":
        PinCode = request.POST['PinCode']
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+ PinCode +"&distance=5&API_KEY=CC312069-BD64-4B34-AE10-54F9D3564001")
        try:
            api=json.loads(api_request.content)

        except Exception as e:
            api="Error!!!"
        
        if api[0]['Category']['Name'] == "Good":
            cat_desc = "Air quality is satisfactory, and air pollution poses little or no risk."
            cat_clr = "Good"
        elif api[0]['Category']['Name'] == "Moderate":
            cat_desc =  "Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
            cat_clr = "Moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            cat_desc =  "Members of sensitive groups may experience health effects. The general public is less likely to be affected."
            cat_clr = "Unhealthy-for-sensitive-groups"
        elif api[0]['Category']['Name'] == "Unhealthy":
            cat_desc =  "Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
            cat_clr = "Unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            cat_desc =  "Health alert: The risk of health effects is increased for everyone."
            cat_clr = "Veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            cat_desc =  "Health warning of emergency conditions: everyone is more likely to be affected."
            cat_clr = "Hazardous"
        
        return render(request,'home.html',{
            'api':api,
            'cat_desc':cat_desc,
            'cat_clr':cat_clr
            })
    else:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=CC312069-BD64-4B34-AE10-54F9D3564001")
        try:
            api=json.loads(api_request.content)

        except Exception as e:
            api="Error!!!"
        
        if api[0]['Category']['Name'] == "Good":
            cat_desc = "Air quality is satisfactory, and air pollution poses little or no risk."
            cat_clr = "Good"
        elif api[0]['Category']['Name'] == "Moderate":
            cat_desc =  "Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
            cat_clr = "Moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            cat_desc =  "Members of sensitive groups may experience health effects. The general public is less likely to be affected."
            cat_clr = "Unhealthy-for-sensitive-groups"
        elif api[0]['Category']['Name'] == "Unhealthy":
            cat_desc =  "Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
            cat_clr = "Unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            cat_desc =  "Health alert: The risk of health effects is increased for everyone."
            cat_clr = "Veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            cat_desc =  "Health warning of emergency conditions: everyone is more likely to be affected."
            cat_clr = "Hazardous"
        
        return render(request,'home.html',{
            'api':api,
            'cat_desc':cat_desc,
            'cat_clr':cat_clr
            })


    

def about(request):
    return render(request,'about.html',{})
