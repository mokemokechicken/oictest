#!/usr/bin/env python
from testfunc import policy_uri
from testfunc import logo_uri
from testfunc import tos_uri
from testfunc import static_jwk

__author__ = 'roland'

USERINFO_REQUEST_AUTH_METHOD = (
    "userinfo", {
        "kwargs_mod": {"authn_method": "bearer_header"},
        "method": "GET"
    })

HEADLINES = {
    "A": "UMA Dynamic Discovery",
    "B": "OIDC Dynamic Discovery",
    "C": "OAuth2 Dynamic Client Registration",
    "D": "OIDC Dynamic Client Registration",
    "E": "Response Type & Response Mode",
    "F": "Discovery",
    "G": "OAuth behaviors",
    "H": "redirect_uri",
    "I": "Client Authentication",
    "J": "Key Rollover",
}

FLOWS = {
    'OP-A-01': {
        "desc": 'Verify UMA discovery',
        "sequence": ['_uma_discover_'],
        "profile": ".T.",
        "tests": {"verify-op-has-dynamic-client-endpoint": {}},
    },
    'OP-B-01': {
        "desc": 'Verify OIDC discovery',
        "sequence": ['_discover_'],
        "profile": ".T.",
        "tests": {"verify-op-has-registration-endpoint": {}},
    },
    'OP-C-01': {
        "desc": 'Dynamic OAuth2 Client registration Request',
        "sequence": [
            '_uma_discover_',
            "_oauth_register_"
        ],
        "profile": "..T",
        "tests": {"check-http-response": {}},
    },
    'OP-C-02': {
        "desc": 'Registration with policy_uri',
        "sequence": [
            'note',
            "rm_cookie",
            '_uma_discover_',
            ('oauth-registration', {"function": policy_uri}),
            "_login_"
        ],
        "profile": "..T",
        'note': "When you get the login page this time you should have a "
                "link to the client policy",
        "tests": {"check-http-response": {}},
    },
    'OP-C-03': {
        "desc": 'Registration with logo uri',
        "sequence": [
            'note',
            "rm_cookie",
            '_uma_discover_',
            ('oauth-registration', {"function": logo_uri}),
            "_login_"
        ],
        "profile": "..T",
        'note': "When you get the login page this time you should have the "
                "clients logo on the page",
        "tests": {"check-http-response": {}},
    },
    'OP-C-04': {
        "desc": 'Registration with tos url',
        "sequence": [
            'note',
            'rm_cookie',
            '_uma_discover_',
            ('oauth-registration', {"function": tos_uri}),
            '_login_'
        ],
        "profile": "..T",
        'note': "When you get the login page this time you should have a "
                "link to the clients Terms of Service",
        "tests": {"check-http-response": {}},
    },
    'OP-C-05': {
        "desc": 'Uses Keys Registered with jwks_uri Value',
        "sequence": [
            '_uma_discover_',
            '_oauth_register_',
            '_login_',
            ("_accesstoken_",
             {
                 "kwargs_mod": {"authn_method": "private_key_jwt"},
                 "support": {
                     "warning": {
                         "token_endpoint_auth_methods_supported":
                             "client_secret_jwt"}}
             }),
        ],
        "profile": "..T",
        'tests': {"check-http-response": {}}
    },
    'OP-C-06': {
        "desc": 'Registering and then read the client info',
        "sequence": [
            '_uma_discover_',
            '_oauth_register_',
            "read-registration"
        ],
        "profile": "..T",
        "tests": {"check-http-response": {}},
    },
    "OP-C-07": {
        "desc": "Modify client registration",
        "sequence": [
            '_uma_discover_',
            '_oauth_register_',
            "modify-registration"
        ],
        "profile": "..T",
        "tests": {"check-http-response": {}},
    },
    "OP-C-08": {
        "desc": "Delete client registration",
        "sequence": [
            '_uma_discover_',
            '_oauth_register_',
            "delete-registration"
        ],
        "profile": "..T",
        "tests": {"check-http-response": {}},
    },
    'OP-D-01': {
        "desc": 'Dynamic UMA Client registration Request',
        "sequence": [
            '_discover_',
            "_oauth_register_"
        ],
        "profile": "..T",
        "tests": {"check-http-response": {}},
    },
    'OP-D-02': {
        "desc": 'Registration with policy_uri',
        "sequence": [
            'note',
            "rm_cookie",
            '_discover_',
            ('oic-registration', {"function": policy_uri}),
            "_login_"
        ],
        "profile": "..T",
        'note': "When you get the login page this time you should have a "
                "link to the client policy",
        "tests": {"check-http-response": {}},
    },
    'OP-D-03': {
        "desc": 'Registration with logo uri',
        "sequence": [
            'note',
            "rm_cookie",
            '_discover_',
            ('oic-registration', {"function": logo_uri}),
            "_login_"
        ],
        "profile": "..T",
        'note': "When you get the login page this time you should have the "
                "clients logo on the page",
        "tests": {"check-http-response": {}},
    },
    'OP-D-04': {
        "desc": 'Registration with tos url',
        "sequence": [
            'note',
            'rm_cookie',
            '_discover_',
            ('oic-registration', {"function": tos_uri}),
            '_login_'
        ],
        "profile": "..T",
        'note': "When you get the login page this time you should have a "
                "link to the clients Terms of Service",
        "tests": {"check-http-response": {}},
    },
    'OP-D-05': {
        "desc": 'Uses Keys Registered with jwks Value',
        "sequence": [
            '_discover_',
            ('_register_',
             {
                 "request_args": {
                     "token_endpoint_auth_method": "private_key_jwt"},
                 "function": static_jwk
             }),
            '_login_',
            ("_accesstoken_",
             {
                 "kwargs_mod": {"authn_method": "private_key_jwt"},
                 "support": {
                     "warning": {
                         "token_endpoint_auth_methods_supported":
                             "client_secret_jwt"}}
             }),
        ],
        "profile": "..T",
        "tests": {"check-http-response": {}},
    },
    'OP-D-06': {
        "desc": 'Uses Keys Registered with jwks_uri Value',
        "sequence": [
            '_discover_',
            '_register_',
            '_login_',
            ("_accesstoken_",
             {
                 "kwargs_mod": {"authn_method": "private_key_jwt"},
                 "support": {
                     "warning": {
                         "token_endpoint_auth_methods_supported":
                             "client_secret_jwt"}}
             }),
        ],
        "profile": "..T",
        'tests': {"check-http-response": {}}
    },
    'OP-D-07': {
        "desc": 'Registering and then read the client info',
        "sequence": [
            '_discover_',
            '_register_',
            "read-registration"
        ],
        "profile": "..T..+",
        "tests": {"check-http-response": {}},
    },
    'OP-E-01': {
        "desc": 'Request with response_type=code',
        "sequence": ['_uma_discover_', "_oauth_register_", "_login_"],
        "profile": "C..",
        'tests': {"check-http-response": {}},
        "mti": "MUST"
    },
    'OP-E-02': {
        "desc": 'Authorization request missing the response_type parameter',
        "sequence": [
            '_uma_discover_',
            '_oauth_register_',
            'note',
            ('_login_', {
                "request_args": {"response_type": []},
            })
        ],
        "tests": {
            "verify-error": {"error": ["invalid_request",
                                       "unsupported_response_type"]}},
        "note": "There are two correct responses: 1) returning error response "
                "to the RP 2) returning error message to the User and that in "
                "case (2) occurs the tester must submit a screen shot as proof "
                "when sending in a certification application",
        "profile": "..",
        "mti": "MUST"
    },
    'OP-E-03': {
        "desc": 'Request with response_type=token',
        "sequence": ['_uma_discover_', "_oauth_register_", "_login_"],
        "profile": "T..",
        'tests': {"check-http-response": {}},
        "mti": "MUST"
    },
    'OP-E-04 ': {
        "desc": 'Request with response_mode=form_post',
        "sequence": [
            '_uma_discover_',
            '_oauth_register_',
            ('_login_',
             {"request_args": {"response_mode": ["form_post"]}})
        ],
        "profile": "....+",
        'tests': {"check-http-response": {}},
        "mti": "MUST"
    },
    # 'OP-C-01': {
    #     "desc": 'Publish openid-configuration discovery information',
    #     "sequence": ['_discover_'],
    #     "profile": ".T.",
    #     'tests': {"check-http-response": {}},
    # },
    # 'OP-C-02': {
    #     "desc": 'Verify that jwks_uri and claims_supported are published',
    #     "sequence": ['_discover_'],
    #     "tests": {"providerinfo-has-jwks_uri": {},
    #               "providerinfo-has-claims_supported": {},
    #               "check-http-response": {}},
    #     "profile": ".T.",
    # },
    # 'OP-C-03': {
    #     "desc": 'Keys in OP JWKs well formed',
    #     "sequence": ['_discover_'],
    #     "profile": ".T.",
    #     "tests": {"verify-base64url": {}, "check-http-response": {}},
    # },
    # 'OP-C-05': {
    #     "desc": 'Can Discover Identifiers using E-Mail Syntax',
    #     "profile": ".T...+",
    #     #"profile": ".T.",
    #     "sequence": [
    #         ("webfinger",
    #          {"kwarg_func": (get_principal, {"param": "webfinger_email"})})],
    #     "tests": {"check-http-response": {}},
    # },
    # 'OP-C-06': {
    #     "desc": 'Can Discover Identifiers using URL Syntax',
    #     "profile": ".T...+",
    #     "sequence": [
    #         ("webfinger",
    #          {"kwarg_func": (get_principal, {"param": "webfinger_url"})})],
    #     "tests": {"check-http-response": {}},
    # },
    # 'OP-D-01': {
    #     "desc": 'Trying to use access code twice should result in an error',
    #     "sequence": [
    #         '_discover_',
    #         '_register_',
    #         '_login_',
    #         "_accesstoken_",
    #         "_accesstoken_"
    #     ],
    #     "profile": "C,CI,CT,CIT..",
    #     "tests": {"verify-bad-request-response": {"status": WARNING}},
    #     "mti": "SHOULD",
    #     "reference": "http://tools.ietf.org/html/draft-ietf-oauth-v2-31"
    #                  "#section-4.1",
    # },
    # 'OP-D-02': {
    #     "desc": 'Trying to use access code twice should result in '
    #             'revoking previous issued tokens',
    #     "sequence": [
    #         '_discover_',
    #         '_register_',
    #         '_login_',
    #         "_accesstoken_",
    #         "_accesstoken_",
    #         USERINFO_REQUEST_AUTH_METHOD
    #     ],
    #     "profile": "C,CI,CT,CIT..",
    #     "tests": {"verify-bad-request-response": {"status": WARNING}},
    #     "mti": "SHOULD",
    #     "reference": "http://tools.ietf.org/html/draft-ietf-oauth-v2-31"
    #                  "#section-4.1",
    # },
    # 'OP-D-03': {
    #     "desc": 'Trying to use access code twice with 30 seconds in between '
    #             'must result in an error',
    #     "sequence": [
    #         'note',
    #         '_discover_',
    #         '_register_',
    #         '_login_',
    #         "_accesstoken_",
    #         "intermission",
    #         "_accesstoken_"
    #     ],
    #     "profile": "C,CI,CT,CIT..",
    #     "tests": {"verify-bad-request-response": {"status": ERROR}},
    #     "mti": "SHOULD",
    #     "note": "An 30 second delay is added between the first and the second "
    #             "access token request.",
    #     "reference": "http://tools.ietf.org/html/draft-ietf-oauth-v2-31"
    #                  "#section-4.1",
    # },
    # 'OP-E-01': {
    #     "desc": 'The sent redirect_uri does not match the registered',
    #     "sequence": [
    #         '_discover_',
    #         '_register_',
    #         "expect_err",
    #         ("_login_", {"function": mismatch_return_uri})
    #     ],
    #     "profile": "..",
    #     "note": "The next request should result in the OpenID Connect Provider "
    #             "returning an error message to your web browser.",
    #     'tests': {"check-http-response": {}},
    #     "mti": "MUST",
    # },
    # 'OP-E-02': {
    #     "desc": 'Reject request without redirect_uri when multiple registered',
    #     "sequence": [
    #         '_discover_',
    #         ('_register_', {"function": multiple_return_uris}),
    #         "expect_err",
    #         ("_login_", {"request_args": {"redirect_uri": ""}})
    #     ],
    #     "profile": "..T",
    #     'tests': {"check-http-response": {}},
    #     "note": "The next request should result in the OpenID Connect Provider "
    #             "returning an error message to your web browser.",
    #     "mti": "MUST",
    # },
    # 'OP-E-03': {
    #     "desc": 'Request with redirect_uri with query component',
    #     "sequence": [
    #         '_discover_',
    #         '_register_',
    #         ("_login_",
    #          {"function": (redirect_uri_with_query_component, {"foo": "bar"})})
    #     ],
    #     "profile": "..T",
    #     "mti": "MUST",
    #     'tests': {"verify-redirect_uri-query_component": {"foo": "bar"},
    #               "check-http-response": {}}
    # },
    # 'OP-E-04': {
    #     "desc": 'Registration where a redirect_uri has a query component',
    #     "sequence": [
    #         '_discover_',
    #         ('_register_',
    #          {"function": (
    #              redirect_uris_with_query_component, {"foo": "bar"})}),
    #     ],
    #     "profile": "..T",
    #     "mti": "MUST",
    #     "reference": "http://tools.ietf.org/html/draft-ietf-oauth-v2-31"
    #                  "#section-3.1.2",
    #     'tests': {"check-http-response": {}},
    # },
    # 'OP-E-05': {
    #     "desc": 'Rejects redirect_uri when Query Parameter Does Not Match',
    #     "sequence": [
    #         '_discover_',
    #         ('_register_',
    #          {
    #              "function": (
    #                  redirect_uris_with_query_component, {"foo": "bar"})}),
    #         'expect_err',
    #         ("_login_", {
    #             # different from the one registered
    #             "function": (redirect_uri_with_query_component, {"bar": "foo"})
    #         })
    #     ],
    #     "profile": "..T",
    #     "reference": "http://tools.ietf.org/html/draft-ietf-oauth-v2-31"
    #                  "#section-3.1.2",
    #     'tests': {"check-http-response": {}},
    #     "mti": "MUST",
    # },
    # 'OP-E-06': {
    #     "desc": 'Reject registration where a redirect_uri has a fragment',
    #     "sequence": [
    #         '_discover_',
    #         ('_register_', {
    #             "function": (redirect_uris_with_fragment, {"foo": "bar"})})
    #     ],
    #     "profile": "..T",
    #     "tests": {"verify-bad-request-response": {}},
    #     "mti": "MUST",
    #     "reference": "http://tools.ietf.org/html/draft-ietf-oauth-v2-31"
    #                  "#section-3.1.2",
    # },
    # 'OP-E-07': {
    #     "desc": 'No redirect_uri in request with one registered',
    #     "sequence": [
    #         '_discover_',
    #         '_register_',
    #         "expect_err",
    #         ('_login_', {"request_args": {"redirect_uri": ""}})
    #     ],
    #     "profile": "....+",
    #     'tests': {"check-http-response": {}},
    # },
    # 'OP-F-01d': {
    #     "desc": 'Access token request with client_secret_basic authentication',
    #     # Register token_endpoint_auth_method=client_secret_basic
    #     "sequence": [
    #         '_discover_',
    #         ('_register_',
    #          {
    #              "request_args": {
    #                  "token_endpoint_auth_method": "client_secret_basic"},
    #          }),
    #         '_login_',
    #         ("_accesstoken_",
    #          {
    #              "kwargs_mod": {"authn_method": "client_secret_basic"},
    #              "support": {
    #                  "warning": {
    #                      "token_endpoint_auth_methods_supported":
    #                          "client_secret_basic"}}
    #          }),
    #     ],
    #     "profile": "C,CI,CIT,CT..T",
    #     'tests': {"check-http-response": {}},
    # },
    # 'OP-F-01s': {
    #     "desc": 'Access token request with client_secret_basic authentication',
    #     # client_secret_basic is the default
    #     "sequence": [
    #         '_discover_',
    #         '_login_',
    #         ("_accesstoken_",
    #          {
    #              "kwargs_mod": {"authn_method": "client_secret_basic"},
    #              "support": {
    #                  "warning": {
    #                      "token_endpoint_auth_methods_supported":
    #                          "client_secret_basic"}}
    #          }),
    #     ],
    #     "profile": "C,CI,CIT,CT..F",
    #     'tests': {"check-http-response": {}},
    # },
    # 'OP-F-02d': {
    #     "desc": 'Access token request with client_secret_post authentication',
    #     # Should register token_endpoint_auth_method=client_secret_post
    #     "sequence": [
    #         '_discover_',
    #         ('_register_',
    #          {
    #              "request_args": {
    #                  "token_endpoint_auth_method": "client_secret_post"},
    #          }),
    #         '_login_',
    #         ("_accesstoken_",
    #          {
    #              "kwargs_mod": {"authn_method": "client_secret_post"},
    #              "support": {
    #                  "warning": {
    #                      "token_endpoint_auth_methods_supported":
    #                          "client_secret_post"}}
    #          }),
    #     ],
    #     "profile": "C,CI,CIT,CT..T",
    #     'tests': {"check-http-response": {}},
    # },
    # 'OP-F-02s': {
    #     "desc": 'Access token request with client_secret_post authentication',
    #     # Should register token_endpoint_auth_method=client_secret_post
    #     "sequence": [
    #         '_discover_',
    #         '_login_',
    #         ("_accesstoken_",
    #          {
    #              "kwargs_mod": {"authn_method": "client_secret_post"},
    #              "support": {
    #                  "warning": {
    #                      "token_endpoint_auth_methods_supported":
    #                          "client_secret_post"}}
    #          }),
    #     ],
    #     "profile": "C,CI,CIT,CT..F",
    #     'tests': {"check-http-response": {}},
    # },
    # 'OP-F-03': {
    #     "desc": 'Access token request with public_key_jwt authentication',
    #     "sequence": [
    #         '_discover_',
    #         ('_register_',
    #          {
    #              "request_args": {
    #                  "token_endpoint_auth_method": "public_key_jwt"},
    #          }),
    #         '_login_',
    #         ("_accesstoken_",
    #          {
    #              "kwargs_mod": {"authn_method": "public_key_jwt"},
    #              "support": {
    #                  "warning": {
    #                      "token_endpoint_auth_methods_supported":
    #                          "public_key_jwt"}}
    #          }),
    #     ],
    #     "profile": "...s.+",
    #     'tests': {"check-http-response": {}},
    # },
    # 'OP-F-04': {
    #     "desc": 'Access token request with client_secret_jwt authentication',
    #     "sequence": [
    #         '_discover_',
    #         ('_register_',
    #          {
    #              "request_args": {
    #                  "token_endpoint_auth_method": "client_secret_jwt"},
    #          }),
    #         '_login_',
    #         ("_accesstoken_",
    #          {
    #              "kwargs_mod": {"authn_method": "client_secret_jwt"},
    #              "support": {
    #                  "warning": {
    #                      "token_endpoint_auth_methods_supported":
    #                          "client_secret_jwt"}}
    #          }),
    #     ],
    #     "profile": "...s.+",
    #     'tests': {"check-http-response": {}},
    # },
    # 'OP-G-01': {
    #     "desc": "Can Rollover OP Signing Key",
    #     "sequence": [
    #         '_discover_',
    #         'fetch_keys',
    #         "note",
    #         '_discover_',
    #         'fetch_keys',
    #     ],
    #     "note": "Please make your OP roll over signing keys. "
    #             'If you are not able to cause the server to roll over the key '
    #             'while running the test, then you will have to self-assert '
    #             'that your deployment can do OP signing key rollover.',
    #     "profile": ".T.T.s",
    #     # "profile": ".T.T.s.+",
    #     "tests": {"new-signing-keys": {}, "check-http-response": {}}
    # },
    # 'OP-G-02': {
    #     "desc": 'Request access token, change RSA sign key and request another '
    #             'access token',
    #     "sequence": [
    #         '_discover_',
    #         ('_register_',
    #          {
    #              "request_args": {
    #                  "token_endpoint_auth_method": "private_key_jwt"},
    #              "support": {"error": {
    #                  "token_endpoint_auth_methods_supported":
    #                      "private_key_jwt"}}
    #          }),
    #         '_login_',
    #         ("_accesstoken_",
    #          {
    #              "kwargs_mod": {"authn_method": "private_key_jwt"},
    #          }),
    #         "rotate_sign_keys",
    #         ("refresh-access-token",
    #          {
    #              "kwargs_mod": {"authn_method": "private_key_jwt"},
    #          })
    #     ],
    #     "profile": "..T.s",
    #     "tests": {"check-http-response": {}}
    # },
    # 'OP-G-03': {
    #     "desc": "Can Rollover OP Encryption Key",
    #     "sequence": [
    #         '_discover_',
    #         'fetch_keys',
    #         "note",
    #         '_discover_',
    #         'fetch_keys',
    #     ],
    #     "note": "Please make your OP roll over encryption keys."
    #             'If you are not able to cause the server to roll over the keys '
    #             'while running the test, then you will have to self-assert '
    #             'that your deployment can do OP encryption key rollover.',
    #     # "profile": ".T..e.+",
    #     "profile": ".T..e",
    #     "tests": {"new-encryption-keys": {}, "check-http-response": {}}
    # },
    # 'OP-G-04': {
    #     # where is the RPs encryption keys used => userinfo encryption
    #     "desc": 'Request encrypted user info, change RSA enc key and request '
    #             'user info again',
    #     "sequence": [
    #         '_discover_',
    #         ("oic-registration",
    #          {
    #              "request_args": {
    #                  "userinfo_signed_response_alg": "none",
    #                  "userinfo_encrypted_response_alg": "RSA1_5",
    #                  "userinfo_encrypted_response_enc": "A128CBC-HS256"
    #              },
    #              "support": {
    #                  "warning": {
    #                      "userinfo_signing_alg_values_supported": "none",
    #                      "userinfo_encryption_alg_values_supported": "RSA1_5",
    #                      "userinfo_encryption_enc_values_supported":
    #                          "A128CBC-HS256"
    #                  }
    #              }
    #          }
    #         ),
    #         '_login_',
    #         "_accesstoken_",
    #         "rotate_sign_keys",
    #         "userinfo"
    #     ],
    #     "profile": "..T.se.+",
    #     "tests": {"check-http-response": {}}
    # },
}
