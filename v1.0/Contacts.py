import Helpers


# ----------------------------------------------------------------------------------------------------------------------
# As descrições contidas aqui, servem para todos os metodos.
# Caso algum metodo utilise-as de forma diferente, tera uma descrição na parte superior do metodo.
# apiKey => Sua chave de acesso a api do Zapus.
# chatWid => Informe o número do contato no formato id do WhatsApp. EX 5522999999999@c.us.

# ----------------------------------------------------------------------------------------------------------------------
def blockeds(apiKey):
    header = {
        'Connection': 'keep-alive',
        'content-type': 'application/json',
        'apiKey': apiKey
    }

    body = {}

    post = Helpers.post('/contacts/blockeds', header, body)
    Helpers.logs('contacts', 'blockeds', post)
    return post


# ----------------------------------------------------------------------------------------------------------------------
# type => Informe o tipo de retorno que deseja, "all" para todos, "mute" para mutados e "nomute" para desmutados.
def listMute(apiKey, type):
    header = {
        'Connection': 'keep-alive',
        'content-type': 'application/json',
        'apiKey': apiKey
    }

    body = {
        'type': type,
    }

    post = Helpers.post('/contacts/list-mute', header, body)
    Helpers.logs('contacts', 'list-mute', post)
    return post


# ----------------------------------------------------------------------------------------------------------------------
def getAll(apiKey):
    header = {
        'Connection': 'keep-alive',
        'content-type': 'application/json',
        'apiKey': apiKey
    }

    body = {}

    post = Helpers.post('/contacts/get-all', header, body)
    Helpers.logs('contacts', 'get-all', post)
    return post


# ----------------------------------------------------------------------------------------------------------------------
# block => Envie true para bloquear e false para desbloquear.
def block(apiKey, chatWid, block):
    header = {
        'Connection': 'keep-alive',
        'content-type': 'application/json',
        'apiKey': apiKey
    }

    body = {
        'chat_wid': chatWid,
        'block': block,
    }

    post = Helpers.post('/contacts/block', header, body)
    Helpers.logs('contacts', 'block', post)
    return post


# ----------------------------------------------------------------------------------------------------------------------
# mute => Envie true para mutar um contato e false para desmutar.
# time => Quando tempo deseja deixar o contato mutado.
# type => Envie o período de mutação, (hours, minutes, year)
def mute(apiKey, chatWid, mute, time, type):
    header = {
        'Connection': 'keep-alive',
        'content-type': 'application/json',
        'apiKey': apiKey
    }

    body = {
        'chat_wid': chatWid,
        'mute': mute,
        'time': time,
        'type': type,
    }

    post = Helpers.post('/contacts/mute', header, body)
    Helpers.logs('contacts', 'mute', post)
    return post


# ----------------------------------------------------------------------------------------------------------------------
def status(apiKey, chatWid):
    header = {
        'Connection': 'keep-alive',
        'content-type': 'application/json',
        'apiKey': apiKey
    }

    body = {
        'chat_wid': chatWid,
    }

    post = Helpers.post('/contacts/status', header, body)
    Helpers.logs('contacts', 'status', post)
    return post
# ----------------------------------------------------------------------------------------------------------------------
