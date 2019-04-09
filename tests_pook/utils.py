import json


## Definitions used in the mocks here
# These had to be HAND BUILT from looking at the response scheme located at behance's API

BEHANCE_PROJECTS_REPONSE = {
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

BEHANCE_PROJECTS_REPONSE_STR = json.dumps(BEHANCE_PROJECTS_REPONSE)

BHENACE_PROJECTS_LENGTH = len(BEHANCE_PROJECTS_REPONSE_STR)