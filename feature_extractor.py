import re
from urllib.parse import urlparse

def extract_features(url):
    features = []
    
    # Feature 1: Length of URL
    features.append(len(url))
    
    # Feature 2: Count of '.'
    features.append(url.count('.'))
    
    # Feature 3: '@' in URL
    features.append(1 if '@' in url else 0)
    
    # Feature 4: '-' in domain
    features.append(1 if '-' in url else 0)
    
    # Feature 5: Uses HTTPS
    features.append(1 if url.startswith('https') else 0)
    
    return features
