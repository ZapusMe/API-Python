import Helpers


# ----------------------------------------------------------------------------------------------------------------------
# As descrições contidas aqui, servem para todos os metodos.
# Caso algum metodo utilise-as de forma diferente, tera uma descrição na parte superior do metodo.
# apiKey => Sua chave de acesso a api do Zapus.
# webHooks => Você receberá nessa url eventos de confirmação de envio, status, ...

# ----------------------------------------------------------------------------------------------------------------------
# webHooks => Você receberá nessa url eventos de confirmação de envio, status, ...
def login(apiKey, webHooks=None):
    header = {
        'Connection': 'Keep-Alive',
        'Content-type': 'application/json',
        'apiKey': apiKey
    }

    if webHooks is None:
        body = {}
    else:
        body = {
            'webhookMessage': webHooks.webhookMessage,
            'webhookIncomingCall': webHooks.webhookIncomingCall,
            'webhookStateChanged': webHooks.webhookStateChanged,
            'webhookQrcode': webHooks.webhookQrcode,
            'webhookLiveLocation': webHooks.webhookLiveLocation,
            'webhookParticipantsChanged': webHooks.webhookParticipantsChanged,
            'webhookAddedToGroup': webHooks.webhookAddedToGroup,
        }

    post = Helpers.post('/auth/login', header, body)
    Helpers.logs('auth', 'login', post)
    return post


# ----------------------------------------------------------------------------------------------------------------------
def logout(apiKey):
    header = {
        'Connection': 'Keep-Alive',
        'Content-type': 'application/json',
        'apiKey': apiKey
    }

    body = {}

    post = Helpers.post('/auth/logout', header, body)
    Helpers.logs('auth', 'logout', post)
    return post


# ----------------------------------------------------------------------------------------------------------------------
def close(apiKey):
    header = {
        'Connection': 'Keep-Alive',
        'Content-type': 'application/json',
        'apiKey': apiKey
    }

    body = {}

    post = Helpers.post('/auth/close', header, body)
    Helpers.logs('auth', 'close', post)
    return post


# ----------------------------------------------------------------------------------------------------------------------
def restart(apiKey):
    header = {
        'Connection': 'Keep-Alive',
        'Content-type': 'application/json',
        'apiKey': apiKey
    }

    body = {}

    post = Helpers.post('/auth/restart', header, body)
    Helpers.logs('auth', 'restart', post)
    return post


# ----------------------------------------------------------------------------------------------------------------------
def browserSessionToken(apiKey):
    header = {
        'Connection': 'Keep-Alive',
        'Content-type': 'application/json',
        'apiKey': apiKey
    }

    body = {}

    post = Helpers.post('/auth/browser-session-token', header, body)
    Helpers.logs('auth', 'browser-session-token', post)
    return post


# ----------------------------------------------------------------------------------------------------------------------
def status(apiKey):
    header = {
        'Connection': 'Keep-Alive',
        'Content-type': 'application/json',
        'apiKey': apiKey
    }

    body = {}

    post = Helpers.post('/auth/status', header, body)
    Helpers.logs('auth', 'status', post)
    return post
# ----------------------------------------------------------------------------------------------------------------------
