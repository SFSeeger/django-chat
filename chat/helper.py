from chat.models import Chat


def check_for_chat(name1, name2):
        name = name1 + "_" + name2
        if Chat.objects.filter(name=name):
            return name
        else:
            name = name2 + "_" + name1

        if Chat.objects.filter(name=name):
            return name
        else:
            return False