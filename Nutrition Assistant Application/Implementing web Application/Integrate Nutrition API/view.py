from django.shortcuts import render


# Create your views here.
 
def nutitionapi(imagelink,image_id):
    configuration = openapi_client.Configuration(
        host = "https://api.spoonacular.com"
    )
    configuration.api_key['apiKeyScheme'] = os.getenv("NUTRITIONAPI")

    with openapi_client.ApiClient(configuration) as api_client:
        api_instance = misc_api.MiscApi(api_client)
        image_url =imagelink
    try:
        api_response = api_instance.image_analysis_by_url(image_url)
        pprint(api_response)
