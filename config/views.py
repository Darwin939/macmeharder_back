from django.http import HttpResponse


def show_chema(request):

    with open('./data/schema.graphql', 'rt') as file:
        data = ''
        for line in file:
            data+=line+"<br>"



    return HttpResponse(data)