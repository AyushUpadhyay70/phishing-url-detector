import re
from urllib.parse import urlparse  # <-- Ye line zaroori hai

def extract_features_from_form(form_data):
    return [
        int(form_data['SFH']),
        int(form_data['popUpWidnow']),
        int(form_data['SSLfinal_State']),
        int(form_data['Request_URL']),
        int(form_data['URL_of_Anchor']),
        int(form_data['web_traffic']),
        int(form_data['URL_Length']),
        int(form_data['age_of_domain']),
        int(form_data['having_IP_Address']),
    ]

