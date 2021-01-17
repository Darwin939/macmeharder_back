from django.http import HttpResponse , FileResponse


def show_chema(request):

    # with open('./data/schema.graphql', 'rt') as file:
    #     data = ''
    #     for line in file:
    #         data+=line+"<br>"
    #
    #
    #
    # return HttpResponse(data)

    file = open('./data/schema.graphql', 'rt')

    response = FileResponse(file)

    return response