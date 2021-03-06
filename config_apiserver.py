import web_oauth
from models import db
from oauth2 import config_oauth


def config_api_server(app, mode) :

    oauth_config = {
    'OAUTH2_REFRESH_TOKEN_GENERATOR': False,
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///' + mode.db_path + '/db.sqlite',
    'OAUTH2_TOKEN_EXPIRES_IN' : {
        'authorization_code': 300,
        #'implicit': 3000,
        #'password': 3000,
        'client_credentials': 3000
        }
    }
    app.config.update(oauth_config)
    db.init_app(app)
    config_oauth(app)

    # Resolver
    app.add_url_rule('/resolver', view_func=web_oauth.resolver, methods = ['GET', 'POST'], defaults ={'mode' : mode})

    # Create credentials
    app.add_url_rule('/api/v1', view_func=web_oauth.home, methods = ['GET', 'POST'], defaults ={'mode' : mode})
    app.add_url_rule('/api/v1/create_client', view_func=web_oauth.create_client, methods = ['GET', 'POST'])

    # Identity Provider
    app.add_url_rule('/api/v1/oauth_login', view_func=web_oauth.oauth_login, methods = ['GET', 'POST'], defaults ={'mode' : mode})
    app.add_url_rule('/api/v1/oauth_login_larger', view_func=web_oauth.oauth_login_larger, methods = ['GET', 'POST'], defaults ={'mode' : mode})   
    app.add_url_rule('/api/v1/oauth_wc_login/', view_func=web_oauth.oauth_wc_login, methods = ['GET', 'POST'], defaults ={'mode' : mode})

    app.add_url_rule('/api/v1/oauth_logout', view_func=web_oauth.oauth_logout, methods = ['GET', 'POST'])
    #app.add_url_rule('/api/v1/oauth_two_factor', view_func=web_oauth.oauth_two_factor, methods = ['GET', 'POST'], defaults ={'mode' : mode})

    # Authorization Server
    app.add_url_rule('/api/v1/authorize', view_func=web_oauth.authorize, methods = ['GET', 'POST'], defaults={'mode' : mode})
    app.add_url_rule('/api/v1/oauth/token', view_func=web_oauth.issue_token, methods = ['POST'])
    app.add_url_rule('/api/v1/oauth_revoke', view_func=web_oauth.revoke_token, methods = ['GET', 'POST'])

    # authorization code flow with user consent screen
    app.add_url_rule('/api/v1/user_info', view_func=web_oauth.user_info, methods = ['GET', 'POST'], defaults={'mode' : mode})
    app.add_url_rule('/api/v1/user_accepts_company_partnership', view_func=web_oauth.user_accepts_company_partnership, methods = ['GET', 'POST'], defaults={'mode' : mode})
    app.add_url_rule('/api/v1/user_accepts_company_referent', view_func=web_oauth.user_accepts_company_referent, methods = ['GET', 'POST'], defaults={'mode' : mode})   
    app.add_url_rule('/api/v1/user_issues_certificate', view_func=web_oauth.user_issues_certificate, methods = ['GET', 'POST'], defaults={'mode' : mode})
    app.add_url_rule('/api/v1/user_adds_referent', view_func=web_oauth.user_adds_referent, methods = ['GET', 'POST'], defaults={'mode' : mode})
    app.add_url_rule('/api/v1/user_updates_company_settings', view_func=web_oauth.user_updates_company_settings, methods = ['GET', 'POST'], defaults={'mode' : mode})
    app.add_url_rule('/api/v1/user_uploads_signature', view_func=web_oauth.user_uploads_signature, methods = ['GET', 'POST'], defaults={'mode' : mode})
    app.add_url_rule('/api/v1/user_uploads_logo', view_func=web_oauth.user_uploads_picture, methods = ['GET', 'POST'], defaults={'mode' : mode})
    app.add_url_rule('/api/v1/user_uploads_picture', view_func=web_oauth.user_uploads_picture, methods = ['GET', 'POST'], defaults={'mode' : mode}) # same as previous

    # client credentials code flow
    app.add_url_rule('/api/v1/create_person_identity', view_func=web_oauth.oauth_create_person_identity, methods = ['GET', 'POST'], defaults={'mode' : mode})
    app.add_url_rule('/api/v1/create_company_identity', view_func=web_oauth.oauth_create_company_identity, methods = ['GET', 'POST'], defaults={'mode' : mode})
    app.add_url_rule('/api/v1/issue_agreement', view_func=web_oauth.oauth_issue_agreement, methods = ['GET', 'POST'], defaults={'mode' : mode})
    app.add_url_rule('/api/v1/issue_reference', view_func=web_oauth.oauth_issue_reference, methods = ['GET', 'POST'], defaults={'mode' : mode})
    app.add_url_rule('/api/v1/get_certificate_list', view_func=web_oauth.oauth_get_certificate_list, methods = ['GET', 'POST'], defaults={'mode' : mode})
    app.add_url_rule('/api/v1/get_certificate', view_func=web_oauth.oauth_get_certificate, methods = ['GET', 'POST'], defaults={'mode' : mode})
    app.add_url_rule('/api/v1/issue_experience', view_func=web_oauth.oauth_issue_experience, methods = ['GET', 'POST'], defaults={'mode' : mode})
    app.add_url_rule('/api/v1/get_status', view_func=web_oauth.oauth_get_status, methods = ['GET', 'POST'], defaults={'mode' : mode})

    return