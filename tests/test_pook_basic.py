"""
Basic example showing a single request with `pook`
"""

import pytest
import pook
import pook.exceptions
import requests
import json

### This had to be HAND BUILT from looking at the response scheme located at behance's API
behance_projects_response = {
    "projects": [
        {
            'covers': {
                '115': 'https://picsum.photos/115/115?image=359',
                '202': 'https://picsum.photos/202/202?image=837'
            },
            'created_on': 1420757994,
            'fields': ['Textile Design', 'Photojournalism', 'Metal Working', 'Philosophy', 'Programming',
                       'Entrepreneurship', 'Graphic Design', 'Cartooning', 'Photography', 'Jewelry Design',
                       'Interaction Design', 'Caricature', 'Dance', 'Comedy', 'Illustration', 'Hair Styling',
                       'Art Direction', 'MakeUp Arts (MUA)', 'Fashion Styling', 'Toy Design', 'Icon Design',
                       'Lighting Design', 'Academia', 'Motion Graphics', 'Enology (Wines)', 'Poetry', 'Costume Design',
                       'Ice Sculpting', 'Wood Working', 'Retouching', 'DJing', 'Calligraphy', 'Carpentry', 'Publishing',
                       'Singing', 'Screenwriting', 'Storytelling', 'Journalism', 'Industrial Design', 'Sound Design',
                       'Masonry', 'Installation Design', 'Music Composition', 'Production', 'Television', 'Playwriting',
                       'Pattern Design', 'Photo Illustration', 'Writing', 'Philanthropy', 'Copywriting', 'Sculpting',
                       'Architecture', 'Video Arts', 'Computer Animation', 'Puppetry', 'Branding', 'Digital Art',
                       'Typography', 'Design', 'Advertising', 'Perfumery', 'Video Blogging'],
            'id': 1337,
            'mature_content': 0,
            'modified_on': 1424113656,
            'name': 'maximized',
            'owners': [
                 {
                    'city': 'Dickensstad',
                    'company': 'Schmitt, Kerluke and Jakubowski',
                    'country': 'Mauritius',
                    'created_on': 1649927779,
                    'display_name': 'Raegan Stehr',
                    'first_name': 'Raegan',
                    'id': 5514,
                    'images': {
                       '32': 'https://picsum.photos/32/32?image=716',
                       '50': 'https://picsum.photos/50/50?image=679',
                       '78': 'https://picsum.photos/78/78?image=155',
                       '115': 'https://picsum.photos/115/115?image=11',
                       '129': 'https://picsum.photos/129/129?image=776',
                       '138': 'https://picsum.photos/138/138?image=569'
                    },
                    'last_name': 'Stehr',
                    'occupation': 'Global Infrastructure Manager',
                    'state': 'Utah',
                    'url': 'http://www.behance.net/Jovani_McClure',
                    'username': 'Jovani_McClure'
                 },
                {
                    'city': 'North Madietown',
                    'company': 'Harber, Gibson and Steuber',
                    'country': 'Christmas Island',
                    'created_on': 1616823973,
                    'display_name': 'Oswald Hermiston',
                    'first_name': 'Oswald',
                    'id': 4639,
                    'images': {
                       '32': 'https://picsum.photos/32/32?image=601',
                       '50': 'https://picsum.photos/50/50?image=337',
                       '78': 'https://picsum.photos/78/78?image=841',
                       '115': 'https://picsum.photos/115/115?image=134',
                       '129': 'https://picsum.photos/129/129?image=213',
                       '138': 'https://picsum.photos/138/138?image=61'
                    },
                    'last_name': 'Hermiston',
                    'occupation': 'Regional Directives Technician',
                    'state': 'West Virginia',
                    'url': 'http://www.behance.net/Hettie.Lockman',
                    'username': 'Hettie.Lockman'
                },
                {
                    'city': 'North Maeveland',
                    'company': 'Reichel LLC',
                    'country': 'Jamaica',
                    'created_on': 1378870105,
                    'display_name': 'Scot Wintheiser',
                    'first_name': 'Scot',
                    'id': 9911,
                    'images': {
                        '32': 'https://picsum.photos/32/32?image=246',
                        '50': 'https://picsum.photos/50/50?image=701',
                        '78': 'https://picsum.photos/78/78?image=65',
                        '115': 'https://picsum.photos/115/115?image=77',
                        '129': 'https://picsum.photos/129/129?image=500',
                        '138': 'https://picsum.photos/138/138?image=718'
                    },
                    'last_name': 'Wintheiser',
                    'occupation': 'Central Branding Designer',
                    'state': 'North Carolina',
                    'url': 'http://www.behance.net/Mittie_Buckridge67',
                    'username': 'Mittie_Buckridge67'
                }
            ],
            'published_on': 1661963862,
            'stats': {
                'appreciations': 74,
                'comments': 24,
                'views': 4028
            },
            'url': 'http://www.behance.net/gallery/maximized/2674'
        }
    ]
}

behance_projects_response_str = json.dumps(behance_projects_response)

pook.on()
# Query parameters have to be explictly written down; you can filter by Headers if needed, though.
pook.get("https://www.behance.net/v2/projects?api_key=u_n_m_o_c_k_200").reply(200).headers(
    {  # Headers also needed to be manually contstructed
        "Content-Length": str(len(behance_projects_response_str)),
        "Content-Type": "application/json; charset=utf-8",
        "ETag": "W/\"5e5e-Skxf9ruz9l1grCAr8kIDbgRdcw8\"",
        "Access-Control-Allow-Origin": "*",
        "X-DNS-Prefetch-Control": "off",
        "X-Frame-Options": "SAMEORIGIN",
        "Strict-Transport-Security": "max-age=15552000; includeSubDomains",
        "X-Download-Options": "noopen",
        "X-Content-Type-Options": "nosniff",
        "X-XSS-Protection": "1; mode=block",
    }
).json(behance_projects_response)


def test_pook_once():
    res = requests.get("https://www.behance.net/v2/projects?api_key=u_n_m_o_c_k_200")
    assert res.status_code == 200  # Hard coded to succeed!
    content = res.json()
    assert content.get('projects')
    assert content.get('projects')[0].get('id') == 1337
    assert "json" in res.headers.get("Content-Type", "")

# Pook raises an exception if no match was found
def test_pook_missing():
    with pytest.raises(pook.exceptions.PookNoMatches):
        res = requests.get("https://www.example.com")